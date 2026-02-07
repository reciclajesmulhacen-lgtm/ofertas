import os, json, threading as th, telebot as tb
from telebot import types
from flask import Flask, request
from html import escape as esc
import mates, lengua, ingles, frances, ciencias

# --- Configuración ---
lock = th.Lock(); app = Flask(__name__)
TOKEN = os.getenv("TELEGRAM_BOT_TOKEN")
DOMAIN = os.getenv("RAILWAY_PUBLIC_DOMAIN")
if not TOKEN: print("❌ ERROR: TOKEN no definido"); exit(1)

bot = tb.TeleBot(TOKEN)
user_state = {}
MATERIAS = {"mates":mates,"lengua":lengua,"ingles":ingles,"frances":frances,"ciencias":ciencias}
EMOJIS = {"mates":"📐","lengua":"📚","ingles":"🇬🇧","frances":"🇫🇷","ciencias":"🔬"}

# --- Persistencia ---
def save_json(path,data):
    with lock, open(path,"w+") as f: json.dump(data,f)
def load_json(path):
    try: return json.load(open(path,"r"))
    except: return {}
def guardar_estado_usuario(uid,estado):
    user_state[uid]=estado; save_json(f"{uid}.json",estado)
def restaurar_estado_usuario(uid):
    estado=load_json(f"{uid}.json")
    if estado: user_state[uid]=estado
    return estado
def borrar_estado_usuario(uid):
    user_state.pop(uid,None)
    if os.path.exists(f"{uid}.json"): os.remove(f"{uid}.json")

# --- Teclados ---
def get_materias_keyboard():
    mk=types.InlineKeyboardMarkup()
    for k in MATERIAS.keys(): mk.add(types.InlineKeyboardButton(f"{EMOJIS[k]} {k.capitalize()}",callback_data=f"m:{k}"))
    return mk.add(types.InlineKeyboardButton("❌ Cancelar / Salir",callback_data="salir_menu"))

def get_temas_keyboard(m_key):
    mk=types.InlineKeyboardMarkup(); temario=MATERIAS[m_key].TEMARIO
    for i,k in enumerate(temario.keys()): mk.add(types.InlineKeyboardButton(f"📖 {k}",callback_data=f"t:{m_key}:{i}"))
    return mk.row(types.InlineKeyboardButton("🔙 Volver",callback_data="menu"),types.InlineKeyboardButton("❌ Salir",callback_data="salir_menu"))

def get_examenes_keyboard(m_key,t_idx):
    mk=types.InlineKeyboardMarkup(); u_keys=list(MATERIAS[m_key].TEMARIO.keys())
    exs=MATERIAS[m_key].TEMARIO[u_keys[t_idx]].get("examenes",[])
    for i in range(len(exs)): mk.add(types.InlineKeyboardButton(f"📝 Examen {i+1}",callback_data=f"e:{m_key}:{t_idx}:{i}"))
    return mk.row(types.InlineKeyboardButton("🔙 Volver",callback_data=f"m:{m_key}"),types.InlineKeyboardButton("❌ Salir",callback_data="salir_menu"))

def get_pregunta_keyboard(opts,m,t,e,idx):
    mk=types.InlineKeyboardMarkup()
    for i,o in enumerate(opts): mk.add(types.InlineKeyboardButton(f"🅾️ {o}",callback_data=f"p:{m}:{t}:{e}:{idx}:{i}"))
    return mk.row(types.InlineKeyboardButton("🔙 Volver",callback_data=f"e:{m}:{t}:{e}"),types.InlineKeyboardButton("❌ Salir",callback_data="salir_menu"))

# --- Lógica de Examen ---
def enviar_pregunta(uid,mid):
    s=user_state.get(uid)
    if not s or s['p_idx']>=len(s['preguntas']): return finalizar_examen(uid,mid)
    p=s['preguntas'][s['p_idx']]; total=len(s['preguntas']); act=s['p_idx']+1
    bar="▰"*act+"▱"*(total-act)
    txt=f"<b>❓ Pregunta {act}/{total}</b>\n───────────────\n<code>{esc(p['p'])}</code>\n[{bar}]"
    bot.edit_message_text(txt,uid,mid,reply_markup=get_pregunta_keyboard(p['o'],s['materia'],s['t_idx'],s['e_idx'],s['p_idx']),parse_mode='HTML')

