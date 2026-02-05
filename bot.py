import telebot
from telebot.types import InlineKeyboardMarkup, InlineKeyboardButton
import os, time
from preguntas import BANCO_PREGUNTAS

# Carga del TOKEN desde Railway
TOKEN = os.getenv("8441666201:AAHygO1Osx5IdxnmQpQuF__Y8WyGvBKhr4U")
bot = telebot.TeleBot("8441666201:AAHygO1Osx5IdxnmQpQuF__Y8WyGvBKhr4U")
user_states = {}

@bot.message_handler(commands=['start', 'menu'])
def send_welcome(message):
    uid = str(message.from_user.id)
    # Inicializamos el estado del alumno
    user_states[uid] = {'materia': None, 'unidad': None, 'pregunta': 0, 'aciertos': 0}
    
    markup = InlineKeyboardMarkup(row_width=2)
    # Generar botones automáticamente desde el diccionario de preguntas
    btns = [InlineKeyboardButton(m, callback_data=f"mat_{m}") for m in BANCO_PREGUNTAS.keys()]
    markup.add(*btns)
    
    texto = (
        "🚀 *¡BIENVENIDO A TU ACADEMIA VIRTUAL!* 🚀\n"
        "----------------------------------------\n"
        "Hola, soy tu tutor de 5º de Primaria.\n"
        "¿Qué asignatura quieres practicar hoy?"
    )
    bot.send_message(message.chat.id, texto, reply_markup=markup, parse_mode="Markdown")

@bot.callback_query_handler(func=lambda call: call.data.startswith('mat_'))
def select_subject(call):
    uid = str(call.from_user.id)
    materia = call.data.replace("mat_", "")
    user_states[uid]['materia'] = materia
    
    markup = InlineKeyboardMarkup(row_width=1)
    for uni_id, info in BANCO_PREGUNTAS[materia].items():
        markup.add(InlineKeyboardButton(info['titulo'], callback_data=f"uni_{uni_id}"))
    
    markup.add(InlineKeyboardButton("⬅️ Volver a Materias", callback_data="back_main"))
    
    bot.edit_message_text(f"📚 Asignatura: *{materia}*\nElige el tema del examen:", 
                         call.message.chat.id, call.message.message_id, 
                         reply_markup=markup, parse_mode="Markdown")

@bot.callback_query_handler(func=lambda call: call.data.startswith('uni_'))
def start_exam(call):
    uid = str(call.from_user.id)
    unidad = call.data.replace("uni_", "")
    user_states[uid]['unidad'] = unidad
    user_states[uid]['pregunta'] = 0
    user_states[uid]['aciertos'] = 0
    
    bot.edit_message_text("⚙️ *Generando preguntas aleatorias...*", 
                         call.message.chat.id, call.message.message_id, parse_mode="Markdown")
    time.sleep(1)
    send_question(uid, call.message.chat.id)

def send_question(uid, chat_id):
    estado = user_states[uid]
    preguntas = BANCO_PREGUNTAS[estado['materia']][estado['unidad']]['preguntas']
    idx = estado['pregunta']
    
    if idx >= len(preguntas):
        finish_exam(uid, chat_id)
        return

    p_data = preguntas[idx]
    # Barra de progreso visual para el niño
    progreso = "⭐" * (idx + 1) + "⚪" * (len(preguntas) - (idx + 1))
    
    markup = InlineKeyboardMarkup(row_width=1)
    for i, opcion in enumerate(p_data['o']):
        markup.add(InlineKeyboardButton(opcion, callback_data=f"ans_{idx}_{i}"))
    
    bot.send_message(chat_id, f"{progreso}\n\n❓ *{p_data['p']}*", 
                     reply_markup=markup, parse_mode="Markdown")

@bot.callback_query_handler(func=lambda call: call.data.startswith('ans_'))
def handle_answer(call):
    uid = str(call.from_user.id)
    if uid not in user_states: return
    
    try:
        _, p_idx, r_idx = call.data.split('_')
        estado = user_states[uid]
        
        # Bloqueo de seguridad para no repetir pregunta
        if int(p_idx) != estado['pregunta']: return
        
        bot.edit_message_reply_markup(call.message.chat.id, call.message.message_id, reply_markup=None)
        
        unidad_data = BANCO_PREGUNTAS[estado['materia']][estado['unidad']]['preguntas'][int(p_idx)]
        
        if int(r_idx) == unidad_data['c']:
            estado['aciertos'] += 1
            bot.send_message(call.message.chat.id, "✅ *¡EXCELENTE!* Estás aprendiendo mucho.")
        else:
            correcta = unidad_data['o'][unidad_data['c']]
            bot.send_message(call.message.chat.id, f"❌ *¡Ánimo!* La respuesta correcta era: *{correcta}*", parse_mode="Markdown")
        
        estado['pregunta'] += 1
        time.sleep(0.6)
        send_question(uid, call.message.chat.id)
    except Exception as e:
        print(f"Error: {e}")

def finish_exam(uid, chat_id):
    estado = user_states[uid]
    aciertos = estado['aciertos']
    total = len(BANCO_PREGUNTAS[estado['materia']][estado['unidad']]['preguntas'])
    
    # Mensaje motivador según la nota
    if aciertos == total: final_msg = "🏆 ¡ERES UN GENIO! Nota máxima."
    elif aciertos >= total/2: final_msg = "👏 ¡Muy bien! Has aprobado el examen."
    else: final_msg = "📚 ¡Tú puedes! Repasa un poco y vuelve a intentarlo."
    
    bot.send_message(chat_id, f"🏁 *¡EXAMEN FINALIZADO!*\n\n🎯 Aciertos: {aciertos}/{total}\n✨ {final_msg}\n\nUsa /menu para estudiar otra cosa.")

@bot.callback_query_handler(func=lambda call: call.data == "back_main")
def back_to_main(call):
    send_welcome(call.message)

if __name__ == "__main__":
    print("Bot Educativo 2026 en marcha...")
    bot.infinity_polling(timeout=20, long_polling_timeout=10)
