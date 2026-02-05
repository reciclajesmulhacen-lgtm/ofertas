import os
import telebot
from telebot import types
import importlib
import random
from flask import Flask, request

# =========================
# CONFIG
# =========================

TOKEN = os.environ.get("8441666201:AAHygO1Osx5IdxnmQpQuF__Y8WyGvBKhr4U").strip()
PUBLIC_DOMAIN = os.environ.get("ofertas-production.up.railway.app").strip()

if not TOKEN or not PUBLIC_DOMAIN:
    raise RuntimeError("❌ Faltan variables de entorno TELEGRAM_BOT_TOKEN o RAILWAY_PUBLIC_DOMAIN")

WEBHOOK_URL = f"https://{PUBLIC_DOMAIN}/webhook"

bot = telebot.TeleBot(TOKEN, parse_mode="Markdown")
app = Flask(__name__)

# Nombres que se muestran en los botones del menú principal
MATERIAS_DISPLAY = {
    "lengua": "📚 Lengua",
    "mates": "🔢 Matemáticas",
    "ciencias": "🧪 Ciencias",
    "ingles": "🇬🇧 Inglés",
    "frances": "🇫🇷 Francés"
}

# Almacén temporal para seguir el juego de cada usuario
user_stats = {}

# Importamos estadísticas (tu archivo estadisticas.py)
from estadisticas import registrar_resultado, ver_estadisticas


# =========================
# UTILIDADES
# =========================

def safe_import_module(nombre):
    """
    Importa y recarga el módulo de materia.
    Si el archivo tiene errores, aquí saltará el fallo.
    """
    modulo = importlib.import_module(nombre)
    importlib.reload(modulo)

    if not hasattr(modulo, "TEMARIO"):
        raise RuntimeError(f"El archivo {nombre}.py no tiene TEMARIO")

    return modulo


def crear_menu_principal():
    markup = types.InlineKeyboardMarkup(row_width=2)

    for id_mat, nombre in MATERIAS_DISPLAY.items():
        markup.add(types.InlineKeyboardButton(nombre, callback_data=f"mat_{id_mat}"))

    markup.add(types.InlineKeyboardButton("📊 Mis estadísticas", callback_data="stats"))
    return markup


def enviar_menu(chat_id, texto="👋 ¡Hola! Elige una materia para empezar:"):
    bot.send_message(chat_id, texto, reply_markup=crear_menu_principal())


# =========================
# COMANDOS
# =========================

@bot.message_handler(commands=["start", "menu"])
def menu_principal(message):
    enviar_menu(message.chat.id)


@bot.message_handler(commands=["stats"])
def stats_command(message):
    texto = ver_estadisticas(message.chat.id)
    bot.send_message(message.chat.id, texto, parse_mode="Markdown")


# =========================
# BOTONES
# =========================

@bot.callback_query_handler(func=lambda call: call.data == "stats")
def stats_boton(call):
    bot.answer_callback_query(call.id)
    texto = ver_estadisticas(call.message.chat.id)
    bot.send_message(call.message.chat.id, texto, parse_mode="Markdown")


@bot.callback_query_handler(func=lambda call: call.data.startswith("mat_"))
def abrir_materia(call):
    materia_id = call.data.split("_")[1]  # lengua, mates...

    try:
        modulo = safe_import_module(materia_id)
        temario = modulo.TEMARIO

        markup = types.InlineKeyboardMarkup(row_width=1)

        # Ordena unidades: U1, U2, U3...
        for uni_id in sorted(temario.keys()):
            datos = temario[uni_id]
            markup.add(
                types.InlineKeyboardButton(
                    f"{uni_id} · {datos['titulo']}",
                    callback_data=f"uni_{materia_id}_{uni_id}"
                )
            )

        markup.add(types.InlineKeyboardButton("⬅️ Volver al menú", callback_data="back_menu"))

        bot.edit_message_text(
            f"✨ Has elegido: **{MATERIAS_DISPLAY[materia_id]}**\n\nAhora elige una unidad:",
            call.message.chat.id,
            call.message.message_id,
            reply_markup=markup
        )

    except Exception as e:
        bot.answer_callback_query(call.id, "❌ Error cargando la materia. Revisa el archivo.", show_alert=True)
        bot.send_message(call.message.chat.id, f"⚠️ Error en `{materia_id}.py`:\n\n`{e}`")


@bot.callback_query_handler(func=lambda call: call.data == "back_menu")
def volver_menu(call):
    bot.answer_callback_query(call.id)
    try:
        bot.delete_message(call.message.chat.id, call.message.message_id)
    except:
        pass
    enviar_menu(call.message.chat.id, "🏠 Menú principal:")


@bot.callback_query_handler(func=lambda call: call.data.startswith("uni_"))
def elegir_examen(call):
    _, mat, uni = call.data.split("_")

    try:
        modulo = safe_import_module(mat)
        temario = modulo.TEMARIO

        if uni not in temario:
            bot.answer_callback_query(call.id, "❌ No encuentro esa unidad.", show_alert=True)
            return

        examenes = temario[uni]["examenes"]

        markup = types.InlineKeyboardMarkup(row_width=1)

        # 3 exámenes fijos
        for i in range(1, 4):
            pool = examenes[i - 1]
            estado = "✅" if pool else "⚠️"
            markup.add(
                types.InlineKeyboardButton(
                    f"{estado} Examen Tipo {i}",
                    callback_data=f"test_{mat}_{uni}_{i}"
                )
            )

        markup.add(types.InlineKeyboardButton("⬅️ Volver a unidades", callback_data=f"mat_{mat}"))

        bot.edit_message_text(
            f"🧩 Unidad **{uni}**\n\nElige un examen:",
            call.message.chat.id,
            call.message.message_id,
            reply_markup=markup
        )

    except Exception as e:
        bot.answer_callback_query(call.id, "❌ Error cargando la unidad.", show_alert=True)
        bot.send_message(call.message.chat.id, f"⚠️ Error:\n\n`{e}`")


