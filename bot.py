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

def generar_markup_pregunta(preguntas, idx):
    pregunta = preguntas[idx]
    markup = types.InlineKeyboardMarkup(row_width=1)
    for opcion in pregunta['o']:
        es_correcta = 1 if opcion == pregunta['r'] else 0
        # Guardamos solo lo mínimo para evitar errores de longitud en callback_data
        markup.add(types.InlineKeyboardButton(opcion, callback_data=f"ans|{es_correcta}|{idx}"))
    markup.add(types.InlineKeyboardButton("🔙 Cancelar Examen", callback_data="menu_principal"))
    return markup

# ===============================
# 🚀 Handlers (Navegación)
# ===============================

@bot.message_handler(commands=['start', 'menu'])
@bot.callback_query_handler(func=lambda call: call.data == "menu_principal")
def menu_principal(obj):
    is_callback = isinstance(obj, types.CallbackQuery)
    chat_id = obj.message.chat.id if is_callback else obj.chat.id
    if chat_id in user_stats: del user_stats[chat_id]
    
    markup = types.InlineKeyboardMarkup(row_width=2)
    botones = [types.InlineKeyboardButton(nom, callback_data=f"mat|{idx}") for idx, nom in materias_display.items()]
    markup.add(*botones)
    markup.add(types.InlineKeyboardButton("📊 Mis Estadísticas", callback_data="ver_estadisticas"))
    
    texto = "👋 *Menú Principal*\nSelecciona una materia:"
    try:
        if is_callback:
            bot.edit_message_text(texto, chat_id, obj.message.message_id, reply_markup=markup, parse_mode='Markdown')
        else:
            bot.send_message(chat_id, texto, reply_markup=markup, parse_mode='Markdown')
    except:
        bot.send_message(chat_id, texto, reply_markup=markup, parse_mode='Markdown')

@bot.callback_query_handler(func=lambda call: call.data.startswith('mat|'))
def mostrar_temas(call):
    materia_id = call.data.split('|')[1]
    try:
        spec = importlib.util.spec_from_file_location(materia_id, f"{materia_id}.py")
        module = importlib.util.module_from_spec(spec)
        sys.modules[materia_id] = module
        spec.loader.exec_module(module)
        temario = getattr(module, "TEMARIO")
        
        markup = types.InlineKeyboardMarkup(row_width=1)
        for tema in temario.keys():
            markup.add(types.InlineKeyboardButton(f"📂 {tema}", callback_data=f"tema|{materia_id}|{tema}"))
        markup.add(types.InlineKeyboardButton("🔙 Volver", callback_data="menu_principal"))
        
        bot.edit_message_text(f"📖 *{materias_display[materia_id]}*\nSelecciona un tema:", 
                             call.message.chat.id, call.message.message_id, reply_markup=markup, parse_mode='Markdown')
    except Exception as e:
        bot.answer_callback_query(call.id, f"Error: {str(e)}")

@bot.callback_query_handler(func=lambda call: call.data.startswith('tema|'))
def mostrar_examenes(call):
    partes = call.data.split('|')
    m_id, t_nombre = partes[1], partes[2]
    markup = types.InlineKeyboardMarkup(row_width=3)
    for i in range(3):
        markup.add(types.InlineKeyboardButton(f"📝 Examen {i+1}", callback_data=f"ex|{m_id}|{t_nombre}|{i}"))
    markup.add(types.InlineKeyboardButton("🔙 Volver", callback_data=f"mat|{m_id}"))
    bot.edit_message_text(f"📍 *Tema:* {t_nombre}\nElige un examen:", 
                         call.message.chat.id, call.message.message_id, reply_markup=markup, parse_mode='Markdown')

@bot.callback_query_handler(func=lambda call: call.data.startswith('ex|'))
def iniciar_examen(call):
    partes = call.data.split('|')
    m_id, t_nombre, ex_idx = partes[1], partes[2], int(partes[3])
    module = sys.modules.get(m_id)
    preguntas = getattr(module, "TEMARIO")[t_nombre]['examenes'][ex_idx]
    
    user_stats[call.message.chat.id] = {
        'preguntas': preguntas,
        'indice': 0, 'aciertos': 0, 'fallos': 0
    }
    
    markup = generar_markup_pregunta(preguntas, 0)
    bot.edit_message_text(f"❓ *Pregunta 1 de {len(preguntas)}:*\n\n{preguntas[0]['p']}", 
                         call.message.chat.id, call.message.message_id, reply_markup=markup, parse_mode='Markdown')

@bot.callback_query_handler(func=lambda call: call.data.startswith('ans|'))
def manejar_respuesta(call):
    chat_id = call.message.chat.id
    datos = user_stats.get(chat_id)
    if not datos: 
        bot.answer_callback_query(call.id, "Sesión expirada")
        return

    partes = call.data.split('|')
    es_correcta = int(partes[1])
    idx_click = int(partes[2])

    if idx_click != datos['indice']:
        bot.answer_callback_query(call.id, "Botón antiguo ignorado")
        return

    if es_correcta:
        datos['aciertos'] += 1
        bot.answer_callback_query(call.id, "✅ ¡Correcto!")
    else:
        datos['fallos'] += 1
        bot.answer_callback_query(call.id, "❌ Incorrecto.")

    datos['indice'] += 1
    if datos['indice'] < len(datos['preguntas']):
        nuevo_idx = datos['indice']
        markup = generar_markup_pregunta(datos['preguntas'], nuevo_idx)
        bot.edit_message_text(f"❓ *Pregunta {nuevo_idx+1} de {len(datos['preguntas'])}:*\n\n{datos['preguntas'][nuevo_idx]['p']}", 
                             chat_id, call.message.message_id, reply_markup=markup, parse_mode='Markdown')
    else:
        registrar_resultado(chat_id, datos['aciertos'], datos['fallos'])
        resumen = f"🏁 *¡Fin del Examen!*\n\n✅ Aciertos: {datos['aciertos']}\n❌ Fallos: {datos['fallos']}"
        markup = types.InlineKeyboardMarkup()
        markup.add(types.InlineKeyboardButton("🔙 Menú Principal", callback_data="menu_principal"))
        bot.edit_message_text(resumen, chat_id, call.message.message_id, reply_markup=markup, parse_mode='Markdown')
        del user_stats[chat_id]

@bot.callback_query_handler(func=lambda call: call.data == 'ver_estadisticas')
def ver_estadisticas(call):
    s = estadisticas.get(call.message.chat.id, {'aciertos': 0, 'fallos': 0, 'intentos': 0})
    markup = types.InlineKeyboardMarkup()
    markup.add(types.InlineKeyboardButton("🔙 Volver", callback_data="menu_principal"))
    msg = f"📊 *Estadísticas*\n\n🔹 Intentos: {s['intentos']}\n✅ Total Aciertos: {s['aciertos']}\n❌ Fallos: {s['fallos']}"
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
