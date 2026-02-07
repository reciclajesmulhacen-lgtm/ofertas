import os, json, threading
from flask import Flask, request
import telebot
from telebot import types
from datetime import datetime
from mates import TEMARIO as MATES
from lengua import TEMARIO as LENGUA
from ingles import TEMARIO as INGLES
from frances import TEMARIO as FRANCES
from ciencias import TEMARIO as CIENCIAS

TOKEN=os.environ.get('TELEGRAM_BOT_TOKEN')
DOMAIN=os.environ.get('RAILWAY_PUBLIC_DOMAIN')
bot=telebot.TeleBot(TOKEN,parse_mode='HTML')
app=Flask(__name__)
user_state={}
lock=threading.Lock()
PROGRESO_FILE="progreso.json"

def escape_html(text): return "" if text is None else str(text).replace("&","&amp;").replace("<","&lt;").replace(">","&gt;")
def load_progreso(): 
    if not os.path.exists(PROGRESO_FILE): return {}
    try: 
        with lock, open(PROGRESO_FILE,"r",encoding="utf-8") as f: return json.load(f)
    except: return {}
def save_progreso(data): 
    try: 
        with lock, open(PROGRESO_FILE,"w",encoding="utf-8") as f: json.dump(data,f,ensure_ascii=False,indent=2)
    except Exception as e: print(f"❌ Error guardando progreso: {e}")
def ensure_user_structure(data,user_id):
    uid=str(user_id)
    if uid not in data: data[uid]={}
    data[uid].setdefault('estado',None)
    data[uid].setdefault('fallos',[])
    if 'stats' not in data[uid]: data[uid]['stats']={k:{'intentos':0,'preguntas_respondidas':0,'aciertos':0,'fallos':0} for k in MATERIAS.keys()}

def guardar_estado_usuario(user_id,estado):
    d=load_progreso(); ensure_user_structure(d,user_id); d[str(user_id)]['estado']=estado; save_progreso(d)
def borrar_estado_usuario(user_id):
    d=load_progreso(); ensure_user_structure(d,user_id); d[str(user_id)]['estado']=None; save_progreso(d)
def get_estado_guardado(user_id):
    d=load_progreso(); ensure_user_structure(d,user_id); return d.get(str(user_id),{}).get('estado')

def registrar_respuesta(user_id,materia,correcta):
    d=load_progreso(); ensure_user_structure(d,user_id)
    s=d[str(user_id)]['stats'].get(materia)
    if not s: d[str(user_id)]['stats'][materia]={'intentos':0,'preguntas_respondidas':0,'aciertos':0,'fallos':0}; s=d[str(user_id)]['stats'][materia]
    s['preguntas_respondidas']+=1; s['aciertos']+=1 if correcta else 0; s['fallos']+=0 if correcta else 1; save_progreso(d)
def registrar_intento_examen(user_id,materia):
    d=load_progreso(); ensure_user_structure(d,user_id)
    s=d[str(user_id)]['stats'].get(materia)
    if not s: d[str(user_id)]['stats'][materia]={'intentos':0,'preguntas_respondidas':0,'aciertos':0,'fallos':0}; s=d[str(user_id)]['stats'][materia]
    s['intentos']+=1; save_progreso(d)
def registrar_fallo(user_id,materia,tema_idx,examen_idx,p,correcta,elegida):
    d=load_progreso(); ensure_user_structure(d,user_id)
    f={'fecha':datetime.utcnow().isoformat()+"Z",'materia':materia,'tema_idx':tema_idx,'examen_idx':examen_idx,'pregunta':str(p),'respuesta_correcta':str(correcta),'respuesta_elegida':str(elegida)}
    d[str(user_id)]['fallos'].append(f)
    if len(d[str(user_id)]['fallos'])>200: d[str(user_id)]['fallos']=d[str(user_id)]['fallos'][-200:]
    save_progreso(d)

MATERIAS={'mates':{'nombre':'📐 Matemáticas','temario':MATES},'lengua':{'nombre':'📚 Lengua','temario':LENGUA},'ingles':{'nombre':'🇬🇧 Inglés','temario':INGLES},'frances':{'nombre':'🇫🇷 Francés','temario':FRANCES},'ciencias':{'nombre':'🔬 Ciencias','temario':CIENCIAS}}

def get_materias_keyboard():
    k=types.InlineKeyboardMarkup(row_width=2)
    k.add(*[types.InlineKeyboardButton(v['nombre'],callback_data=f"m:{i}") for i,v in enumerate(MATERIAS.values())],types.InlineKeyboardButton('❌ Cancelar / Salir',callback_data='salir_menu'))
    return k
