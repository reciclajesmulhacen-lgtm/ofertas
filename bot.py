import telebot
from telebot.types import InlineKeyboardMarkup, InlineKeyboardButton
import os
import time

# 1. Configuración del Token
TOKEN = os.getenv("8441666201:AAHygO1Osx5IdxnmQpQuF__Y8WyGvBKhr4U")
bot = telebot.TeleBot("8441666201:AAHygO1Osx5IdxnmQpQuF__Y8WyGvBKhr4U")

# 2. Base de datos: Tema 3 - Versoladas (FanFest 5º)
preguntas = [
    {"p": "1. ¿Cómo se llama cada una de las líneas que forman un poema?", "o": ["Párrafo", "Verso", "Enlace"], "c": 1},
    {"p": "2. ¿Cómo se llama el conjunto de versos de un poema?", "o": ["Estrofa", "Capítulo", "Oración"], "c": 0},
    {"p": "3. Si dos palabras repiten sonidos a partir de la tónica, decimos que tienen...", "o": ["Ritmo", "Rima", "Métrica"], "c": 1},
    {"p": "4. En 'La niña lee', ¿qué tipo de determinante es 'La'?", "o": ["Artículo determinado", "Artículo indeterminado", "Demostrativo"], "c": 0},
    {"p": "5. ¿Cuál de estos es un determinante POSESIVO de varios poseedores?", "o": ["Mi", "Tu", "Nuestro"], "c": 2},
    {"p": "6. 'Aquella estrella'. ¿Qué distancia indica este demostrativo?", "o": ["Cercanía", "Distancia media", "Lejanía"], "c": 2},
    {"p": "7. ¿Cuál es la regla de la H para palabras como 'hielo' o 'huevo'?", "o": ["Llevan H por empezar por hie- o hue-", "No llevan H", "Llevan H solo al final"], "c": 0},
    {"p": "8. ¿Cómo se escriben las formas de los verbos haber, hacer y hablar?", "o": ["Siempre con H", "Sin H", "Con H solo en el pasado"], "c": 0},
    {"p": "9. ¿Qué palabra está bien escrita siguiendo la regla de la H muda?", "o": ["Ipopótamo", "Hipopótamo", "Ablamos"], "c": 1},
    {"p": "10. ¿Cómo se llama la rima en la que solo se repiten las VOCALES?", "o": ["Rima consonante", "Rima asonante", "Rima libre"], "c": 1}
]

user_states = {}

@bot.message_handler(commands=['start'])
def start(message):
    uid = str(message.from_user.id)
    user_states[uid] = {'pregunta': 0, 'aciertos': 0}
    bot.send_message(message.chat.id, "🎭 *EXAMEN TEMA 3: VERSOLADAS*\n¡Prepárate para demostrar lo que sabes de poesía y lengua!", parse_mode="Markdown")
    enviar_p(uid, message.chat.id)

def enviar_p(uid, chat_id):
    idx = user_states[uid]['pregunta']
    if idx >= 10:
        nota = user_states[uid]['aciertos']
        bot.send_message(chat_id, f"🏁 *¡EXAMEN FINALIZADO!*\n✅ Nota final: {nota}/10", parse_mode="Markdown")
        return
    p = preguntas[idx]
    markup = InlineKeyboardMarkup(row_width=1)
    for i, opcion in enumerate(p['o']):
        markup.add(InlineKeyboardButton(opcion, callback_data=f"{idx}-{i}"))
    bot.send_message(chat_id, f"📝 *Pregunta {idx+1} de 10*\n\n{p['p']}", reply_markup=markup, parse_mode="Markdown")

@bot.callback_query_handler(func=lambda call: True)
def respuesta(call):
    uid = str(call.from_user.id)
    if uid not in user_states: return
    try:
        info = call.data.split('-')
        p_idx, r_idx = int(info[0]), int(info[1])
    except: return
    if p_idx != user_states[uid]['pregunta']: return
    bot.edit_message_reply_markup(call.message.chat.id, call.message.message_id, reply_markup=None)
    if r_idx == preguntas[p_idx]['c']:
        user_states[uid]['aciertos'] += 1
        bot.send_message(call.message.chat.id, "✅ *¡Muy bien hecho!*")
    else:
        bot.send_message(call.message.chat.id, f"❌ *No es correcto.*\nLa buena era: {preguntas[p_idx]['o'][preguntas[p_idx]['c']]}")
    user_states[uid]['pregunta'] += 1
    time.sleep(1)
    enviar_p(uid, call.message.chat.id)

if __name__ == "__main__":
    bot.infinity_polling(timeout=10, long_polling_timeout=5)
