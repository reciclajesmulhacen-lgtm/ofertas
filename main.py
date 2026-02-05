import os
import re
import logging
import telebot
from telebot import types

# =========================
# CONFIGURACIÓN
# =========================

TOKEN = os.getenv("8441666201:AAHygO1Osx5IdxnmQpQuF__Y8WyGvBKhr4U")
if not TOKEN:
    raise RuntimeError("❌ No se ha definido TELEGRAM_BOT_TOKEN en variables de entorno")

bot = telebot.TeleBot(TOKEN, parse_mode="HTML")

logging.basicConfig(
    level=logging.INFO,
    format="%(asctime)s - %(levelname)s - %(message)s"
)

# =========================
# UTILIDADES
# =========================

ASIN_REGEX = re.compile(r"(?:dp|gp/product|product)/([A-Z0-9]{10})")

def is_amazon_link(text: str) -> bool:
    return "amazon." in text.lower() or "amzn.to" in text.lower()

def extract_asin(text: str) -> str | None:
    """Extrae ASIN desde enlaces largos (dp/gp/product)."""
    match = ASIN_REGEX.search(text)
    return match.group(1) if match else None

def build_keyboard(asin: str) -> types.InlineKeyboardMarkup:
    markup = types.InlineKeyboardMarkup(row_width=1)

    markup.add(
        types.InlineKeyboardButton(
            "♻️ Ver reacondicionados",
            url=f"https://www.amazon.es/dp/{asin}?condition=used"
        ),
        types.InlineKeyboardButton(
            "🇪🇺 Comparar en Amazon Europa",
            url=f"https://www.hagglezon.com/es/s/{asin}"
        ),
        types.InlineKeyboardButton(
            "🔍 Buscar en AliExpress",
            url=f"https://www.aliexpress.com/wholesale?SearchText={asin}"
        )
    )
    return markup

# =========================
# COMANDOS
# =========================

@bot.message_handler(commands=["start", "help"])
def welcome(message):
    bot.reply_to(
        message,
        (
            "👋 <b>¡Hola!</b>\n\n"
            "Envíame un <b>enlace de Amazon</b> y te mostraré opciones para ahorrar:\n"
            "• Reacondicionados\n"
            "• Comparar precios en Europa\n"
            "• Buscar alternativa en AliExpress\n\n"
            "📌 Ejemplo: https://www.amazon.es/dp/B0XXXXXXX"
        )
    )

# =========================
# MENSAJES
# =========================

@bot.message_handler(func=lambda m: m.text and is_amazon_link(m.text))
def handle_amazon(message):
    bot.send_chat_action(message.chat.id, "typing")

    asin = extract_asin(message.text)

    if not asin:
        bot.reply_to(
            message,
            "❌ He detectado Amazon, pero no puedo extraer el ASIN.\n"
            "👉 Prueba a copiar el enlace desde el navegador (no desde la app)."
        )
        return

    bot.send_message(
        message.chat.id,
        f"✅ <b>Producto detectado</b>\nASIN: <code>{asin}</code>\n\n"
        "Elige una opción 👇",
        reply_markup=build_keyboard(asin)
    )

@bot.message_handler(func=lambda m: True)
def fallback(message):
    bot.reply_to(
        message,
        "🤖 Por ahora solo entiendo enlaces de Amazon.\n"
        "Pásame uno y te ayudo 😉"
    )

# =========================
# MAIN
# =========================

if __name__ == "__main__":
    logging.info("🤖 Bot iniciado")
    bot.infinity_polling(skip_pending=True)
