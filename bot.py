import telebot
from telebot import types
import importlib
import random

TOKEN = "8441666201:AAHygO1Osx5IdxnmQpQuF__Y8WyGvBKhr4U"
bot = telebot.TeleBot("8441666201:AAHygO1Osx5IdxnmQpQuF__Y8WyGvBKhr4U")

# Nombres que se muestran en los botones del menú principal
MATERIAS_DISPLAY = {
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
    for id_mat, nombre in MATERIAS_DISPLAY.items():
        markup.add(types.InlineKeyboardButton(nombre, callback_data=f"mat_{id_mat}"))
    bot.send_message(message.chat.id, "¡Hola! Elige materia:", reply_markup=markup)

@bot.callback_query_handler(func=lambda call: call.data.startswith('mat_'))
def abrir_materia(call):
    materia_id = call.data.split('_')[1] # Extrae 'mates', 'frances', etc.
    try:
        # Importación dinámica: busca el archivo exacto (ej: mates.py)
        modulo = importlib.import_module(materia_id)
        importlib.reload(modulo) # Recarga por si actualizas el archivo
        
        # Leemos la variable TEMARIO del archivo importado (¡Esto es lo clave!)
        temario = modulo.TEMARIO 
        
        markup = types.InlineKeyboardMarkup()
        for uni_id, datos in temario.items():
            markup.add(types.InlineKeyboardButton(f"{uni_id}: {datos['titulo']}", callback_data=f"uni_{materia_id}_{uni_id}"))
        
        bot.edit_message_text(f"Unidades de {MATERIAS_DISPLAY[materia_id]}:", call.message.chat.id, call.message.message_id, reply_markup=markup)
    except Exception as e:
        # Este error es el que te salía antes. Te dice que el archivo no tiene la variable TEMARIO.
        bot.answer_callback_query(call.id, f"Error: No encuentro la variable 'TEMARIO' en el archivo {materia_id}.py. Revisa el nombre.", show_alert=True)

@bot.callback_query_handler(func=lambda call: call.data.startswith('uni_'))
def elegir_examen(call):
    _, mat, uni = call.data.split('_')
    markup = types.InlineKeyboardMarkup()
    for i in range(1, 4):
        markup.add(types.InlineKeyboardButton(f"📝 Examen Tipo {i}", callback_data=f"test_{mat}_{uni}_{i}"))
    bot.edit_message_text(f"Elige un modelo de examen para la {uni}:", call.message.chat.id, call.message.message_id, reply_markup=markup)

@bot.callback_query_handler(func=lambda call: call.data.startswith('test_'))
def iniciar_test(call):
    _, mat, uni, modelo = call.data.split('_')
    modulo = importlib.import_module(mat)
    
    # Seleccionamos las preguntas del examen específico (índice 0, 1 o 2)
    preguntas_pool = modulo.TEMARIO[uni]['examenes'][int(modelo)-1]
    
    if not preguntas_pool:
         bot.answer_callback_query(call.id, "⚠️ Este examen está vacío, elige otro modelo.", show_alert=True)
         return

    user_stats[call.message.chat.id] = {
        'preguntas': preguntas_pool,
        'actual': 0,
        'aciertos': 0,
        'nombre_materia': MATERIAS_DISPLAY[mat]
    }
    bot.delete_message(call.message.chat.id, call.message.message_id)
    enviar_pregunta(call.message.chat.id)

def enviar_pregunta(chat_id):
    datos = user_stats[chat_id]
    if datos['actual'] < len(datos['preguntas']):
        p = datos['preguntas'][datos['actual']]
        markup = types.InlineKeyboardMarkup(row_width=1)
        opciones = list(p['o'])
        random.shuffle(opciones)
        
        for opcion in opciones:
            es_correcta = "si" if opcion == p['r'] else "no"
            markup.add(types.InlineKeyboardButton(opcion, callback_data=f"res_{es_correcta}"))
        
        texto_pregunta = f"📖 **{datos['nombre_materia']}**\n\n❓ **Pregunta {datos['actual'] + 1} de 10:**\n\n{p['p']}"
        bot.send_message(chat_id, texto_pregunta, reply_markup=markup, parse_mode="Markdown")
    else:
        finalizar_examen(chat_id)

@bot.callback_query_handler(func=lambda call: call.data.startswith('res_'))
def procesar_respuesta(call):
    chat_id = call.message.chat.id
    if chat_id not in user_stats: return

    if call.data == "res_si":
        user_stats[chat_id]['aciertos'] += 1
        bot.answer_callback_query(call.id, "¡Muy bien! ✅", show_alert=False)
    else:
        bot.answer_callback_query(call.id, "¡Sigue intentando! 💡", show_alert=False)

    bot.delete_message(chat_id, call.message.message_id)
    user_stats[chat_id]['actual'] += 1
    enviar_pregunta(chat_id)

def finalizar_examen(chat_id):
    res = user_stats[chat_id]
    nota = res['aciertos']
    total_preguntas = len(res['preguntas'])
    
    if nota == total_preguntas: frase = "🏆 ¡PERFECTO! Eres un genio."
    elif nota >= total_preguntas * 0.7: frase = "🥈 ¡MUY BIEN! Casi lo tienes."
    else: frase = "💪 ¡No te rindas! Vuelve a repasarlo."

    bot.send_message(chat_id, f"🏁 **¡Examen terminado!**\n\nHas acertado **{nota}** de {total_preguntas} preguntas.\n{frase}\n\nPulsa /menu para volver a jugar.", parse_mode="Markdown")
    del user_stats[chat_id]

bot.infinity_polling()
