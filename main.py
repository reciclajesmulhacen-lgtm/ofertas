import telebot
from telebot import types
import os
import urllib.parse
import re
import time
import traceback

# =========================
# CONFIG - RAILWAY (ROBUSTO)
# =========================
try:
    TOKEN = os.getenv("8441666201:AAHygO1Osx5IdxnmQpQuF__Y8WyGvBKhr4U")
    if not TOKEN:
        print("❌ TELEGRAM_TOKEN no encontrado")
        exit(1)
    
    bot = telebot.TeleBot(TOKEN)
    print("✅ Bot creado correctamente")
except Exception as e:
    print(f"❌ Error config: {e}")
    exit(1)

# =========================
# COMANDO START
# =========================
@bot.message_handler(commands=['start'])
def start(message):
    welcome_text = (
        "🚀 *Personal Shopper Bot*\n"
        "━━━━━━━━━━━━━━━━━━━━━\n\n"
        "👋 ¡Hola! Soy tu asistente de compras.\n\n"
        "✨ *Funciona así:*\n"
        "• Escribe nombre del producto\n"
        "• Te doy enlaces directos\n\n"
        "💡 *Ejemplo:* `iPhone 15`\n\n"
        "━━━━━━━━━━━━━━━━━━━━━\n"
        "🔍 ¡Prueba ya!"
    )
    try:
        bot.reply_to(message, welcome_text, parse_mode='Markdown')
    except:
        bot.reply_to(message, "🚀 Personal Shopper Bot\nPrueba escribiendo un producto")

# =========================
# HANDLER PRINCIPAL
# =========================
@bot.message_handler(func=lambda m: True)
def handle_product(message):
    try:
        query = message.text.strip()
        if len(query) < 2 or query.startswith('/'):
            return

        query_clean = re.sub(r'^/[a-z]+', '', query).strip()
        if len(query_clean) < 2:
            return

        encoded = urllib.parse.quote_plus(query_clean)
        
        status = bot.reply_to(message, "🔍 Buscando...")
        time.sleep(0.3)

        markup = types.InlineKeyboardMarkup(row_width=1)
        markup.add(
            types.InlineKeyboardButton("🌐 Google Shopping", 
                url=f"https://www.google.com/search?tbm=shop&q={encoded}"),
            types.InlineKeyboardButton("🇪🇸 Amazon ES", 
                url=f"https://www.amazon.es/s?k={encoded}")
        )
        markup.add(
            types.InlineKeyboardButton("🇨🇳 AliExpress", 
                url=f"https://www.aliexpress.com/wholesale?SearchText={encoded}"),
            types.InlineKeyboardButton("🛒 Wallapop", 
                url=f"https://es.wallapop.com/search?keywords={encoded}")
        )

        text = f"✅ *{query_clean}*\n🛍️ Elige dónde buscar:"
        bot.edit_message_text(text, status.chat.id, status.message_id, 
                            reply_markup=markup, parse_mode='Markdown')

    except Exception as e:
        print(f"Handler error: {e}")

# =========================
# RAILWAY 24/7
# =========================
if __name__ == "__main__":
    print("🚀 Iniciando bot...")
    
    while True:
        try:
            print("🔄 Polling...")
            bot.infinity_polling(timeout=30, long_polling_timeout=20)
        except Exception as e:
            print(f"❌ Crash: {e}")
            print("⏳ Reinicio en 5s...")
            time.sleep(5)
