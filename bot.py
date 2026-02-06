import os
import importlib.util
import sys
import random
import sqlite3
import json
from flask import Flask, request
import telebot
from telebot import types

# ===============================
# ⚠️ Configuración y Base de Datos
# ===============================
token = os.environ.get("TELEGRAM_BOT_TOKEN")
bot = telebot.TeleBot(token)
app = Flask(__name__)
RAILWAY_URL = os.environ.get("RAILWAY_PUBLIC_DOMAIN")

def init_db():
    conn = sqlite3.connect('bot_data.db')
    c = conn.cursor()
    # Tabla para no perder el progreso si Railway reinicia
    c.execute('''CREATE TABLE IF NOT EXISTS sesiones 
                 (chat_id INTEGER PRIMARY KEY, preguntas TEXT, indice INTEGER, aciertos INTEGER, fallos INTEGER)''')
    # Tabla para estadísticas permanentes
    c.execute('''CREATE TABLE IF NOT EXISTS stats 
                 (chat_id INTEGER PRIMARY KEY, total_aciertos INTEGER, total_fallos INTEGER, intentos INTEGER)''')
    conn.commit()
    conn.close()

init_db()

materias_display = {
    'lengua': '📚 LENGUA',
    'mates': '🔢 MATEMÁTICAS',
    'ciencias': '🧪 CIENCIAS',
    'ingles': '🇬🇧 INGLÉS',
    'frances': '🇫🇷 FRANCÉS'
}

# ===============================
# 🛠️ Gestión de Datos (SQLite)
# ===============================

def db_get_sesion(chat_id):
    conn = sqlite3.connect('bot_data.db')
    c = conn.cursor()
    c.execute("SELECT preguntas, indice, aciertos, fallos FROM sesiones WHERE chat_id=?", (chat_id,))
    row = c.fetchone()
    conn.close()
    if row:
        return {'preguntas': json.loads(row[0]), 'indice': row[1], 'aciertos': row[2], 'fallos': row[3]}
    return None

def db_save_sesion(chat_id, datos):
    conn = sqlite3.connect('bot_data.db')
    c = conn.cursor()
    c.execute("INSERT OR REPLACE INTO sesiones VALUES (?, ?, ?, ?, ?)", 
              (chat_id, json.dumps(datos['preguntas']), datos['indice'], datos['aciertos'], datos['fallos']))
    conn.commit()
    conn.close()

def db_delete_sesion(chat_id):
    conn = sqlite3.connect('bot_data.db')
    c = conn.cursor()
    c.execute("DELETE FROM sesiones WHERE chat_id=?", (chat_id,))
    conn.commit()
    conn.close()

def db_registrar_final(chat_id, aciertos, fallos):
    conn = sqlite3.connect('bot_data.db')
    c = conn.cursor()
    c.execute("INSERT OR IGNORE INTO stats VALUES (?, 0, 0, 0)", (chat_id,))
    c.execute("UPDATE stats SET total_aciertos = total_aciertos + ?, total_fallos = total_fallos + ?, intentos = intentos + 1 WHERE chat_id=?", 
              (aciertos, fallos, chat_id))
    conn.commit()
    conn.close()

# ===============================
# 🎨 Interfaz Visual
# ===============================

def progreso_visual(actual, total):
    relleno = int((actual / total) * 10)
    return "🔹" * relleno + "🔸" * (10 - relleno)

def generar_markup_pregunta(preguntas, idx):
    pregunta = preguntas[idx]
    markup = types.InlineKeyboardMarkup(row_width=1)
    # Mezclamos opciones para que no siempre sea la misma posición
    opciones = list(pregunta['o'])
    random.shuffle(opciones)
    
    for opcion in opciones:
        es_correcta = 1 if opcion == pregunta['r'] else 0
        markup.add(types.InlineKeyboardButton(opcion, callback_data=f"ans|{es_correcta}|{idx}"))
    markup.add(types.InlineKeyboardButton("🛑 ABANDONAR EXAMEN", callback_data="menu_principal"))
    return markup

