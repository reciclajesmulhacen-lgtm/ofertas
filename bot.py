import os, json, threading as th
import telebot as tb
from telebot import types
from flask import Flask, request
from html import escape as esc

import mates, lengua, ingles, frances, ciencias

lock = th.Lock()
app = Flask(__name__)
TOKEN = os.getenv("TELEGRAM_BOT_TOKEN")
DOMAIN = os.getenv("RAILWAY_PUBLIC_DOMAIN")
if not TOKEN: print("❌ ERROR: TELEGRAM_BOT_TOKEN no definido"); exit(1)

bot = tb.TeleBot(TOKEN)
user_state = {}
MATERIAS = {"mates":mates,"lengua":lengua,"ingles":ingles,"frances":frances,"ciencias":ciencias}
EMOJIS = {"mates":"📐","lengua":"📚","ingles":"🇬🇧","frances":"🇫🇷","ciencias":"🔬"}

def save_json(path,data):
    with lock, open(path,"w+") as f: json.dump(data,f)
def load_json(path):
    try: return json.load(open(path,"r"))
    except: return {}
def guardar_estado_usuario(uid,estado):
    user_state[uid]=estado
    save_json(f"{uid}.json",estado)
def restaurar_estado_usuario(uid):
    estado=load_json(f"{uid}.json")
    if estado: user_state[uid]=estado
    return estado
def borrar_estado_usuario(uid):
    user_state.pop(uid,None)
    try: os.remove(f"{uid}.json")
    except: pass

def get_materias_keyboard():
    mk=types.InlineKeyboardMarkup()
    for key in MATERIAS.keys():
        mk.add(types.InlineKeyboardButton(f"{EMOJIS[key]} {key.capitalize()}", callback_data=f"m:{key}"))
    mk.add(types.InlineKeyboardButton("❌ Cancelar / Salir", callback_data="salir_menu"))
    return mk

def get_temas_keyboard(materia_key):
    mk=types.InlineKeyboardMarkup()
    temario=MATERIAS[materia_key].TEMARIO
    for idx,uni_key in enumerate(temario.keys()):
        mk.add(types.InlineKeyboardButton(f"📖 {uni_key}", callback_data=f"t:{materia_key}:{idx}"))
    mk.row(
        types.InlineKeyboardButton("🔙 Volver", callback_data="menu"),
        types.InlineKeyboardButton("❌ Cancelar / Salir", callback_data="salir_menu")
    )
    return mk

def get_examenes_keyboard(materia_key,tema_idx):
    mk=types.InlineKeyboardMarkup()
    temario=MATERIAS[materia_key].TEMARIO
    unidad_keys=list(temario.keys())
    examenes=temario[unidad_keys[tema_idx]].get("examenes",[])
    for ex_idx in range(len(examenes)):
        mk.add(types.InlineKeyboardButton(f"📝 Examen {ex_idx+1}", callback_data=f"e:{materia_key}:{tema_idx}:{ex_idx}"))
    mk.row(
        types.InlineKeyboardButton("🔙 Volver", callback_data=f"m:{materia_key}"),
        types.InlineKeyboardButton("❌ Cancelar / Salir", callback_data="salir_menu")
    )
    return mk

def get_pregunta_keyboard(opciones,materia,tema_idx,examen_idx,idx):
    mk=types.InlineKeyboardMarkup()
    for i,o in enumerate(opciones):
        mk.add(types.InlineKeyboardButton(f"🅾️ {o}", callback_data=f"p:{materia}:{tema_idx}:{examen_idx}:{idx}:{i}"))
    mk.row(
        types.InlineKeyboardButton("🔙 Volver", callback_data=f"e:{materia}:{tema_idx}:{examen_idx}"),
        types.InlineKeyboardButton("❌ Cancelar / Salir", callback_data="salir_menu")
    )
    return mk

def get_examen_fin_keyboard(state):
    mk=types.InlineKeyboardMarkup()
    mk.row(
        types.InlineKeyboardButton("🔄 Repetir", callback_data=f"e:{state['materia']}:{state['tema_idx']}:{state['examen_idx']}"),
        types.InlineKeyboardButton("📚 Otros temas", callback_data=f"t:{state['materia']}:{state['tema_idx']}")
    ).add(
        types.InlineKeyboardButton("🏠 Menú", callback_data="menu"),
        types.InlineKeyboardButton("❌ Cancelar / Salir", callback_data="salir_menu")
    )
    return mk

def cargar_examen(materia_key,tema_idx,examen_idx):
    temario=MATERIAS[materia_key].TEMARIO
    unidad_keys=list(temario.keys())
    unidad=temario[unidad_keys[tema_idx]]
    return unidad.get("examenes",[])[examen_idx]
def enviar_pregunta(uid,msg_id):
    state=user_state.get(uid)
    if not state: return
    idx=state['pregunta_actual']
    preguntas=state['preguntas']
    if idx>=len(preguntas):
        finalizar_examen(uid,msg_id)
        return
    p=preguntas[idx]
    barra="▰"*(idx+1)+"▱"*(len(preguntas)-idx-1)
    texto=f"<b>❓ Pregunta {idx+1}/{len(preguntas)}</b>\n───────────────\n<code>{esc(p['p'])}</code>\n[{barra}]"
    bot.edit_message_text(texto,uid,msg_id,reply_markup=get_pregunta_keyboard(p['o'],state['materia'],state['tema_idx'],state['examen_idx'],idx),parse_mode='HTML')

