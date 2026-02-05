import telebot
from telebot.types import InlineKeyboardMarkup, InlineKeyboardButton
import os
import time

# 1. Configuración del Token
TOKEN = os.getenv("8441666201:AAHygO1Osx5IdxnmQpQuF__Y8WyGvBKhr4U")
bot = telebot.TeleBot("8441666201:AAHygO1Osx5IdxnmQpQuF__Y8WyGvBKhr4U")

# 2. Base de datos de preguntas
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

# Diccionario para estados
user_states = {}

@bot.message_handler(commands=['start'])
def start(message):
    uid = str(message.from_user.id)
    user_states[uid] = {'pregunta': 0, 'aciertos': 0}
    bot.send_message(message.chat.id, "🎓 *EXAMEN DETERMINANTES*\nResponde a las 10 preguntas.", parse_mode="Markdown")
    enviar_p(uid, message.chat.id)

def enviar_p(uid, chat_id):
    idx = user_states[uid]['pregunta']
    
    if idx >= 10:
        nota = user_states[uid]['aciertos']
        bot.send_message(chat_id, f"🏁 *FINALIZADO*\n✅ Puntuación: {nota}/10\n\nEscribe /start para empezar de nuevo.", parse_mode="Markdown")
        return

    p = preguntas[idx]
    markup = InlineKeyboardMarkup(row_width=1)
    
    for i, opcion in enumerate(p['o']):
        # callback_data simplificado: ej "0-1" (pregunta 0, opción 1)
        markup.add(InlineKeyboardButton(opcion, callback_data=f"{idx}-{i}"))
    
    bot.send_message(chat_id, f"📝 *Pregunta {idx+1}/10*\n\n{p['p']}", reply_markup=markup, parse_mode="Markdown")

@bot.callback_query_handler(func=lambda call: True)
def manejar_respuesta(call):
    uid = str(call.from_user.id)
    
    if uid not in user_states:
        return

    # Extraemos datos evitando el crash
    try:
        info = call.data.split('-')
        p_idx = int(info[0])
        r_idx = int(info[1])
    except:
        return

    estado = user_states[uid]

    # Evitar respuestas duplicadas
    if p_idx != estado['pregunta']:
        bot.answer_callback_query(call.id, "Ya respondiste a esta pregunta.")
        return

    # Quitar botones
    bot.edit_message_reply_markup(call.message.chat.id, call.message.message_id, reply_markup=None)

    # Lógica de corrección
    correcta = preguntas[p_idx]['c']
    if r_idx == correcta:
        estado['aciertos'] += 1
        bot.send_message(call.message.chat.id, "✅ *¡CORRECTO!*", parse_mode="Markdown")
    else:
        solucion = preguntas[p_idx]['o'][correcta]
        bot.send_message(call.message.chat.id, f"❌ *Incorrecto*\nLa respuesta era: {solucion}", parse_mode="Markdown")

    # Siguiente pregunta
    estado['pregunta'] += 1
    time.sleep(0.5)
    enviar_p(uid, call.message.chat.id)

# Arrancar el bot con sistema de autorecuperación
if __name__ == "__main__":
    print("Bot activo...")
    bot.infinity_polling(timeout=10, long_polling_timeout=5)
