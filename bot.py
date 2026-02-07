# ------------------------------
# FUNCIONES DE FORMATO Y ESCAPE
# ------------------------------
def escape_html(text):
    """Escapa &, < y > para <code>"""
    return str(text).replace("&", "&amp;").replace("<", "&lt;").replace(">", "&gt;")


def formato_pregunta(pregunta_idx, total, pregunta_texto):
    """Genera texto con barra de progreso y <code>"""
    progreso = '▰' * (pregunta_idx + 1) + '▱' * (total - pregunta_idx - 1)
    return (
        f"❓ <b>Pregunta {pregunta_idx + 1}/{total}</b>\n"
        f"[{progreso}]\n\n"
        f"<code>{escape_html(pregunta_texto)}</code>"
    )

# ------------------------------
# TECLADOS
# ------------------------------
def get_materias_keyboard():
    markup = types.InlineKeyboardMarkup(row_width=2)
    for idx, mk in enumerate(MATERIAS.keys()):
        nombre = MATERIAS[mk]['nombre']
        markup.add(types.InlineKeyboardButton(nombre, callback_data=f'm:{idx}'))
    markup.add(types.InlineKeyboardButton('❌ Cancelar / Volver', callback_data='salir_menu'))
    return markup


def get_temas_keyboard(materia_idx):
    materia_key = list(MATERIAS.keys())[materia_idx]
    temario = MATERIAS[materia_key]['temario']
    markup = types.InlineKeyboardMarkup(row_width=1)
    for tema_idx, (tema_key, tema_data) in enumerate(temario.items()):
        titulo = tema_data['titulo']
        markup.add(types.InlineKeyboardButton(f'📖 {titulo}', callback_data=f't:{materia_idx}:{tema_idx}'))
    markup.add(types.InlineKeyboardButton('❌ Cancelar / Volver', callback_data='salir_menu'))
    return markup


def get_examenes_keyboard(materia_idx, tema_idx):
    markup = types.InlineKeyboardMarkup(row_width=3)
    for examen_idx in range(3):
        markup.add(types.InlineKeyboardButton(f'📝 Examen {examen_idx+1}', callback_data=f'e:{materia_idx}:{tema_idx}:{examen_idx}'))
    markup.add(types.InlineKeyboardButton('❌ Cancelar / Volver', callback_data='salir_menu'))
    return markup


def get_respuestas_keyboard(state, pregunta_idx):
    """Botones A/B/C"""
    respuestas = state['preguntas'][pregunta_idx]['o']
    markup = types.InlineKeyboardMarkup(row_width=1)
    for idx, r in enumerate(respuestas):
        markup.add(types.InlineKeyboardButton(r, callback_data=f'r:{state["materia_idx"]}:{state["tema_idx"]}:{state["examen_idx"]}:{pregunta_idx}:{idx}'))
    markup.add(types.InlineKeyboardButton('❌ Cancelar / Volver', callback_data='salir_menu'))
    return markup

# ------------------------------
# HANDLERS
# ------------------------------
@bot.callback_query_handler(func=lambda call: call.data.startswith('m:'))
def seleccionar_materia(call):
    user_id = call.message.chat.id
    materia_idx = int(call.data.split(':')[1])
    materia_key = list(MATERIAS.keys())[materia_idx]

    # Guardar materia_idx en user_state
    user_state[user_id] = {'materia': materia_key, 'materia_idx': materia_idx}

    bot.edit_message_text(
        f"<b>{MATERIAS[materia_key]['nombre']}</b>\n\n📖 Selecciona un tema:",
        user_id,
        call.message.message_id,
        reply_markup=get_temas_keyboard(materia_idx),
        parse_mode='HTML'
    )


@bot.callback_query_handler(func=lambda call: call.data.startswith('t:'))
def seleccionar_tema(call):
    user_id = call.message.chat.id
    parts = call.data.split(':')
    materia_idx = int(parts[1])
    tema_idx = int(parts[2])

    materia_key = list(MATERIAS.keys())[materia_idx]
    temario = MATERIAS[materia_key]['temario']
    tema_key = list(temario.keys())[tema_idx]
    preguntas = temario[tema_key]['examenes'][0]  # Placeholder, se elige examen luego

    # Guardar estado parcial
    user_state[user_id].update({'tema_idx': tema_idx})

    bot.edit_message_text(
        f"<b>📚 {temario[tema_key]['titulo']}</b>\n\n📝 Elige un examen:",
        user_id,
        call.message.message_id,
        reply_markup=get_examenes_keyboard(materia_idx, tema_idx),
        parse_mode='HTML'
    )


@bot.callback_query_handler(func=lambda call: call.data.startswith('e:'))
def iniciar_examen(call):
    user_id = call.message.chat.id
    materia_idx, tema_idx, examen_idx = map(int, call.data.split(':')[1:])
    materia_key = list(MATERIAS.keys())[materia_idx]
    temario = MATERIAS[materia_key]['temario']
    tema_key = list(temario.keys())[tema_idx]
    preguntas = temario[tema_key]['examenes'][examen_idx]

    # Guardar todo el estado del examen
    user_state[user_id].update({
        'tema_idx': tema_idx,
        'examen_idx': examen_idx,
        'preguntas': preguntas,
        'pregunta_actual': 0,
        'respuestas_correctas': 0
    })

    enviar_pregunta(user_id, call.message.message_id)


def enviar_pregunta(user_id, message_id):
    state = user_state[user_id]
    idx = state['pregunta_actual']
    preguntas = state['preguntas']

    if idx >= len(preguntas):
        finalizar_examen(user_id, message_id)
        return

    texto = formato_pregunta(idx, len(preguntas), preguntas[idx]['p'])

    bot.edit_message_text(
        texto,
        user_id,
        message_id,
        reply_markup=get_respuestas_keyboard(state, idx),
        parse_mode='HTML'
    )
