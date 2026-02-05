# main.py
import os
import telebot
from flask import Flask, request

# -----------------------
# VARIABLES DE ENTORNO
# -----------------------
TOKEN = os.environ.get("8441666201:AAHygO1Osx5IdxnmQpQuF__Y8WyGvBKhr4U")
PUBLIC_URL = os.environ.get("RAILWAY_PUBLIC_DOMAIN")
PORT = int(os.environ.get("PORT", 5000))

if not TOKEN or not PUBLIC_URL:
    raise RuntimeError("❌ Faltan variables de entorno TELEGRAM_BOT_TOKEN o RAILWAY_PUBLIC_DOMAIN")

# -----------------------
# INICIALIZAR BOT
# -----------------------
bot = telebot.TeleBot(TOKEN, parse_mode="HTML")
app = Flask(__name__)

WEBHOOK_URL = f"https://{PUBLIC_URL}/webhook"

# -----------------------
# COMANDOS DE EJEMPLO
# -----------------------
@bot.message_handler(commands=["start"])
def start(message):
    bot.send_message(message.chat.id, "¡Hola! Envía un link de Amazon y te ayudaré a buscar ofertas.")

# Ejemplo: procesar links de Amazon
@bot.message_handler(func=lambda msg: "amazon." in msg.text.lower())
def handle_amazon(message):
    text = message.text
    import re
    # Extraer ASIN
    asin_match = re.search(r"/([A-Z0-9]{10})(?:[/?]|$)", text)
    if asin_match:
        asin = asin_match.group(1)
        bot.send_message(message.chat.id, f"ASIN detectado: <b>{asin}</b>\nAquí puedes buscar reacondicionados o comparar precios.")
    else:
        bot.send_message(message.chat.id, "No pude detectar un ASIN válido en tu link.")

# -----------------------
# RUTA WEBHOOK
# -----------------------
@app.route("/webhook", methods=["POST"])
def webhook():
    json_str = request.get_data().decode("utf-8")
    update = telebot.types.Update.de_json(json_str)
    bot.process_new_updates([update])
    return "", 200

# -----------------------
# START / DEPLOY
# -----------------------
if __name__ == "__main__":
    # Eliminar webhook previo (importante para redeploy)
    bot.remove_webhook()
    bot.set_webhook(url=WEBHOOK_URL)
    print(f"Bot arrancando con webhook en {WEBHOOK_URL}")
    app.run(host="0.0.0.0", port=PORT)
