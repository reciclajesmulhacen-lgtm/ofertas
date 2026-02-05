import telebot
from telebot.types import InlineKeyboardMarkup, InlineKeyboardButton

TOKEN = "8441666201:AAHygO1Osx5IdxnmQpQuF__Y8WyGvBKhr4U"
bot = telebot.TeleBot(TOKEN)

# Base de datos del Tema 3 según el libro Edelvives FanFest 5
preguntas = [
    {
        "texto": "1. ¿Qué indican los determinantes POSESIVOS como 'nuestro'?",
        "opciones": ["La distancia", "A quién pertenece", "Una cantidad"],
        "correcta": 1,
        "explicacion": "¡Correcto! Los posesivos indican pertenencia."
    },
    {
        "texto": "2. ¿Cuál de estos es un determinante DEMOSTRATIVO de LEJANÍA?",
        "opciones": ["Este", "Ese", "Aquel"],
        "correcta": 2,
        "explicacion": "¡Exacto! 'Aquel' se usa para cosas que están lejos."
    },
    {
        "texto": "3. En la frase 'Unas galletas', ¿qué tipo de artículo es 'Unas'?",
        "opciones": ["Determinado", "Indeterminado", "Numeral"],
        "correcta": 1,
        "explicacion": "Bien hecho. Se usa para algo no conocido o nombrado por primera vez."
    },
    {
        "texto": "4. ¿Cómo se llaman los numerales que indican orden (primero, segundo...)?",
        "opciones": ["Cardinales", "Ordinales", "Indefinidos"],
        "correcta": 1,
        "explicacion": "¡Eso es! Los ordinales indican el lugar en una serie."
    }
]

@bot.message_handler(commands=['start'])
def enviar_pregunta(message, index=0):
    if index < len(preguntas):
        p = preguntas[index]
        markup = InlineKeyboardMarkup()
        for i, opcion in enumerate(p["opciones"]):
            markup.add(InlineKeyboardButton(opcion, callback_data=f"{index}_{i}"))
        bot.send_message(message.chat.id, p["texto"], reply_markup=markup)
    else:
        bot.send_message(message.chat.id, "¡Felicidades! Has terminado el examen del Tema 3.")

@bot.callback_query_handler(func=lambda call: True)
def respuesta(call):
    p_idx, r_idx = map(int, call.data.split('_'))
    if r_idx == preguntas[p_idx]["correcta"]:
        bot.answer_callback_query(call.id, "✅ " + preguntas[p_idx]["explicacion"], show_alert=True)
        enviar_pregunta(call.message, p_idx + 1)
    else:
        bot.answer_callback_query(call.id, "❌ Inténtalo de nuevo", show_alert=True)

bot.polling()
