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

bot = telebot.TeleBot(TOKEN, parse_mode='HTML')
app = Flask(__name__)

user_state = {}
progreso_lock = threading.Lock()
PROGRESO_FILE = "progreso.json"

# ================= UTILIDADES =================
def escape_html(text):
    if text is None:
        return ""
    return str(text).replace("&", "&amp;").replace("<", "&lt;").replace(">", "&gt;")

def load_progreso():
    if not os.path.exists(PROGRESO_FILE):
        return {}
    try:
        with progreso_lock:
            with open(PROGRESO_FILE, "r", encoding="utf-8") as f:
                return json.load(f)
    except Exception:
        return {}

def save_progreso(data):
    try:
        with progreso_lock:
            with open(PROGRESO_FILE, "w", encoding="utf-8") as f:
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
    if correcta:
        stats['aciertos'] += 1
    else:
        stats['fallos'] += 1
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

# ================= MATERIAS =================
MATERIAS = {
    'mates':{'nombre':'📐 Matemáticas','temario':MATES},
    'lengua':{'nombre':'📚 Lengua','temario':LENGUA},
    'ingles':{'nombre':'🇬🇧 Inglés','temario':INGLES},
    'frances':{'nombre':'🇫🇷 Francés','temario':FRANCES},
    'ciencias':{'nombre':'🔬 Ciencias','temario':CIENCIAS}
}

# ================= TECLADOS =================
def get_materias_keyboard():
    markup = types.InlineKeyboardMarkup(row_width=2)
    for i, v in enumerate(MATERIAS.values()):
        markup.add(types.InlineKeyboardButton(v['nombre'], callback_data=f"m:{i}"))
    markup.add(types.InlineKeyboardButton('❌ Cancelar / Salir', callback_data='salir_menu'))
    return markup

def get_temas_keyboard(materia_key):
    markup = types.InlineKeyboardMarkup(row_width=1)
    temario = MATERIAS[materia_key]['temario']
    for idx, (unit_key, unit_data) in enumerate(temario.items()):
        markup.add(types.InlineKeyboardButton(f"{unit_key}: {unit_data['titulo']}", callback_data=f"t:{materia_key}:{idx}"))
    markup.add(types.InlineKeyboardButton('🔙 Volver', callback_data='menu'))
    markup.add(types.InlineKeyboardButton('❌ Cancelar / Salir', callback_data='salir_menu'))
    return markup

def get_examenes_keyboard(materia_key, tema_idx):
    markup = types.InlineKeyboardMarkup(row_width=3)
    for ex_idx in range(3):
        markup.add(types.InlineKeyboardButton(f"📝 Examen {ex_idx+1}", callback_data=f"e:{materia_key}:{tema_idx}:{ex_idx}"))
    markup.add(types.InlineKeyboardButton('🔙 Volver', callback_data=f"t:{materia_key}"))
    markup.add(types.InlineKeyboardButton('❌ Cancelar / Salir', callback_data='salir_menu'))
    return markup

def get_pregunta_keyboard(respuestas, materia_key, tema_idx, examen_idx, pregunta_idx):
    markup = types.InlineKeyboardMarkup(row_width=1)
    for idx, opcion in enumerate(respuestas):
        markup.add(types.InlineKeyboardButton(opcion, callback_data=f"r:{materia_key}:{tema_idx}:{examen_idx}:{pregunta_idx}:{idx}"))
    markup.add(types.InlineKeyboardButton('❌ Cancelar / Salir', callback_data='salir_menu'))
    return markup

def get_reanudar_keyboard():
    markup = types.InlineKeyboardMarkup(row_width=1)
    markup.add(types.InlineKeyboardButton('▶️ Continuar examen', callback_data='reanudar'))
    markup.add(types.InlineKeyboardButton('🆕 Empezar de cero', callback_data='reiniciar'))
    markup.add(types.InlineKeyboardButton('❌ Cancelar / Salir', callback_data='salir_menu'))
    return markup

# ================= HANDLERS =================
@bot.message_handler(commands=['start'])
def start(message):
    user_id = message.chat.id
    estado_guardado = get_estado_guardado(user_id)
    if estado_guardado:
        bot.send_message(user_id, "📌 He encontrado un examen a medias.\n\n¿Qué quieres hacer?", reply_markup=get_reanudar_keyboard())
        return
    user_state[user_id] = {}
    bot.send_message(user_id, "¡Hola! 👋\n\nSoy tu asistente de estudios para 5º de primaria.\n\n📚 Elige una materia para comenzar:", reply_markup=get_materias_keyboard())

