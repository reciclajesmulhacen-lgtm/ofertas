import os, json, threading as th
import telebot as tb
from telebot import types
from flask import Flask, request
from html import escape as esc

# --- Importar materias ---
import mates, lengua, ingles, frances, ciencias

# --- Configuración ---
lock = th.Lock()
app = Flask(__name__)
TOKEN = os.getenv("TELEGRAM_BOT_TOKEN")
DOMAIN = os.getenv("RAILWAY_PUBLIC_DOMAIN")
if not TOKEN:
    print("❌ ERROR: No se ha definido TELEGRAM_BOT_TOKEN")
    exit(1)

bot = tb.TeleBot(TOKEN)
user_state = {}
MATERIAS = {"mates": mates, "lengua": lengua, "ingles": ingles, "frances": frances, "ciencias": ciencias}

# --- Persistencia minimalista ---
def save_json(path, data):
    with lock, open(path,"w+") as f: json.dump(data,f)
def load_json(path):
    try: return json.load(open(path,"r"))
    except: return {}
guardar_estado_usuario = lambda uid, s: save_json(f"{uid}.json", s)
borrar_estado_usuario = lambda uid: os.remove(f"{uid}.json") if os.path.exists(f"{uid}.json") else None
registrar_respuesta = lambda uid, m, correcta: None
registrar_fallo = lambda uid, m, tema, exam, p, r_correct, r_user: None

# --- Teclados ---
def get_materias_keyboard():
    mk = types.InlineKeyboardMarkup()
    for key in MATERIAS.keys():
        mk.add(types.InlineKeyboardButton(key.capitalize(), callback_data=f"m:{key}"))
    return mk

def get_temas_keyboard(materia_key):
    mk = types.InlineKeyboardMarkup()
    temario = MATERIAS[materia_key].TEMARIO
    for idx, uni_key in enumerate(temario.keys()):
        mk.add(types.InlineKeyboardButton(uni_key, callback_data=f"t:{materia_key}:{idx}"))
    mk.add(types.InlineKeyboardButton("🏠 Menú principal", callback_data="menu"))
    return mk

def get_examenes_keyboard(materia_key, tema_idx):
    mk = types.InlineKeyboardMarkup()
    temario = MATERIAS[materia_key].TEMARIO
    unidad_keys = list(temario.keys())
    examenes = temario[unidad_keys[tema_idx]].get("examenes", [])
    for ex_idx, _ in enumerate(examenes):
        mk.add(types.InlineKeyboardButton(f"Examen {ex_idx+1}", callback_data=f"e:{materia_key}:{tema_idx}:{ex_idx}"))
    mk.add(types.InlineKeyboardButton("🏠 Menú principal", callback_data="menu"))
    return mk

def get_kb(tipo, *a):
    if tipo=="pregunta":
        opts,materia,tema,exam,idx=a
        return types.InlineKeyboardMarkup().add(
            *[types.InlineKeyboardButton(o, callback_data=f"p:{materia}:{tema}:{exam}:{idx}:{i}") for i,o in enumerate(opts)]
        )
    elif tipo=="examen_fin":
        state=a[0]
        mk=types.InlineKeyboardMarkup()
        mk.row(
            types.InlineKeyboardButton("🔄 Repetir", callback_data=f"e:{state['materia']}:{state['tema_idx']}:{state['examen_idx']}"),
            types.InlineKeyboardButton("📚 Otros temas", callback_data=f"t:{state['materia']}:{state['tema_idx']}")
        ).add(
            types.InlineKeyboardButton("🏠 Menú", callback_data="menu"),
            types.InlineKeyboardButton("❌ Salir", callback_data="salir_menu")
        )
        return mk

# --- Funciones de examen ---
def cargar_examen(materia_key, tema_idx, examen_idx):
    temario = MATERIAS[materia_key].TEMARIO
    unidad_keys = list(temario.keys())
    unidad = temario[unidad_keys[tema_idx]]
    return unidad.get("examenes", [])[examen_idx]

def enviar_pregunta(uid, msg_id):
    state = user_state.get(uid)
    if not state: return
    idx = state['pregunta_actual']
    preguntas = state['preguntas']
    if idx>=len(preguntas):
        finalizar_examen(uid,msg_id)
        return
    p = preguntas[idx]
    prog = "▰"*(idx+1)+"▱"*(len(preguntas)-idx-1)
    texto = f"❓ Pregunta {idx+1}/{len(preguntas)}\n[{prog}]\n\n<code>{esc(p['p'])}</code>"
    bot.edit_message_text(texto,uid,msg_id,reply_markup=get_kb("pregunta",p['o'],state['materia'],state['tema_idx'],state['examen_idx'],idx))

