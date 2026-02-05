# main.py
import os
from flask import Flask, request
import telebot
import importlib
import random

# ===============================
# ⚠️ Variables de entorno
# ===============================
TOKEN = os.environ.get("8441666201:AAHygO1Osx5IdxnmQpQuF__Y8WyGvBKhr4U")
PUBLIC_URL = os.environ.get("ofertas-production.up.railway.app")
PORT = int(os.environ.get("PORT", 8080))

if not TOKEN or not PUBLIC_URL:
    raise RuntimeError(
        "❌ Faltan variables de entorno TELEGRAM_BOT_TOKEN o RAILWAY_PUBLIC_DOMAIN"
    )

# ===============================
# ⚙️ Inicialización del bot
# ===============================
bot = telebot.TeleBot(TOKEN)
app = Flask(__name__)

# ===============================
# 📌 Datos y almacenamiento
# ===============================
MATERIAS_DISPLAY = {
    'lengua': '📚 Lengua',
    'mates': '🔢 Matemáticas',
    'ciencias': '🧪 Ciencias',
    'ingles': '🇬🇧 Inglés',
    'frances': '🇫🇷 Francés'
}

# Diccionario temporal por usuario para seguimiento del examen
user_stats = {}

# Estadísticas persistentes por usuario
estadisticas = {}  # {chat_id: {'aciertos': n, 'fallos': n, 'intentos': n}}

def registrar_resultado(chat_id, aciertos, fallos):
    if chat_id not in estadisticas:
        estadisticas[chat_id] = {'aciertos': 0, 'fallos': 0, 'intentos': 0}
    estadisticas[chat_id]['aciertos'] += aciertos
    estadisticas[chat_id]['fallos'] += fallos
    estadisticas[chat_id]['intentos'] += 1

def ver_estadisticas(chat_id):
    if chat_id not in estadisticas:
        return {'aciertos': 0, 'fallos': 0, 'intentos': 0}
    return estadisticas[chat_id]

# ===============================
# 📚 Handlers del bot
# ===============================
@bot.message_handler(commands=['start', 'menu'])
def menu_principal(message):
    from telebot import types
    markup = types.InlineKeyboardMarkup(row_width=2)
    for id_mat, nombre in MATERIAS_DISPLAY.items():
        markup.add(types.InlineKeyboardButton(nombre, callback_data=f"mat_{id_mat}"))
    markup.add(types.InlineKeyboardButton("📊 Mis estadísticas", callback_data="ver_estadisticas"))
    bot.send_message(message.chat.id, "¡Hola! Elige materia o revisa tus estadísticas:", reply_markup=markup)

@bot.callback_query_handler(func=lambda call: call.data.startswith('mat_'))
def abrir_materia(call):
    materia_id = call.data.split('_')[1]
    try:
        modulo = importlib.import_module(materia_id)
        importlib.reload(modulo)
        temario = modulo.TEMARIO

        from telebot import types
        markup = types.InlineKeyboardMarkup()
        for uni_id, datos in temario.items():
            markup.add(types.InlineKeyboardButton(f"{uni_id}: {datos['titulo']}", callback_data=f"uni_{materia_id}_{uni_id}"))
        
        bot.edit_message_text(f"Unidades de {MATERIAS_DISPLAY[materia_id]}:", call.message.chat.id, call.message.message_id, reply_markup=markup)
    except Exception as e:
        bot.answer_callback_query(call.id, f"Error: No se encontró la variable TEMARIO en {materia_id}.py", show_alert=True)

@bot.callback_query_handler(func=lambda call: call.data.startswith('uni_'))
def elegir_examen(call):
    _, mat, uni = call.data.split('_')
    from telebot import types
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
        bot.answer_callback_query(call.id, "⚠️ Este examen está vacío, elige otro modelo.", show_alert=True)
        return

    # Guardamos el estado del examen por usuario
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
        from telebot import types
        markup = types.InlineKeyboardMarkup(row_width=1)
        opciones = list(p['o'])
        random.shuffle(opciones)
        for opcion in opciones:
            es_correcta = "si" if opcion == p['r'] else "no"
            markup.add(types.InlineKeyboardButton(opcion, callback_data=f"res_{es_correcta}"))
        
        texto_pregunta = f"📖 **{datos['nombre_materia']}**\n\n❓ **Pregunta {datos['actual'] + 1} de {len(datos['preguntas'])}:**\n\n{p['p']}"
        bot.send_message(chat_id, texto_pregunta, reply_markup=markup, parse_mode="Markdown")
    else:
        finalizar_examen(chat_id)

@bot.callback_query_handler(func=lambda call: call.data.startswith('res_'))
def procesar_respuesta(call):
    chat_id = call.message.chat.id
    if chat_id not in user_stats: return
    datos = user_stats[chat_id]

    if call.data == "res_si":
        datos['aciertos'] += 1
        bot.answer_callback_query(call.id, "✅ ¡Correcto!", show_alert=False)
    else:
        datos['fallos'] += 1
        bot.answer_callback_query(call.id, "💡 Intenta la siguiente", show_alert=False)

    bot.delete_message(chat_id, call.message.message_id)
    datos['actual'] += 1
    enviar_pregunta(chat_id)

def finalizar_examen(chat_id):
    res = user_stats[chat_id]
    nota = res['aciertos']
    total = len(res['preguntas'])
    registrar_resultado(chat_id, res['aciertos'], res['fallos'])

    if nota == total:
        frase = "🏆 ¡Perfecto! Eres un genio."
    elif nota >= total*0.7:
        frase = "🥈 Muy bien, casi lo logras."
    else:
        frase = "💪 No te rindas, sigue practicando."

    bot.send_message(chat_id, f"🏁 **Examen terminado**\nHas acertado **{nota}** de {total} preguntas.\n{frase}\n\nPulsa /menu para volver a jugar.", parse_mode="Markdown")
    del user_stats[chat_id]

@bot.callback_query_handler(func=lambda call: call.data == "ver_estadisticas")
def mostrar_estadisticas(call):
    stats = ver_estadisticas(call.message.chat.id)
    texto = f"📊 **Tus estadísticas:**\n\n"
    texto += f"✅ Aciertos totales: {stats['aciertos']}\n"
    texto += f"❌ Fallos totales: {stats['fallos']}\n"
    texto += f"📝 Intentos de examen: {stats['intentos']}\n\nPulsa /menu para volver."
    bot.edit_message_text(texto, call.message.chat.id, call.message.message_id, parse_mode="Markdown")

# ===============================
# 🔗 Flask Webhook
# ===============================
@app.route(f"/webhook/{TOKEN}", methods=['POST'])
def webhook():
    json_str = request.get_data().decode('utf-8')
    update = telebot.types.Update.de_json(json_str)
    bot.process_new_updates([update])
    return "", 200

@app.route("/")
def index():
    bot.remove_webhook()
    bot.set_webhook(url=f"{PUBLIC_URL}/webhook/{TOKEN}")
    return f"Webhook configurado en: {PUBLIC_URL}/webhook/{TOKEN}"

# ===============================
# ⚡ Arranque para pruebas locales
# ===============================
if __name__ == "__main__":
    bot.remove_webhook()
    bot.set_webhook(url=f"http://127.0.0.1:{PORT}/webhook/{TOKEN}")
    app.run(host="0.0.0.0", port=PORT)
