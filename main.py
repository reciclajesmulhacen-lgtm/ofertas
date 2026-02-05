import telebot
from telebot import types
import os
import urllib.parse
import re
import time
import traceback

# =========================
# CONFIG - RAILWAY
# =========================
TOKEN = os.getenv("8441666201:AAHygO1Osx5IdxnmQpQuF__Y8WyGvBKhr4U")
if not TOKEN:
    raise ValueError("TELEGRAM_TOKEN no configurado")

bot = telebot.TeleBot(TOKEN, parse_mode='Markdown')

# =========================
# COMANDO START
# =========================
@bot.message_handler(commands=['start'])
def start(message):
    welcome_text = (
        "🚀 *Personal Shopper Bot*\n"
        "━━━━━━━━━━━━━━━━━━━━━\n\n"
        "👋 ¡Hola! Soy tu asistente de compras inteligente.\n\n"
        "✨ *¿Cómo funciono?*\n"
        "• Envía el nombre de cualquier producto\n"
        "• Te daré enlaces directos a los mejores buscadores\n"
        "• Compara precios en segundos 📊\n\n"
        "💡 *Ejemplo:* `iPhone 15 Pro`\n\n"
        "━━━━━━━━━━━━━━━━━━━━━\n"
        "🔍 ¡Envía tu primer producto!"
    )
    bot.reply_to(message, welcome_text)

# =========================
# HANDLER PRINCIPAL
# =========================
@bot.message_handler(func=lambda message: True)
def handle_product_search(message):
    try:
        query = message.text.strip()
        
        if len(query) < 2:
            bot.reply_to(message, 
                "❌ *Producto muy corto*\n\n"
                "💡 Escribe al menos 2 letras\n"
                "`Ejemplo: Samsung Galaxy`"
            )
            return

        # Limpiar query
        query_clean = re.sub(r'^/[a-zA-Z]+', '', query).strip()
        if len(query_clean) < 2:
            return

        encoded_query = urllib.parse.quote_plus(query_clean)
        
        status_msg = bot.reply_to(message, "🔍 *Buscando ofertas...* ⏳")
        time.sleep(0.5)

        # Botones de búsqueda
        markup = types.InlineKeyboardMarkup(row_width=1)
        
        markup.add(
            types.InlineKeyboardButton(
                "🌐 Google Shopping", 
                url=f"https://www.google.com/search?tbm=shop&q={encoded_query}"
            ),
            types.InlineKeyboardButton(
                "🇪🇸 Amazon España", 
                url=f"https://www.amazon.es/s?k={encoded_query}"
            )
        )
        markup.add(
            types.InlineKeyboardButton(
                "🇨🇳 AliExpress", 
                url=f"https://www.aliexpress.com/wholesale?SearchText={encoded_query}"
            ),
            types.InlineKeyboardButton(
                "🟦 Bing Shoppi
