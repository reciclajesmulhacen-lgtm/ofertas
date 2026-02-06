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
token = os.environ.get("TELEGRAM_BOT_TOKEN")
bot = telebot.TeleBot(token)
app = Flask(__name__)
RAILWAY_URL = os.environ.get("RAILWAY_PUBLIC_DOMAIN")

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
    
    markup.add(types.InlineKeyboardButton("🔙 Cancelar Examen", callback_data="menu_principal"))

    bot.send_message(
        chat_id, 
        f"❓ *Pregunta {idx+1} de {len(datos['preguntas'])}:*\n\n{pregunta['p']}", 
        reply_markup=markup,
        parse_mode='Markdown'
    )

# ===============================
# 🚀 Handlers (Navegación)
# ===============================

# 1. Menú Principal (Materias)
@bot.message_handler(commands=['start', 'menu'])
@bot.callback_query_handler(func=lambda call: call.data == "menu_principal")
def menu_principal(message):
    chat_id = message.chat.id if hasattr(message, 'chat') else message.message.chat.id
    if chat_id in user_stats: del user_stats[chat_id]
    
    markup = types.InlineKeyboardMarkup(row_width=2)
    botones = [types.InlineKeyboardButton(nom, callback_data=f"mat_{idx}") for idx, nom in materias_display.items()]
    markup.add(*botones)
    markup.add(types.InlineKeyboardButton("📊 Mis Estadísticas", callback_data="ver_estadisticas"))
    
    texto = "👋 *Bienvenido.*\nSelecciona una materia:"
    if hasattr(message, 'chat'):
        bot.send_message(chat_id, texto, reply_markup=markup, parse_mode='Markdown')
    else:
        bot.edit_message_text(texto, chat_id, message.message_id, reply_markup=markup, parse_mode='Markdown')

# 2. Menú de Temas
@bot.callback_query_handler(func=lambda call: call.data.startswith('mat_'))
def mostrar_temas(call):
    materia_id = call.data.split('_')[1]
    try:
        spec = importlib.util.spec_from_file_location(materia_id, f"{materia_id}.py")
        module = importlib.util.module_from_spec(spec)
        sys.modules[materia_id] = module
        spec.loader.exec_module(module)
        
        temario = getattr(module, "TEMARIO")
        markup = types.InlineKeyboardMarkup(row_width=1)
        for tema in temario.keys():
            markup.add(types.InlineKeyboardButton(f"📂 {tema}", callback_data=f"tema_{materia_id}_{tema}"))
        markup.add(types.InlineKeyboardButton("🔙 Volver", callback_data="menu_principal"))
        
        bot.edit_message_text(f"📖 *{materias_display[materia_id]}*\nSelecciona un tema:", 
                             call.message.chat.id, call.message.message_id, reply_markup=markup, parse_mode='Markdown')
    except Exception as e:
        bot.answer_callback_query(call.id, "Error al cargar temas.")

# 3. Menú de Exámenes (1, 2 o 3)
@bot.callback_query_handler(func=lambda call: call.data.startswith('tema_'))
def mostrar_examenes(call):
    # Formato: tema_materia_nombretema
    partes = call.data.split('_')
    m_id, t_nombre = partes[1], partes[2]
    
    markup = types.InlineKeyboardMarkup(row_width=3)
    botones = [
        types.InlineKeyboardButton("📝 Examen 1", callback_data=f"ex_{m_id}_{t_nombre}_0"),
        types.InlineKeyboardButton("📝 Examen 2", callback_data=f"ex_{m_id}_{t_nombre}_1"),
        types.InlineKeyboardButton("📝 Examen 3", callback_data=f"ex_{m_id}_{t_nombre}_2")
    ]
    markup.add(*botones)
    markup.add(types.InlineKeyboardButton("🔙 Volver a Temas", callback_data=f"mat_{m_id}"))
    
    bot.edit_message_text(f"📍 *Tema:* {t_nombre}\nElige un examen:", 
                         call.message.chat.id, call.message.message_id, reply_markup=markup, parse_mode='Markdown')

# 4. Iniciar Examen seleccionado
@bot.callback_query_handler(func=lambda call: call.data.startswith('ex_'))
def iniciar_examen(call):
    partes = call.data.split('_')
    m_id, t_nombre, ex_idx = partes[1], partes[2], int(partes[3])
    
    module = sys.modules.get(m_id)
    preguntas = getattr(module, "TEMARIO")[t_nombre]['examenes'][ex_idx]

    user_stats[call.message.chat.id] = {
        'preguntas': preguntas,
        'indice': 0, 'aciertos': 0, 'fallos': 0, 'materia': m_id
    }
    
    bot.delete_message(call.message.chat.id, call.message.message_id)
    enviar_pregunta(call.message.chat.id)

# 5. Manejar respuestas
@bot.callback_query_handler(func=lambda call: call.data.startswith('ans_'))
def manejar_respuesta(call):
    chat_id = call.message.chat.id
    datos = user_stats.get(chat_id)
    if not datos: return

    es_correcta = int(call.data.split('_')[1])
    if es_correcta:
        datos['aciertos'] += 1
        bot.answer_callback_query(call.id, "✅ ¡Correcto!")
    else:
        datos['fallos'] += 1
        bot.answer_callback_query(call.id, "❌ Incorrecto.")

    datos['indice'] += 1
    if datos['indice'] < len(datos['preguntas']):
        bot.delete_message(chat_id, call.message.message_id)
        enviar_pregunta(chat_id)
    else:
        registrar_resultado(chat_id, datos['aciertos'], datos['fallos'])
        resumen = f"🏁 *¡Fin del Examen!*\n\n✅ Aciertos: {datos['aciertos']}\n❌ Fallos: {datos['fallos']}"
        markup = types.InlineKeyboardMarkup()
        markup.add(types.InlineKeyboardButton("🔙 Volver al Menú", callback_data="menu_principal"))
        bot.edit_message_text(resumen, chat_id, call.message.message_id, reply_markup=markup, parse_mode='Markdown')
        del user_stats[chat_id]

@bot.callback_query_handler(func=lambda call: call.data == 'ver_estadisticas')
def ver_estadisticas(call):
    s = estadisticas.get(call.message.chat.id, {'aciertos': 0, 'fallos': 0, 'intentos': 0})
    markup = types.InlineKeyboardMarkup()
    markup.add(types.InlineKeyboardButton("🔙 Volver", callback_data="menu_principal"))
    msg = f"📊 *Estadísticas*\n\n🔹 Intentos: {s['intentos']}\n✅ Aciertos: {s['aciertos']}\n❌ Fallos: {s['fallos']}"
    bot.edit_message_text(msg, call.message.chat.id, call.message.message_id, reply_markup=markup, parse_mode='Markdown')

# ===============================
# 🌐 Servidor y Webhook
# ===============================

@app.route(f'/{token}', methods=['POST'])
def get_message():
    if request.headers.get('content-type') == 'application/json':
        json_string = request.get_data().decode('utf-8')
        update = telebot.types.Update.de_json(json_string)
        bot.process_new_updates([update])
        return "!", 200
    return "error", 403

@app.route("/")
def index(): return "Bot Online", 200

if __name__ == "__main__":
    port = int(os.environ.get("PORT", 8080))
    if RAILWAY_URL and token:
        bot.remove_webhook()
        bot.set_webhook(url=f"https://{RAILWAY_URL}/{token}")
    app.run(host="0.0.0.0", port=port)
