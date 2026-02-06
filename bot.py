import os
import importlib.util
import sys
import random
from flask import Flask, request
import telebot
from telebot import types

# ===============================
# ⚠️ Configuración
# ===============================
# Railway leerá "telegram_token" de las variables de entorno
token = os.environ.get("TELEGRAM_BOT_TOKEN")
bot = telebot.TeleBot(token)
app = Flask(__name__)

# URL de Railway (la genera Railway automáticamente en la pestaña Networking)
# Necesaria para que Telegram sepa a dónde enviar los mensajes
RAILWAY_URL = os.environ.get("RAILWAY_PUBLIC_DOMAIN", "")

# Datos en memoria (Se pierden al reiniciar)
user_stats = {} 
estadisticas = {}

materias_display = {
    'lengua': '📚 Lengua',
    'mates': '🔢 Matemáticas',
    'ciencias': '🧪 Ciencias',
    'ingles': '🇬🇧 Inglés',
    'frances': '🇫🇷 Francés'
}

# ===============================
# 🛠️ Funciones de Apoyo
# ===============================

def registrar_resultado(chat_id, aciertos, fallos):
    if chat_id not in estadisticas:
        estadisticas[chat_id] = {'aciertos': 0, 'fallos': 0, 'intentos': 0}
    estadisticas[chat_id]['aciertos'] += aciertos
    estadisticas[chat_id]['fallos'] += fallos
    estadisticas[chat_id]['intentos'] += 1

def enviar_pregunta(chat_id):
    datos = user_stats.get(chat_id)
    idx = datos['indice']
    pregunta = datos['preguntas'][idx]

    markup = types.InlineKeyboardMarkup(row_width=1)
    for opcion in pregunta['o']:
        es_correcta = 1 if opcion == pregunta['r'] else 0
        markup.add(types.InlineKeyboardButton(opcion, callback_data=f"ans_{es_correcta}"))
    
    markup.add(types.InlineKeyboardButton("🔙 Volver al Menú Principal", callback_data="menu_principal"))

    bot.send_message(
        chat_id, 
        f"📖 *Materia:* {materias_display[datos['materia']]}\n"
        f"❓ *Pregunta {idx+1}:*\n\n"
        f"{pregunta['p']}", 
        reply_markup=markup,
        parse_mode='Markdown'
    )

# ===============================
# 🚀 Handlers (Manejadores)
# ===============================

@bot.message_handler(commands=['start', 'menu'])
@bot.callback_query_handler(func=lambda call: call.data == "menu_principal")
def menu_principal(message):
    chat_id = message.chat.id if hasattr(message, 'chat') else message.message.chat.id
    
    if chat_id in user_stats:
        del user_stats[chat_id]
    
    markup = types.InlineKeyboardMarkup(row_width=2)
    botones = [types.InlineKeyboardButton(nom, callback_data=f"mat_{idx}") for idx, nom in materias_display.items()]
    markup.add(*botones)
    markup.add(types.InlineKeyboardButton("📊 Mis Estadísticas", callback_data="ver_estadisticas"))
    
    texto = "👋 *¡Hola! Bienvenido al Bot de Estudio.*\n\nSelecciona una materia para ponerte a prueba:"
    bot.send_message(chat_id, texto, reply_markup=markup, parse_mode='Markdown')

