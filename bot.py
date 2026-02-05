import telebot
from telebot import types
import importlib
import random
from estadisticas import registrar_resultado, ver_estadisticas

TOKEN = "8441666201:AAHygO1Osx5IdxnmQpQuF__Y8WyGvBKhr4U"
bot = telebot.TeleBot("8441666201:AAHygO1Osx5IdxnmQpQuF__Y8WyGvBKhr4U")

MATERIAS_DISPLAY = {
    'lengua': '📚 Lengua',
    'mates': '🔢 Matemáticas',
    'ciencias': '🧪 Ciencias',
    'ingles': '🇬🇧 Inglés',
    'frances': '🇫🇷 Francés'
}

user_stats = {}

# -------------------- MENÚ PRINCIPAL --------------------
@bot.message_handler(commands=['start', 'menu'])
def menu_principal(message):
    markup = types.InlineKeyboardMarkup(row_width=2)
    for id_mat, nombre in MATERIAS_DISPLAY.items():
        markup.add(types.InlineKeyboardButton(nombre, callback_data=f"mat_{id_mat}"))
    bot.send_message(
        message.chat.id,
        "🎓 ¡Bienvenido al Aula Virtual!\n\nElige la materia que quieres repasar:",
        reply_markup=markup
    )

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
            markup.add(types.InlineKeyboardButton(
                f"{uni_id}: {datos['titulo']}",
                callback_data=f"uni_{materia_id}_{uni_id}"
            ))
        bot.edit_message_text(
            f"📚 Unidades de {MATERIAS_DISPLAY[materia_id]}:",
            call.message.chat.id,
            call.message.message_id,
            reply_markup=markup
        )
    except Exception:
        bot.answer_callback_query(
            call.id,
            f"❌ No encuentro la variable 'TEMARIO' en el archivo {materia_id}.py.",
            show_alert=True
        )

# -------------------- SELECCIÓN DE EXAMEN --------------------
@bot.callback_query_handler(func=lambda call: call.data.startswith('uni_'))
def elegir_examen(call):
    _, mat, uni = call.data.split('_')
    markup = types.InlineKeyboardMarkup()
    for i in range(1, 4):
        markup.add(types.InlineKeyboardButton(
            f"📝 Examen Tipo {i}",
            callback_data=f"test_{mat}_{uni}_{i}"
        ))
    bot.edit_message_text(
        f"Elige un modelo de examen para la {uni}:",
        call.message.chat.id,
        call.message.message_id,
        reply_markup=markup
    )

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
        'fallos': [],
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
    correcto = call.data.replace("res_", "")
    datos['respuestas_usuario'].append(correcto)
    if correcto == "si":
        datos['aciertos'] += 1
        bot.answer_callback_query(call.id, "✅ ¡Correcto!", show_alert=False)
    else:
        datos['fallos'].append(datos['actual'] + 1)
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

    # Guardar resultados
    respuestas_reales = []
    for idx, preg in enumerate(datos['preguntas']):
        if datos['respuestas_usuario'][idx] == "si":
            respuestas_reales.append(preg['r'])
        else:
            respuestas_reales.append("INCORRECTA")

    registrar_resultado(chat_id, unidad, examen_num, respuestas_reales, modulo.TEMARIO)

    # Mensaje final con gamificación
    nota = datos['aciertos']
    total = len(datos['preguntas'])
    if nota == total:
        frase = "🏆 ¡Perfecto! Has acertado todas las preguntas."
    elif nota >= total * 0.7:
        frase = "🥈 ¡Muy bien! Casi perfecto."
    else:
        frase = "💪 ¡No te rindas! Repasa las preguntas falladas."

    markup = types.InlineKeyboardMarkup()
    markup.add(types.InlineKeyboardButton("🔄 Repasar fallos", callback_data=f"repasar_{unidad}_{examen_num}"))
    markup.add(types.InlineKeyboardButton("🏠 Volver al menú", callback_data="volver_menu"))

    bot.send_message(
        chat_id,
        f"🏁 **Examen terminado!**\n\nHas acertado **{nota}** de {total} preguntas.\n{frase}",
        parse_mode="Markdown",
        reply_markup=markup
    )

    user_stats[chat_id]['fallos_guardados'] = datos['fallos']

# -------------------- REPASO DE FALLOS --------------------
@bot.callback_query_handler(func=lambda call: call.data.startswith('repasar_'))
def repasar_fallos(call):
    chat_id = call.message.chat.id
    _, unidad, examen_num = call.data.split('_')
    datos = user_stats.get(chat_id)
    if not datos or not datos.get('fallos_guardados'):
        bot.answer_callback_query(call.id, "❌ No hay fallos para repasar.", show_alert=True)
        return

    fallos = datos['fallos_guardados']
    preguntas = [datos['preguntas'][i - 1] for i in fallos]  # Preguntas falladas
    datos['preguntas'] = preguntas
    datos['actual'] = 0
    datos['aciertos'] = 0
    datos['respuestas_usuario'] = []
    bot.delete_message(chat_id, call.message.message_id)
    enviar_pregunta(chat_id)

# -------------------- VOLVER AL MENÚ --------------------
@bot.callback_query_handler(func=lambda call: call.data == "volver_menu")
def volver_menu(call):
    bot.delete_message(call.message.chat.id, call.message.message_id)
    menu_principal(call.message)

# -------------------- COMANDO ESTADÍSTICAS --------------------
@bot.message_handler(commands=['estadisticas'])
def mostrar_estadisticas(message):
    chat_id = message.chat.id
    textos = []
    for mat_id in MATERIAS_DISPLAY.keys():
        for uni_id in user_stats.get(chat_id, {}).keys():
            pass  # Podrías implementar estadísticas por materia si quieres
    bot.send_message(chat_id, "📊 Consulta de estadísticas completa disponible al terminar cada examen.")

# -------------------- INICIAR BOT --------------------
bot.infinity_polling()
