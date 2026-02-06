import os
import telebot
from flask import Flask, request
from telebot import types
import html
import json
import threading
from datetime import datetime

# Importar temarios
from mates import TEMARIO as MATES
from lengua import TEMARIO as LENGUA
from ingles import TEMARIO as INGLES
from frances import TEMARIO as FRANCES
from ciencias import TEMARIO as CIENCIAS

# Configuración
TOKEN = os.environ.get('TELEGRAM_BOT_TOKEN')
DOMAIN = os.environ.get('RAILWAY_PUBLIC_DOMAIN')

bot = telebot.TeleBot(TOKEN)
app = Flask(__name__)

# Almacenar el estado de cada usuario
user_state = {}

# Anti-spam: timestamp del último callback por usuario
last_callback_time = {}

# Persistencia simple en archivo JSON
PROGRESO_FILE = "progreso.json"
progreso_lock = threading.Lock()


def escape_telegram(text):
    """Escapa caracteres especiales para evitar errores en Telegram"""
    return html.escape(str(text))


def load_progreso():
    """Cargar progreso desde archivo"""
    if not os.path.exists(PROGRESO_FILE):
        return {}
    try:
        with progreso_lock:
            with open(PROGRESO_FILE, "r", encoding="utf-8") as f:
                return json.load(f)
    except Exception:
        return {}


def save_progreso(data):
    """Guardar progreso en archivo"""
    try:
        with progreso_lock:
            with open(PROGRESO_FILE, "w", encoding="utf-8") as f:
                json.dump(data, f, ensure_ascii=False, indent=2)
    except Exception as e:
        print(f"❌ Error guardando progreso: {e}")


def ensure_user_structure(data, user_id):
    """Asegura que el usuario tenga estructura completa en progreso.json"""
    uid = str(user_id)
    if uid not in data:
        data[uid] = {}

    if 'estado' not in data[uid]:
        data[uid]['estado'] = None  # estado de examen a medias

    if 'fallos' not in data[uid]:
        data[uid]['fallos'] = []  # lista de preguntas falladas

    if 'stats' not in data[uid]:
        # stats por materia
        data[uid]['stats'] = {}
        for mk in MATERIAS.keys():
            data[uid]['stats'][mk] = {
                'intentos': 0,
                'preguntas_respondidas': 0,
                'aciertos': 0,
                'fallos': 0
            }


def guardar_estado_usuario(user_id, estado):
    """Guardar estado del examen a medias"""
    data = load_progreso()
    ensure_user_structure(data, user_id)
    data[str(user_id)]['estado'] = estado
    save_progreso(data)


def borrar_estado_usuario(user_id):
    """Borrar estado del examen a medias"""
    data = load_progreso()
    ensure_user_structure(data, user_id)
    data[str(user_id)]['estado'] = None
    save_progreso(data)


def get_estado_guardado(user_id):
    """Recuperar estado guardado si existe"""
    data = load_progreso()
    ensure_user_structure(data, user_id)
    return data.get(str(user_id), {}).get('estado')


def registrar_respuesta(user_id, materia_key, correcta):
    """Actualizar stats por materia"""
    data = load_progreso()
    ensure_user_structure(data, user_id)

    stats = data[str(user_id)]['stats'].get(materia_key)
    if not stats:
        data[str(user_id)]['stats'][materia_key] = {
            'intentos': 0,
            'preguntas_respondidas': 0,
            'aciertos': 0,
            'fallos': 0
        }
        stats = data[str(user_id)]['stats'][materia_key]

    stats['preguntas_respondidas'] += 1
    if correcta:
        stats['aciertos'] += 1
    else:
        stats['fallos'] += 1

    save_progreso(data)


