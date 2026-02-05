import telebot
from telebot import types
import random

# CONFIGURACIÓN
TOKEN = "8441666201:AAHygO1Osx5IdxnmQpQuF__Y8WyGvBKhr4U"
bot = telebot.TeleBot("8441666201:AAHygO1Osx5IdxnmQpQuF__Y8WyGvBKhr4U")

# BANCO DE DATOS INTEGRADO (Para evitar errores de importación)
BANCO_PREGUNTAS = {
    'mates': {
        'U1': {
            'titulo': 'Números hasta 1.000.000',
            'preguntas': [
                {'p': '¿Cómo se lee 540.030?', 'o': ['Quinientos cuarenta mil treinta', 'Quinientos cuatro mil treinta'], 'r': 'Quinientos cuarenta mil treinta'},
                {'p': 'Valor del 3 en 130.500:', 'o': ['30.000 unidades', '3.000 unidades'], 'r': '30.000 unidades'},
                {'p': '¿Qué número es 4 CM, 2 UM y 5 D?', 'o': ['402.050', '420.050'], 'r': '402.050'},
                {'p': 'Redondea 8.600 a la U. de millar:', 'o': ['9.000', '8.000'], 'r': '9.000'},
                {'p': 'Anterior a 1.000.000:', 'o': ['999.999', '1.000.001'], 'r': '999.999'},
                {'p': 'Suma 100.000 + 50.000 + 200:', 'o': ['150.200', '105.200'], 'r': '150.200'},
                {'p': 'Cifra de las Centenas en 456.789:', 'o': ['7', '8'], 'r': '7'},
                {'p': 'Setecientos mil siete se escribe:', 'o': ['700.007', '700.700'], 'r': '700.007'},
                {'p': '¿Qué es mayor?', 'o': ['45.600', '45.099'], 'r': '45.600'},
                {'p': '¿Cuántas decenas hay en una centena?', 'o': ['10', '100'], 'r': '10'}
            ]
        },
        'U2': {
            'titulo': 'Operaciones naturales',
            'preguntas': [
                {'p': '1.250 + 750 =', 'o': ['2.000', '1.900'], 'r': '2.000'},
                {'p': 'Diferencia de 100 menos 40:', 'o': ['60', '140'], 'r': '60'},
                {'p': '25 x 4 =', 'o': ['100', '125'], 'r': '100'},
                {'p': '120 x 10 =', 'o': ['1.200', '1.100'], 'r': '1.200'},
                {'p': '50 caramelos entre 5 niños:', 'o': ['10', '5'], 'r': '10'},
                {'p': 'Lo que sobra en una división es el...', 'o': ['Resto', 'Cociente'], 'r': 'Resto'},
                {'p': '(10 + 5) x 2 =', 'o': ['30', '20'], 'r': '30'},
                {'p': 'El doble de 150 es:', 'o': ['300', '450'], 'r': '300'},
                {'p': '20 : 4 =', 'o': ['5', '4'], 'r': '5'},
                {'p': '¿Qué se hace antes?', 'o': ['5 + 2 x 3', 'Multiplicar'], 'r': 'Multiplicar'}
            ]
        }
    },
    'frances': {
        'U1': {
            'titulo': 'Bonjour! (Saludos)',
            'preguntas': [
                {'p': '¿Cómo se dice "Hola" informal?', 'o': ['Salut', 'Merci'], 'r': 'Salut'},
                {'p': '¿Qué es "Enchanté"?', 'o': ['Encantado', 'Adiós'], 'r': 'Encantado'},
                {'p': '¿Cómo se escribe 15?', 'o': ['Quinze', 'Treize'], 'r': 'Quinze'},
                {'p': 'Para despedirse:', 'o': ['Au revoir', 'Bonjour'], 'r': 'Au revoir'},
                {'p': '¿Qué número es "douze"?', 'o': ['12', '2'], 'r': '12'},
                {'p': 'Saludamos por la noche con:', 'o': ['Bonsoir', 'Bonjour'], 'r': 'Bonsoir'},
                {'p': 'Ça va ?', 'o': ['Ça va bien', 'Merci'], 'r': 'Ça va bien'},
                {'p': 'Número 8:', 'o': ['Huit', 'Sept'], 'r': 'Huit'},
                {'p': '¿Qué es "Monsieur"?', 'o': ['Señor', 'Niño'], 'r': 'Señor'},
                {'p': 'Número 20:', 'o': ['Vingt', 'Dix'], 'r': 'Vingt'}
            ]
        }
    }
    # Se pueden añadir 'ingles', 'lengua' y 'ciencias' aquí siguiendo el mismo patrón
}

