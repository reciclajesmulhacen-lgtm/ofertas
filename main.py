import telebot
from telebot.types import InlineKeyboardMarkup, InlineKeyboardButton
import os
from collections import defaultdict
import time

TOKEN = os.getenv("8441666201:AAHygO1Osx5IdxnmQpQuF__Y8WyGvBKhr4U")
bot = telebot.TeleBot(TOKEN, parse_mode='Markdown')

user_states = defaultdict(lambda: {
    'pregunta_actual': 0, 'aciertos': 0, 'fallos': 0, 'iniciado': False
})

preguntas = [
    {"id": 1, "titulo": "📚 DETERMINANTES POSESIVOS", "pregunta": "¿Qué indican los **determinantes POSSESIVOS**?", "opciones": ["📏 Distancia", "👤 *Pertenencia*", "🔢 Cantidad"], "correcta": 1, "explicacion": "*Mi, tu, su, nuestro...* indican **a quién pertenece** algo.", "emoji": "👨‍👩‍👧‍👦"},
    {"id": 2, "titulo": "🎯 DEMOSTRATIVOS", "pregunta": "¿Cuál es un **DEMONSTRATIVO** de *lejanía*?", "opciones": ["📱 *Este* (cerca)", "📦 Ese (medio)", "🌌 *Aquel* (lejos)"], "correcta": 2, "explicacion": "`Aquel` = **muy lejos**. Ej: *Aquel monte* (allá lejos).", "emoji": "🌠"},
    {"id": 3, "titulo": "🎭 ARTÍCULOS", "pregunta": "En **'Unas mesas'**, ¿qué tipo de artículo es *'Unas'*?", "opciones": ["*Indeterminado*", "Determinado", "Numeral"], "correcta": 0, "explicacion": "`Unas` **no especifica** cuáles mesas. Es *indeterminado*.", "emoji": "🪑"},
    {"id": 4, "titulo": "🔢 NUMERALES", "pregunta": "Los numerales **'primero, segundo, tercero'** son...", "opciones": ["Cardinales", "*Ordinales*", "Indefinidos"], "correcta": 1, "explicacion": "Indican **posición/orden**: *primer puesto, segundo lugar*.", "emoji": "🥇🥈🥉"},
    {"id": 5, "titulo": "❓ INDEFINIDOS", "pregunta": "¿Cuál es un **determinante INDEFINIDO**?", "opciones": ["*Varios*", "Tres", "Los"], "correcta": 0, "explicacion": "`Varios` = **cantidad imprecisa**. Otros: *algunos, pocos*.", "emoji": "🤷"},
    {"id": 6, "titulo": "⚔️ ARTÍCULOS DETERMINADOS", "pregunta": "¿Cuál es artículo **DETERMINADO** masculino plural?", "opciones": ["Unos", "*Los*", "Estos"], "correcta": 1, "explicacion": "`Los` = **específico**. Ej: *Los libros de la mesa*.", "emoji": "📚"},
    {"id": 7, "titulo": "👥 POSESIVOS PLURAL", "pregunta": "En **'Vuestra casa'**, *'vuestra'* es posesivo de...", "opciones": ["Un poseedor", "*Varios poseedores*", "Cercanía"], "correcta": 1, "explicacion": "`Vuestra` = **ustedes/vosotros**. Plural de poseedores.", "emoji": "🏠"},
    {"id": 8, "titulo": "📏 DISTANCIAS", "pregunta": "**'Ese estuche'**. ¿Qué distancia indica *'Ese'*?", "opciones": ["Cercanía", "*Distancia media*", "Lejanía"], "correcta": 1, "explicacion": "`Este`=cerca, `Ese`=medio, `Aquel`=lejos. **Ese=medio**.", "emoji": "📦"},
    {"id": 9, "titulo": "🧮 CARDINALES vs ORDINALES", "pregunta": "¿Cuál es **numeral CARDINAL**?", "opciones": ["Sexto", "Muchos", "*Diez*"], "correcta": 2, "explicacion": "Cardinal = **cantidad exacta**: *Diez libros*. No orden.", "emoji": "🔟"},
    {"id": 10, "titulo": "👑 ARTÍCULO FEMENINO", "pregunta": "¿Cuál es artículo **DETERMINADO** femenino singular?", "opciones": ["Una", "*La*", "Esa"], "correcta": 1, "explicacion": "`La` = **específica**. Ej: *La casa blanca*.", "emoji": "🏛️"}
]