def finalizar_examen(uid,mid):
    s=user_state.get(uid); c=s['respuestas_correctas']; t=len(s['preguntas']); pct=int((c/t)*100); borrar_estado_usuario(uid)
    emo,msg,con=("🏆","¡EXCELENTE!","Dominas el tema") if pct>=90 else ("⭐","¡MUY BIEN!","Buen trabajo") if pct>=70 else ("👍","BIEN","Sigue así") if pct>=50 else ("📚","REPASAR","No te rindas")
    txt=f"{emo} <b>{msg}</b>\n───────────────\n📊 Nota: {c}/{t} ({pct}%)\n<code>{'▰'*int(pct/10)+'▱'*(10-int(pct/10))}</code>\n\n💡 {con}"
    mk=types.InlineKeyboardMarkup().row(types.InlineKeyboardButton("🏠 Menú",callback_data="menu"),types.InlineKeyboardButton("❌ Salir",callback_data="salir_menu"))
    bot.edit_message_text(txt,uid,mid,reply_markup=mk,parse_mode='HTML')

# --- Handlers ---
@bot.message_handler(commands=['start'])
def start(msg):
    uid=msg.chat.id; restaurar_estado_usuario(uid)
    bot.send_message(uid,"<b>🎓 ESTUDIO 5º PRIMARIA</b>\nSelecciona materia:",reply_markup=get_materias_keyboard(),parse_mode='HTML')

@bot.callback_query_handler(func=lambda c: True)
def calls(c):
    u=c.message.chat.id; d=c.data; mid=c.message.message_id; bot.answer_callback_query(c.id)
    if d=="menu" or d=="salir_menu": borrar_estado_usuario(u); bot.edit_message_text("<b>Selecciona materia:</b>",u,mid,reply_markup=get_materias_keyboard(),parse_mode='HTML')
    elif d.startswith("m:"): 
        m=d.split(":")[1]; bot.edit_message_text(f"<b>{MATERIAS[m]['nombre'] if hasattr(MATERIAS[m],'nombre') else m.upper()}</b>\nTemas:",u,mid,reply_markup=get_temas_keyboard(m),parse_mode='HTML')
    elif d.startswith("t:"):
        _,m,ti=d.split(":"); bot.edit_message_text("<b>Selecciona Examen:</b>",u,mid,reply_markup=get_examenes_keyboard(m,int(ti)),parse_mode='HTML')
    elif d.startswith("e:"):
        _,m,ti,ei=d.split(":"); u_keys=list(MATERIAS[m].TEMARIO.keys()); pregs=MATERIAS[m].TEMARIO[u_keys[int(ti)]]["examenes"][int(ei)]
        user_state[u]={'materia':m,'t_idx':int(ti),'e_idx':int(ei),'p_idx':0,'respuestas_correctas':0,'preguntas':pregs}; guardar_estado_usuario(u,user_state[u]); enviar_pregunta(u,mid)
    elif d.startswith("p:"):
        _,m,ti,ei,pi,ri=d.split(":"); s=user_state.get(u)
        if s and int(pi)==s['p_idx']:
            cor=(s['preguntas'][int(pi)]['o'][int(ri)]==s['preguntas'][int(pi)]['r'])
            if cor: s['respuestas_correctas']+=1
            bot.edit_message_text(f"<b>{'✅ CORRECTO' if cor else '❌ INCORRECTO'}</b>\n\n<code>{esc(s['preguntas'][int(pi)]['p'])}</code>",u,mid,parse_mode='HTML')
            s['p_idx']+=1; guardar_estado_usuario(u,s); th.Timer(1.0,enviar_pregunta,[u,mid]).start()

# --- Webhook & Flask ---
@app.route('/'+TOKEN,methods=['POST'])
def webhook(): bot.process_new_updates([tb.types.Update.de_json(request.get_data().decode("utf-8"))]); return '!',200
@app.route('/set_webhook')
def set(): bot.remove_webhook(); bot.set_webhook(url=f"https://{DOMAIN}/{TOKEN}"); return "✅ Webhook listo",200
@app.route('/')
def index(): return "Bot online",200

if __name__ == '__main__':
    if not DOMAIN: bot.infinity_polling()
    else: app.run(host='0.0.0.0',port=int(os.environ.get('PORT',5000)))
