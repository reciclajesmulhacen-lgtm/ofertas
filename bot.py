import telebot
from telebot.types import InlineKeyboardMarkup, InlineKeyboardButton
import os
import time

TOKEN = os.getenv("8441666201:AAHygO1Osx5IdxnmQpQuF__Y8WyGvBKhr4U")
if not TOKEN:
    print("8441666201:AAHygO1Osx5IdxnmQpQuF__Y8WyGvBKhr4U")
    exit(1)

bot = telebot.TeleBot(TOKEN)

user_states = {}

preguntas = [
    {"id": 1, "p": "¿Qué indican los POSESIVOS?", "o": ["Distancia", "Pertenencia", "Cantidad"], "c": 1},
    {"id": 2, "p": "DEMONSTRATIVO de lejanía?", "o": ["Este", "Ese", "Aquel"], "c": 2},
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
    bot.send_message(message.chat.id, "🎓 EXAMEN DETERMINANTES\n10 preguntas - ¡Comienza!")
    siguiente_pregunta(uid, message.chat.id)

def siguiente_pregunta(uid, chat_id):
    if uid not in user_states:
        return
        
    estado = user_states[uid]
    idx = estado['pregunta']
    
    if idx >= 10:
        nota = estado['aciertos']
        resultado = "¡PERFECCIÓN!" if nota == 10 else f"Nota: {nota}/10"
        bot.send_message(chat_id, f"🏁 FINALIZADO\n✅ {nota}/10\n\n{resultado}\n\n/start nuevo")
        del user_states[uid]
        return
    
    p = preguntas[idx]
    markup = InlineKeyboardMarkup(row_width=1)
    for i, opcion in enumerate(p['o']):
        markup.add(InlineKeyboardButton(opcion, callback_data=f"{idx}_{i}"))
    
    bot.send_message(chat_id, f"📝 {p['id']}/10\n\n{p['p']}", reply_markup=markup)

@bot.callback_query_handler(func=lambda call: True)
def respuesta(call):
    uid = str(call.from_user.id)
    chat_id = call.message.chat.id
    
    if uid not in user_states:
        return
        
    datos = call.data.split('_')
    idx = int(datos[0])
    respuesta = int(datos[1])
    
    estado = user_states[uid]
    
    if idx != estado['pregunta']:
        bot.answer_callback_query(call.id, "Ya respondiste")
        return
    
    p = preguntas[idx]
    correcta = p['c']
    
    bot.edit_message_reply_markup(chat_id, call.message.message_id, reply_markup=None)
    
    if respuesta == correcta:
        estado['aciertos'] += 1
        bot.send_message(chat_id, "✅ ¡CORRECTO!")
    else:
        bot.send_message(chat_id, f"❌ Incorrecto\nCorrecta: {p['o'][correcta]}")
    
    estado['pregunta'] += 1
    time.sleep(1)
    siguiente_pregunta(uid, chat_id)

print("Bot iniciado")
bot.infinity_polling(none_stop=True)
