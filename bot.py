import telebot
from telebot import types
import importlib
import random

TOKEN = "8441666201:AAHygO1Osx5IdxnmQpQuF__Y8WyGvBKhr4U"
bot = telebot.TeleBot("8441666201:AAHygO1Osx5IdxnmQpQuF__Y8WyGvBKhr4U")

# Nombres que se muestran en los botones del menú principal
MATERIAS = {
    'lengua': '📚 Lengua',
    'mates': '🔢 Matemáticas',
    'ciencias': '🧪 Ciencias',
    'ingles': '🇬🇧 Inglés',
    'frances': '🇫🇷 Francés'
}

# Almacén temporal para seguir el juego de cada usuario
user_stats = {}

@bot.message_handler(commands=['start', 'menu'])
def menu_principal(message):
    markup = types.InlineKeyboardMarkup(row_width=2)
    # Generamos los botones con los nombres bonitos
    for id_mat, nombre in MATERIAS.items():
        markup.add(types.InlineKeyboardButton(nombre, callback_data=f"mat_{id_mat}"))
    bot.send_message(message.chat.id, "¡Hola! Elige materia:", reply_markup=markup)

@bot.callback_query_handler(func=lambda call: call.data.startswith('mat_'))
def abrir_materia(call):
    materia_id = call.data.split('_')[1] # Extrae 'mates', 'frances', etc.
    try:
        # Importación dinámica: busca el archivo exacto (ej: mates.py)
        modulo = importlib.import_module(materia_id)
        importlib.reload(modulo) # Recarga por si actualizas el archivo
        
        # Leemos la variable TEMARIO del archivo importado
        temario = modulo.TEMARIO 
        
        markup = types.InlineKeyboardMarkup()
        for uni_id, datos in temario.items():
            markup.add(types.InlineKeyboardButton(f"{uni_id}: {datos['titulo']}", callback_data=f"uni_{materia_id}_{uni_id}"))
        
        bot.edit_message_text(f"Unidades de {MATERIAS[materia_id]}:", call.message.chat.id, call.message.message_id, reply_markup=markup)
    except Exception as e:
        # Este mensaje de error te dirá exactamente dónde está el fallo
        bot.answer_callback_query(call.id, f"Error: No puedo leer la variable 'TEMARIO' del archivo {materia_id}.py. Revisa que exista y esté bien escrita.", show_alert=True)

@bot.callback_query_handler(func=lambda call: call.data.startswith('uni_'))
def elegir_examen(call):
    _, mat, uni = call.data.split('_')
    markup = types.InlineKeyboardMarkup()
    for i in range(1, 4):
        markup.add(types.InlineKeyboardButton(f"📝 Examen Tipo {i}", callback_data=f"test_{mat}_{uni}_{i}"))
    bot.edit_message_text(f"Elige un modelo de examen para la {uni}:", call.message.chat.id, call.message.message_id, reply_markup=markup)

@bot.callback_query_handler(func=lambda call: call.data.startswith('test_'))
def iniciar_test(call):
    # Aquí iría la lógica para cargar las 10 preguntas y empezar a jugar
    bot.answer_callback_query(call.id, "¡Perfecto! Ya tienes el motor principal funcionando. Ahora podemos añadir el resto de preguntas.")
    bot.send_message(call.message.chat.id, "Ahora que el menú funciona, pulsa /menu para volver a la pantalla principal.")

bot.infinity_polling()