def registrar_intento_examen(user_id, materia_key):
    """Sumar intento de examen por materia"""
    data = load_progreso()
    ensure_user_structure(data, user_id)

    stats = data[str(user_id)]['stats'].get(materia_key)
    if not stats:
        data[str(user_id)]['stats'][materia_key] = {
            'intentos': 0,
            'preguntas_respondidas': 0,
            'aciertos': 0,
            'fallos': 0
        }
        stats = data[str(user_id)]['stats'][materia_key]

    stats['intentos'] += 1
    save_progreso(data)


def registrar_fallo(user_id, materia_key, tema_idx, examen_idx, pregunta_texto, correcta, elegida):
    """Guardar un fallo en el historial"""
    data = load_progreso()
    ensure_user_structure(data, user_id)

    fallo = {
        'fecha': datetime.utcnow().isoformat() + "Z",
        'materia': materia_key,
        'tema_idx': tema_idx,
        'examen_idx': examen_idx,
        'pregunta': str(pregunta_texto),
        'respuesta_correcta': str(correcta),
        'respuesta_elegida': str(elegida)
    }

    data[str(user_id)]['fallos'].append(fallo)

    # Limitar a los últimos 200 fallos para no inflar el JSON infinito
    if len(data[str(user_id)]['fallos']) > 200:
        data[str(user_id)]['fallos'] = data[str(user_id)]['fallos'][-200:]

    save_progreso(data)


# Mapeo de materias
MATERIAS = {
    'mates': {'nombre': '📐 Matemáticas', 'temario': MATES},
    'lengua': {'nombre': '📚 Lengua', 'temario': LENGUA},
    'ingles': {'nombre': '🇬🇧 Inglés', 'temario': INGLES},
    'frances': {'nombre': '🇫🇷 Francés', 'temario': FRANCES},
    'ciencias': {'nombre': '🔬 Ciencias', 'temario': CIENCIAS}
}


def get_materias_keyboard():
    """Teclado con las 5 materias"""
    markup = types.InlineKeyboardMarkup(row_width=2)
    buttons = [
        types.InlineKeyboardButton('📐 Matemáticas', callback_data='m:0'),
        types.InlineKeyboardButton('📚 Lengua', callback_data='m:1'),
        types.InlineKeyboardButton('🇬🇧 Inglés', callback_data='m:2'),
        types.InlineKeyboardButton('🇫🇷 Francés', callback_data='m:3'),
        types.InlineKeyboardButton('🔬 Ciencias', callback_data='m:4')
    ]
    markup.add(*buttons)
    markup.add(types.InlineKeyboardButton('❌ Cancelar y Salir', callback_data='salir_menu'))
    return markup


def get_temas_keyboard(materia_key):
    """Teclado con los temas de una materia (usando índices)"""
    markup = types.InlineKeyboardMarkup(row_width=1)
    temario = MATERIAS[materia_key]['temario']

    for idx, (unit_key, unit_data) in enumerate(temario.items()):
        titulo = unit_data['titulo']
        materia_idx = list(MATERIAS.keys()).index(materia_key)
        callback = f't:{materia_idx}:{idx}'
        markup.add(types.InlineKeyboardButton(f'{unit_key}: {titulo}', callback_data=callback))

    markup.add(types.InlineKeyboardButton('🔙 Volver', callback_data='volver'))
    markup.add(types.InlineKeyboardButton('❌ Cancelar y Salir', callback_data='salir_menu'))
    return markup


def get_examenes_keyboard(materia_key, tema_idx):
    """Teclado con los 3 exámenes de un tema"""
    markup = types.InlineKeyboardMarkup(row_width=3)
    materia_idx = list(MATERIAS.keys()).index(materia_key)

    buttons = [
        types.InlineKeyboardButton('📝 Examen 1', callback_data=f'e:{materia_idx}:{tema_idx}:0'),
        types.InlineKeyboardButton('📝 Examen 2', callback_data=f'e:{materia_idx}:{tema_idx}:1'),
        types.InlineKeyboardButton('📝 Examen 3', callback_data=f'e:{materia_idx}:{tema_idx}:2')
    ]
    markup.add(*buttons)
    markup.add(types.InlineKeyboardButton('🔙 Volver', callback_data=f't:{materia_idx}'))
    markup.add(types.InlineKeyboardButton('❌ Cancelar y Salir', callback_data='salir_menu'))
    return markup


