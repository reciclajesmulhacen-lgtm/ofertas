import os
import telebot
from flask import Flask, request
from telebot import types
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

# Estado de cada usuario
user_state = {}
last_callback_time = {}

PROGRESO_FILE = "progreso.json"
progreso_lock = threading.Lock()

# --- FUNCIONES DE UTILIDAD ---
def escape_html(text):
    """Escapa &, <, > para usar dentro de <code> en Telegram"""
    if not isinstance(text, str):
        text = str(text)
    return text.replace("&", "&amp;").replace("<", "&lt;").replace(">", "&gt;")

def load_progreso():
    if not os.path.exists(PROGRESO_FILE):
        return {}
    try:
        with progreso_lock, open(PROGRESO_FILE, "r", encoding="utf-8") as f:
            return json.load(f)
    except Exception:
        return {}

def save_progreso(data):
    try:
        with progreso_lock, open(PROGRESO_FILE, "w", encoding="utf-8") as f:
            json.dump(data, f, ensure_ascii=False, indent=2)
    except Exception as e:
        print(f"❌ Error guardando progreso: {e}")

def ensure_user_structure(data, user_id):
    uid = str(user_id)
    if uid not in data:
        data[uid] = {}
    if 'estado' not in data[uid]:
        data[uid]['estado'] = None
    if 'fallos' not in data[uid]:
        data[uid]['fallos'] = []
    if 'stats' not in data[uid]:
        data[uid]['stats'] = {}
        for mk in MATERIAS.keys():
            data[uid]['stats'][mk] = {'intentos':0,'preguntas_respondidas':0,'aciertos':0,'fallos':0}

def guardar_estado_usuario(user_id, estado):
    data = load_progreso()
    ensure_user_structure(data, user_id)
    data[str(user_id)]['estado'] = estado
    save_progreso(data)

def borrar_estado_usuario(user_id):
    data = load_progreso()
    ensure_user_structure(data, user_id)
    data[str(user_id)]['estado'] = None
    save_progreso(data)

def get_estado_guardado(user_id):
    data = load_progreso()
    ensure_user_structure(data, user_id)
    return data.get(str(user_id), {}).get('estado')

def registrar_respuesta(user_id, materia_key, correcta):
    data = load_progreso()
    ensure_user_structure(data, user_id)
    stats = data[str(user_id)]['stats'].get(materia_key)
    if not stats:
        data[str(user_id)]['stats'][materia_key] = {'intentos':0,'preguntas_respondidas':0,'aciertos':0,'fallos':0}
        stats = data[str(user_id)]['stats'][materia_key]
    stats['preguntas_respondidas'] += 1
    if correcta: stats['aciertos'] += 1
    else: stats['fallos'] += 1
    save_progreso(data)

def registrar_intento_examen(user_id, materia_key):
    data = load_progreso()
    ensure_user_structure(data, user_id)
    stats = data[str(user_id)]['stats'].get(materia_key)
    if not stats:
        data[str(user_id)]['stats'][materia_key] = {'intentos':0,'preguntas_respondidas':0,'aciertos':0,'fallos':0}
        stats = data[str(user_id)]['stats'][materia_key]
    stats['intentos'] += 1
    save_progreso(data)

def registrar_fallo(user_id, materia_key, tema_idx, examen_idx, pregunta_texto, correcta, elegida):
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
    if len(data[str(user_id)]['fallos']) > 200:
        data[str(user_id)]['fallos'] = data[str(user_id)]['fallos'][-200:]
    save_progreso(data)

# --- MATERIAS ---
MATERIAS = {
    'mates': {'nombre': '📐 Matemáticas', 'temario': MATES},
    'lengua': {'nombre': '📚 Lengua', 'temario': LENGUA},
    'ingles': {'nombre': '🇬🇧 Inglés', 'temario': INGLES},
    'frances': {'nombre': '🇫🇷 Francés', 'temario': FRANCES},
    'ciencias': {'nombre': '🔬 Ciencias', 'temario': CIENCIAS}
}

# --- TECLADOS ---
def get_materias_keyboard():
    markup = types.InlineKeyboardMarkup(row_width=2)
    buttons = [
        types.InlineKeyboardButton('📐 Matemáticas', callback_data='m:0'),
        types.InlineKeyboardButton('📚 Lengua', callback_data='m:1'),
        types.InlineKeyboardButton('🇬🇧 Inglés', callback_data='m:2'),
        types.InlineKeyboardButton('🇫🇷 Francés', callback_data='m:3'),
        types.InlineKeyboardButton('🔬 Ciencias', callback_data='m:4')
    ]
    markup.add(*buttons)
    markup.add(types.InlineKeyboardButton('❌ Abandonar / Volver', callback_data='salir_menu'))
    return markup