@bot.callback_query_handler(func=lambda call: True)
def callbacks(call):
    user_id = call.message.chat.id
    data = call.data
    bot.answer_callback_query(call.id)
    # ------------------ Materias ------------------
    if data.startswith("m:"):
        idx = int(data.split(":")[1])
        materia_key = list(MATERIAS.keys())[idx]
        user_state[user_id] = {'materia': materia_key}
        bot.edit_message_text(f"{MATERIAS[materia_key]['nombre']}\n\n📖 Selecciona un tema:", user_id, call.message.message_id, reply_markup=get_temas_keyboard(materia_key))
    # ------------------ Temas ------------------
    elif data.startswith("t:"):
        parts = data.split(":")
        materia_key = parts[1]
        if len(parts) == 2:
            bot.edit_message_text(f"{MATERIAS[materia_key]['nombre']}\n\n📖 Selecciona un tema:", user_id, call.message.message_id, reply_markup=get_temas_keyboard(materia_key))
        else:
            tema_idx = int(parts[2])
            temario = MATERIAS[materia_key]['temario']
            tema_key = list(temario.keys())[tema_idx]
            user_state[user_id].update({'tema_idx': tema_idx})
            bot.edit_message_text(f"📚 {temario[tema_key]['titulo']}\n\nElige un examen:", user_id, call.message.message_id, reply_markup=get_examenes_keyboard(materia_key, tema_idx))
    # ------------------ Exámenes ------------------
    elif data.startswith("e:"):
        parts = data.split(":")
        materia_key = parts[1]
        tema_idx = int(parts[2])
        examen_idx = int(parts[3])
        temario = MATERIAS[materia_key]['temario']
        tema_key = list(temario.keys())[tema_idx]
        preguntas = temario[tema_key]['examenes'][examen_idx]
        user_state[user_id].update({'materia':materia_key,'tema_idx':tema_idx,'examen_idx':examen_idx,'preguntas':preguntas,'pregunta_actual':0,'respuestas_correctas':0})
        registrar_intento_examen(user_id, materia_key)
        guardar_estado_usuario(user_id, {'materia':materia_key,'materia_idx':list(MATERIAS.keys()).index(materia_key),'tema_idx':tema_idx,'examen_idx':examen_idx,'pregunta_actual':0,'respuestas_correctas':0})
        enviar_pregunta(user_id, call.message.message_id)
    # ------------------ Respuestas ------------------
    elif data.startswith("r:"):
        procesar_respuesta(call)
    # ------------------ Reanudar ------------------
    elif data == "reanudar":
        estado_guardado = get_estado_guardado(user_id)
        if estado_guardado:
            materia_key = estado_guardado['materia']
            tema_idx = estado_guardado['tema_idx']
            examen_idx = estado_guardado['examen_idx']
            temario = MATERIAS[materia_key]['temario']
            tema_key = list(temario.keys())[tema_idx]
            preguntas = temario[tema_key]['examenes'][examen_idx]
            user_state[user_id] = {'materia':materia_key,'tema_idx':tema_idx,'examen_idx':examen_idx,'preguntas':preguntas,'pregunta_actual':estado_guardado['pregunta_actual'],'respuestas_correctas':estado_guardado['respuestas_correctas']}
            enviar_pregunta(user_id, call.message.message_id)
    # ------------------ Reiniciar ------------------
    elif data == "reiniciar":
        borrar_estado_usuario(user_id)
        user_state[user_id] = {}
        bot.edit_message_text("📚 Elige una materia para comenzar:", user_id, call.message.message_id, reply_markup=get_materias_keyboard())
    # ------------------ Salir/Menu ------------------
    elif data in ["salir_menu","menu"]:
        user_state[user_id] = {}
        bot.edit_message_text("📚 Menú principal:\nElige una materia:", user_id, call.message.message_id, reply_markup=get_materias_keyboard())

# ================= PREGUNTAS =================
def enviar_pregunta(user_id, message_id):
    state = user_state[user_id]
    idx = state['pregunta_actual']
    preguntas = state['preguntas']
    if idx >= len(preguntas):
        finalizar_examen(user_id, message_id)
        return
    pregunta = preguntas[idx]
    total = len(preguntas)
    progreso = "▰"* (idx+1) + "▱"*(total-idx-1)
    texto = f"❓ Pregunta {idx+1}/{total}\n[{progreso}]\n\n<code>{escape_html(pregunta['p'])}</code>"
    bot.edit_message_text(texto,user_id,message_id,reply_markup=get_pregunta_keyboard(pregunta['o'],state['materia'],state['tema_idx'],state['examen_idx'],idx))

