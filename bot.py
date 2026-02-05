import telebot
from telebot.types import InlineKeyboardMarkup, InlineKeyboardButton
import os, time
from preguntas import BANCO_PREGUNTAS

TOKEN = os.getenv("8441666201:AAHygO1Osx5IdxnmQpQuF__Y8WyGvBKhr4U")
bot = telebot.TeleBot("8441666201:AAHygO1Osx5IdxnmQpQuF__Y8WyGvBKhr4U")
user_states = {}

@bot.message_handler(commands=['start', 'menu'])
def start(message):
    uid = str(message.from_user.id)
    user_states[uid] = {'materia': None, 'unidad': None, 'examen': None, 'pregunta': 0, 'aciertos': 0}
    
    markup = InlineKeyboardMarkup(row_width=2)
    btns = [InlineKeyboardButton(m, callback_data=f"mat_{m}") for m in BANCO_PREGUNTAS.keys()]
    markup.add(*btns)
    
    bot.send_message(message.chat.id, "🎓 *CENTRO DE ESTUDIOS 5º*\nElige materia:", reply_markup=markup, parse_mode="Markdown")

@bot.callback_query_handler(func=lambda call: call.data.startswith('mat_'))
def elegir_materia(call):
    materia = call.data.split('_')[1]
    user_states[str(call.from_user.id)]['materia'] = materia
    
    markup = InlineKeyboardMarkup(row_width=1)
    for uni_id, info in BANCO_PREGUNTAS[materia].items():
        markup.add(InlineKeyboardButton(info['titulo'], callback_data=f"uni_{uni_id}"))
    
    bot.edit_message_text(f"📚 *{materia}*\nElige unidad:", call.message.chat.id, call.message.message_id, reply_markup=markup, parse_mode="Markdown")

@bot.callback_query_handler(func=lambda call: call.data.startswith('uni_'))
def elegir_examen(call):
    unidad = call.data.split('_')[1]
    user_states[str(call.from_user.id)]['unidad'] = unidad
    
    markup = InlineKeyboardMarkup()
    markup.add(
        InlineKeyboardButton("📝 Examen A", callback_data="ex_A"),
        InlineKeyboardButton("📝 Examen B", callback_data="ex_B"),
        InlineKeyboardButton("📝 Examen C", callback_data="ex_C")
    )
    
    bot.edit_message_text("🎯 *Elige el nivel de examen:*", call.message.chat.id, call.message.message_id, reply_markup=markup, parse_mode="Markdown")

@bot.callback_query_handler(func=lambda call: call.data.startswith('ex_'))
def iniciar_examen(call):
    uid = str(call.from_user.id)
    examen_tipo = call.data.split('_')[1]
    user_states[uid]['examen'] = examen_tipo
    
    # Verificar si el examen existe en preguntas.py
    estado = user_states[uid]
    if not BANCO_PREGUNTAS[estado['materia']][estado['unidad']]['examenes'].get(examen_tipo):
        bot.answer_callback_query(call.id, "⚠️ Este examen aún no está cargado.", show_alert=True)
        return

    bot.delete_message(call.message.chat.id, call.message.message_id)
    enviar_pregunta(uid, call.message.chat.id)

def enviar_pregunta(uid, chat_id):
    estado = user_states[uid]
    preguntas = BANCO_PREGUNTAS[estado['materia']][estado['unidad']]['examenes'][estado['examen']]
    idx = estado['pregunta']
    
    if idx >= len(preguntas):
        finalizar(uid, chat_id)
        return

    p = preguntas[idx]
    markup = InlineKeyboardMarkup(row_width=1)
    for i, opcion in enumerate(p['o']):
        markup.add(InlineKeyboardButton(opcion, callback_data=f"ans_{idx}_{i}"))
    
    bot.send_message(chat_id, f"📝 *Pregunta {idx+1}/{len(preguntas)}*\n\n{p['p']}", reply_markup=markup, parse_mode="Markdown")

@bot.callback_query_handler(func=lambda call: call.data.startswith('ans_'))
def respuesta(call):
    uid = str(call.from_user.id)
    _, p_idx, r_idx = call.data.split('_')
    estado = user_states[uid]
    
    if int(p_idx) != estado['pregunta']: return
    bot.edit_message_reply_markup(call.message.chat.id, call.message.message_id, reply_markup=None)
    
    preg_list = BANCO_PREGUNTAS[estado['materia']][estado['unidad']]['examenes'][estado['examen']]
    if int(r_idx) == preg_list[int(p_idx)]['c']:
        estado['aciertos'] += 1
        bot.send_message(call.message.chat.id, "✅")
    else:
        bot.send_message(call.message.chat.id, f"❌ Era: {preg_list[int(p_idx)]['o'][preg_list[int(p_idx)]['c']]}")
    
    estado['pregunta'] += 1
    time.sleep(0.5)
    enviar_pregunta(uid, call.message.chat.id)

def finalizar(uid, chat_id):
    nota = user_states[uid]['aciertos']
    bot.send_message(chat_id, f"🏁 *¡FIN!* Nota: {nota}/10\nEscribe /start.")

bot.infinity_polling()
polling_timeout=10)