@bot.callback_query_handler(func=lambda call: call.data.startswith('mat_'))
def abrir_materia(call):
    # Corrección: split devuelve lista, tomamos el segundo elemento
    materia_id = call.data.split('_')[1] 
    try:
        spec = importlib.util.spec_from_file_location(materia_id, f"{materia_id}.py")
        module = importlib.util.module_from_spec(spec)
        sys.modules[materia_id] = module
        spec.loader.exec_module(module)
        
        temario = getattr(module, "TEMARIO")
        todas_preguntas = []
        for u in temario.values():
            for examen in u['examenes']:
                todas_preguntas.extend(examen)

        seleccionadas = random.sample(todas_preguntas, min(len(todas_preguntas), 5))

        user_stats[call.message.chat.id] = {
            'materia': materia_id,
            'preguntas': seleccionadas,
            'indice': 0, 'aciertos': 0, 'fallos': 0
        }
        enviar_pregunta(call.message.chat.id)

    except Exception as e:
        print(f"Error cargando materia: {e}")
        markup = types.InlineKeyboardMarkup()
        markup.add(types.InlineKeyboardButton("🔙 Volver al Menú", callback_data="menu_principal"))
        bot.send_message(call.message.chat.id, "⚠️ Error al cargar la materia. Verifica que el archivo existe.", reply_markup=markup)

@bot.callback_query_handler(func=lambda call: call.data.startswith('ans_'))
def manejar_respuesta(call):
    chat_id = call.message.chat.id
    datos = user_stats.get(chat_id)
    if not datos: 
        menu_principal(call)
        return

    es_correcta = int(call.data.split('_')[1])
    if es_correcta:
        datos['aciertos'] += 1
        bot.answer_callback_query(call.id, "✅ ¡Correcto!")
    else:
        datos['fallos'] += 1
        bot.answer_callback_query(call.id, "❌ Incorrecto.")

    datos['indice'] += 1
    if datos['indice'] < len(datos['preguntas']):
        enviar_pregunta(chat_id)
    else:
        registrar_resultado(chat_id, datos['aciertos'], datos['fallos'])
        markup = types.InlineKeyboardMarkup()
        markup.add(types.InlineKeyboardButton("🔙 Volver al Menú Principal", callback_data="menu_principal"))
        
        resumen = (f"🏁 *¡Examen Finalizado!*\n\n"
                  f"Materia: {materias_display[datos['materia']]}\n"
                  f"✅ Aciertos: {datos['aciertos']}\n"
                  f"❌ Fallos: {datos['fallos']}")
        
        bot.send_message(chat_id, resumen, reply_markup=markup, parse_mode='Markdown')
        del user_stats[chat_id]

@bot.callback_query_handler(func=lambda call: call.data == 'ver_estadisticas')
def ver_estadisticas(call):
    chat_id = call.message.chat.id
    s = estadisticas.get(chat_id, {'aciertos': 0, 'fallos': 0, 'intentos': 0})
    
    markup = types.InlineKeyboardMarkup()
    markup.add(types.InlineKeyboardButton("🔙 Volver al Menú Principal", callback_data="menu_principal"))
    
    msg = f"📊 *Tus Estadísticas*\n\n" \
          f"🔹 Intentos: {s['intentos']}\n" \
          f"✅ Total Aciertos: {s['aciertos']}\n" \
          f"❌ Total Fallos: {s['fallos']}"
    
    bot.send_message(chat_id, msg, reply_markup=markup, parse_mode='Markdown')

# ===============================
# 🌐 Configuración del Servidor Flask
# ===============================

@app.route(f'/{token}', methods=['POST'])
def get_message():
    if request.headers.get('content-type') == 'application/json':
        json_string = request.get_data().decode('utf-8')
        update = telebot.types.Update.de_json(json_string)
        bot.process_new_updates([update])
        return "!", 200
    else:
        return "error", 403

@app.route("/")
def index():
    # Establecer el webhook automáticamente al entrar a la URL
    if RAILWAY_URL:
        bot.remove_webhook()
        bot.set_webhook(url=f"https://{RAILWAY_URL}/{token}")
        return "Bot de estudio activo y Webhook configurado correctamente.", 200
    return "Bot funcionando, pero falta configurar RAILWAY_PUBLIC_DOMAIN.", 200

if __name__ == "__main__":
    # Railway asigna el puerto mediante la variable PORT
    port = int(os.environ.get("PORT", 5000))
    app.run(host="0.0.0.0", port=port)
