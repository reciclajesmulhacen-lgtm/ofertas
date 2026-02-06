import os
import importlib.util
import sys
import random
from flask import Flask, request
import telebot
from telebot import types

# ===============================
# ⚠️ Configuración Crítica
# ===============================
token = os.environ.get("TELEGRAM_BOT_TOKEN")
# Desactivar hilos (threaded=False) es vital para estabilidad en Railway
bot = telebot.TeleBot(token, threaded=False)
app = Flask(__name__)
RAILWAY_URL = os.environ.get("RAILWAY_PUBLIC_DOMAIN")

user_stats = {} 

materias_display = {
    'lengua': '📚 LENGUA',
    'mates': '🔢 MATEMÁTICAS',
    'ciencias': '🧪 CIENCIAS',
    'ingles': '🇬🇧 INGLÉS',
    'frances': '🇫🇷 FRANCÉS'
}

# ===============================
# 🛠️ Funciones Visuales
# ===============================

def barra_progreso(actual, total):
    relleno = int((actual / total) * 10)
    return "🔹" * relleno + "🔸" * (10 - relleno) + f" {int((actual/total)*100)}%"

def generar_markup_pregunta(preguntas, idx):
    try:
        pregunta = preguntas[idx]
        markup = types.InlineKeyboardMarkup(row_width=1)
        opciones = list(pregunta['o'])
        random.shuffle(opciones)
        for opcion in opciones:
            es_correcta = 1 if opcion == pregunta['r'] else 0
            markup.add(types.InlineKeyboardButton(opcion, callback_data=f"ans:{es_correcta}:{idx}"))
        markup.add(types.InlineKeyboardButton("🛑 ABANDONAR", callback_data="menu_principal"))
        return markup
    except:
        return None

# ===============================
# 🚀 Handlers Corregidos
# ===============================

@bot.message_handler(commands=['start', 'menu'])
@bot.callback_query_handler(func=lambda call: call.data == "menu_principal")
def menu_principal(obj):
    is_cb = isinstance(obj, types.CallbackQuery)
    chat_id = obj.message.chat.id if is_cb else obj.chat.id
    if chat_id in user_stats: del user_stats[chat_id]
    
    markup = types.InlineKeyboardMarkup(row_width=1)
    for idx, nom in materias_display.items():
        markup.add(types.InlineKeyboardButton(nom, callback_data=f"mat:{idx}"))
    
    texto = "🎓 *CENTRO DE ESTUDIOS VIRTUAL*\n\nSelecciona una materia para comenzar:"
    if is_cb:
        bot.edit_message_text(texto, chat_id, obj.message.message_id, reply_markup=markup, parse_mode='Markdown')
    else:
        bot.send_message(chat_id, texto, reply_markup=markup, parse_mode='Markdown')

@bot.callback_query_handler(func=lambda call: call.data.startswith('mat:'))
def mostrar_temas(call):
    m_id = call.data.split(':')[1]
    try:
        # Forzar limpieza de caché del módulo
        if m_id in sys.modules: del sys.modules[m_id]
        spec = importlib.util.spec_from_file_location(m_id, f"{m_id}.py")
        module = importlib.util.module_from_spec(spec)
        spec.loader.exec_module(module)
        temario = getattr(module, "TEMARIO")
        
        markup = types.InlineKeyboardMarkup(row_width=1)
        for tema in temario.keys():
            markup.add(types.InlineKeyboardButton(f"📂 {tema}", callback_data=f"tema:{m_id}:{tema}"))
        markup.add(types.InlineKeyboardButton("🔙 VOLVER", callback_data="menu_principal"))
        
        bot.edit_message_text(f"📖 *MATERIA:* {materias_display[m_id]}\n\nSelecciona un tema:", 
                             call.message.chat.id, call.message.message_id, reply_markup=markup, parse_mode='Markdown')
    except:
        bot.answer_callback_query(call.id, "Error al cargar temario.")