def get_pregunta_keyboard(respuestas, materia_idx, tema_idx, examen_idx, pregunta_idx):
    """Teclado con las opciones de una pregunta"""
    markup = types.InlineKeyboardMarkup(row_width=1)

    for idx, opcion in enumerate(respuestas):
        callback = f'r:{materia_idx}:{tema_idx}:{examen_idx}:{pregunta_idx}:{idx}'
        markup.add(types.InlineKeyboardButton(opcion, callback_data=callback))

    markup.add(types.InlineKeyboardButton('❌ Cancelar y Salir', callback_data='salir_menu'))
    return markup


def get_reanudar_keyboard():
    """Teclado para reanudar o reiniciar"""
    markup = types.InlineKeyboardMarkup(row_width=1)
    markup.add(types.InlineKeyboardButton('▶️ Continuar examen', callback_data='reanudar'))
    markup.add(types.InlineKeyboardButton('🆕 Empezar de cero', callback_data='reiniciar'))
    markup.add(types.InlineKeyboardButton('❌ Cancelar y Salir', callback_data='salir_menu'))
    return markup


@bot.message_handler(commands=['start'])
def start(message):
    """Comando /start - Mostrar menú principal o reanudar"""
    user_id = message.chat.id

    estado_guardado = get_estado_guardado(user_id)
    if estado_guardado:
        bot.send_message(
            user_id,
            "📌 He encontrado un examen a medias.\n\n¿Qué quieres hacer?",
            reply_markup=get_reanudar_keyboard()
        )
        return

    user_state[user_id] = {}
    bot.send_message(
        user_id,
        '¡Hola! 👋\n\n'
        'Soy tu asistente de estudios para 5º de primaria.\n\n'
        '📚 Elige una materia para comenzar:',
        reply_markup=get_materias_keyboard()
    )


@bot.callback_query_handler(func=lambda call: call.data == 'reanudar')
def reanudar(call):
    user_id = call.message.chat.id
    bot.answer_callback_query(call.id)

    estado_guardado = get_estado_guardado(user_id)
    if not estado_guardado:
        bot.edit_message_text(
            "⚠️ No hay progreso guardado. Usa /start.",
            user_id,
            call.message.message_id
        )
        return

    user_state[user_id] = estado_guardado

    materia_key = estado_guardado['materia']
    tema_idx = estado_guardado['tema_idx']
    examen_idx = estado_guardado['examen_idx']

    temario = MATERIAS[materia_key]['temario']
    tema_key = list(temario.keys())[tema_idx]
    preguntas = temario[tema_key]['examenes'][examen_idx]
    user_state[user_id]['preguntas'] = preguntas

    enviar_pregunta(user_id, call.message.message_id)


@bot.callback_query_handler(func=lambda call: call.data == 'reiniciar')
def reiniciar(call):
    user_id = call.message.chat.id
    bot.answer_callback_query(call.id)

    borrar_estado_usuario(user_id)
    user_state[user_id] = {}

    bot.edit_message_text(
        '📚 Elige una materia para comenzar:',
        user_id,
        call.message.message_id,
        reply_markup=get_materias_keyboard()
    )


@bot.callback_query_handler(func=lambda call: call.data == 'salir_menu')
def cancelar(call):
    """Cancelar flujo y salir"""
    user_id = call.message.chat.id

    try:
        bot.answer_callback_query(call.id)
    except Exception:
        pass

    user_state[user_id] = {}

    try:
        bot.delete_message(user_id, call.message.message_id)
    except Exception:
        try:
            bot.edit_message_text(
                "Operación cancelada. Usa /start para volver a empezar.",
                user_id,
                call.message.message_id
            )
            return
        except Exception:
            pass

    bot.send_message(
        user_id,
        "Operación cancelada. Usa /start para volver a empezar."
    )


