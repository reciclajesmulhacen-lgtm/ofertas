import telebot
from telebot import types
import importlib
import random
from estadisticas import registrar_resultado, ver_estadisticas

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

# Almacén temporal para seguir el examen de cada usuario
user_stats = {}

# -------------------- MENÚ PRINCIPAL --------------------
@bot.message_handler(commands=['start', 'menu'])
def menu_principal(message):
    markup = types.InlineKeyboardMarkup(row_width=2)
    for id_mat, nombre in MATERIAS_DISPLAY.items():
        markup.add(types.InlineKeyboardButton(nombre, callback_data=f"mat_{id_mat}"))
    bot.send_message(message.chat.id, "🎓 ¡Hola! Bienvenido al Aula Virtual 📖\n\nElige la materia que quieres repasar:", reply_markup=markup)

# -------------------- SELECCIÓN DE MATERIA --------------------
@bot.callback_query_handler(func=lambda call: call.data.startswith('mat_'))
def abrir_materia(call):
    materia_id = call.data.split('_')[1]
    try:
        modulo = importlib.import_module(materia_id)
        importlib.reload(modulo)
        temario = modulo.TEMARIO
        markup = types.InlineKeyboardMarkup()
        for uni_id, datos in temario.items():
            markup.add(types.InlineKeyboardButton(f"{uni_id}: {datos['titulo']}", callback_data=f"uni_{materia_id}_{uni_id}"))
        bot.edit_message_text(f"📚 Unidades de {MATERIAS_DISPLAY[materia_id]}:", call.message.chat.id, call.message.message_id, reply_markup=markup)
    except Exception:
        bot.answer_callback_query(call.id, f"❌ No encuentro la variable 'TEMARIO' en el archivo {materia_id}.py.", show_alert=True)

# -------------------- SELECCIÓN DE EXAMEN --------------------
@bot.callback_query_handler(func=lambda call: call.data.startswith('uni_'))
def elegir_examen(call):
    _, mat, uni = call.data.split('_')
    markup = types.InlineKeyboardMarkup()
    for i in range(1, 4):
        markup.add(types.InlineKeyboardButton(f"📝 Examen Tipo {i}", callback_data=f"test_{mat}_{uni}_{i}"))
    bot.edit_message_text(f"Elige un modelo de examen para la {uni}:", call.message.chat.id, call.message.message_id, reply_markup=markup)

# -------------------- INICIO DE EXAMEN --------------------
@bot.callback_query_handler(func=lambda call: call.data.startswith('test_'))
def iniciar_test(call):
    _, mat, uni, modelo = call.data.split('_')
    modulo = importlib.import_module(mat)
    preguntas_pool = modulo.TEMARIO[uni]['examenes'][int(modelo)-1]

    if not preguntas_pool:
        bot.answer_callback_query(call.id, "⚠️ Este examen está vacío, elige otro modelo.", show_alert=True)
        return

    user_stats[call.message.chat.id] = {
        'preguntas': preguntas_pool,
        'actual': 0,
        'aciertos': 0,
        'respuestas_usuario': [],
        'nombre_materia': MATERIAS_DISPLAY[mat],
        'unidad': uni,
        'examen_num': int(modelo),
        'materia_modulo': modulo
    }

    bot.delete_message(call.message.chat.id, call.message.message_id)
    enviar_pregunta(call.message.chat.id)

# -------------------- ENVÍO DE PREGUNTAS --------------------
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
        texto_pregunta = f"📖 **{datos['nombre_materia']}**\n\n❓ **Pregunta {datos['actual'] + 1} de {len(datos['preguntas'])}:**\n\n{p['p']}"
        bot.send_message(chat_id, texto_pregunta, reply_markup=markup, parse_mode="Markdown")
    else:
        finalizar_examen(chat_id)

# -------------------- PROCESAR RESPUESTAS --------------------
@bot.callback_query_handler(func=lambda call: call.data.startswith('res_'))
def procesar_respuesta(call):
    chat_id = call.message.chat.id
    if chat_id not in user_stats: return

    datos = user_stats[chat_id]
    pregunta_actual = datos['preguntas'][datos['actual']]
    datos['respuestas_usuario'].append(call.data.replace("res_", ""))  # Guardamos "si" o "no"

    if call.data == "res_si":
        datos['aciertos'] += 1
        bot.answer_callback_query(call.id, "✅ ¡Correcto!", show_alert=False)
    else:
        bot.answer_callback_query(call.id, "❌ ¡Casi! Sigue adelante 💪", show_alert=False)

    bot.delete_message(chat_id, call.message.message_id)
    datos['actual'] += 1
    enviar_pregunta(chat_id)

# -------------------- FINALIZAR EXAMEN --------------------
def finalizar_examen(chat_id):
    datos = user_stats[chat_id]
    modulo = datos['materia_modulo']
    unidad = datos['unidad']
    examen_num = datos['examen_num']

    # Guardamos resultados reales en estadisticas.py
    respuestas_reales = []
    for idx, preg in enumerate(datos['preguntas']):
        if datos['respuestas_usuario'][idx] == "si":
            respuestas_reales.append(preg['r'])
        else:
            # Usuario falló, guardamos algo diferente para repaso
            respuestas_reales.append("INCORRECTA")

    registrar_resultado(
        usuario_id=chat_id,
        unidad=unidad,
        examen_num=examen_num,
        respuestas_usuario=respuestas_reales,
        TEMARIO=modulo.TEMARIO
    )

    nota = datos['aciertos']
    total = len(datos['preguntas'])
    if nota == total:
        frase = "🏆 ¡Perfecto! ¡Has acertado todas las preguntas!"
    elif nota >= total * 0.7:
        frase = "🥈 ¡Muy bien! Estás casi ahí."
    else:
        frase = "💪 ¡No te rindas! Revisa las preguntas y vuelve a intentarlo."

    bot.send_message(
        chat_id,
        f"🏁 **Examen terminado!**\n\nHas acertado **{nota}** de {total} preguntas.\n{frase}\n\nPulsa /menu para volver al menú.",
        parse_mode="Markdown"
    )

    # Mostrar estadísticas completas
    estadisticas = ver_estadisticas(chat_id, unidad, examen_num)
    bot.send_message(chat_id, f"📊 **Estadísticas del examen:**\n{estadisticas}", parse_mode="Markdown")

    del user_stats[chat_id]

# -------------------- INICIAR BOT --------------------
bot.infinity_polling()
