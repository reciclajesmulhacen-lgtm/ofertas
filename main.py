import os
import re
import logging
from flask import Flask, request
import telebot
from telebot import types

# =========================
# LOGGING
# =========================
logging.basicConfig(level=logging.INFO, format="%(asctime)s - %(levelname)s - %(message)s")

# =========================
# ENV
# =========================
TOKEN = os.getenv("8441666201:AAHygO1Osx5IdxnmQpQuF__Y8WyGvBKhr4U")
PUBLIC_DOMAIN = os.getenv("RAILWAY_PUBLIC_DOMAIN")
PORT = int(os.getenv("PORT", "8080"))

# Logs útiles (para Railway)
logging.info(f"PORT detectado: {PORT}")
logging.info(f"RAILWAY_PUBLIC_DOMAIN: {PUBLIC_DOMAIN}")
logging.info(f"TELEGRAM_BOT_TOKEN existe?: {'SI' if TOKEN else 'NO'}")

if not TOKEN:
    raise RuntimeError("❌ Falta TELEGRAM_BOT_TOKEN en Railway → Service → Variables")

if not PUBLIC_DOMAIN:
    raise RuntimeError(
        "❌ Falta RAILWAY_PUBLIC_DOMAIN. Activa un dominio público en Railway:\n"
        "Settings → Networking → Generate Domain"
    )

# =========================
# BOT + FLASK
# =========================
bot = telebot.TeleBot(TOKEN, parse_mode="HTML")
app = Flask(__name__)

WEBHOOK_PATH = f"/webhook/{TOKEN}"
WEBHOOK_URL = f"https://{PUBLIC_DOMAIN}{WEBHOOK_PATH}"

# =========================
# UTILIDADES
# =========================

ASIN_REGEX = re.compile(r"(?:dp|gp/product|product)/([A-Z0-9]{10})")

def is_amazon_link(text: str) -> bool:
    text = text.lower()
    return ("amazon." in text) or ("amzn.to" in text)

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
            "🇪🇺 Comparar precios en Europa",
            url=f"https://www.hagglezon.com/es/s/{asin}"
        ),
        types.InlineKeyboardButton(
            "🔍 Buscar en AliExpress",
            url=f"https://www.aliexpress.com/wholesale?SearchText={asin}"
        )
    )
    return markup

# =========================
# HANDLERS TELEGRAM
# =========================

@bot.message_handler(commands=["start", "help"])
def welcome(message):
    bot.reply_to(
        message,
        (
            "👋 <b>¡Hola!</b>\n\n"
            "Envíame un <b>enlace de Amazon</b> y te mostraré opciones para ahorrar.\n\n"
            "📌 Ejemplo:\n"
            "<code>https://www.amazon.es/dp/B08N5WRWNW</code>"
        )
    )

@bot.message_handler(func=lambda m: m.text and is_amazon_link(m.text))
def handle_amazon(message):
    bot.send_chat_action(message.chat.id, "typing")

    asin = extract_asin(message.text)

    if not asin:
        bot.reply_to(
            message,
            "❌ He detectado Amazon, pero no he podido extraer el ASIN.\n"
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
        "🤖 Solo entiendo enlaces de Amazon.\n"
        "Pásame uno y te muestro opciones 😉"
    )

# =========================
# RUTAS FLASK
# =========================

@app.get("/")
def index():
    return "OK", 200

@app.get("/health")
def health():
    return {
        "status": "ok",
        "webhook": WEBHOOK_URL,
        "domain": PUBLIC_DOMAIN
    }, 200

@app.post(WEBHOOK_PATH)
def telegram_webhook():
    json_str = request.get_data().decode("utf-8")
    update = telebot.types.Update.de_json(json_str)
    bot.process_new_updates([update])
    return "OK", 200

# =========================
# SETUP WEBHOOK
# =========================

def setup_webhook():
    bot.remove_webhook()
    ok = bot.set_webhook(url=WEBHOOK_URL)
    logging.info(f"Webhook set: {ok} -> {WEBHOOK_URL}")

setup_webhook()

# =========================
# RUN
# =========================

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=PORT)