# ===============================
# 🚀 Handlers (Navegación)
# ===============================

@bot.message_handler(commands=['start', 'menu'])
@bot.callback_query_handler(func=lambda call: call.data == "menu_principal")
def menu_principal(obj):
    is_cb = isinstance(obj, types.CallbackQuery)
    chat_id = obj.message.chat.id if is_cb else obj.chat.id
    db_delete_sesion(chat_id)
    
    markup = types.InlineKeyboardMarkup(row_width=2)
    botones = [types.InlineKeyboardButton(nom, callback_data=f"mat|{idx}") for idx, nom in materias_display.items()]
    markup.add(*botones)
    markup.add(types.InlineKeyboardButton("📈 MIS ESTADÍSTICAS", callback_data="ver_stats"))
    
    texto = "🎓 *CENTRO DE ESTUDIOS VIRTUAL*\n\nBienvenido. Selecciona una materia para comenzar tu evaluación:"
    
    if is_cb:
        bot.edit_message_text(texto, chat_id, obj.message.message_id, reply_markup=markup, parse_mode='Markdown')
    else:
        bot.send_message(chat_id, texto, reply_markup=markup, parse_mode='Markdown')

@bot.callback_query_handler(func=lambda call: call.data.startswith('mat|'))
def mostrar_temas(call):
    materia_id = call.data.split('|')[1]
    try:
        spec = importlib.util.spec_from_file_location(materia_id, f"{materia_id}.py")
        module = importlib.util.module_from_spec(spec)
        sys.modules[materia_id] = module
        spec.loader.exec_module(module)
        temario = getattr(module, "TEMARIO")
        
        markup = types.InlineKeyboardMarkup(row_width=1)
        for tema in temario.keys():
            markup.add(types.InlineKeyboardButton(f"📂 {tema}", callback_data=f"tema|{materia_id}|{tema}"))
        markup.add(types.InlineKeyboardButton("🔙 VOLVER", callback_data="menu_principal"))
        
        bot.edit_message_text(f"📖 *MATERIA:* {materias_display[materia_id]}\n\nSelecciona el tema que deseas repasar:", 
                             call.message.chat.id, call.message.message_id, reply_markup=markup, parse_mode='Markdown')
    except:
        bot.answer_callback_query(call.id, "Error al cargar temario.")

@bot.callback_query_handler(func=lambda call: call.data.startswith('tema|'))
def mostrar_examenes(call):
    p = call.data.split('|')
    markup = types.InlineKeyboardMarkup(row_width=1)
    for i in range(3):
        markup.add(types.InlineKeyboardButton(f"📝 SIMULACRO DE EXAMEN {i+1}", callback_data=f"ex|{p[1]}|{p[2]}|{i}"))
    markup.add(types.InlineKeyboardButton("🔙 VOLVER A TEMAS", callback_data=f"mat|{p[1]}"))
    bot.edit_message_text(f"📍 *TEMA:* {p[2]}\n\nElige un nivel de examen:", 
                         call.message.chat.id, call.message.message_id, reply_markup=markup, parse_mode='Markdown')

@bot.callback_query_handler(func=lambda call: call.data.startswith('ex|'))
def iniciar_examen(call):
    p = call.data.split('|')
    module = sys.modules.get(p[1])
    preguntas = getattr(module, "TEMARIO")[p[2]]['examenes'][int(p[3])]
    
    datos = {'preguntas': preguntas, 'indice': 0, 'aciertos': 0, 'fallos': 0}
    db_save_sesion(call.message.chat.id, datos)
    
    markup = generar_markup_pregunta(preguntas, 0)
    texto = f"📝 *EXAMEN EN CURSO*\n\nPregunta 1 de {len(preguntas)}\n{progreso_visual(1, len(preguntas))}\n\n*P:* {preguntas[0]['p']}"
    bot.edit_message_text(texto, call.message.chat.id, call.message.message_id, reply_markup=markup, parse_mode='Markdown')

