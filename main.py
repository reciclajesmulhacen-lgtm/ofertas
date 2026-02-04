import telebot
from telebot import types
import os
import urllib.parse
import traceback
import re

# =========================
# CONFIG - RAILWAY
# =========================
TOKEN = os.getenv("8441666201:AAHygO1Osx5IdxnmQpQuF__Y8WyGvBKhr4U")
if not TOKEN:
    raise ValueError("TELEGRAM_TOKEN no configurado en variables de entorno")

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
        "💡 *Ejemplo:* `iPhone 15 Pro` o `Auriculares Sony`\n\n"
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
                "💡 Escribe al menos 2 palabras\n"
                "`Ejemplo: Samsung Galaxy S24`"
            )
            return

        # Limpiar query (quitar comandos y emojis)
        query_clean = re.sub(r'^/[a-zA-Z]+|[\U0001F600-\U0001F64F]', '', query).strip()
        
        if len(query_clean) < 2:
            bot.reply_to(message, 
                "❌ *No encuentro producto válido*\n\n"
                "💡 Escribe el nombre del producto"
            )
            return

        # Encoding para URLs
        encoded_query = urllib.parse.quote_plus(query_clean)
        
        # Status message
        status_msg = bot.reply_to(message, "🔍 *Buscando ofertas...* ⏳")
        import time
        time.sleep(0.8)

        # Crear botones modernos
        markup = types.InlineKeyboardMarkup(row_width=1)
        
        # Buscadores principales
        google = types.InlineKeyboardButton(
            "🌐 *Google Shopping*", 
            url=f"https://www.google.com/search?tbm=shop&q={encoded_query}"
        )
        duckduckgo = types.InlineKeyboardButton(
            "🔍 *DuckDuckGo*", 
            url=f"https://duckduckgo.com/?q={encoded_query}&t=h_&iax=shopping&ia=shopping"
        )
        bing = types.InlineKeyboardButton(
            "🟦 *Bing Shopping*", 
            url=f"https://www.bing.com/shop?q={encoded_query}"
        )
        
        # Comparadores de precios
        amazon_es = types.InlineKeyboardButton(
            "🇪🇸 *Amazon España*", 
            url=f"https://www.amazon.es/s?k={encoded_query}"
        )
        amazon = types.InlineKeyboardButton(
            "🌍 *Amazon Global*", 
            url=f"https://www.amazon.com/s?k={encoded_query}"
        )
        aliexpress = types.InlineKeyboardButton(
            "🇨🇳 *AliExpress*", 
            url=f"https://www.aliexpress.com/wholesale?SearchText={encoded_query}"
        )
        
        # Segunda mano
        wallapop = types.InlineKeyboardButton(
            "🛒 *Wallapop*", 
            url=f"https://es.wallapop.com/search?keywords={encoded_query}"
        )
        vinted = types.InlineKeyboardButton(
            "👗 *Vinted*", 
            url=f"https://www.vinted.es/catalog?search_text={encoded_query}"
        )

        # Añadir a markup
        markup.add(google, duckduckgo, bing)
        markup.add(amazon_es, amazon, aliexpress)
        markup.add(wallapop, vinted)

        # Mensaje final moderno
        final_text = (
            f"✅ *¡{len(query_clean.split())} ofertas encontradas!*\n"
            "━━━━━━━━━━━━━━━━━━━━━\n\n"
            f"📦 *Producto:* `{query_clean}`\n\n"
            f"🛍️ *Elige dónde buscar el mejor precio:*\n\n"
            "━━━━━━━━━━━━━━━━━━━━━"
        )

        bot.edit_message_text(
            final_text,
            
