import telebot
from telebot import types
import re
import os

# Configuración del Token (Se recomienda usar variables de entorno)
TOKEN = os.getenv('8441666201:AAHygO1Osx5IdxnmQpQuF__Y8WyGvBKhr4U')
bot = telebot.TeleBot(TOKEN)

def extract_asin(text):
    """Extrae el ASIN de enlaces largos y cortos de Amazon."""
    # Patrón para enlaces largos (/dp/ASIN o /gp/product/ASIN) y cortos
    asin_pattern = r"(?:[/dp/]|$)([A-Z0-9]{10})(?:[/?]|/|$)"
    match = re.search(asin_pattern, text)
    return match.group(1) if match else None

@bot.message_handler(commands=['start', 'help'])
def send_welcome(message):
    bot.reply_to(message, "👋 ¡Hola! Pásame un enlace de Amazon y buscaré ahorros para ti.")

@bot.message_handler(func=lambda message: True)
def handle_message(message):
    text = message.text
    # Detección de cualquier enlace que parezca de Amazon
    if "amazon" in text or "amzn.to" in text:
        asin = extract_asin(text)
        
        if asin:
            # Crear botones profesionales
            markup = types.InlineKeyboardMarkup(row_width=1)
            btn_reacondicionado = types.InlineKeyboardButton("♻️ Ver Reacondicionados", url=f"https://www.amazon.es{asin}/?condition=used")
            btn_europa = types.InlineKeyboardButton("🇪🇺 Comparar en Amazon Europa", url=f"https://www.hagglezon.com{asin}")
            btn_aliexpress = types.InlineKeyboardButton("🔍 Buscar en AliExpress", url=f"https://www.aliexpress.com{asin}")
            
            markup.add(btn_reacondicionado, btn_europa, btn_aliexpress)
            
            bot.send_message(message.chat.id, f"✅ Producto detectado (ASIN: {asin})\nElige una opción de ahorro:", reply_markup=markup)
        else:
            # Feedback inmediato si el enlace falla
            bot.send_message(message.chat.id, "❌ He visto el enlace, pero no he podido extraer el código del producto. Prueba a compartirlo desde la web.")
    else:
        bot.reply_to(message, "Por ahora solo entiendo enlaces de Amazon. ¡Pásame uno!")

if __name__ == "__main__":
    bot.infinity_polling()
