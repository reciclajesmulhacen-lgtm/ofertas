import os
import importlib.util
import sys
import random
from flask import Flask, request
import telebot
from telebot import types

# ===============================
# ⚠️ Configuración
# ===============================
token = os.environ.get("TELEGRAM_BOT_TOKEN")
bot = telebot.TeleBot(token)
app = Flask(__name__)
RAILWAY_URL = os.environ.get("RAILWAY_PUBLIC_DOMAIN")

# Datos en memoria (Simples para evitar bloqueos en Railway)
user_stats = {} 
global_stats = {}

materias_display = {
    'lengua': '📚 LENGUA',
    'mates': '🔢 MATEMÁTICAS',
    'ciencias': '🧪 CIENCIAS',
    'ingles': '🇬🇧 INGLÉS',
    'frances': '🇫🇷 FRANCÉS'
}

# ===============================
# 🛠️ Funciones de Apoyo Visual
# ===============================

def barra_progreso(actual, total):
    porcentaje = (actual / total)
    relleno = int(porcentaje * 10)
    return "🔹" * relleno + "🔸" * (10 - relleno) + f" {int(porcentaje*100)}%"

def generar_markup_pregunta(preguntas, idx):
    pregunta = preguntas[idx]
    markup = types.InlineKeyboardMarkup(row_width=1)
    
    # Mezclar respuestas para que no sea predecible
    opciones = list(pregunta['o'])
    random.shuffle(opciones)
    
    for opcion in opciones:
        es_correcta = 1 if opcion == pregunta['r'] else 0
        # SEGURO: Usamos "|" y el índice para evitar saltos de preguntas
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
    
    # Limpiar sesión actual
    if chat_id in user_stats:
        del user_stats[chat_id]
    
    markup = types.InlineKeyboardMarkup(row_width=2)
    botones = [types.InlineKeyboardButton(nom, callback_data=f"mat|{idx}") for idx, nom in materias_display.items()]
    markup.add(*botones)
    markup.add(types.InlineKeyboardButton("📈 VER MIS ESTADÍSTICAS", callback_data="ver_stats"))
    
    texto = "🎓 *CENTRO DE ESTUDIOS VIRTUAL*\n\n¡Hola! Selecciona una materia para poner a prueba tus conocimientos:"
    
    if is_cb:
        bot.edit_message_text(texto, chat_id, obj.message.message_id, reply_markup=markup, parse_mode='Markdown')
    else:
        bot.send_message(chat_id, texto, reply_markup=markup, parse_mode='Markdown')

@bot.callback_query_handler(func=lambda call: call.data.startswith('mat|'))
def mostrar_temas(call):
    m_id = call.data.split('|')[1]
    try:
        spec = importlib.util.spec_from_file_location(m_id, f"{m_id}.py")
        module = importlib.util.module_from_spec(spec)
        sys.modules[m_id] = module
        spec.loader.exec_module(module)
        temario = getattr(module, "TEMARIO")
        
        markup = types.InlineKeyboardMarkup(row_width=1)
        for tema in temario.keys():
            markup.add(types.InlineKeyboardButton(f"📂 {tema}", callback_data=f"tema|{m_id}|{tema}"))
        markup.add(types.InlineKeyboardButton("🔙 VOLVER AL INICIO", callback_data="menu_principal"))
        
        bot.edit_message_text(f"📖 *MATERIA:* {materias_display[m_id]}\n\nSelecciona el tema que deseas estudiar:", 
                             call.message.chat.id, call.message.message_id, reply_markup=markup, parse_mode='Markdown')
    except:
        bot.answer_callback_query(call.id, "⚠️ Error cargando materia.")

