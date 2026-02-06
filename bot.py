import os
import importlib.util
import sys
import random
from flask import Flask, request
import telebot
from telebot import types

# 1. Configuración básica sin hilos para evitar cuelgues en Railway
token = os.environ.get("TELEGRAM_BOT_TOKEN")
bot = telebot.TeleBot(token, threaded=False)
app = Flask(__name__)
RAILWAY_URL = os.environ.get("RAILWAY_PUBLIC_DOMAIN")

user_stats = {}

# 2. Menú Principal
@bot.message_handler(commands=['start', 'menu'])
@bot.callback_query_handler(func=lambda call: call.data == "menu")
def menu_principal(obj):
    chat_id = obj.message.chat.id if isinstance(obj, types.CallbackQuery) else obj.chat.id
    if chat_id in user_stats: del user_stats[chat_id]
    markup = types.InlineKeyboardMarkup(row_width=1)
    # Materias
    for k in ['lengua', 'mates', 'ciencias', 'ingles', 'frances']:
        markup.add(types.InlineKeyboardButton(k.upper(), callback_data=f"mat_{k}"))
    
    if isinstance(obj, types.CallbackQuery):
        bot.edit_message_text("Elige Materia:", chat_id, obj.message.message_id, reply_markup=markup)
    else:
        bot.send_message(chat_id, "Elige Materia:", reply_markup=markup)

# 3. Cargar Temas del archivo (ej: lengua.py)
@bot.callback_query_handler(func=lambda call: call.data.startswith('mat_'))
def mostrar_temas(call):
    m_id = call.data.replace('mat_', '')
    try:
        spec = importlib.util.spec_from_file_location(m_id, f"{m_id}.py")
        module = importlib.util.module_from_spec(spec)
        spec.loader.exec_module(module)
        temario = getattr(module, "TEMARIO")
        
        markup = types.InlineKeyboardMarkup(row_width=1)
        for tema in temario.keys():
            markup.add(types.InlineKeyboardButton(tema, callback_data=f"tem_{m_id}_{tema}"))
        markup.add(types.InlineKeyboardButton("🔙 Volver", callback_data="menu"))
        bot.edit_message_text(f"Materia: {m_id}", call.message.chat.id, call.message.message_id, reply_markup=markup)
    except:
        bot.answer_callback_query(call.id, "Error al cargar archivo")

# 4. Seleccionar Examen (0, 1 o 2)
@bot.callback_query_handler(func=lambda call: call.data.startswith('tem_'))
def mostrar_examenes(call):
    p = call.data.split('_')
    m_id, t_id = p[1], p[2]
    markup = types.InlineKeyboardMarkup(row_width=1)
    for i in range(3):
        markup.add(types.InlineKeyboardButton(f"Examen {i+1}", callback_data=f"ex_{m_id}_{t_id}_{i}"))
    markup.add(types.InlineKeyboardButton("🔙 Volver", callback_data=f"mat_{m_id}"))
    bot.edit_message_text(f"Tema: {t_id}", call.message.chat.id, call.message.message_id, reply_markup=markup)

# 5. Iniciar y lanzar preguntas
@bot.callback_query_handler(func=lambda call: call.data.startswith('ex_'))
def iniciar_examen(call):
    p = call.data.split('_')
    m_id, t_id, ex_idx = p[1], p[2], int(p[3])
    
    spec = importlib.util.spec_from_file_location(m_id, f"{m_id}.py")
    module = importlib.util.module_from_spec(spec)
    spec.loader.exec_module(module)
    
    preguntas = getattr(module, "TEMARIO")[t_id]['examenes'][ex_idx]
    user_stats[call.message.chat.id] = {'lista': preguntas, 'index': 0, 'ok': 0}
    lanzar_pregunta(call.message.chat.id, call.message.message_id)

def lanzar_pregunta(chat_id, msg_id):
    u = user_stats[chat_id]
    pre = u['lista'][u['index']]
    markup = types.InlineKeyboardMarkup(row_width=1)
    for o in pre['o']:
        # Solo pasamos si es correcto o no (0 o 1)
        es_r = 1 if o == pre['r'] else 0
        markup.add(types.InlineKeyboardButton(o, callback_data=f"ans_{es_r}"))
    
    bot.edit_message_text(f"Pregunta {u['index']+1}:\n{pre['p']}", chat_id, msg_id, reply_markup=markup)

# 6. Procesar respuestas
@bot.callback_query_handler(func=lambda call: call.data.startswith('ans_'))
def respuesta(call):
    chat_id = call.message.chat.id
    if chat_id not in user_stats: return
    
    u = user_stats[chat_id]
    if call.data == "ans_1": u['ok'] += 1
    
    u['index'] += 1
    if u['index'] < len(u['lista']):
        lanzar_pregunta(chat_id, call.message.message_id)
    else:
        res = f"¡Terminado!\nAciertos: {u['ok']}/{len(u['lista'])}"
        markup = types.InlineKeyboardMarkup()
        markup.add(types.InlineKeyboardButton("Menú", callback_data="menu"))
        bot.edit_message_text(res, chat_id, call.message.message_id, reply_markup=markup)
        del user_stats[chat_id]

# 7. Webhook para Railway
@app.route(f'/{token}', methods=['POST'])
def webhook():
    bot.process_new_updates([telebot.types.Update.de_json(request.get_data().decode('utf-8'))])
    return "!", 200

if __name__ == "__main__":
    if RAILWAY_URL: bot.set_webhook(url=f"https://{RAILWAY_URL}/{token}")
    app.run(host="0.0.0.0", port=int(os.environ.get("PORT", 8080)))