@bot.message_handler(commands=['start'])
def start(message):
    uid = message.from_user.id
    user_states[uid] = {'pregunta_actual': 0, 'aciertos': 0, 'fallos': 0, 'iniciado': True}
    
    bienvenida = "🎓 **EXAMEN LENGUA - DETERMINANTES** 🎓\n\n⚡ **REGLAS:**\n• 10 preguntas tipo test\n• **1 sola respuesta** por pregunta\n• Explicación detallada inmediata\n• Progreso guardado automáticamente\n\n🚀 **¡Prepárate!** 👇"
    bot.send_message(message.chat.id, bienvenida)
    enviar_pregunta(uid, message.chat.id)

def enviar_pregunta(uid, chat_id):
    estado = user_states[uid]
    idx = estado['pregunta_actual']
    
    if idx >= len(preguntas):
        finalizar_examen(uid, chat_id)
        return
    
    p = preguntas[idx]
    progreso = f"**Pregunta {p['id']}/10** • **{estado['aciertos']}/{idx} aciertos**"
    
    markup = InlineKeyboardMarkup(row_width=1)
    for i, opcion in enumerate(p['opciones']):
        markup.add(InlineKeyboardButton(opcion, callback_data=f"resp_{idx}_{i}"))
    
    mensaje = f"{p['emoji']} **{p['titulo']}**\n\n{progreso}\n\n📝 {p['pregunta']}\n\n⏰ *Elige tu respuesta* 👇"
    bot.send_message(chat_id, mensaje, reply_markup=markup)

@bot.callback_query_handler(func=lambda call: call.data.startswith('resp_'))
def manejar_respuesta(call):
    uid = call.from_user.id
    chat_id = call.message.chat.id
    
    if uid not in user_states or not user_states[uid]['iniciado']:
        bot.answer_callback_query(call.id, "🔄 Usa /start para comenzar")
        return
    
    _, idx_pregunta, idx_respuesta = call.data.split('_')
    idx_pregunta = int(idx_pregunta)
    idx_respuesta = int(idx_respuesta)
    
    estado = user_states[uid]
    
    if idx_pregunta != estado['pregunta_actual']:
        bot.answer_callback_query(call.id, "✅ Ya respondiste esta pregunta")
        return
    
    bot.edit_message_reply_markup(chat_id, call.message.message_id, reply_markup=None)
    
    p = preguntas[idx_pregunta]
    correcta = p['correcta']
    
    if idx_respuesta == correcta:
        estado['aciertos'] += 1
        feedback = f"🎉 **¡CORRECTO!** 🎉\n\n{p['explicacion']}"
        bot.answer_callback_query(call.id, "¡Perfecto! ✅")
    else:
        estado['fallos'] += 1
        feedback = f"❌ **Incorrecto.**\n\n💡 *Respuesta correcta:*\n{p['opciones'][correcta]}\n\n{p['explicacion']}"
        bot.answer_callback_query(call.id, "¡Repasa la explicación! 📚")
    
    bot.send_message(chat_id, feedback)
    
    time.sleep(1.5)
    estado['pregunta_actual'] += 1
    enviar_pregunta(uid, chat_id)

def finalizar_examen(uid, chat_id):
    estado = user_states[uid]
    nota = estado['aciertos']
    
    if nota == 10:
        resultado = "🏆 **¡PERFECCIÓN ABSOLUTA!** 🏆\n*¡Eres un experto en determinantes!*"
    elif nota >= 8:
        resultado = "⭐ **¡EXCELENTE!** ⭐\n*¡Dominas los determinantes!*"
    elif nota >= 6:
        resultado = "📈 **¡APROBADO!** 📈\n*¡Buen trabajo, sigue así!*"
    elif nota >= 4:
        resultado = "⚠️ **RECUPERABLE** ⚠️\n*Repasa los conceptos clave.*"
    else:
        resultado = "📚 **A REPASAR** 📚\n*¡Vuelve a estudiar los determinantes!*"
    
    mensaje_final = f"**RESULTADO FINAL**\n\n✅ **Aciertos:** {estado['aciertos']}/10\n❌ **Fallos:** {estado['fallos']}/10\n📊 **Nota:** {nota}/10\n\n{resultado}\n\n🔄 `/start` para **nuevo examen**"
    bot.send_message(chat_id, mensaje_final)
    del user_states[uid]

if __name__ == '__main__':
    print("🤖 Bot examen iniciado...")
    bot.infinity_polling(none_stop=True)