def procesar_respuesta(call):
    user_id = call.message.chat.id
    parts = call.data.split(":")
    pregunta_idx = int(parts[4])
    opcion_idx = int(parts[5])
    state = user_state.get(user_id)
    if not state:
        bot.answer_callback_query(call.id,"⚠️ Sesión expirada. Usa /start",show_alert=True)
        return
    if pregunta_idx != state['pregunta_actual']:
        bot.answer_callback_query(call.id,"⏭️ Ya respondiste esta pregunta")
        return
    pregunta = state['preguntas'][pregunta_idx]
    respuesta_usuario = pregunta['o'][opcion_idx]
    respuesta_correcta = pregunta['r']
    correcta = (respuesta_usuario == respuesta_correcta)
    if correcta:
        state['respuestas_correctas'] += 1
        emoji = "✅"
    else:
        emoji = "❌"
        registrar_fallo(user_id,state['materia'],state['tema_idx'],state['examen_idx'],pregunta['p'],respuesta_correcta,respuesta_usuario)
    registrar_respuesta(user_id,state['materia'],correcta)
    bot.answer_callback_query(call.id,f"{emoji}",show_alert=False)
    state['pregunta_actual'] += 1
    guardar_estado_usuario(user_id,{'materia':state['materia'],'materia_idx':list(MATERIAS.keys()).index(state['materia']),'tema_idx':state['tema_idx'],'examen_idx':state['examen_idx'],'pregunta_actual':state['pregunta_actual'],'respuestas_correctas':state['respuestas_correctas']})
    enviar_pregunta(user_id,call.message.message_id)

def finalizar_examen(user_id,message_id):
    state = user_state[user_id]
    correctas = state['respuestas_correctas']
    total = len(state['preguntas'])
    incorrectas = total - correctas
    porcentaje = (correctas/total)*100
    borrar_estado_usuario(user_id)
    barras_llenas = int((correctas/total)*10)
    barra_resultado = "▰"*barras_llenas + "▱"*(10-barras_llenas)
    if porcentaje >= 90:
        emoji = "🏆"
        mensaje = "¡EXCELENTE!"
        consejo = "Dominas el tema perfectamente. ¡Sigue así!"
    elif porcentaje >= 70:
        emoji = "⭐"
        mensaje = "¡MUY BIEN!"
        consejo = "Buen trabajo. Repasa los errores para mejorar aún más."
    elif porcentaje >= 50:
        emoji = "👍"
        mensaje = "BIEN HECHO"
        consejo = "Practica un poco más para dominar el tema."
    else:
        emoji = "📚"
        mensaje = "SIGUE PRACTICANDO"
        consejo = "No te desanimes. Revisa el tema y vuelve a intentarlo."
    texto = f"{emoji} {mensaje}\n\n📊 Tu puntuación: {correctas}/{total} ({porcentaje:.0f}%)\n[{barra_resultado}]\n\n✅ Correctas: {correctas}\n❌ Incorrectas: {incorrectas}\n\n💡 {consejo}"
    markup = types.InlineKeyboardMarkup()
    markup.row(types.InlineKeyboardButton("🔄 Repetir examen",callback_data=f"e:{state['materia']}:{state['tema_idx']}:{state['examen_idx']}"),
               types.InlineKeyboardButton("📚 Otros temas",callback_data=f"t:{state['materia']}"))
    markup.add(types.InlineKeyboardButton("🏠 Menú principal",callback_data="menu"))
    markup.add(types.InlineKeyboardButton("❌ Cancelar / Salir",callback_data="salir_menu"))
    bot.edit_message_text(texto,user_id,message_id,reply_markup=markup)

# ================= FLASK & WEBHOOK =================
@app.route('/')
def index():
    return "Bot funcionando ✅"

@app.route(f"/{TOKEN}",methods=["POST"])
def webhook():
    try:
        json_str = request.get_data().decode("UTF-8")
        update = telebot.types.Update.de_json(json_str)
        bot.process_new_updates([update])
        return '',200
    except Exception as e:
        print(f"❌ Error en webhook: {e}")
        return '',500

@app.route("/set_webhook")
def set_webhook():
    webhook_url = f"https://{DOMAIN}/{TOKEN}"
    bot.remove_webhook()
    bot.set_webhook(url=webhook_url)
    return f"Webhook configurado: {webhook_url}"

if __name__ == "__main__":
    port = int(os.environ.get('PORT', 5000))
    bot.remove_webhook()
    bot.set_webhook(url=f"https://{DOMAIN}/{TOKEN}") if DOMAIN else None
    app.run(host="0.0.0.0", port=port)
