import telebot
from telebot.types import InlineKeyboardMarkup, InlineKeyboardButton

TOKEN = "8441666201:AAHygO1Osx5IdxnmQpQuF__Y8WyGvBKhr4U"
bot = telebot.TeleBot(TOKEN)

# Diccionario para guardar el progreso
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
    bot.send_message(message.chat.id, "📝 **Examen Tema 3: Los Determinantes**\nResponde con cuidado, no se puede cambiar la respuesta.")
    enviar_pregunta(message.chat.id)

def enviar_pregunta(chat_id):
    idx = user_stats[chat_id]["pregunta_actual"]
    
    if idx < len(preguntas):
        p = preguntas[idx]
        markup = InlineKeyboardMarkup()
        # Creamos los botones
        for i, opcion in enumerate(p["opciones"]):
            # El callback_data ahora es más claro: "pregunta_opcion"
            markup.add(InlineKeyboardButton(opcion, callback_data=f"{idx}_{i}"))
        bot.send_message(chat_id, p["texto"], reply_markup=markup)
    else:
        finalizar_examen(chat_id)

@bot.callback_query_handler(func=lambda call: True)
def procesar_respuesta(call):
    chat_id = call.message.chat.id
    
    # Extraer los datos del callback (pregunta_opcion)
    datos = call.data.split('_')
    idx_pregunta = int(datos[0])
    idx_respuesta = int(datos[1])
    
    # Seguridad: Solo procesar si coincide con la pregunta actual del usuario
    if idx_pregunta != user_stats[chat_id]["pregunta_actual"]:
        return

    # 1. Bloqueo: Eliminar botones para que no pueda pulsar más veces
    bot.edit_message_reply_markup(chat_id, call.message.message_id, reply_markup=None)
    
    p = preguntas[idx_pregunta]
    
    # 2. Verificar si es correcta
    if idx_respuesta == p["correcta"]:
        res_texto = f"✅ **¡Correcto!**\n{p['explic']}"
    else:
        user_stats[chat_id]["fallos"] += 1
        res_texto = f"❌ **Incorrecto.**\n{p['explic']}"
    
    bot.send_message(chat_id, res_texto)
    
    # 3. Avanzar a la siguiente pregunta
    user_stats[chat_id]["pregunta_actual"] += 1
    enviar_pregunta(chat_id)

def finalizar_examen(chat_id):
    fallos = user_stats[chat_id]["fallos"]
    total = len(preguntas)
    aciertos = total - fallos
    
    mensaje_final = (f"🏁 **¡Examen terminado!**\n\n"
                     f"✅ Aciertos: {aciertos}\n"
                     f"❌ Fallos: {fallos}\n"
                     f"📊 Nota final: {aciertos}/{total}")
    
    bot.send_message(chat_id, mensaje_final)

bot.polling()