@bot.callback_query_handler(func=lambda call: call.data.startswith('ans|'))
def manejar_respuesta(call):
    chat_id = call.message.chat.id
    datos = db_get_sesion(chat_id)
    if not datos: return

    p = call.data.split('|')
    if int(p[2]) != datos['indice']: return # Evita doble clic

    if int(p[1]):
        datos['aciertos'] += 1
        bot.answer_callback_query(call.id, "✅ ¡CORRECTO!")
    else:
        datos['fallos'] += 1
        bot.answer_callback_query(call.id, "❌ INCORRECTO")

    datos['indice'] += 1
    if datos['indice'] < len(datos['preguntas']):
        db_save_sesion(chat_id, datos)
        idx = datos['indice']
        markup = generar_markup_pregunta(datos['preguntas'], idx)
        texto = f"📝 *EXAMEN EN CURSO*\n\nPregunta {idx+1} de {len(datos['preguntas'])}\n{progreso_visual(idx+1, len(datos['preguntas']))}\n\n*P:* {datos['preguntas'][idx]['p']}"
        bot.edit_message_text(texto, chat_id, call.message.message_id, reply_markup=markup, parse_mode='Markdown')
    else:
        db_registrar_final(chat_id, datos['aciertos'], datos['fallos'])
        resumen = (f"🏁 *EXAMEN FINALIZADO*\n\n"
                   f"✅ Aciertos: `{datos['aciertos']}`\n"
                   f"❌ Fallos: `{datos['fallos']}`\n"
                   f"📊 Calificación: `{(datos['aciertos']/len(datos['preguntas']))*10:.2f}/10`\n\n"
                   f"¡Buen trabajo!")
        markup = types.InlineKeyboardMarkup()
        markup.add(types.InlineKeyboardButton("🔙 VOLVER AL INICIO", callback_data="menu_principal"))
        bot.edit_message_text(resumen, chat_id, call.message.message_id, reply_markup=markup, parse_mode='Markdown')
        db_delete_sesion(chat_id)

@bot.callback_query_handler(func=lambda call: call.data == 'ver_stats')
def ver_stats(call):
    conn = sqlite3.connect('bot_data.db')
    c = conn.cursor()
    c.execute("SELECT total_aciertos, total_fallos, intentos FROM stats WHERE chat_id=?", (call.message.chat.id,))
    s = c.fetchone() or (0, 0, 0)
    conn.close()
    
    msg = f"📊 *TU RENDIMIENTO ACADÉMICO*\n\n🔹 Exámenes realizados: `{s[2]}`\n✅ Aciertos totales: `{s[0]}`\n❌ Fallos totales: `{s[1]}`"
    markup = types.InlineKeyboardMarkup()
    markup.add(types.InlineKeyboardButton("🔙 VOLVER", callback_data="menu_principal"))
    bot.edit_message_text(msg, call.message.chat.id, call.message.message_id, reply_markup=markup, parse_mode='Markdown')

# ===============================
# 🌐 Webhook y Servidor
# ===============================

@app.route(f'/{token}', methods=['POST'])
def get_message():
    if request.headers.get('content-type') == 'application/json':
        json_string = request.get_data().decode('utf-8')
        update = telebot.types.Update.de_json(json_string)
        bot.process_new_updates([update])
        return "!", 200
    return "error", 403

@app.route("/")
def index(): return "Bot Profesional Online", 200

if __name__ == "__main__":
    port = int(os.environ.get("PORT", 8080))
    if RAILWAY_URL and token:
        bot.remove_webhook()
        bot.set_webhook(url=f"https://{RAILWAY_URL}/{token}")
    app.run(host="0.0.0.0", port=port)
