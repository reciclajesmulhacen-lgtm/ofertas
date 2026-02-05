import telebot
from telebot import types
import importlib

# Configuración inicial
TOKEN = "8441666201:AAHygO1Osx5IdxnmQpQuF__Y8WyGvBKhr4U"
bot = telebot.TeleBot("8441666201:AAHygO1Osx5IdxnmQpQuF__Y8WyGvBKhr4U")

# Diccionario de materias vinculadas a tus archivos .py
MATERIAS = {
    'lengua': '📚 Lengua',
    'mates': '🔢 Matemáticas',
    'ciencias': '🧪 Ciencias',
    'ingles': '🇬🇧 Inglés',
    'frances': '🇫🇷 Francés'
}

# Almacén temporal de notas: {chat_id: {aciertos: 0, total: 0}}
user_stats = {}

@bot.message_handler(commands=['start', 'menu'])
def menu_principal(message):
    markup = types.InlineKeyboardMarkup(row_width=2)
    botones = [types.InlineKeyboardButton(nom, callback_data=f"sel_{id}") for id, nom in MATERIAS.items()]
    markup.add(*botones)
    
    bienvenida = (
        "¡Hola, explorador! 🚀\n"
        "Soy tu **Profe-Bot del CEIP Las Encinas**.\n"
        "Elige una asignatura para empezar el reto:"
    )
    bot.send_message(message.chat.id, bienvenida, reply_markup=markup, parse_mode="Markdown")

@bot.callback_query_handler(func=lambda call: call.data.startswith('sel_'))
def seleccionar_unidad(call):
    materia_id = call.data.split('_')[1]
    # Carga dinámica del archivo (ej: frances.py)
    try:
        modulo = importlib.import_module(materia_id)
        temario = modulo.TEMARIO
    except:
        bot.answer_callback_query(call.id, "⚠️ Materia en construcción...")
        return

    markup = types.InlineKeyboardMarkup()
    for id_u, datos in temario.items():
        markup.add(types.InlineKeyboardButton(f"{id_u}: {datos['titulo']}", callback_data=f"exam_{materia_id}_{id_u}"))
    
    bot.edit_message_text(f"✨ ¡Genial! ¿Qué unidad de **{MATERIAS[materia_id]}** quieres repasar?", 
                          call.message.chat.id, call.message.message_id, reply_markup=markup)

@bot.callback_query_handler(func=lambda call: call.data.startswith('exam_'))
def preparar_examen(call):
    _, materia, unidad = call.data.split('_')
    # Inicializamos estadísticas del alumno
    user_stats[call.message.chat.id] = {'aciertos': 0, 'pregunta_actual': 0, 'materia': materia, 'unidad': unidad}
    enviar_pregunta(call.message.chat.id)

def enviar_pregunta(chat_id):
    stats = user_stats[chat_id]
    modulo = importlib.import_module(stats['materia'])
    preguntas = modulo.TEMARIO[stats['unidad']]['preguntas']
    
    if stats['pregunta_actual'] < len(preguntas):
        p = preguntas[stats['pregunta_actual']]
        markup = types.InlineKeyboardMarkup()
        
        # Mezclamos opciones para que no siempre sea la misma posición
        opciones = list(p['o'])
        for opt in opciones:
            es_correcta = "si" if opt == p['r'] else "no"
            markup.add(types.InlineKeyboardButton(opt, callback_data=f"res_{es_correcta}"))
        
        bot.send_message(chat_id, f"❓ **Pregunta {stats['pregunta_actual']+1}/10:**\n\n{p['p']}", 
                         reply_markup=markup, parse_mode="Markdown")
    else:
        finalizar_examen(chat_id)

@bot.callback_query_handler(func=lambda call: call.data.startswith('res_'))
def procesar_respuesta(call):
    chat_id = call.message.chat.id
    if chat_id not in user_stats: return

    correcta = call.data.split('_')[1] == "si"
    
    if correcta:
        user_stats[chat_id]['aciertos'] += 1
        bot.answer_callback_query(call.id, "¡Excelente! 🌟", show_alert=False)
    else:
        bot.answer_callback_query(call.id, "¡Casi! Sigue intentándolo 💡", show_alert=False)

    # Borramos el mensaje anterior para que el chat no sea infinito y sea más fluido
    bot.delete_message(chat_id, call.message.message_id)
    user_stats[chat_id]['pregunta_actual'] += 1
    enviar_pregunta(chat_id)

def finalizar_examen(chat_id):
    res = user_stats[chat_id]
    nota = res['aciertos']
    
    # Medallas según nota
    if nota == 10: medalla = "🏆 ¡PERFECTO! Eres un genio."
    elif nota >= 7: medalla = "🥈 ¡MUY BIEN! Casi lo tienes."
    elif nota >= 5: medalla = "🥉 ¡APROBADO! Sigue practicando."
    else: medalla = "💪 ¡No te rindas! Vuelve a repasarlo."

    mensaje_final = (
        f"🏁 **¡Examen terminado!**\n\n"
        f"Has acertado **{nota}** de 10 preguntas.\n"
        f"{medalla}\n\n"
        "Pulsa /menu para otra materia."
    )
    bot.send_message(chat_id, mensaje_final, parse_mode="Markdown")
    del user_stats[chat_id]

bot.infinity_polling()