def get_temas_keyboard(materia): k=types.InlineKeyboardMarkup(row_width=1); k.add(*[types.InlineKeyboardButton(f"{u}: {d['titulo']}",callback_data=f"t:{materia}:{i}") for i,(u,d) in enumerate(MATERIAS[materia]['temario'].items())],types.InlineKeyboardButton('🔙 Volver',callback_data='menu'),types.InlineKeyboardButton('❌ Cancelar / Salir',callback_data='salir_menu')); return k
def get_examenes_keyboard(materia,tema_idx): k=types.InlineKeyboardMarkup(row_width=3); k.add(*[types.InlineKeyboardButton(f"📝 Examen {i+1}",callback_data=f"e:{materia}:{tema_idx}:{i}") for i in range(3)],types.InlineKeyboardButton('🔙 Volver',callback_data=f"t:{materia}"),types.InlineKeyboardButton('❌ Cancelar / Salir',callback_data='salir_menu')); return k
def get_pregunta_keyboard(respuestas,materia,tema_idx,examen_idx,preg_idx): k=types.InlineKeyboardMarkup(row_width=1); k.add(*[types.InlineKeyboardButton(op,callback_data=f"r:{materia}:{tema_idx}:{examen_idx}:{preg_idx}:{i}") for i,op in enumerate(respuestas)],types.InlineKeyboardButton('❌ Cancelar / Salir',callback_data='salir_menu')); return k
def get_reanudar_keyboard(): k=types.InlineKeyboardMarkup(row_width=1); k.add(types.InlineKeyboardButton('▶️ Continuar examen',callback_data='reanudar'),types.InlineKeyboardButton('🆕 Empezar de cero',callback_data='reiniciar'),types.InlineKeyboardButton('❌ Cancelar / Salir',callback_data='salir_menu')); return k

@bot.message_handler(commands=['start'])
def start(message):
    uid=message.chat.id
    e=get_estado_guardado(uid)
    if e: bot.send_message(uid,"📌 He encontrado un examen a medias.\n\n¿Qué quieres hacer?",reply_markup=get_reanudar_keyboard()); return
    user_state[uid]={}
    bot.send_message(uid,"¡Hola! 👋\n\nSoy tu asistente de estudios para 5º de primaria.\n\n📚 Elige una materia para comenzar:",reply_markup=get_materias_keyboard())

@bot.callback_query_handler(func=lambda c: True)
def callbacks(call):
    uid=call.message.chat.id
    d=call.data
    bot.answer_callback_query(call.id)
    if d.startswith("m:"):
        i=int(d.split(":")[1]); m=list(MATERIAS.keys())[i]; user_state[uid]={'materia':m}; bot.edit_message_text(f"{MATERIAS[m]['nombre']}\n\n📖 Selecciona un tema:",uid,call.message.message_id,reply_markup=get_temas_keyboard(m))
    elif d.startswith("t:"):
        p=d.split(":"); m=p[1]
        if len(p)==2: bot.edit_message_text(f"{MATERIAS[m]['nombre']}\n\n📖 Selecciona un tema:",uid,call.message.message_id,reply_markup=get_temas_keyboard(m))
        else:
            t=int(p[2]); tem=MATERIAS[m]['temario']; key=list(tem.keys())[t]; user_state[uid].update({'tema_idx':t}); bot.edit_message_text(f"📚 {tem[key]['titulo']}\n\nElige un examen:",uid,call.message.message_id,reply_markup=get_examenes_keyboard(m,t))
    elif d.startswith("e:"):
        p=d.split(":"); m=p[1]; t=int(p[2]); e_idx=int(p[3]); tem=MATERIAS[m]['temario']; key=list(tem.keys())[t]; preguntas=tem[key]['examenes'][e_idx]
        user_state[uid].update({'materia':m,'tema_idx':t,'examen_idx':e_idx,'preguntas':preguntas,'pregunta_actual':0,'respuestas_correctas':0})
        registrar_intento_examen(uid,m)
        guardar_estado_usuario(uid,{'materia':m,'materia_idx':list(MATERIAS.keys()).index(m),'tema_idx':t,'examen_idx':e_idx,'pregunta_actual':0,'respuestas_correctas':0})
        enviar_pregunta(uid,call.message.message_id)
def enviar_pregunta(user_id,message_id):
    state=user_state[user_id]; idx=state['pregunta_actual']; preguntas=state['preguntas']
    if idx>=len(preguntas): finalizar_examen(user_id,message_id); return
    p=preguntas[idx]; total=len(preguntas); prog="▰"*(idx+1)+"▱"*(total-idx-1)
    texto=f"❓ Pregunta {idx+1}/{total}\n[{prog}]\n\n<code>{escape_html(p['p'])}</code>"
    bot.edit_message_text(texto,user_id,message_id,reply_markup=get_pregunta_keyboard(p['o'],state['materia'],state['tema_idx'],state['examen_idx'],idx))

