import telebot
from telebot import types
import os
import urllib.parse
import re
import time

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
            bot.reply_to(message, "❌ *Producto muy corto*\nEscribe al menos 2 letras.")
            return

        query_clean = re.sub(r'^/[a-zA-Z]+', '', query).strip()
        encoded_query = urllib.parse.quote_plus(query_clean)
        
        status_msg = bot.reply_to(message, "🔍 *Buscando ofertas...* ⏳")
        time.sleep(0.5)

        markup = types.InlineKeyboardMarkup(row_width=1)
        
        # Botones de búsqueda
        markup.add(
            types.InlineKeyboardButton("🌐 Google Shopping", url=f"https://www.google.com{encoded_query}"),
            types.InlineKeyboardButton("🇪🇸 Amazon España", url=f"https://www.amazon.es{encoded_query}"),
            types.InlineKeyboardButton("🇨🇳 AliExpress", url=f"https://www.aliexpress.com{encoded_query}"),
            types.InlineKeyboardButton("👗 Vinted", url=f"https://www.vinted.es{encoded_query}"),
            types.InlineKeyboardButton("🛒 Wallapop", url=f"https://es.wallapop.com{encoded_query}")
        )

        final_text = (
            f"✅ *¡Ofertas encontradas!*\n"
            "━━━━━━━━━━━━━━━━━━━━━\n\n"
            f"📦 *Producto:* `{query_clean}`\n\n"
            f"🛍️ *Elige dónde comparar:*"
        )

        # AQUÍ ESTABA EL ERROR (LÍNEA 125): Ahora está cerrado correctamente
        bot.edit_message_text(
            text=final_text,
            chat_id=status_msg.chat.id,
            message_id=status_msg.message_id,
            reply_markup=markup,
            parse_mode='Markdown'
        )

    except Exception as e:
        print(f"Error: {e}")
        bot.reply_to(message, "⚠️ *Error temporal*. Inténtalo de nuevo.")

if __name__ == "__main__":
    print("🚀 Bot iniciado correctamente...")
    bot.infinity_polling(timeout=30)
