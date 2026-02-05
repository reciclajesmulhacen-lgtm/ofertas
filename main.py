import telebot
from telebot.types import InlineKeyboardMarkup, InlineKeyboardButton

TOKEN = "8441666201:AAHygO1Osx5IdxnmQpQuF__Y8WyGvBKhr4U"
bot = telebot.TeleBot(TOKEN)

# Diccionario para guardar el progreso de cada usuario (fallos y pregunta actual)
user_stats = {}

preguntas = [
    {"texto": "1. ¿Qué indican los determinantes POSESIVOS?", "opciones": ["Distancia", "Pertenencia", "Cantidad"], "correcta": 1, "explic": "Los posesivos indican a quién pertenece algo (mío, tu, nuestro)."},
    {"texto": "2. ¿Cuál es un determinante DEMOSTRATIVO de lejanía?", "opciones": ["Este", "Ese", "Aquel"], "correcta": 2, "explic": "'Aquel' se usa para lo que está muy lejos."},
    {"texto": "3. En 'Unas mesas', ¿qué tipo de artículo es 'Unas'?", "opciones": ["Indeterminado", "Determinado", "Contable"], "correcta": 0, "explic": "Es indeterminado porque no conocemos específicamente las mesas."},
    {"texto": "4. Los numerales 'primero, segundo, tercero' son...", "opciones": ["Cardinales", "Ordinales", "Posesivos"], "correcta": 1, "explic": "Indican el orden (ordinales)."},
    {"texto": "5. ¿Cuál es un determinante INDEFINIDO?", "opciones": ["Varios", "Tres", "Los"], "correcta": 0, "explic": "'Varios' indica una cantidad que no es exacta."},
    {"texto": "6. ¿Qué palabra es un artículo determinado masculino plural?", "opciones": ["Unos", "Los", "Estos"], "correcta": 1, "explic": "'Los' es determinado, masculino y plural."},
    {"texto": "7. En 'Vuestra casa', 'vuestra' es un posesivo de...", "opciones": ["Un poseedor", "Varios poseedores", "Lejanía"], "correcta": 1, "explic": "Vuestra indica que la casa es de todos vosotros."},
    {"texto": "8. 'Ese estuche'. ¿Qué distancia indica 'Ese'?", "opciones": ["Cercanía", "Distancia media", "Lejanía"], "correcta": 1, "explic": "Distancia media."},
    {"texto": "9. ¿Cuál de estos es un numeral CARDINAL?", "opciones": ["Sexto", "Muchos", "Diez"], "correcta": 2, "explic": "Los cardinales son los números naturales (1, 2, 10...)."},
    {"texto": "10. ¿Cuál es el artículo determinado femenino singular?", "opciones": ["Una", "La", "Esa"], "correcta": 1, "explic": "'La' es el artículo determinado femenino singular."}
]

@bot.message_handler(commands=['start'])
def iniciar(message):
    user_stats[message.chat.id] = {"pregunta_actual": 0, "fallos": 0}
    bot.send_message(message.chat.id, "📝 **Examen Tema 3: Los Determinantes**\nNo puedes cambiar la respuesta una vez elegida. ¡Suerte!")
    enviar_pregunta(message.chat.id)

def enviar_pregunta(chat_id):
    idx = user_stats[chat_id]["pregunta_actual"]
    if idx < len(preguntas):
        p = preguntas[idx]
        markup = InlineKeyboardMarkup()
        for i, opcion in enumerate(p["opciones"]):
            markup.add(InlineKeyboardButton(opcion, callback_data=f"ans_{i}"))
        bot.send_message(chat_id, p["texto"], reply_markup=markup)
    else:
        finalizar_examen(chat_id)

@bot.callback_query_handler(func=lambda call: call.data.startswith('ans_'))
def procesar_respuesta(call):
    chat_id = call.message.chat.id
    idx = user_stats[chat_id]["pregunta_actual"]
    eleccion = int(call.data.split('_')[1])
    
    # Bloqueo: Quitamos los botones del mensaje actual para que no pueda pulsar de nuevo
    bot.edit_message_reply_markup(chat_id, call.message.message_id, reply_markup=None)
    
    p = preguntas[idx]
    if eleccion == p["correcta"]:
        res_texto = f"✅ **¡Correcto!**\n{p['explic']}"
    else:
        user_stats[chat_id]["fallos"] += 1
        res_texto = f"❌ **Incorrecto.**\n{p['explic']}"
    
    bot.send_message(chat_id, res_texto)
    
    # Avanzar a la siguiente
    user_stats[chat_id]["pregunta_actual"] += 1
    enviar_pregunta(chat_id)

def finalizar_examen(chat_id):
    fallos = user_stats[chat_id]["fallos"]
    aciertos = len(preguntas) - fallos
    nota = aciertos # En un examen de 10, cada acierto es un punto
    
    mensaje_final = (f"🏁 **¡Examen terminado!**\n\n"
                     f"✅ Aciertos: {aciertos}\n"
                     f"❌ Fallos: {fallos}\n"
                     f"📊 Nota final: {nota}/10\n\n")
    
    if nota >= 5: mensaje_final += "¡Enhorabuena, has aprobado! 🎉"
    else: mensaje_final += "Hay que repasar un poco más. ¡Tú puedes! 💪"
    
    bot.send_message(chat_id, mensaje_final)

bot.polling()
