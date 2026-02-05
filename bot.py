import telebot
from telebot import types
import importlib
import random

# CONFIGURACIÓN
TOKEN = "8441666201:AAHygO1Osx5IdxnmQpQuF__Y8WyGvBKhr4U"
bot = telebot.TeleBot("8441666201:AAHygO1Osx5IdxnmQpQuF__Y8WyGvBKhr4U")

# Los nombres de las llaves deben ser IGUALES a los nombres de tus archivos .py
MATERIAS = {
    'lengua': '📚 Lengua',
    'mates': '🔢 Matemáticas',
    'ciencias': '🧪 Ciencias',
    'ingles': '🇬🇧 Inglés',
    'frances': '🇫🇷 Francés'
}

user_stats = {}

@bot.message_handler(commands=['start', 'menu'])
def menu_principal(message):
    markup = types.InlineKeyboardMarkup(row_width=2)
    # Generamos los botones basados en el diccionario MATERIAS
    botones = [types.InlineKeyboardButton(nom, callback_data=f"sel_{id}") for id, nom in MATERIAS.items()]
    markup.add(*botones)
    
    texto = (
        "¡Hola, explorador! 🚀\n"
        "Soy tu **Profe-Bot de Apoyo**.\n"
        "Elige una asignatura para empezar el reto:"
    )
    bot.send_message(message.chat.id, texto, reply_markup=markup, parse_mode="Markdown")

@bot.callback_query_handler(func=lambda call: call.data.startswith('sel_'))
def seleccionar_unidad(call):
    materia_id = call.data.split('_')[1] # Extrae 'mates', 'frances', etc.
    
    try:
        # Esto busca el archivo mates.py, frances.py, etc.
        modulo = importlib.import_module(materia_id)
        # Recargamos el módulo por si has hecho cambios en las preguntas
        importlib.reload(modulo)
        temario = modulo.TEMARIO
        
        markup = types.InlineKeyboardMarkup()
        for id_u, datos in temario.items():
            markup.add(types.InlineKeyboardButton(f"{id_u}: {datos['titulo']}", callback_data=f"exam_{materia_id}_{id_u}"))
        
        # Botón para volver atrás
        markup.add(types.InlineKeyboardButton("🔙 Volver al Menú", callback_data="volver_menu"))
        
        bot.edit_message_text(f"✨ ¡Genial! Elige un tema de **{MATERIAS[materia_id]}**:", 
                              call.message.chat.id, call.message.message_id, reply_markup=markup)
    except Exception as e:
        print(f"Error al cargar {materia_id}: {e}")
        bot.answer_callback_query(call.id, "⚠️ Archivo no encontrado. Asegúrate de tener creado " + materia_id + ".py", show_alert=True)

@bot.callback_query_handler(func=lambda call: call.data == "volver_menu")
def volver(call):
    bot.delete_message(call.message.chat.id, call.message.message_id)
    menu_principal(call.message)

@bot.callback_query_handler(func=lambda call: call.data.startswith('exam_'))
def preparar_examen(call):
    _, materia, unidad = call.data.split('_')
    modulo = importlib.import_module(materia)
    preguntas_pool = modulo.TEMARIO[unidad]['preguntas']
    
    # Seleccionamos 10 preguntas aleatorias de la unidad
    seleccionadas = random.sample(preguntas_pool, min(len(preguntas_pool), 10))
    
    user_stats[call.message.chat.id] = {
        'preguntas': seleccionadas,
        'aciertos': 0,
        'actual': 0,
        'materia': materia,
        'nombre_materia': MATERIAS[materia]
    }
    bot.delete_message(call.message.chat.id, call.message.message_id)
    enviar_pregunta(call.message.chat.id)

def enviar_pregunta(chat_id):
    datos = user_stats[chat_id]
    if datos['actual'] < len(datos['preguntas']):
        p = datos['preguntas'][datos['actual']]
        
        markup = types.InlineKeyboardMarkup(row_width=1)
        # Barajamos las opciones para que no estén siempre en el mismo orden
        opciones = p['o']
        random.shuffle(opciones)
        
        for opcion in opciones:
            es_correcta = "si" if opcion == p['r'] else "no"
            markup.add(types.InlineKeyboardButton(opcion, callback_data=f"res_{es_correcta}"))
        
        texto_pregunta = f"📖 **{datos['nombre_materia']}**\n\n❓ **Pregunta {datos['actual'] + 1} de 10:**\n\n{p['p']}"
        bot.send_message(chat_id, texto_pregunta, reply_markup=markup, parse_mode="Markdown")
    else:
        finalizar(chat_id)

@bot.callback_query_handler(func=lambda call: call.data.startswith('res_'))
def procesar_respuesta(call):
    chat_id = call.message.chat.id
    if chat_id not in user_stats: return

    if call.data == "res_si":
        user_stats[chat_id]['aciertos'] += 1
        bot.answer_callback_query(call.id, "¡Muy bien! ✅")
    else:
        bot.answer_callback_query(call.id, "¡Ánimo! Sigue aprendiendo 💡")

    bot.delete_message(chat_id, call.message.message_id)
    user_stats[chat_id]['actual'] += 1
    enviar_pregunta(chat_id)

def finalizar(chat_id):
    res = user_stats[chat_id]
    nota = res['aciertos']
    
    if nota >= 9: frase = "🏆 ¡Increíble! Eres un experto/a."
    elif nota >= 6: frase = "🥈 ¡Muy buen trabajo! Sigue así."
    else: frase = "🥉 ¡No te rindas! Repasa un poco más."
    
    texto_final = (
        f"🏁 **¡Reto completado!**\n\n"
        f"Has acertado **{nota}** de 10 preguntas.\n"
        f"{frase}\n\n"
        "Pulsa /menu para jugar otra vez."
    )
    bot.send_message(chat_id, texto_final, parse_mode="Markdown")
    if chat_id in user_stats: del user_stats[chat_id]

print("Bot Profe-Bot encendido... 🚀")
bot.infinity_polling()