def procesar_respuesta(call):
    uid = call.message.chat.id
    d = call.data.split(":")
    idx,opt=int(d[4]),int(d[5])
    state = user_state.get(uid)
    if not state:
        bot.answer_callback_query(call.id,"⚠️ Sesión expirada. Usa /start",show_alert=True)
        return
    if idx!=state['pregunta_actual']:
        bot.answer_callback_query(call.id,"⏭️ Ya respondiste esta pregunta")
        return
    pregunta = state['preguntas'][idx]
    r_user,r_correct=pregunta['o'][opt],pregunta['r']
    correcta=r_user==r_correct
    try:
        if correcta: state['respuestas_correctas']+=1; emoji="✅"
        else:
            emoji="❌"
            registrar_fallo(uid,state['materia'],state['tema_idx'],state['examen_idx'],pregunta['p'],r_correct,r_user)
        registrar_respuesta(uid,state['materia'],correcta)
    except: pass
    bot.answer_callback_query(call.id,emoji)
    state['pregunta_actual']+=1
    guardar_estado_usuario(uid,state)
    enviar_pregunta(uid,call.message.message_id)

def finalizar_examen(uid,msg_id):
    state=user_state.get(uid)
    if not state: return
    correct=len([r for r in state['preguntas'] if r['r'] in r['o']])  # solo ejemplo
    total=len(state['preguntas'])
    incorrect=total-correct
    pct=int((correct/total)*100)
    borrar_estado_usuario(uid)
    barra="▰"*int((correct/total)*10)+"▱"*(10-int((correct/total)*10))
    if pct>=90: emoji,msg,consejo="🏆","¡EXCELENTE!","Dominas el tema perfectamente. ¡Sigue así!"
    elif pct>=70: emoji,msg,consejo="⭐","¡MUY BIEN!","Buen trabajo. Repasa los errores."
    elif pct>=50: emoji,msg,consejo="👍","BIEN HECHO","Practica un poco más."
    else: emoji,msg,consejo="📚","SIGUE PRACTICANDO","No te desanimes."
    texto=f"{emoji} {msg}\n\n📊 Puntuación: {correct}/{total} ({pct}%)\n[{barra}]\n✅ Correctas: {correct}\n❌ Incorrectas: {incorrect}\n\n💡 {consejo}"
    bot.edit_message_text(texto,uid,msg_id,reply_markup=get_kb("examen_fin",state))

# --- Handlers ---
@bot.message_handler(commands=['start'])
def start(msg):
    uid=msg.chat.id
    user_state.pop(uid,None)
    bot.send_message(uid,"¡Bienvenido! Selecciona una materia:",reply_markup=get_materias_keyboard())

@bot.callback_query_handler(func=lambda call: True)
def callbacks(call):
    data = call.data
    uid = call.message.chat.id

    if data.startswith("m:"):
        materia = data.split(":")[1]
        bot.edit_message_text("Selecciona un tema:",uid,call.message.message_id,reply_markup=get_temas_keyboard(materia))
    elif data.startswith("t:"):
        _,materia,tema_idx = data.split(":")
        tema_idx=int(tema_idx)
        bot.edit_message_text("Selecciona un examen:",uid,call.message.message_id,reply_markup=get_examenes_keyboard(materia,tema_idx))
    elif data.startswith("e:"):
        _,materia,tema_idx,examen_idx = data.split(":")
        tema_idx=int(tema_idx); examen_idx=int(examen_idx)
        preguntas=cargar_examen(materia,tema_idx,examen_idx)
        state={'materia':materia,'tema_idx':tema_idx,'examen_idx':examen_idx,'pregunta_actual':0,'respuestas_correctas':0,'preguntas':preguntas}
        user_state[uid]=state
        guardar_estado_usuario(uid,state)
        enviar_pregunta(uid,call.message.message_id)
    elif data.startswith("p:"):
        procesar_respuesta(call)
    elif data in ("menu","salir_menu"):
        user_state.pop(uid,None)
        bot.edit_message_text("Menú principal. Selecciona una materia:",uid,call.message.message_id,reply_markup=get_materias_keyboard())

# --- Flask ---
@app.route('/')
def index():
    return "Bot funcionando ✅"

@app.route(f'/{TOKEN}',methods=['POST'])
def webhook():
    try:
        update=tb.types.Update.de_json(request.get_data().decode("UTF-8"))
        bot.process_new_updates([update])
        return '',200
    except Exception as e:
        print(f"❌ Error en webhook: {e}")
        return '',500

@app.route('/set_webhook')
def set_webhook():
    if not DOMAIN: return "❌ RAILWAY_PUBLIC_DOMAIN no definido"
    url=f"https://{DOMAIN}/{TOKEN}"
    bot.remove_webhook()
    bot.set_webhook(url=url)
    return f"Webhook configurado: {url}"

# --- Main ---
if __name__=='__main__':
    if not DOMAIN:
        print("⚠️ Modo desarrollo (polling)")
        bot.infinity_polling()
    else:
        bot.remove_webhook()
        bot.set_webhook(url=f"https://{DOMAIN}/{TOKEN}")
        app.run(host='0.0.0.0',port=int(os.environ.get('PORT',5000)))
