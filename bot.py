import os, json, threading as th
import telebot as tb
from telebot import types
from flask import Flask, request
from html import escape as esc

# --- Importar archivos de materias ---
import mates, lengua, ingles, frances, ciencias

# --- Configuración básica ---
lock = th.Lock()
app = Flask(__name__)
TOKEN = os.getenv("TOKEN")
DOMAIN = os.getenv("DOMAIN")
bot = tb.TeleBot(TOKEN)
user_state = {}
MATERIAS = {"mates": mates, "lengua": lengua, "ingles": ingles, "frances": frances, "ciencias": ciencias}

# --- Persistencia minimalista ---
def save_json(path, data):
    with lock, open(path, 'w+') as f:
        json.dump(data, f)

def load_json(path):
    try:
        return json.load(open(path, 'r'))
    except:
        return {}

guardar_estado_usuario = lambda uid, state: save_json(f"{uid}.json", state)
borrar_estado_usuario = lambda uid: (os.remove(f"{uid}.json") if os.path.exists(f"{uid}.json") else None)
registrar_respuesta = lambda uid, materia, correcta: None
registrar_fallo = lambda uid, materia, tema, exam, p, r_correct, r_user: None

# --- Teclados dinámicos ---
def get_kb(tipo, *a):
    kbs = {
        "pregunta": lambda opts, materia, tema, exam, idx: types.InlineKeyboardMarkup().add(
            *[types.InlineKeyboardButton(o, callback_data=f"p:{materia}:{tema}:{exam}:{idx}:{i}") for i, o in enumerate(opts)]
        ),
        "examen_fin": lambda state: (lambda mk: mk.row(
            types.InlineKeyboardButton("🔄 Repetir", callback_data=f"e:{state['materia']}:{state['tema_idx']}:{state['examen_idx']}"),
            types.InlineKeyboardButton("📚 Otros temas", callback_data=f"t:{state['materia']}")
        ).add(
            types.InlineKeyboardButton("🏠 Menú", callback_data="menu"),
            types.InlineKeyboardButton("❌ Salir", callback_data="salir_menu")
        ) or mk)(types.InlineKeyboardMarkup())
    }
    return kbs.get(tipo, lambda *_: None)(*a)

# --- Enviar pregunta ---
def enviar_pregunta(uid, msg_id):
    state = user_state.get(uid)
    if not state:
        return
    idx = state['pregunta_actual']
    preguntas = state['preguntas']
    if idx >= len(preguntas):
        finalizar_examen(uid, msg_id)
        return
    p = preguntas[idx]
    prog = "▰" * (idx + 1) + "▱" * (len(preguntas) - idx - 1)
    texto = f"❓ Pregunta {idx + 1}/{len(preguntas)}\n[{prog}]\n\n<code>{esc(p['p'])}</code>"
    bot.edit_message_text(
        texto, uid, msg_id,
        reply_markup=get_kb("pregunta", p['o'], state['materia'], state['tema_idx'], state['examen_idx'], idx)
    )

# --- Procesar respuesta ---
def procesar_respuesta(call):
    uid = call.message.chat.id
    d = call.data.split(":")
    idx, opt = int(d[4]), int(d[5])
    state = user_state.get(uid)
    if not state:
        bot.answer_callback_query(call.id, "⚠️ Sesión expirada. Usa /start", show_alert=True)
        return
    if idx != state['pregunta_actual']:
        bot.answer_callback_query(call.id, "⏭️ Ya respondiste esta pregunta")
        return
    pregunta = state['preguntas'][idx]
    r_user = pregunta['o'][opt]
    r_correct = pregunta['r']
    correcta = r_user == r_correct
    try:
        if correcta:
            state['respuestas_correctas'] += 1
            emoji = "✅"
        else:
            emoji = "❌"
            registrar_fallo(uid, state['materia'], state['tema_idx'], state['examen_idx'], pregunta['p'], r_correct, r_user)
        registrar_respuesta(uid, state['materia'], correcta)
    except:
        pass
    bot.answer_callback_query(call.id, emoji)
    state['pregunta_actual'] += 1
    guardar_estado_usuario(uid, state)
    enviar_pregunta(uid, call.message.message_id)

# --- Finalizar examen ---
def finalizar_examen(uid, msg_id):
    state = user_state.get(uid)
    if not state:
        return
    correct = state['respuestas_correctas']
    total = len(state['preguntas'])
    incorrect = total - correct
    pct = int((correct / total) * 100)
    borrar_estado_usuario(uid)
    barra = "▰" * int((correct / total) * 10) + "▱" * (10 - int((correct / total) * 10))
    if pct >= 90:
        emoji, msg, consejo = "🏆", "¡EXCELENTE!", "Dominas el tema perfectamente. ¡Sigue así!"
    elif pct >= 70:
        emoji, msg, consejo = "⭐", "¡MUY BIEN!", "Buen trabajo. Repasa los errores para mejorar aún más."
    elif pct >= 50:
        emoji, msg, consejo = "👍", "BIEN HECHO", "Practica un poco más para dominar el tema."
    else:
        emoji, msg, consejo = "📚", "SIGUE PRACTICANDO", "No te desanimes. Revisa el tema y vuelve a intentarlo."
    texto = f"{emoji} {msg}\n\n📊 Tu puntuación: {correct}/{total} ({pct}%)\n[{barra}]\n\n✅ Correctas: {correct}\n❌ Incorrectas: {incorrect}\n\n💡 {consejo}"
    bot.edit_message_text(
        texto, uid, msg_id,
        reply_markup=get_kb("examen_fin", state)
    )

# --- Flask ---
@app.route('/')
def index():
    return "Bot funcionando ✅"

@app.route(f'/{TOKEN}', methods=['POST'])
def webhook():
    try:
        update = tb.types.Update.de_json(request.get_data().decode("UTF-8"))
        bot.process_new_updates([update])
        return '', 200
    except Exception as e:
        print(f"❌ Error en webhook: {e}")
        return '', 500

@app.route('/set_webhook')
def set_webhook():
    url = f"https://{DOMAIN}/{TOKEN}"
    bot.remove_webhook()
    bot.set_webhook(url=url)
    return f"Webhook configurado: {url}"

# --- Main ---
if __name__ == '__main__':
    if not DOMAIN:
        print("⚠️ Modo desarrollo (sin webhook)")
        bot.remove_webhook()
        bot.infinity_polling()
    else:
        bot.remove_webhook()
        bot.set_webhook(url=f"https://{DOMAIN}/{TOKEN}")
        app.run(host='0.0.0.0', port=int(os.environ.get('PORT', 5000)))