@bot.callback_query_handler(func=lambda call: call.data.startswith('m:'))
def seleccionar_materia(call):
    """Selección de materia"""
    user_id = call.message.chat.id
    materia_idx = int(call.data.split(':')[1])
    materia_key = list(MATERIAS.keys())[materia_idx]

    user_state[user_id] = {'materia': materia_key}

    bot.edit_message_text(
        f"{MATERIAS[materia_key]['nombre']}\n\n"
        "📖 Selecciona un tema:",
        user_id,
        call.message.message_id,
        reply_markup=get_temas_keyboard(materia_key)
    )


@bot.callback_query_handler(func=lambda call: call.data.startswith('t:'))
def seleccionar_tema(call):
    """Selección de tema"""
    user_id = call.message.chat.id
    parts = call.data.split(':')

    materia_idx = int(parts[1])
    materia_key = list(MATERIAS.keys())[materia_idx]

    if len(parts) == 2:
        user_state[user_id] = {'materia': materia_key}
        bot.edit_message_text(
            f"{MATERIAS[materia_key]['nombre']}\n\n"
            "📖 Selecciona un tema:",
            user_id,
            call.message.message_id,
            reply_markup=get_temas_keyboard(materia_key)
        )
    else:
        tema_idx = int(parts[2])
        temario = MATERIAS[materia_key]['temario']
        tema_key = list(temario.keys())[tema_idx]
        tema_titulo = temario[tema_key]['titulo']

        user_state[user_id] = {
            'materia': materia_key,
            'tema_idx': tema_idx
        }

        bot.edit_message_text(
            f"📚 {tema_titulo}\n\n"
            "Elige un examen:",
            user_id,
            call.message.message_id,
            reply_markup=get_examenes_keyboard(materia_key, tema_idx)
        )


@bot.callback_query_handler(func=lambda call: call.data.startswith('e:'))
def iniciar_examen(call):
    """Iniciar examen seleccionado"""
    user_id = call.message.chat.id
    parts = call.data.split(':')

    materia_idx = int(parts[1])
    tema_idx = int(parts[2])
    examen_idx = int(parts[3])

    materia_key = list(MATERIAS.keys())[materia_idx]
    temario = MATERIAS[materia_key]['temario']
    tema_key = list(temario.keys())[tema_idx]

    preguntas = temario[tema_key]['examenes'][examen_idx]

    user_state[user_id] = {
        'materia': materia_key,
        'materia_idx': materia_idx,
        'tema_idx': tema_idx,
        'examen_idx': examen_idx,
        'pregunta_actual': 0,
        'respuestas_correctas': 0,
        'preguntas': preguntas
    }

    # Registrar intento y guardar estado inicial
    registrar_intento_examen(user_id, materia_key)

    guardar_estado_usuario(user_id, {
        'materia': materia_key,
        'materia_idx': materia_idx,
        'tema_idx': tema_idx,
        'examen_idx': examen_idx,
        'pregunta_actual': 0,
        'respuestas_correctas': 0
    })

    enviar_pregunta(user_id, call.message.message_id)


def enviar_pregunta(user_id, message_id):
    """Enviar pregunta actual"""
    state = user_state[user_id]
    pregunta_idx = state['pregunta_actual']
    preguntas = state['preguntas']

    if pregunta_idx >= len(preguntas):
        finalizar_examen(user_id, message_id)
        return

    pregunta = preguntas[pregunta_idx]

    total = len(preguntas)
    progreso = '▰' * (pregunta_idx + 1) + '▱' * (total - pregunta_idx - 1)

    texto = (
        f"❓ Pregunta {pregunta_idx + 1}/{total}\n"
        f"[{progreso}]\n\n"
        f"{pregunta['p']}"
    )

    bot.edit_message_text(
        texto,
        user_id,
        message_id,
        reply_markup=get_pregunta_keyboard(
            pregunta['o'],
            state['materia_idx'],
            state['tema_idx'],
            state['examen_idx'],
            pregunta_idx
        )
    )


