import telebot
from telebot.types import InlineKeyboardMarkup, InlineKeyboardButton
import os
import time

# Obtención del Token desde las variables de entorno de Railway
TOKEN = os.getenv("8441666201:AAHygO1Osx5IdxnmQpQuF__Y8WyGvBKhr4U")
if not TOKEN:
    print("8441666201:AAHygO1Osx5IdxnmQpQuF__Y8WyGvBKhr4U")
    exit(1)

bot = telebot.TeleBot(TOKEN)

# Diccionario para estados de usuario
user_states = {}

# Base de datos de preguntas
preguntas = [
    {"id": 1, "p": "¿Qué indican los POSESIVOS?", "o": ["Distancia", "Pertenencia", "Cantidad"], "c": 1},
    {"id": 2, "p": "¿Cuál es un DEMOSTRATIVO de lejanía?", "o": ["Este", "Ese", "Aquel"], "c": 2},
    {"id": 3, "p": "En 'Unas mesas', ¿qué es 'Unas'?", "o": ["Indeterminado", "Determinado", "Numeral"], "c": 0},
    {"id": 4, "p": "'Primero, segundo...' son numerales:", "o": ["Cardinales", "Ordinales", "Indefinidos"], "c": 1},
    {"id": 5, "p": "¿Cuál es un determinante INDEFINIDO?", "o": ["Varios", "Tres", "Los"], "c": 0},
    {"id": 6, "p": "DETERMINADO masculino plural:", "o": ["Unos", "Los", "Estos"], "c": 1},
    {"id": 7, "p": "'Vuestra casa' indica:", "o": ["1 poseedor", "Varios poseedores", "Cercanía"], "c": 1},
    {"id": 8, "p": "'Ese estuche' indica distancia:", "o": ["Cerca", "Media", "Lejos"], "c": 1},
    {"id": 9, "p": "¿Cuál es un numeral CARDINAL?", "o": ["Sexto", "Muchos", "Diez"], "c": 2},
    {"id": 10, "p": "DETERMINADO femenino singular:", "o": ["Una", "La", "Esa"], "c": 1}
]

@bot.message_handler(commands=['start'])
def start(message):
    uid = str(message.from_user.id)
    user_states[uid] = {'pregunta': 0, 'aciertos': 0}
    
    bienvenida = (
        "🎓 *EXAMEN DE LENGUA: TEMA 3*\n"
        "----------------------------------\n"
        "Demuestra lo que sabes sobre los determinantes.\n"
        "¡Son 10 preguntas, mucha suerte! 💪"
    )
    bot.send_message(message.chat.id, bienvenida, parse_mode="Markdown")
    siguiente_pregunta(uid, message.chat.id)

def siguiente_pregunta(uid, chat_id):
    if uid not in user_states:
        return
        
    estado = user_states[uid]
    idx = estado['pregunta']
    
    if idx >= len(preguntas):
        finalizar_examen(uid, chat_id)
        return
    
    p = preguntas[idx]
    # Crear barra de progreso visual (ej: 🟦🟦⬜⬜...)
    progreso = "🟦" * idx + "⬜" * (len(preguntas) - idx)
    
    markup = InlineKeyboardMarkup(row_width=1)
    for i, opcion in enumerate(p['o']):
        markup.add(InlineKeyboardButton(opcion, callback_data=f"{idx}_{i}"))
    
    texto_pregunta = (
        f"{progreso}\n\n"
        f"❓ *PREGUNTA {p['id']}/10*\n\n"
        f"*{p['p']}*"
    )
    
    bot.send_message(chat_id, texto_pregunta, reply_markup=markup, parse_mode="Markdown")

@bot.callback_query_handler(func=lambda call: True)
def respuesta(call):
    uid = str(call.from_user.id)
    chat_id = call.message.chat.id
    
    if uid not in user_states:
        bot.answer_callback_query(call.id, "Usa /start para empezar")
        return
        
    try:
        datos = call.data.split('_')
        idx = int(datos[0])
        res_usuario = int(datos[1])
        
        estado = user_states[uid]
        
        # Validar que no responda una pregunta vieja
        if idx != estado['pregunta']:
            bot.answer_callback_query(call.id, "❌ Esta pregunta ya caducó.")
            return

        # Quitar botones inmediatamente
        bot.edit_message_reply_markup(chat_id, call.message.message_id, reply_markup=None)
        
        p = preguntas[idx]
        es_correcta = (res_usuario == p['c'])
        
        if es_correcta:
            estado['aciertos'] += 1
            bot.answer_callback_query(call.id, "¡Muy bien! ✅", show_alert=False)
            bot.send_message(chat_id, "✅ *¡CORRECTO!*", parse_mode="Markdown")
        else:
            bot.answer_callback_query(call.id, "¡Oh, no! ❌", show_alert=False)
            bot.send_message(chat_id, f"❌ *INCORRECTO*\n\nLa respuesta era: *{p['o'][p['c']]}*", parse_mode="Markdown")
        
        estado['pregunta'] += 1
        time.sleep(0.5) # Pausa breve para que lea el resultado
        siguiente_pregunta(uid, chat_id)
        
    except Exception as e:
        print(f"Error: {e}")

def finalizar_examen(uid, chat_id):
    estado = user_states[uid]
    nota = estado['aciertos']
    
    # Mensaje según la nota
    if nota == 10: mensaje = "🌟 ¡PERFECCIÓN ABSOLUTA! Eres un genio."
    elif nota >= 8: mensaje = "👏 ¡Excelente trabajo! Casi perfecto."
    elif nota >= 5: mensaje = "👍 ¡Aprobado! Pero puedes mejorar."
    else: mensaje = "📚 Hay que repasar un poco más. ¡Tú puedes!"

    resumen = (
        "🏁 *¡EXAMEN FINALIZADO!*\n"
        "----------------------------------\n"
        f"✅ Aciertos: *{nota}*\n"
        f"❌ Fallos: *{10 - nota}*\n"
        f"📊 Puntuación: *{nota}/10*\n\n"
        f"{mensaje}\n\n"
        "Pulsa /start para volver a intentarlo."
    )
    
    bot.send_message(chat_id, resumen, parse_mode="Markdown")
    del user_states[uid]

if __name__ == "__main__":
    print("Bot iniciado con éxito...")
    bot.infinity_polling(none_stop=True, timeout=60)
