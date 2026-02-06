import os
import importlib
import random
from flask import Flask, request
import telebot
from telebot import types

# ===============================
# ⚠️ Configuración de Variables
# ===============================
# Se recomienda usar os.getenv() para mayor seguridad en producción
TOKEN = os.environ.get("TELEGRAM_TOKEN", "8441666201:AAHygO1Osx5IdxnmQpQuF__Y8WyGvBKhr4U")
PUBLIC_URL = os.environ.get("PUBLIC_URL", "https://ofertas-production.up.railway.app")
PORT = int(os.environ.get("PORT", 5000))

if not TOKEN:
    raise RuntimeError("ERROR: No se ha configurado el TELEGRAM_TOKEN")

bot = telebot.TeleBot(TOKEN)
app = Flask(__name__)

# ===============================
# 📌 Datos y Persistencia Temporal
# ===============================
MATERIAS_DISPLAY = {
    'lengua': '📚 Lengua',
    'mates': '🔢 Matemáticas',
    'ciencias': '🧪 Ciencias',
    'ingles': '🇬🇧 Inglés',
    'frances': '🇫🇷 Francés'
}

user_stats = {} # Estado actual del examen
estadisticas = {} # Acumulado (Se pierde al reiniciar el servidor)

def registrar_resultado(chat_id, aciertos, fallos):
    if chat_id not in estadisticas:
        estadisticas[chat_id] = {'aciertos': 0, 'fallos': 0, 'intentos': 0}
    estadisticas[chat_id]['aciertos'] += aciertos
    estadisticas[chat_id]['fallos'] += fallos
    estadisticas[chat_id]['intentos'] += 1

# ===============================
# 📚 Manejadores (Handlers)
# ===============================
@bot.message_handler(commands=['start', 'menu'])
def menu_principal(message):
    markup = types.InlineKeyboardMarkup(row_width=2)
    botones = [types.InlineKeyboardButton(nom, callback_data=f"mat_{idx}") for idx, nom in MATERIAS_DISPLAY.items()]
    markup.add(*botones)
    markup.add(types.InlineKeyboardButton("📊 Mis estadísticas", callback_data="ver_estadisticas"))
    bot.send_message(message.chat.id, "¡Bienvenido! Selecciona una materia para comenzar:", reply_markup=markup)

@bot.callback_query_handler(func=lambda call: call.data.startswith('mat_'))
def abrir_materia(call):
    materia_id = call.data.split('_')[1]
    try:
        # Carga dinámica del módulo (ej: lengua.py)
        modulo = importlib.import_module(materia_id)
        importlib.reload(modulo)
        temario = modulo.TEMARIO

        markup = types.InlineKeyboardMarkup()
        for uni_id, datos in temario.items():
            markup.add(types.InlineKeyboardButton(f"{uni_id}: {datos['titulo']}", callback_data=f"uni_{materia_id}_{uni_id}"))
        
        bot.edit_message_text(f"Unidades de {MATERIAS_DISPLAY[materia_id]}:", call.message.chat.id, call.message.message_id, reply_markup=markup)
    except Exception:
        bot.answer_callback_query(call.id, f"Error: No se encontró el archivo {materia_id}.py o la variable TEMARIO", show_alert=True)

@bot.callback_query_handler(func=lambda call: call.data.startswith('uni_'))
def elegir_examen(call):
    _, mat, uni = call.data.split('_')
    markup = types.InlineKeyboardMarkup()
    for i in range(1, 4):
        markup.add(types.InlineKeyboardButton(f"📝 Examen Tipo {i}", callback_data=f"test_{mat}_{uni}_{i}"))
    bot.edit_message_text(f"Elige un modelo de examen para {uni}:", call.message.chat.id, call.message.message_id, reply_markup=markup)

@bot.callback_query_handler(func=lambda call: call.data.startswith('test_'))
def iniciar_test(call):
    _, mat, uni, modelo = call.data.split('_')
    modulo = importlib.import_module(mat)
    preguntas_pool = modulo.TEMARIO[uni]['examenes'][int(modelo)-1]

    if not preguntas_pool:
        bot.answer_callback_query(call.id, "⚠️ Este examen no tiene preguntas aún.", show_alert=True)
        return

    user_stats[call.message.chat.id] = {
        'preguntas': preguntas_pool,
        'actual': 0,
        'aciertos': 0,
        'fallos': 0,
        'nombre_materia': MATERIAS_DISPLAY[mat]
    }
    bot.delete_message(call.message.chat.id, call.message.message_id)
    enviar_pregunta(call.message.chat.id)

def enviar_pregunta(chat_id):
    datos = user_stats[chat_id]
    if datos['actual'] < len(datos['preguntas']):
        p = datos['preguntas'][datos['actual']]
        markup = types.InlineKeyboardMarkup(row_width=1)
        opciones = list(p['o'])
        random.shuffle(opciones)
        for opcion in opciones:
            es_correcta = "si" if opcion == p['r'] else "no"
            markup.add(types.InlineKeyboardButton(opcion, callback_data=f"res_{es_correcta}"))
        
        texto = f"📖 *{datos['nombre_materia']}*\n❓ *Pregunta {datos['actual'] + 1}/{len(datos['preguntas'])}:*\n\n{p['p']}"
        bot.send_message(chat_id, texto, reply_markup=markup, parse_mode="Markdown")
    else:
        finalizar_examen(chat_id)

@bot.callback_query_handler(func=lambda call: call.data.startswith('res_'))
def procesar_respuesta(call):
    chat_id = call.message.chat.id
    if chat_id not in user_stats: return
    
    if call.data == "res_si":
        user_stats[chat_id]['aciertos'] += 1
        bot.answer_callback_query(call.id, "✅ ¡Correcto!")
    else:
        user_stats[chat_id]['fallos'] += 1
        bot.answer_callback_query(call.id, "❌ Incorrecto")

    bot.delete_message(chat_id, call.message.message_id)
    user_stats[chat_id]['actual'] += 1
    enviar_pregunta(chat_id)

def finalizar_examen(chat_id):
    res = user_stats[chat_id]
    registrar_resultado(chat_id, res['aciertos'], res['fallos'])
    
    texto = f"🏁 *Examen terminado*\n\n✅ Aciertos: {res['aciertos']}\n❌ Fallos: {res['fallos']}\n\nUsa /menu para intentar otro."
    bot.send_message(chat_id, texto, parse_mode="Markdown")
    del user_stats[chat_id]

@bot.callback_query_handler(func=lambda call: call.data == "ver_estadisticas")
def mostrar_estadisticas(call):
    s = estadisticas.get(call.message.chat.id, {'aciertos': 0, 'fallos': 0, 'intentos': 0})
    texto = f"📊 *Tus estadísticas:*\n\n✅ Aciertos: {s['aciertos']}\n❌ Fallos: {s['fallos']}\n📝 Exámenes: {s['intentos']}"
    bot.edit_message_text(texto, call.message.chat.id, call.message.message_id, parse_mode="Markdown")

# ===============================
# 🔗 Webhook & Flask
# ===============================
@app.route(f"/{TOKEN}", methods=['POST'])
def getMessage():
    json_string = request.get_data().decode('utf-8')
    update = telebot.types.Update.de_json(json_string)
    bot.process_new_updates([update])
    return "!", 200

@app.route("/")
def webhook():
    bot.remove_webhook()
    bot.set_webhook(url=f"{PUBLIC_URL}/{TOKEN}")
    return "Bot Online", 200

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=PORT)