def procesar_respuesta(call):
    uid=call.message.chat.id; p=call.data.split(":"); idx=int(p[4]); opt=int(p[5])
    state=user_state.get(uid)
    if not state: bot.answer_callback_query(call.id,"⚠️ Sesión expirada. Usa /start",show_alert=True); return
    if idx!=state['pregunta_actual']: bot.answer_callback_query(call.id,"⏭️ Ya respondiste esta pregunta"); return
    pregunta=state['preguntas'][idx]; r_user=pregunta['o'][opt]; r_correct=pregunta['r']; correcta=(r_user==r_correct)
    if correcta: state['respuestas_correctas']+=1; emoji="✅"; texto_fb="¡Correcto! 👏"
    else: emoji="❌"; texto_fb=f"Incorrecto. 💡 La respuesta correcta era:\n<code>{escape_html(r_correct)}</code>"; registrar_fallo(uid,state['materia'],state['tema_idx'],state['examen_idx'],pregunta['p'],r_correct,r_user)
    registrar_respuesta(uid,state['materia'],correcta)
    bot.answer_callback_query(call.id,f"{emoji}",show_alert=False)
    state['pregunta_actual']+=1
    guardar_estado_usuario(uid,{'materia':state['materia'],'materia_idx':list(MATERIAS.keys()).index(state['materia']),'tema_idx':state['tema_idx'],'examen_idx':state['examen_idx'],'pregunta_actual':state['pregunta_actual'],'respuestas_correctas':state['respuestas_correctas']})
    enviar_pregunta(uid,call.message.message_id)

def finalizar_examen(user_id,message_id):
    state=user_state[user_id]; correct=state['respuestas_correctas']; total=len(state['preguntas']); incorrect=total-correct; pct=(correct/total)*100; borrar_estado_usuario(user_id)
    barras=int((correct/total)*10); barra="▰"*barras+"▱"*(10-barras)
    if pct>=90: emoji="🏆"; msg="¡EXCELENTE!"; consejo="Dominas el tema perfectamente. ¡Sigue así!"
    elif pct>=70: emoji="⭐"; msg="¡MUY BIEN!"; consejo="Buen trabajo. Repasa los errores para mejorar aún más."
    elif pct>=50: emoji="👍"; msg="BIEN HECHO"; consejo="Practica un poco más para dominar el tema."
    else: emoji="📚"; msg="SIGUE PRACTICANDO"; consejo="No te desanimes. Revisa el tema y vuelve a intentarlo."
    texto=f"{emoji} {msg}\n\n📊 Tu puntuación: {correct}/{total} ({pct:.0f}%)\n[{barra}]\n\n✅ Correctas: {correct}\n❌ Incorrectas: {incorrect}\n\n💡 {consejo}"
    mk=types.InlineKeyboardMarkup()
    mk.row(types.InlineKeyboardButton("🔄 Repetir examen",callback_data=f"e:{state['materia']}:{state['tema_idx']}:{state['examen_idx']}"),types.InlineKeyboardButton("📚 Otros temas",callback_data=f"t:{state['materia']}"))
    mk.add(types.InlineKeyboardButton("🏠 Menú principal",callback_data="menu"),types.InlineKeyboardButton("❌ Cancelar / Salir",callback_data="salir_menu"))
    bot.edit_message_text(texto,user_id,message_id,reply_markup=mk)

@app.route('/')
def index(): return "Bot funcionando ✅"

@app.route(f"/{TOKEN}",methods=["POST"])
def webhook():
    try:
        update=telebot.types.Update.de_json(request.get_data().decode("UTF-8"))
        bot.process_new_updates([update])
        return '',200
    except Exception as e: print(f"❌ Error en webhook: {e}"); return '',500

@app.route("/set_webhook")
def set_webhook():
    url=f"https://{DOMAIN}/{TOKEN}"; bot.remove_webhook(); bot.set_webhook(url=url); return f"Webhook configurado: {url}"

if __name__=="__main__":
    if not DOMAIN: print("⚠️ Modo desarrollo (sin webhook)"); bot.remove_webhook(); bot.infinity_polling()
    else: bot.remove_webhook(); bot.set_webhook(url=f"https://{DOMAIN}/{TOKEN}"); app.run(host="0.0.0.0",port=int(os.environ.get("PORT",5000)))