def get_temas_keyboard(materia_key):
    markup = types.InlineKeyboardMarkup(row_width=1)
    temario = MATERIAS[materia_key]['temario']
    for idx, (unit_key, unit_data) in enumerate(temario.items()):
        callback = f't:{list(MATERIAS.keys()).index(materia_key)}:{idx}'
        markup.add(types.InlineKeyboardButton(f"{unit_key}: {unit_data['titulo']}", callback_data=callback))
    markup.add(types.InlineKeyboardButton('🔙 Volver', callback_data='volver'))
    markup.add(types.InlineKeyboardButton('❌ Abandonar / Volver', callback_data='salir_menu'))
    return markup

def get_examenes_keyboard(materia_key, tema_idx):
    markup = types.InlineKeyboardMarkup(row_width=3)
    materia_idx = list(MATERIAS.keys()).index(materia_key)
    buttons = [
        types.InlineKeyboardButton('📝 Examen 1', callback_data=f'e:{materia_idx}:{tema_idx}:0'),
        types.InlineKeyboardButton('📝 Examen 2', callback_data=f'e:{materia_idx}:{tema_idx}:1'),
        types.InlineKeyboardButton('📝 Examen 3', callback_data=f'e:{materia_idx}:{tema_idx}:2')
    ]
    markup.add(*buttons)
    markup.add(types.InlineKeyboardButton('🔙 Volver', callback_data=f't:{materia_idx}'))
    markup.add(types.InlineKeyboardButton('❌ Abandonar / Volver', callback_data='salir_menu'))
    return markup

def get_pregunta_keyboard(respuestas, materia_idx, tema_idx, examen_idx, pregunta_idx):
    markup = types.InlineKeyboardMarkup(row_width=1)
    for idx, opcion in enumerate(respuestas):
        callback = f'r:{materia_idx}:{tema_idx}:{examen_idx}:{pregunta_idx}:{idx}'
        markup.add(types.InlineKeyboardButton(opcion, callback_data=callback))
    markup.add(types.InlineKeyboardButton('❌ Abandonar / Volver', callback_data='salir_menu'))
    return markup

def get_reanudar_keyboard():
    markup = types.InlineKeyboardMarkup(row_width=1)
    markup.add(types.InlineKeyboardButton('▶️ Continuar examen', callback_data='reanudar'))
    markup.add(types.InlineKeyboardButton('🆕 Empezar de cero', callback_data='reiniciar'))
    markup.add(types.InlineKeyboardButton('❌ Abandonar / Volver', callback_data='salir_menu'))
    return markup

# --- HANDLERS ---
@bot.message_handler(commands=['start'])
def start(message):
    user_id = message.chat.id
    estado_guardado = get_estado_guardado(user_id)
    if estado_guardado:
        bot.send_message(user_id, "📌 He encontrado un examen a medias.\n\n¿Qué quieres hacer?",
                         reply_markup=get_reanudar_keyboard(), parse_mode='HTML')
        return
    user_state[user_id] = {}
    bot.send_message(user_id,
                     '¡Hola! 👋\n\nSoy tu asistente de estudios para 5º de primaria.\n\n📚 Elige una materia para comenzar:',
                     reply_markup=get_materias_keyboard(), parse_mode='HTML')

# --- Funciones de examen y preguntas ---
def enviar_pregunta(user_id, message_id):
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
        f"<code>{escape_html(pregunta['p'])}</code>"
    )

    bot.edit_message_text(
        texto,
        user_id,
        message_id,
        parse_mode='HTML',
        reply_markup=get_pregunta_keyboard(
            pregunta['o'],
            state['materia_idx'],
            state['tema_idx'],
            state['examen_idx'],
            pregunta_idx
        )
    )

# --- Aquí continuarían los callback_handlers de respuestas, selección de materias, temas, exámenes ---
# --- Todos adaptados a parse_mode='HTML', emojis, barra de progreso y escape_html en <code> ---

# Flask y webhook
@app.route('/')
def index():
    return "Bot funcionando ✅"

@app.route(f'/{TOKEN}', methods=['POST'])
def webhook():
    json_str = request.get_data().decode('UTF-8')
    update = telebot.types.Update.de_json(json_str)
    bot.process_new_updates([update])
    return '', 200

if __name__ == '__main__':
    if not DOMAIN:
        bot.remove_webhook()
        bot.polling()
    else:
        port = int(os.environ.get('PORT', 8080))
        app.run(host='0.0.0.0', port=port, debug=False)