@bot.callback_query_handler(func=lambda call: call.data.startswith('r:'))
def procesar_respuesta(call):
    """Procesar respuesta del usuario"""
    user_id = call.message.chat.id
    parts = call.data.split(':')

    pregunta_idx = int(parts[4])
    opcion_idx = int(parts[5])

    state = user_state.get(user_id)
    if not state:
        bot.answer_callback_query(call.id, "⚠️ Sesión expirada. Usa /start", show_alert=True)
        return

    if pregunta_idx != state['pregunta_actual']:
        bot.answer_callback_query(call.id, "⏭️ Ya respondiste esta pregunta")
        return

    pregunta = state['preguntas'][pregunta_idx]
    respuesta_usuario = pregunta['o'][opcion_idx]
    respuesta_correcta = pregunta['r']

    correcta = (respuesta_usuario == respuesta_correcta)

    if correcta:
        state['respuestas_correctas'] += 1
        emoji = '✅'
        texto = '¡Correcto! Muy bien 👏'
    else:
        emoji = '❌'
        texto = f'Incorrecto.\n\n💡 La respuesta correcta era:\n"{respuesta_correcta}"'

        # Registrar fallo
        registrar_fallo(
            user_id,
            state['materia'],
            state['tema_idx'],
            state['examen_idx'],
            pregunta['p'],
            respuesta_correcta,
            respuesta_usuario
        )

    # Registrar stats por materia
    registrar_respuesta(user_id, state['materia'], correcta)

    bot.answer_callback_query(call.id, f'{emoji}', show_alert=False)

    state['pregunta_actual'] += 1

    # Guardar progreso tras cada respuesta
    guardar_estado_usuario(user_id, {
        'materia': state['materia'],
        'materia_idx': state['materia_idx'],
        'tema_idx': state['tema_idx'],
        'examen_idx': state['examen_idx'],
        'pregunta_actual': state['pregunta_actual'],
        'respuestas_correctas': state['respuestas_correctas']
    })

    enviar_pregunta(user_id, call.message.message_id)


def finalizar_examen(user_id, message_id):
    """Mostrar resultados finales"""
    state = user_state[user_id]
    correctas = state['respuestas_correctas']
    total = len(state['preguntas'])
    incorrectas = total - correctas
    porcentaje = (correctas / total) * 100

    # Al terminar el examen, borramos progreso guardado (estado a medias)
    borrar_estado_usuario(user_id)

    if porcentaje >= 90:
        emoji = '🏆'
        mensaje = '¡EXCELENTE!'
        consejo = 'Dominas el tema perfectamente. ¡Sigue así!'
    elif porcentaje >= 70:
        emoji = '⭐'
        mensaje = '¡MUY BIEN!'
        consejo = 'Buen trabajo. Repasa los errores para mejorar aún más.'
    elif porcentaje >= 50:
        emoji = '👍'
        mensaje = 'BIEN HECHO'
        consejo = 'Vas por buen camino. Practica un poco más para dominar el tema.'
    else:
        emoji = '📚'
        mensaje = 'SIGUE PRACTICANDO'
        consejo = 'No te desanimes. Revisa el tema y vuelve a intentarlo.'

    barras_llenas = int((correctas / total) * 10)
    barra_resultado = '▰' * barras_llenas + '▱' * (10 - barras_llenas)

    texto = (
        f"{emoji} {mensaje}\n\n"
        f"📊 Tu puntuación: {correctas}/{total} ({porcentaje:.0f}%)\n"
        f"[{barra_resultado}]\n\n"
        f"✅ Respuestas correctas: {correctas}\n"
        f"❌ Respuestas incorrectas: {incorrectas}\n\n"
        f"💡 {consejo}"
    )

    markup = types.InlineKeyboardMarkup()
    markup.row(
        types.InlineKeyboardButton(
            '🔄 Repetir examen',
            callback_data=f'e:{state["materia_idx"]}:{state["tema_idx"]}:{state["examen_idx"]}'
        ),
        types.InlineKeyboardButton(
            '📚 Otros temas',
            callback_data=f't:{state["materia_idx"]}'
        )
    )
    markup.add(types.InlineKeyboardButton('🏠 Menú principal', callback_data='menu'))
    markup.add(types.InlineKeyboardButton('❌ Cancelar y Salir', callback_data='salir_menu'))

    bot.edit_message_text(texto, user_id, message_id, reply_markup=markup)


