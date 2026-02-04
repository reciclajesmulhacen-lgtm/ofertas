import telebot
from telebot import types
import os
import urllib.parse

# Railway leerá el token de las Variables de Entorno por seguridad
TOKEN_TELEGRAM = os.getenv("8441666201:AAHygO1Osx5IdxnmQpQuF__Y8WyGvBKhr4U")
bot = telebot.TeleBot(TOKEN_TELEGRAM, parse_mode="Markdown")

@bot.message_handler(commands=['start'])
def send_welcome(message):
    bot.reply_to(message, "🚀 *¡RADAR 2026 EN RAILWAY ACTIVO!* 🚀\nEnvíame un nombre de producto o enlace.")

@bot.message_handler(func=lambda m: True)
def buscar(message):
    q = message.text.strip()
    q_encoded = urllib.parse.quote(q)
    
    markup = types.InlineKeyboardMarkup(row_width=2)
    markup.add(
        types.InlineKeyboardButton("🇪🇸 Amazon ES", url=f"https://www.amazon.es{q_encoded}"),
        types.InlineKeyboardButton("🇨🇳 AliExpress", url=f"https://www.aliexpress.com{q_encoded}"),
        types.InlineKeyboardButton("👗 Vinted", url=f"https://www.vinted.es{q_encoded}"),
        types.InlineKeyboardButton("🌎 eBay", url=f"https://www.ebay.com{q_encoded}")
    )
    
    bot.send_message(message.chat.id, f"🔍 Resultados globales para: `{q.upper()}`", reply_markup=markup)

if __name__ == "__main__":
    bot.infinity_polling()