@bot.callback_query_handler(func=lambda call: call.data.startswith("test_"))
def iniciar_test(call):
    _, mat, uni, modelo = call.data.split("_")
    modelo = int(modelo)

    try:
        modulo = safe_import_module(mat)
        preguntas_pool = modulo.TEMARIO[uni]["examenes"][modelo - 1]

        if not preguntas_pool:
            bot.answer_callback_query(call.id, "⚠️ Ese examen está vacío. Elige otro.", show_alert=True)
            return

        # Guardamos estado del usuario
        user_stats[call.message.chat.id] = {
            "preguntas": preguntas_pool,
            "actual": 0,
            "aciertos": 0,
            "fallos": 0,
            "materia_id": mat,
            "unidad_id": uni,
            "modelo": modelo,
            "nombre_materia": MATERIAS_DISPLAY[mat]
        }

        bot.answer_callback_query(call.id)
        bot.delete_message(call.message.chat.id, call.message.message_id)

        bot.send_message(
            call.message.chat.id,
            f"📝 **Examen iniciado**\n\n📚 {MATERIAS_DISPLAY[mat]}\n🧩 Unidad {uni}\n🧪 Modelo {modelo}\n\n¡Vamos a por ello! 💪"
        )

        enviar_pregunta(call.message.chat.id)

    except Exception as e:
        bot.answer_callback_query(call.id, "❌ Error iniciando examen.", show_alert=True)
        bot.send_message(call.message.chat.id, f"⚠️ Error:\n\n`{e}`")


def enviar_pregunta(chat_id):
    datos = user_stats.get(chat_id)

    if not datos:
        return

    if datos["actual"] >= len(datos["preguntas"]):
        finalizar_examen(chat_id)
        return

    p = datos["preguntas"][datos["actual"]]

    opciones = list(p["o"])
    random.shuffle(opciones)

    markup = types.InlineKeyboardMarkup(row_width=1)

    for opcion in opciones:
        es_correcta = "si" if opcion == p["r"] else "no"
        markup.add(types.InlineKeyboardButton(opcion, callback_data=f"res_{es_correcta}"))

    # Progreso bonito
    num = datos["actual"] + 1
    total = len(datos["preguntas"])

    texto = (
        f"📖 **{datos['nombre_materia']}**\n"
        f"🧩 Unidad **{datos['unidad_id']}** · 🧪 Modelo **{datos['modelo']}**\n\n"
        f"❓ **Pregunta {num} de {total}:**\n\n"
        f"{p['p']}"
    )

    bot.send_message(chat_id, texto, reply_markup=markup)


@bot.callback_query_handler(func=lambda call: call.data.startswith("res_"))
def procesar_respuesta(call):
    chat_id = call.message.chat.id
    if chat_id not in user_stats:
        bot.answer_callback_query(call.id)
        return

    correcto = (call.data == "res_si")

    if correcto:
        user_stats[chat_id]["aciertos"] += 1
        bot.answer_callback_query(call.id, "✅ ¡Muy bien!", show_alert=False)
    else:
        user_stats[chat_id]["fallos"] += 1
        bot.answer_callback_query(call.id, "❌ Casi... ¡sigue!", show_alert=False)

    # borramos pregunta anterior
    try:
        bot.delete_message(chat_id, call.message.message_id)
    except:
        pass

    user_stats[chat_id]["actual"] += 1
    enviar_pregunta(chat_id)


def finalizar_examen(chat_id):
    res = user_stats.get(chat_id)
    if not res:
        return

    aciertos = res["aciertos"]
    fallos = res["fallos"]
    total = len(res["preguntas"])

    # Frases motivadoras
    if aciertos == total:
        frase = "🏆 ¡PERFECTO! ¡Eres una máquina!"
    elif aciertos >= total * 0.7:
        frase = "🥈 ¡MUY BIEN! ¡Vas genial!"
    else:
        frase = "💪 ¡Buen intento! Si lo repites, mejoras seguro."

    # Guardamos estadísticas
    registrar_resultado(
        chat_id=chat_id,
        materia=res["materia_id"],
        unidad=res["unidad_id"],
        modelo=res["modelo"],
        aciertos=aciertos,
        fallos=fallos,
        total=total
    )

    # Limpieza estado
    del user_stats[chat_id]

    markup = types.InlineKeyboardMarkup(row_width=1)
    markup.add(types.InlineKeyboardButton("📊 Ver mis estadísticas", callback_data="stats"))
    markup.add(types.InlineKeyboardButton("🏠 Volver al menú", callback_data="back_menu"))

    bot.send_message(
        chat_id,
        f"🏁 **¡Examen terminado!**\n\n"
        f"✅ Aciertos: **{aciertos}**\n"
        f"❌ Fallos: **{fallos}**\n"
        f"📌 Nota: **{aciertos}/{total}**\n\n"
        f"{frase}",
        reply_markup=markup
    )


# =========================
# WEBHOOK (RAILWAY)
# =========================

@app.route("/")
def home():
    return "Bot online OK", 200


@app.route("/webhook", methods=["POST"])
def webhook():
    json_str = request.get_data().decode("UTF-8")
    update = telebot.types.Update.de_json(json_str)
    bot.process_new_updates([update])
    return "OK", 200


def configurar_webhook():
    # Borra webhooks antiguos y configura el nuevo
    bot.remove_webhook()
    bot.set_webhook(url=WEBHOOK_URL)


configurar_webhook()