@bot.callback_query_handler(func=lambda call: call.data == 'volver')
def volver_materias(call):
    """Volver al menú de materias"""
    user_id = call.message.chat.id
    user_state[user_id] = {}

    bot.edit_message_text(
        '📚 Elige una materia para comenzar:',
        user_id,
        call.message.message_id,
        reply_markup=get_materias_keyboard()
    )


@bot.callback_query_handler(func=lambda call: call.data == 'menu')
def menu_principal(call):
    """Volver al menú principal"""
    volver_materias(call)


# CONFIGURACIÓN FLASK Y WEBHOOK
@app.route('/')
def index():
    return "Bot funcionando ✅"


@app.route(f'/{TOKEN}', methods=['POST'])
def webhook():
    """Recibir actualizaciones de Telegram"""
    try:
        json_str = request.get_data().decode('UTF-8')
        update = telebot.types.Update.de_json(json_str)
        bot.process_new_updates([update])
        return '', 200
    except Exception as e:
        print(f"❌ Error en webhook: {e}")
        return '', 500


@bot.message_handler(func=lambda message: True)
def handle_unknown(message):
    """Manejar mensajes desconocidos"""
    bot.reply_to(
        message,
        "🤔 No entiendo ese comando.\n\n"
        "Usa /start para comenzar."
    )


@bot.callback_query_handler(func=lambda call: call.data == 'stats')
def ver_stats(call):
    """Mostrar estadísticas del usuario"""
    user_id = call.message.chat.id
    bot.answer_callback_query(call.id)

    data = load_progreso()
    ensure_user_structure(data, user_id)
    stats = data[str(user_id)]['stats']

    texto = "📊 <b>Estadísticas por materia</b>\n\n"
    for mk, st in stats.items():
        nombre = MATERIAS[mk]['nombre']
        preguntas = st['preguntas_respondidas']
        aciertos = st['aciertos']
        fallos = st['fallos']
        intentos = st['intentos']

        if preguntas > 0:
            pct = (aciertos / preguntas) * 100
        else:
            pct = 0

        texto += (
            f"{nombre}\n"
            f"📝 Intentos: {intentos}\n"
            f"📌 Preguntas: {preguntas}\n"
            f"✅ Aciertos: {aciertos}\n"
            f"❌ Fallos: {fallos}\n"
            f"🎯 Precisión: {pct:.0f}%\n\n"
        )

    bot.send_message(user_id, texto, parse_mode="HTML")


# Manejo de errores global
@bot.callback_query_handler(func=lambda call: True)
def handle_unknown_callback(call):
    """Capturar callbacks no manejados"""
    bot.answer_callback_query(call.id, "⚠️ Acción no reconocida. Usa /start", show_alert=True)


@app.route('/set_webhook')
def set_webhook():
    """Configurar webhook (llamar una vez al desplegar)"""
    webhook_url = f'https://{DOMAIN}/{TOKEN}'
    bot.remove_webhook()
    bot.set_webhook(url=webhook_url)
    return f'Webhook configurado: {webhook_url}'


if __name__ == '__main__':
    if not DOMAIN:
        print("⚠️  Modo desarrollo (sin webhook)")
        bot.remove_webhook()
        bot.polling()
    else:
        port = int(os.environ.get('PORT', 8080))
        print(f"🚀 Iniciando servidor en puerto {port}")
        app.run(host='0.0.0.0', port=port, debug=False)
