import os
import re
import logging
from flask import Flask, request
import telebot
from telebot import types

# =========================
# CONFIG
# =========================

TOKEN = os.getenv("8441666201:AAHygO1Osx5IdxnmQpQuF__Y8WyGvBKhr4U")
if not TOKEN:
    raise RuntimeError("❌ Falta TELEGRAM_BOT_TOKEN en Railway > Variables")

PUBLIC_URL = os.getenv("RAILWAY_PUBLIC_DOMAIN")
if not PUBLIC_URL:
    raise RuntimeError("❌ Falta RAILWAY_PUBLIC_DOMAIN (Railway la pone automáticamente)")

WEBHOOK_URL = f"https://{PUBLIC_URL}/webhook"

bot = telebot.TeleBot(TOKEN, parse_mode="HTML")
app = Flask(__name__)

logging.basicConfig(level=logging.INFO)

# =========================
# UTILIDADES
# =========================

ASIN_REGEX = re.compile(r"(?:dp|gp/product|product)/([A-Z0-9]{10})")

def is_amazon_link(text: str) -> bool:
    return "amazon." in text.lower() or "amzn.to" in text.lower()

def extract_asin(text: str) -> str | None:
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
# TELEGRAM HANDLERS
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
            "📌 Ejemplo: https://www.amazon.es/dp/B08N5WRWNW"
        )
    )

@bot.message_handler(func=lambda m: m.text and is_amazon_link(m.text))
def handle_amazon(message):
    asin = extract_asin(message.text)

    if not asin:
        bot.reply_to(
            message,
            "❌ He detectado Amazon, pero no puedo extraer el ASIN.\n"
            "👉 Prueba a copiar el enlace desde el navegador."
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
# FLASK ROUTES (WEBHOOK)
# =========================

@app.route("/", methods=["GET"])
def home():
    return "OK", 200

@app.route("/webhook", methods=["POST"])
def webhook():
    update = telebot.types.Update.de_json(request.stream.read().decode("utf-8"))
    bot.process_new_updates([update])
    return "OK", 200

# =========================
# ARRANQUE + WEBHOOK SETUP
# =========================

def setup_webhook():
    bot.remove_webhook()
    bot.set_webhook(url=WEBHOOK_URL)
    logging.info(f"✅ Webhook configurado: {WEBHOOK_URL}")

setup_webhook()

if __name__ == "__main__":
    port = int(os.getenv("PORT", 8080))
    app.run(host="0.0.0.0", port=port)

    logging.info("🤖 Bot iniciado")
    bot.infinity_polling(skip_pending=True)
