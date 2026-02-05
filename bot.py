import telebot
from telebot import types
import random

TOKEN = "8441666201:AAHygO1Osx5IdxnmQpQuF__Y8WyGvBKhr4U"
bot = telebot.TeleBot("8441666201:AAHygO1Osx5IdxnmQpQuF__Y8WyGvBKhr4U")

# BANCO DE DATOS COMPLETO
BANCO_PREGUNTAS = {
    'lengua': {
        'U1': {
            'titulo': '¡Por nuestra salud!',
            'preguntas': [
                {'p': '¿Qué es un párrafo?', 'o': ['Conjunto de oraciones', 'Una palabra sola'], 'r': 'Conjunto de oraciones'},
                {'p': 'Se escribe con J:', 'o': ['Equipaje', 'Geranio'], 'r': 'Equipaje'},
                {'p': '¿Qué letra falta en "masa_e"?', 'o': ['j', 'g'], 'r': 'j'},
                {'p': 'El eslogan de un anuncio es...', 'o': ['Frase corta y pegadiza', 'El precio'], 'r': 'Frase corta y pegadiza'},
                {'p': 'Punto que separa párrafos:', 'o': ['Punto y aparte', 'Punto y seguido'], 'r': 'Punto y aparte'},
                {'p': 'Se escribe con G:', 'o': ['Geología', 'Jirafa'], 'r': 'Geología'},
                {'p': '¿Para qué sirve un anuncio?', 'o': ['Convencer e informar', 'Solo divertir'], 'r': 'Convencer e informar'},
                {'p': '¿Qué falta en "re_illa"?', 'o': ['j', 'g'], 'r': 'j'},
                {'p': 'El punto final indica...', 'o': ['Que el texto termina', 'Que sigue otra idea'], 'r': 'Que el texto termina'},
                {'p': '¿Quién recibe el mensaje del anuncio?', 'o': ['Receptor', 'Emisor'], 'r': 'Receptor'}
            ]
        }
    },
    'mates': {
        'U1': {
            'titulo': 'Números hasta 1.000.000',
            'preguntas': [
                {'p': '¿Cómo se lee 540.030?', 'o': ['Quinientos cuarenta mil treinta', 'Cincuenta mil treinta'], 'r': 'Quinientos cuarenta mil treinta'},
                {'p': 'Valor del 3 en 130.500:', 'o': ['30.000 unidades', '3.000 unidades'], 'r': '30.000 unidades'},
                {'p': '¿Qué número es 4 CM y 2 UM?', 'o': ['402.000', '420.000'], 'r': '402.000'},
                {'p': 'Redondea 8.600 a la U.M:', 'o': ['9.000', '8.000'], 'r': '9.000'},
                {'p': 'Anterior a 1.000.000:', 'o': ['999.999', '1.000.001'], 'r': '999.999'},
                {'p': 'Suma 100.000 + 50.000:', 'o': ['150.000', '105.000'], 'r': '150.000'},
                {'p': 'Centenas en 456.789:', 'o': ['7', '8'], 'r': '7'},
                {'p': 'Setecientos mil siete:', 'o': ['700.007', '700.700'], 'r': '700.007'},
                {'p': '¿Qué es mayor?', 'o': ['45.600', '45.099'], 'r': '45.600'},
                {'p': '¿Decenas en una centena?', 'o': ['10', '100'], 'r': '10'}
            ]
        }
    },
    'ciencias': {
        'U1': {
            'titulo': 'Seres vivos',
            'preguntas': [
                {'p': '¿Cuál es la unidad básica de la vida?', 'o': ['La célula', 'El átomo'], 'r': 'La célula'},
                {'p': 'Las plantas son seres...', 'o': ['Autótrofos', 'Heterótrofos'], 'r': 'Autótrofos'},
                {'p': 'Reino al que pertenecen las bacterias:', 'o': ['Moneras', 'Fungi'], 'r': 'Moneras'},
                {'p': '¿Qué expulsan las plantas en la fotosíntesis?', 'o': ['Oxígeno', 'Dióxido de carbono'], 'r': 'Oxígeno'},
                {'p': 'Los hongos pertenecen al reino...', 'o': ['Fungi', 'Protoctista'], 'r': 'Fungi'},
                {'p': '¿Qué órgano usan los peces para respirar?', 'o': ['Branquias', 'Pulmones'], 'r': 'Branquias'},
                {'p': 'Un animal vertebrado tiene...', 'o': ['Esqueleto interno', 'Concha'], 'r': 'Esqueleto interno'},
                {'p': 'Las algas son del reino...', 'o': ['Protoctista', 'Plantae'], 'r': 'Protoctista'},
                {'p': 'La nutrición puede ser...', 'o': ['Autótrofa o Heterótrofa', 'Solo comer plantas'], 'r': 'Autótrofa o Heterótrofa'},
                {'p': '¿Qué parte de la planta absorbe agua?', 'o': ['Raíz', 'Hoja'], 'r': 'Raíz'}
            ]
        }
    },
    'ingles': {
        'U1': {
            'titulo': 'Hello! (Basics)',
            'preguntas': [
                {'p': 'How do you say 75?', 'o': ['Seventy-five', 'Seven-five'], 'r': 'Seventy-five'},
                {'p': 'Color of a lemon:', 'o': ['Yellow', 'Purple'], 'r': 'Yellow'},
                {'p': 'Spell 100:', 'o': ['One hundred', 'Ten ten'], 'r': 'One hundred'},
                {'p': 'Blue + Red =', 'o': ['Purple', 'Green'], 'r': 'Purple'},
                {'p': 'Number 13:', 'o': ['Thirteen', 'Thirty'], 'r': 'Thirteen'},
                {'p': 'Grass is...', 'o': ['Green', 'Blue'], 'r': 'Green'},
                {'p': 'How do you say 40?', 'o': ['Forty', 'Fourty'], 'r': 'Forty'},
                {'p': 'The sky is...', 'o': ['Blue', 'Black'], 'r': 'Blue'},
                {'p': 'Number 50:', 'o': ['Fifty', 'Fifteen'], 'r': 'Fifty'},
                {'p': 'Formal "Hola":', 'o': ['Hello', 'Bye'], 'r': 'Hello'}
            ]
        }
    },
    'frances': {
        'U1': {
            'titulo': 'Bonjour! (Francés)',
            'preguntas': [
                {'p': '¿Hola informal?', 'o': ['Salut', 'Merci'], 'r': 'Salut'},
                {'p': '¿Enchanté?', 'o': ['Encantado', 'Adiós'], 'r': 'Encantado'},
                {'p': '¿Número 15?', 'o': ['Quinze', 'Treize'], 'r': 'Quinze'},
                {'p': 'Para despedirse:', 'o': ['Au revoir', 'Bonjour'], 'r': 'Au revoir'},
                {'p': '¿Douze?', 'o': ['12', '2'], 'r': '12'},
                {'p': 'Noche:', 'o': ['Bonsoir', 'Bonjour'], 'r': 'Bonsoir'},
                {'p': 'Ça va ?', 'o': ['Ça va bien', 'Merci'], 'r': 'Ça va bien'},
                {'p': 'Número 8:', 'o': ['Huit', 'Sept'], 'r': 'Huit'},
                {'p': 'Monsieur:', 'o': ['Señor', 'Niño'], 'r': 'Señor'},
                {'p': 'Número 20:', 'o': ['Vingt', 'Dix'], 'r': 'Vingt'}
            ]
        }
    }
}

