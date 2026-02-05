import telebot
from telebot.types import InlineKeyboardMarkup, InlineKeyboardButton
import os
from collections import defaultdict
import time
import sys

TOKEN = os.getenv("8441666201:AAHygO1Osx5IdxnmQpQuF__Y8WyGvBKhr4U")
if not TOKEN:
    print("8441666201:AAHygO1Osx5IdxnmQpQuF__Y8WyGvBKhr4U"")
    sys.exit(1)

print(f"✅ Bot OK")
bot = telebot.TeleBot(TOKEN)

user_states = defaultdict(lambda: {'pregunta_actual': 0, 'aciertos': 0, 'fallos': 0, 'iniciado': False})

preguntas = [
    {"id": 1, "titulo": "📚 POSSESIVOS", "pregunta": "¿Qué indican los **POSESIVOS**?", "opciones": ["Distancia", "*Pertenencia*", "Cantidad"], "correcta": 1, "explicacion": "*Mi, tu, su...* = a quién pertenece.", "emoji": "👨‍👩‍👧‍👦"},
    {"id": 2, "titulo": "🎯 DEMOSTRATIVOS", "pregunta": "DEMONSTRATIVO de *lejanía*?", "opciones": ["Este", "Ese", "*Aquel*"], "correcta": 2, "explicacion": "`Aquel` = muy lejos.", "emoji": "🌠"},
    {"id": 3, "titulo": "🎭 ARTÍCULOS", "pregunta": "'Unas mesas' = ?", "opciones": ["*Indeterminado*", "Determinado", "Numeral"], "correcta": 0, "explicacion": "`Unas` no especifica cuáles.", "emoji": "🪑"},
    {"id": 4, "titulo": "🔢 NUMERALES", "pregunta": "'primero, segundo' = ?", "opciones": ["Cardinales", "*Ordinales*", "Indefinidos"], "correcta": 1, "explicacion": "Indican orden/posición.", "emoji": "🥇"},
    {"id": 5, "titulo": "❓ INDEFINIDOS", "pregunta": "Determinante **INDEFINIDO**?", "opciones": ["*Varios*", "Tres", "Los"], "correcta": 0, "explicacion": "`Varios` = cantidad imprecisa.", "emoji": "🤷"},
    {"id": 6, "titulo": "⚔️ ARTÍCULOS", "pregunta": "DETERMINADO masculino plural?", "opciones": ["Unos", "*Los*", "Estos"], "correcta": 1, "explicacion": "`Los` = específico.", "emoji": "📚"},
    {"id": 7, "titulo": "'Vuestra casa'?", "pregunta": "*'vuestra'* = ?", "opciones": ["1 poseedor", "*Varios poseedores*", "Cercanía"], "correcta": 1, "explicacion": "`Vuestra` = plural.", "emoji": "🏠"},
    {"id": 8, "titulo": "📏 DISTANCIAS", "pregunta": "'Ese estuche' = ?", "opciones": ["Cerca", "*Distancia media*", "Lejos"], "correcta": 1, "explicacion": "`Ese` = medio.", "emoji": "📦"},
    {"id": 9, "titulo": "🧮 CARDINAL", "pregunta": "Numeral **CARDINAL**?", "opciones": ["Sexto", "Muchos", "*Diez*"], "correcta": 2, "explicacion": "Cantidad exacta.", "emoji": "🔟"},
    {"id": 10, "titulo": "👑 FEMENINO", "pregunta": "DETERMINADO fem. singular?", "opciones": ["Una", "*La*", "Esa"], "correcta": 1, "explicacion": "`La` = específica.", "emoji": "🏛️"}
]

@bot.message_handler(commands=['start'])
def start(message):
    uid = message.from_user.id
    user_states[uid] = {'pregunta_actual': 0, 'aciertos': 0, 'fallos': 0, 'iniciado': True}
    bot.send_message(message.chat.id, "🎓 **EXAMEN DETERMINANTES** 🎓\n\n⚡ 10 preguntas • 1 respuesta\n🚀 ¡Comienza!")
    enviar_pregunta(uid, message.chat.id)

def enviar_pregunta(uid, chat_id):
    estado = user_states[uid]
    idx = estado['pregunta_actual']
    
    if idx