@bot.callback_query_handler(func=lambda call: call.data.startswith('tema|'))
def mostrar_examenes(call):
    partes = call.data.split('|')
    m_id, t_nombre = partes[1], partes[2]
    
    markup = types.InlineKeyboardMarkup(row_width=1)
    for i in range(3):
        markup.add(types.InlineKeyboardButton(f"📝 SIMULACRO EXAMEN {i+1}", callback_data=f"ex|{m_id}|{t_nombre}|{i}"))
    markup.add(types.InlineKeyboardButton("🔙 VOLVER A TEMAS", callback_data=f"mat|{m_id}"))
    
    bot.edit_message_text(f"📍 *TEMA:* {t_nombre}\n\nSelecciona un examen para comenzar:", 
                         call.message.chat.id, call.message.message_id, reply_markup=markup, parse_mode='Markdown')

@bot.callback_query_handler(func=lambda call: call.data.startswith('ex|'))
def iniciar_examen(call):
    p = call.data.split('|')
    m_id, t_nombre, ex_idx = p[1], p[2], int(p[3])
    
    module = sys.modules.get(m_id)
    preguntas = getattr(module, "TEMARIO")[t_nombre]['examenes'][ex_idx]
    
    user_stats[call.message.chat.id] = {
        'preguntas': preguntas,
        'indice': 0, 'aciertos': 0, 'fallos': 0
    }
    
    markup = generar_markup_pregunta(preguntas, 0)
    texto = (f"📝 *EXAMEN:* {t_nombre}\n"
             f"Pregunta 1 de {len(preguntas)}\n"
             f"{barra_progreso(1, len(preguntas))}\n\n"
             f"*P:* {preguntas[0]['p']}")
    
    bot.edit_message_text(texto, call.message.chat.id, call.message.message_id, reply_markup=markup, parse_mode='Markdown')

@bot.callback_query_handler(func=lambda call: call.data.startswith('ans|'))
def manejar_respuesta(call):
    chat_id = call.message.chat.id
    datos = user_stats.get(chat_id)
    if not datos: return

    p = call.data.split('|')
    es_correcta, idx_click = int(p[1]), int(p[2])

    # SEGURO ANTI-SALTOS: Ignora si no coincide con la pregunta actual
    if idx_click != datos['indice']: return

    if es_correcta:
        datos['aciertos'] += 1
        bot.answer_callback_query(call.id, "✅ ¡Correcto!")
    else:
        datos['fallos'] += 1
        bot.answer_callback_query(call.id, "❌ Incorrecto")

    datos['indice'] += 1
    if datos['indice'] < len(datos['preguntas']):
        idx = datos['indice']
        markup = generar_markup_pregunta(datos['preguntas'], idx)
        texto = (f"📝 *EXAMEN EN CURSO*\n"
                 f"Pregunta {idx+1} de {len(datos['preguntas'])}\n"
                 f"{barra_progreso(idx+1, len(datos['preguntas']))}\n\n"
                 f"*P:* {datos['preguntas'][idx]['p']}")
        bot.edit_message_text(texto, chat_id, call.message.message_id, reply_markup=markup, parse_mode='Markdown')
    else:
        # FIN EXAMEN
        total = len(datos['preguntas'])
        aciertos = datos['aciertos']
        nota = (aciertos/total)*10
        
        resumen = (f"🏁 *¡EXAMEN FINALIZADO!*\n\n"
                   f"✅ Aciertos: `{aciertos}`\n"
                   f"❌ Fallos: `{datos['fallos']}`\n"
                   f"📊 Nota Final: `{nota:.1f}/10`\n\n"
                   f"{'🌟 ¡Excelente trabajo!' if nota >= 9 else '📚 ¡Sigue practicando!'}")
        
        markup = types.InlineKeyboardMarkup()
        markup.add(types.InlineKeyboardButton("🔙 VOLVER AL MENÚ", callback_data="menu_principal"))
        bot.edit_message_text(resumen, chat_id, call.message.message_id, reply_markup=markup, parse_mode='Markdown')
        del user_stats[chat_id]

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
def index(): return "Bot Online", 200

if __name__ == "__main__":
    port = int(os.environ.get("PORT", 8080))
    if RAILWAY_URL and token:
        bot.remove_webhook()
        bot.set_webhook(url=f"https://{RAILWAY_URL}/{token}")
    app.run(host="0.0.0.0", port=port)
