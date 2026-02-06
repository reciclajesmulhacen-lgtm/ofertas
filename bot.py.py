import os
import telebot
from flask import Flask, request
from telebot import types
import html

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


def escape_telegram(text):
    """Escapa caracteres especiales para evitar errores en Telegram"""
    # HTML entities básicos para modo HTML
    return html.escape(str(text))


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
    return markup


def get_temas_keyboard(materia_key):
    """Teclado con los temas de una materia (usando índices)"""
    markup = types.InlineKeyboardMarkup(row_width=1)
    temario = MATERIAS[materia_key]['temario']
    
    for idx, (unit_key, unit_data) in enumerate(temario.items()):
        titulo = unit_data['titulo']
        # callback_data: t:materia_idx:tema_idx
        materia_idx = list(MATERIAS.keys()).index(materia_key)
        callback = f't:{materia_idx}:{idx}'
        markup.add(types.InlineKeyboardButton(f'{unit_key}: {titulo}', callback_data=callback))
    
    # Botón volver
    markup.add(types.InlineKeyboardButton('🔙 Volver', callback_data='volver'))
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
    return markup


def get_pregunta_keyboard(respuestas, materia_idx, tema_idx, examen_idx, pregunta_idx):
    """Teclado con las opciones de una pregunta"""
    markup = types.InlineKeyboardMarkup(row_width=1)
    
    for idx, opcion in enumerate(respuestas):
        # callback_data: r:materia:tema:examen:pregunta:opcion
        callback = f'r:{materia_idx}:{tema_idx}:{examen_idx}:{pregunta_idx}:{idx}'
        markup.add(types.InlineKeyboardButton(opcion, callback_data=callback))
    
    return markup


@bot.message_handler(commands=['start'])
def start(message):
    """Comando /start - Mostrar menú principal"""
    user_id = message.chat.id
    user_state[user_id] = {}
    
    bot.send_message(
        user_id,
        '¡Hola! 👋\n\n'
        'Soy tu asistente de estudios para 5º de primaria.\n\n'
        '📚 Elige una materia para comenzar:',
        reply_markup=get_materias_keyboard()
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
        # Volver a temas
        user_state[user_id] = {'materia': materia_key}
        bot.edit_message_text(
            f"{MATERIAS[materia_key]['nombre']}\n\n"
            "📖 Selecciona un tema:",
            user_id,
            call.message.message_id,
            reply_markup=get_temas_keyboard(materia_key)
        )
    else:
        # Seleccionar tema específico
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
    
    # Guardar estado del examen
    user_state[user_id] = {
        'materia': materia_key,
        'materia_idx': materia_idx,
        'tema_idx': tema_idx,
        'examen_idx': examen_idx,
        'pregunta_actual': 0,
        'respuestas_correctas': 0,
        'preguntas': preguntas
    }
    
    # Enviar primera pregunta
    enviar_pregunta(user_id, call.message.message_id)


def enviar_pregunta(user_id, message_id):
    """Enviar pregunta actual"""
    state = user_state[user_id]
    pregunta_idx = state['pregunta_actual']
    preguntas = state['preguntas']
    
    if pregunta_idx >= len(preguntas):
        # Examen terminado
        finalizar_examen(user_id, message_id)
        return
    
    pregunta = preguntas[pregunta_idx]
    
    # Barra de progreso visual
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
    
    # Anti-spam: verificar que sea la pregunta actual
    if pregunta_idx != state['pregunta_actual']:
        bot.answer_callback_query(call.id, "⏭️ Ya respondiste esta pregunta")
        return
    
    pregunta = state['preguntas'][pregunta_idx]
    respuesta_usuario = pregunta['o'][opcion_idx]
    respuesta_correcta = pregunta['r']
    
    # Verificar respuesta
    if respuesta_usuario == respuesta_correcta:
        state['respuestas_correctas'] += 1
        emoji = '✅'
        texto = '¡Correcto! Muy bien 👏'
    else:
        emoji = '❌'
        texto = f'Incorrecto.\n\n💡 La respuesta correcta era:\n"{respuesta_correcta}"'
    
    # Mostrar resultado con explicación
    bot.answer_callback_query(call.id, f'{emoji}', show_alert=False)
    
    # Siguiente pregunta
    state['pregunta_actual'] += 1
    enviar_pregunta(user_id, call.message.message_id)


def finalizar_examen(user_id, message_id):
    """Mostrar resultados finales"""
    state = user_state[user_id]
    correctas = state['respuestas_correctas']
    total = len(state['preguntas'])
    incorrectas = total - correctas
    porcentaje = (correctas / total) * 100
    
    # Determinar emoji y mensaje según nota
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
    
    # Barra de progreso visual del resultado
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
        types.InlineKeyboardButton('🔄 Repetir examen', callback_data=f'e:{state["materia_idx"]}:{state["tema_idx"]}:{state["examen_idx"]}'),
        types.InlineKeyboardButton('📚 Otros temas', callback_data=f't:{state["materia_idx"]}')
    )
    markup.add(types.InlineKeyboardButton('🏠 Menú principal', callback_data='menu'))
    
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
    # Para desarrollo local (sin webhook)
    if not DOMAIN:
        print("⚠️  Modo desarrollo (sin webhook)")
        bot.remove_webhook()
        bot.polling()
    else:
        # Producción con webhook en Railway
        port = int(os.environ.get('PORT', 8080))
        print(f"🚀 Iniciando servidor en puerto {port}")
        app.run(host='0.0.0.0', port=port, debug=False)