NOMBRES = {'lengua': '📚 Lengua', 'mates': '🔢 Mates', 'ciencias': '🧪 Ciencias', 'ingles': '🇬🇧 Inglés', 'frances': '🇫🇷 Francés'}
user_stats = {}

@bot.message_handler(commands=['start', 'menu'])
def menu(message):
    markup = types.InlineKeyboardMarkup(row_width=2)
    botones = [types.InlineKeyboardButton(v, callback_data=f"sel_{k}") for k, v in NOMBRES.items()]
    markup.add(*botones)
    bot.send_message(message.chat.id, "✨ **¡Hola! Bienvenido a tu Profe-Bot.**\nElige una materia:", reply_markup=markup, parse_mode="Markdown")

@bot.callback_query_handler(func=lambda call: call.data.startswith('sel_'))
def elegir_tema(call):
    m = call.data.split('_')[1]
    markup = types.InlineKeyboardMarkup()
    for id_u, info in BANCO_PREGUNTAS[m].items():
        markup.add(types.InlineKeyboardButton(f"{id_u}: {info['titulo']}", callback_data=f"ex_{m}_{id_u}"))
    bot.edit_message_text(f"Has elegido **{NOMBRES[m]}**. Elige unidad:", call.message.chat.id, call.message.message_id, reply_markup=markup, parse_mode="Markdown")

@bot.callback_query_handler(func=lambda call: call.data.startswith('ex_'))
def inicio(call):
    _, mat, uni = call.data.split('_')
    p_pool = BANCO_PREGUNTAS[mat][uni]['preguntas']
    user_stats[call.message.chat.id] = {'p': random.sample(p_pool, 10), 'i': 0, 'ok': 0}
    bot.delete_message(call.message.chat.id, call.message.message_id)
    lanzar(call.message.chat.id)

def lanzar(cid):
    s = user_stats[cid]
    if s['i'] < 10:
        q = s['p'][s['i']]
        mk = types.InlineKeyboardMarkup()
        for o in q['o']: mk.add(types.InlineKeyboardButton(o, callback_data=f"r_{'y' if o==q['r'] else 'n'}"))
        bot.send_message(cid, f"❓ **Pregunta {s['i']+1}/10**\n\n{q['p']}", reply_markup=mk, parse_mode="Markdown")
    else:
        n = s['ok']
        bot.send_message(cid, f"🏁 **¡Fin!**\nNota: **{n}/10**\n/menu para volver.")

@bot.callback_query_handler(func=lambda call: call.data.startswith('r_'))
def respuesta(call):
    cid = call.message.chat.id
    if call.data == "r_y": user_stats[cid]['ok'] += 1
    bot.delete_message(cid, call.message.message_id)
    user_stats[cid]['i'] += 1
    lanzar(cid)

bot.infinity_polling()
