import telebot
from telebot.types import InlineKeyboardMarkup, InlineKeyboardButton
import os
import time

# 1. Configuración del Token
TOKEN = os.getenv("8441666201:AAHygO1Osx5IdxnmQpQuF__Y8WyGvBKhr4U")
bot = telebot.TeleBot("8441666201:AAHygO1Osx5IdxnmQpQuF__Y8WyGvBKhr4U")

# 2. Base de datos de preguntas didácticas
preguntas = [
    {
        "id": 1, 
        "p": "🌟 ¿Cuál es la función principal de los determinantes POSESIVOS?", 
        "o": ["Indicar a qué distancia está algo", "Indicar a quién pertenece un objeto", "Decir el número exacto de cosas"], 
        "c": 1
    },
    {
        "id": 2, 
        "p": "📏 Si un objeto está MUY LEJOS de ti, ¿qué determinante demostrativo deberías usar?", 
        "o": ["Este (cercanía)", "Ese (distancia media)", "Aquel (lejanía)"], 
        "c": 2
    },
    {
        "id": 3, 
        "p": "🍎 En la frase 'Unas manzanas', ¿qué nos indica el artículo 'Unas'?", 
        "o": ["Que son unas manzanas cualquiera (Indeterminado)", "Que sabemos exactamente qué manzanas son (Determinado)", "Que solo hay una manzana"], 
        "c": 0
    },
    {
        "id": 4, 
        "p": "🥇 Los numerales que sirven para indicar el ORDEN en una fila (como primero o segundo) son...", 
        "o": ["Numerales Cardinales", "Numerales Ordinales", "Determinantes Indefinidos"], 
        "c": 1
    },
    {
        "id": 5, 
        "p": "❓ Si digo 'Varios amigos vinieron a casa', ¿qué tipo de determinante es 'Varios'?", 
        "o": ["Indefinido (no sabemos el número exacto)", "Numeral (sabemos cuántos son)", "Artículo determinado"], 
        "c": 0
    },
    {
        "id": 6, 
        "p": "👦 ¿Cuál de estos es un artículo DETERMINADO, masculino y plural?", 
        "o": ["Unos niños", "Los niños", "Estos niños"], 
        "c": 1
    },
    {
        "id": 7, 
        "p": "🏠 En la expresión 'Vuestra casa', el determinante indica que la casa pertenece a...", 
        "o": ["A una sola persona (un poseedor)", "A varias personas (varios poseedores)", "A nadie en particular"], 
        "c": 1
    },
    {
        "id": 8, 
        "p": "✏️ Si digo 'Ese estuche', ¿dónde se encuentra el estuche respecto a la persona que habla?", 
        "o": ["Muy cerca (cercanía)", "A una distancia media", "Muy lejos (lejanía)"], 
        "c": 1
    },
    {
        "id": 9, 
        "p": "🔢 ¿Qué tipo de numeral es el número 'Diez'?", 
        "o": ["Ordinal (indica orden)", "Indefinido (indica duda)", "Cardinal (indica una cantidad exacta)"], 
        "c": 2
    },
    {
        "id": 10, 
        "p": "🌸 ¿Cuál es el artículo DETERMINADO que acompaña a un sustantivo femenino y singular?", 
        "o": ["Una", "La", "Esa"], 
        "c": 1
    }
]

# Diccionario para estados
user_states = {}

@bot.message_handler(commands=['start'])
def start(message):
    uid = str(message.from_user.id)
    user_states[uid] = {'pregunta': 0, 'aciertos': 0}
    bot.send_message(message.chat.id, "🎓 *¡BIENVENIDO AL EXAMEN DEL TEMA 3!*\n\nLee cada pregunta con atención antes de responder. ¡Tú puedes!", parse_mode="Markdown")
    enviar_p(uid, message.chat.id)

def enviar_p(uid, chat_id):
    idx = user_states[uid]['pregunta']
    
    if idx >= 10:
        nota = user_states[uid]['aciertos']
        resultado = "🌈 ¡Excelente! Has dominado los determinantes." if nota >= 8 else "👍 ¡Buen intento! Repasa un poquito más."
        bot.send_message(chat_id, f"🏁 *EXAMEN COMPLETADO*\n\n✅ Aciertos: {nota}/10\n\n{resultado}\n\nEscribe /start para practicar de nuevo.", parse_mode="Markdown")
        return

    p = preguntas[idx]
    markup = InlineKeyboardMarkup(row_width=1)
    
    for i, opcion in enumerate(p['o']):
        markup.add(InlineKeyboardButton(opcion, callback_data=f"{idx}-{i}"))
    
    bot.send_message(chat_id, f"📝 *PREGUNTA {idx+1} de 10*\n\n{p['p']}", reply_markup=markup, parse_mode="Markdown")

@bot.callback_query_handler(func=lambda call: True)
def manejar_respuesta(call):
    uid = str(call.from_user.id)
    
    if uid not in user_states:
        return

    try:
        info = call.data.split('-')
        p_idx = int(info[0])
        r_idx = int(info[1])
    except:
        return

    estado = user_states[uid]

    if p_idx != estado['pregunta']:
        bot.answer_callback_query(call.id, "Ya has respondido esta pregunta.")
        return

    bot.edit_message_reply_markup(call.message.chat.id, call.message.message_id, reply_markup=None)

    correcta = preguntas[p_idx]['c']
    if r_idx == correcta:
        estado['aciertos'] += 1
        bot.send_message(call.message.chat.id, "✅ *¡Muy bien! Respuesta correcta.*", parse_mode="Markdown")
    else:
        solucion = preguntas[p_idx]['o'][correcta]
        bot.send_message(call.message.chat.id, f"❌ *No es correcto...*\n\nLa respuesta correcta era: *{solucion}*", parse_mode="Markdown")

    estado['pregunta'] += 1
    time.sleep(1) # Un segundo de pausa para que pueda leer la corrección
    enviar_p(uid, call.message.chat.id)

if __name__ == "__main__":
    print("Bot activo con preguntas didácticas...")
    bot.infinity_polling(timeout=10, long_polling_timeout=5)
