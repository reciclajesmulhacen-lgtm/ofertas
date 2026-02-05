import telebot
from telebot.types import InlineKeyboardMarkup, InlineKeyboardButton
import os
import time

# Obtención del Token
TOKEN = os.getenv("8441666201:AAHygO1Osx5IdxnmQpQuF__Y8WyGvBKhr4U")
if not TOKEN:
    print("8441666201:AAHygO1Osx5IdxnmQpQuF__Y8WyGvBKhr4U")
    exit(1)

bot = telebot.TeleBot(TOKEN)

user_states = {}

preguntas = [
    {"id": 1, "p": "¿Qué indican los POSESIVOS?", "o": ["Distancia", "Pertenencia", "Cantidad"], "c": 1},
    {"id": 2, "p": "DEMOSTRATIVO de lejanía?", "o": ["Este", "Ese", "Aquel"], "c": 2},
    {"id": 3, "p": "'Unas mesas' = ?", "o": ["Indeterminado", "Determinado", "Numeral"], "c": 0},
    {"id": 4, "p": "'primero, segundo' = ?", "o": ["Cardinales", "Ordinales", "Indefinidos"], "c": 1},
    {"id": 5, "p": "Determinante INDEFINIDO?", "o": ["Varios", "Tres", "Los"], "c": 0},
    {"id": 6, "p": "DETERMINADO masc. plural?", "o": ["Unos", "Los", "Estos"], "c": 1},
    {"id": 7, "p": "'vuestra' = ?", "o": ["1 poseedor", "Varios poseedores", "Cercanía"], "c": 1},
    {"id": 8, "p": "'Ese estuche' = ?", "o": ["Cerca", "Distancia media", "Lejos"], "c": 1},
    {"id": 9, "p": "Numeral CARDINAL?", "o": ["Sexto", "Muchos", "Diez"], "c": 2},
    {"id": 10, "p": "DETERMINADO fem. singular?", "o": ["Una", "La", "Esa"], "c": 1}
]

@bot.message_handler(commands=['start'])
def start(message):
    uid = str(message.from_user.id)
    user_states[uid] = {'pregunta': 0, 'aciertos': 0}
    bot.send_message(message.chat.id, "🎓 *EXAMEN DETERMINANTES*\n10 preguntas - ¡Comienza!", parse_mode="Markdown")
    siguiente_pregunta(uid, message.chat.id)

def siguiente_pregunta(uid, chat_id):
    if uid not in user_states: return
    
    estado = user_states[uid]
    idx = estado['pregunta']
    
    if idx >= 10:
        nota = estado['aciertos']
        bot.send_message(chat_id, f"🏁 *FINALIZADO*\n✅ Aciertos: {nota}/10\n\nUsa /start para repetir.", parse_mode="Markdown")
        del user_states[uid]
        return
    
    p = preguntas[idx]
    markup = InlineKeyboardMarkup(row_width=1)
    for i, opcion in enumerate(p['o']):
        # El callback_data guarda "pregunta_respuesta"
        markup.add(InlineKeyboardButton(opcion, callback_data=f"{idx}_{i}"))
    
    bot.send_message(chat_id, f"📝 *Pregunta {p['id']}/10*\n\n{p['p']}", reply_markup=markup, parse_mode="Markdown")

@bot.callback_query_handler(func=lambda call: True)
def respuesta(call):
    uid = str(call.from_user.id)
    chat_id = call.message.chat.id
    
    if uid not in user_states: return
        
    # CORRECCIÓN AQUÍ: Separamos y convertimos a entero correctamente
    try:
        data_parts = call.data.split('_')
        idx_pregunta = int(data_parts[0])
        idx_respuesta = int(data_parts[1])
    except:
        return

    estado = user_states[uid]
    
    # Si la pregunta no es la que toca, ignoramos para evitar fallos
    if idx_pregunta != estado['pregunta']:
        bot.answer_callback_query(call.id, "Esa pregunta ya pasó")
        return
    
    # Quitamos botones para que no repita
    bot.edit_message_reply_markup(chat_id, call.message.message_id, reply_markup=None)
    
    p = preguntas[idx_pregunta]
    if idx_respuesta == p['c']:
        estado['aciertos'] += 1
        bot.send_message(chat_id, "✅ *¡CORRECTO!*", parse_mode="Markdown")
    else:
        bot.send_message(chat_id, f"❌ *Incorrecto*\nLa buena era: {p['o'][p['c']]}", parse_mode="Markdown")
    
    estado['pregunta'] += 1
    time.sleep(0.5)
    siguiente_pregunta(uid, chat_id)

print("Bot en marcha...")
bot.infinity_polling(timeout=10, long_polling_timeout=5)