@bot.callback_query_handler(func=lambda call: call.data.startswith('tema:'))
def mostrar_examenes(call):
    p = call.data.split(':')
    m_id, t_nombre = p[1], p[2]
    markup = types.InlineKeyboardMarkup(row_width=3)
    btns = [types.InlineKeyboardButton(f"📝 Ex {i+1}", callback_data=f"ex:{m_id}:{t_nombre}:{i}") for i in range(3)]
    markup.add(*btns)
    markup.add(types.InlineKeyboardButton("🔙 VOLVER", callback_data=f"mat:{m_id}"))
    bot.edit_message_text(f"📍 *TEMA:* {t_nombre}\n\nElige un simulacro:", 
                         call.message.chat.id, call.message.message_id, reply_markup=markup, parse_mode='Markdown')

@bot.callback_query_handler(func=lambda call: call.data.startswith('ex:'))
def iniciar_examen(call):
    p = call.data.split(':')
    m_id, t_nombre, ex_idx = p[1], p[2], int(p[3])
    module = sys.modules.get(m_id)
    preguntas = getattr(module, "TEMARIO")[t_nombre]['examenes'][ex_idx]
    
    user_stats[call.message.chat.id] = {'preguntas': preguntas, 'indice': 0, 'aciertos': 0, 'fallos': 0}
    
    markup = generar_markup_pregunta(preguntas, 0)
    texto = (f"📝 *EXAMEN:* {t_nombre}\nPregunta 1 de {len(preguntas)}\n"
             f"{barra_progreso(1, len(preguntas))}\n\n*P:* {preguntas[0]['p']}")
    bot.edit_message_text(texto, call.message.chat.id, call.message.message_id, reply_markup=markup, parse_mode='Markdown')

@bot.callback_query_handler(func=lambda call: call.data.startswith('ans:'))
def manejar_respuesta(call):
    chat_id = call.message.chat.id
    datos = user_stats.get(chat_id)
    if not datos: return bot.answer_callback_query(call.id, "Sesión caducada.")

    p = call.data.split(':')
    if int(p[2]) != datos['indice']: return # Anti-doble clic
    
    if int(p[1]): datos['aciertos'] += 1
    else: datos['fallos'] += 1

    datos['indice'] += 1
    if datos['indice'] < len(datos['preguntas']):
        idx = datos['indice']
        markup = generar_markup_pregunta(datos['preguntas'], idx)
        texto = (f"📝 *PROGRESO:* {barra_progreso(idx+1, len(datos['preguntas']))}\n\n"
                 f"*P:* {datos['preguntas'][idx]['p']}")
        bot.edit_message_text(texto, chat_id, call.message.message_id, reply_markup=markup, parse_mode='Markdown')
    else:
        resumen = (f"🏁 *¡FIN!*\n\nAciertos: `{datos['aciertos']}`\nNota: `{(datos['aciertos']/len(datos['preguntas']))*10:.1f}/10`")
        markup = types.InlineKeyboardMarkup()
        markup.add(types.InlineKeyboardButton("🔙 INICIO", callback_data="menu_principal"))
        bot.edit_message_text(resumen, chat_id, call.message.message_id, reply_markup=markup, parse_mode='Markdown')
        del user_stats[chat_id]

# ===============================
# 🌐 Servidor
# ===============================

@app.route(f'/{token}', methods=['POST'])
def get_message():
    json_string = request.get_data().decode('utf-8')
    update = telebot.types.Update.de_json(json_string)
    bot.process_new_updates([update])
    return "!", 200

@app.route("/")
def index(): return "Bot Online", 200

if __name__ == "__main__":
    port = int(os.environ.get("PORT", 8080))
    if RAILWAY_URL and token:
        bot.remove_webhook()
        bot.set_webhook(url=f"https://{RAILWAY_URL}/{token}")
    app.run(host="0.0.0.0", port=port)