def procesar_respuesta(call):
    uid=call.message.chat.id
    d=call.data.split(":")
    idx,opt=int(d[4]),int(d[5])
    state=user_state.get(uid)
    if not state:
        bot.answer_callback_query(call.id,"⚠️ Sesión expirada",show_alert=True)
        return
    if idx!=state['pregunta_actual']:
        bot.answer_callback_query(call.id,"⏭️ Ya respondiste esta pregunta")
        return
    pregunta=state['preguntas'][idx]
    r_user,r_correct=pregunta['o'][opt],pregunta['r']
    correcta=r_user==r_correct
    emoji="✅ CORRECTO" if correcta else "❌ INCORRECTO"
    bot.edit_message_text(f"<b>{emoji}</b>\n\n<code>{esc(pregunta['p'])}</code>",uid,call.message.message_id,parse_mode='HTML')
    if correcta: state['respuestas_correctas']+=1
    state['pregunta_actual']+=1
    guardar_estado_usuario(uid,state)
    enviar_pregunta(uid,call.message.message_id)

def finalizar_examen(uid,msg_id):
    state=user_state.get(uid)
    if not state: return
    correct=state['respuestas_correctas']
    total=len(state['preguntas'])
    incorrect=total-correct
    pct=int((correct/total)*100)
    borrar_estado_usuario(uid)
    barra="▰"*int((correct/total)*10)+"▱"*(10-int((correct/total)*10))
    if pct>=90: emoji,msg,consejo="🏆","¡EXCELENTE!","Dominas el tema perfectamente"
    elif pct>=70: emoji,msg,consejo="⭐","¡MUY BIEN!","Buen trabajo"
    elif pct>=50: emoji,msg,consejo="👍","BIEN HECHO","Practica un poco más"
    else: emoji,msg,consejo="📚","SIGUE PRACTICANDO","No te desanimes"
    texto=f"{emoji} <b>{msg}</b>\n───────────────\n📊 Puntuación: {correct}/{total} ({pct}%)\n[{barra}]\n✅ Correctas: {correct}\n❌ Incorrectas: {incorrect}\n\n💡 {consejo}"
    bot.edit_message_text(texto,uid,msg_id,reply_markup=get_examen_fin_keyboard(state),parse_mode='HTML')

@bot.message_handler(commands=['start'])
def start(msg):
    uid=msg.chat.id
    restaurar_estado_usuario(uid)
    bot.send_message(uid,"¡Bienvenido! Selecciona una materia:",reply_markup=get_materias_keyboard())

@bot.callback_query_handler(func=lambda call: True)
def callbacks(call):
    data=call.data
    uid=call.message.chat.id
    if data.startswith("m:"):
        materia=data.split(":")[1]
        bot.edit_message_text("<b>Selecciona un tema:</b>",uid,call.message.message_id,reply_markup=get_temas_keyboard(materia),parse_mode='HTML')
    elif data.startswith("t:"):
        _,materia,tema_idx=data.split(":")
        tema_idx=int(tema_idx)
        bot.edit_message_text("<b>Selecciona un examen:</b>",uid,call.message.message_id,reply_markup=get_examenes_keyboard(materia,tema_idx),parse_mode='HTML')
    elif data.startswith("e:"):
        _,materia,tema_idx,examen_idx=data.split(":")
        tema_idx,examen_idx=int(tema_idx),int(examen_idx)
        preguntas=cargar_examen(materia,tema_idx,examen_idx)
        state={'materia':materia,'tema_idx':tema_idx,'examen_idx':examen_idx,'pregunta_actual':0,'respuestas_correctas':0,'preguntas':preguntas}
        guardar_estado_usuario(uid,state)
        enviar_pregunta(uid,call.message.message_id)
    elif data.startswith("p:"):
        procesar_respuesta(call)
    elif data in ("menu","salir_menu"):
        borrar_estado_usuario(uid)
        bot.edit_message_text("Menú principal. Selecciona una materia:",uid,call.message.message_id,reply_markup=get_materias_keyboard(),parse_mode='HTML')

@app.route('/')
def index(): return "Bot funcionando ✅"

@app.route(f'/{TOKEN}',methods=['POST'])
def webhook():
    try:
        update=tb.types.Update.de_json(request.get_data().decode("UTF-8"))
        bot.process_new_updates([update])
        return '',200
    except Exception as e:
        print(f"❌ Error webhook: {e}")
        return '',500

@app.route('/set_webhook')
def set_webhook():
    if not DOMAIN: return "❌ RAILWAY_PUBLIC_DOMAIN no definido"
    url=f"https://{DOMAIN}/{TOKEN}"
    bot.remove_webhook()
    bot.set_webhook(url=url)
    return f"Webhook configurado: {url}