MATERIAS_NOM = {'lengua': '📚 Lengua', 'mates': '🔢 Matemáticas', 'ciencias': '🧪 Ciencias', 'ingles': '🇬🇧 Inglés', 'frances': '🇫🇷 Francés'}
user_stats = {}

@bot.message_handler(commands=['start', 'menu'])
def menu(message):
    markup = types.InlineKeyboardMarkup(row_width=2)
    botones = [types.InlineKeyboardButton(v, callback_data=f"sel_{k}") for k, v in MATERIAS_NOM.items()]
    markup.add(*botones)
    bot.send_message(message.chat.id, "¡Hola! 👋 Soy tu **Profe-Bot de Apoyo**.\nElige una materia:", reply_markup=markup, parse_mode="Markdown")

@bot.callback_query_handler(func=lambda call: call.data.startswith('sel_'))
def elegir_tema(call):
    materia = call.data.split('_')[1]
    if materia not in BANCO_PREGUNTAS:
        bot.answer_callback_query(call.id, "⚠️ Materia en desarrollo...", show_alert=True)
        return

    markup = types.InlineKeyboardMarkup()
    for id_u, info in BANCO_PREGUNTAS[materia].items():
        markup.add(types.InlineKeyboardButton(f"{id_u}: {info['titulo']}", callback_data=f"exam_{materia}_{id_u}"))
    
    bot.edit_message_text(f"Elige un tema de **{MATERIAS_NOM[materia]}**:", call.message.chat.id, call.message.message_id, reply_markup=markup, parse_mode="Markdown")

@bot.callback_query_handler(func=lambda call: call.data.startswith('exam_'))
def inicio_test(call):
    _, mat, uni = call.data.split('_')
    preguntas = random.sample(BANCO_PREGUNTAS[mat][uni]['preguntas'], 10)
    user_stats[call.message.chat.id] = {'p': preguntas, 'idx': 0, 'ok': 0, 'mat': mat}
    bot.delete_message(call.message.chat.id, call.message.message_id)
    lanzar_pregunta(call.message.chat.id)

def lanzar_pregunta(chat_id):
    s = user_stats[chat_id]
    if s['idx'] < len(s['p']):
        ques = s['p'][s['idx']]
        markup = types.InlineKeyboardMarkup()
        for o in ques['o']:
            markup.add(types.InlineKeyboardButton(o, callback_data=f"r_{'y' if o == ques['r'] else 'n'}"))
        bot.send_message(chat_id, f"❓ **Pregunta {s['idx']+1}/10**\n\n{ques['p']}", reply_markup=markup, parse_mode="Markdown")
    else:
        final(chat_id)

@bot.callback_query_handler(func=lambda call: call.data.startswith('r_'))
def respuesta(call):
    cid = call.message.chat.id
    if call.data == "r_y":
        user_stats[cid]['ok'] += 1
        bot.answer_callback_query(call.id, "¡Correcto! ✅")
    else:
        bot.answer_callback_query(call.id, "¡Sigue intentando! 💡")
    
    bot.delete_message(cid, call.message.message_id)
    user_stats[cid]['idx'] += 1
    lanzar_pregunta(cid)

def final(chat_id):
    n = user_stats[chat_id]['ok']
    msg = f"🏁 **¡Test terminado!**\n\nNota: **{n}/10**\n\n/menu para volver."
    bot.send_message(chat_id, msg, parse_mode="Markdown")
    del user_stats[chat_id]

bot.infinity_polling()
