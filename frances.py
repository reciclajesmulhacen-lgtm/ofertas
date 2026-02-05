import random
from telebot import types

# BANCO DE DATOS COMPLETO (8 UNIDADES x 10 PREGUNTAS)
TEMARIO = {
    'U1': {
        'titulo': 'Bonjour! (Saludos y Números)',
        'preguntas': [
            {'p': '¿Cómo se dice "Hola" de forma informal?', 'o': ['Salut', 'Bonjour', 'Merci'], 'r': 'Salut'},
            {'p': '¿Qué significa "Enchanté"?', 'o': ['Encantado', 'Adiós', 'Mañana'], 'r': 'Encantado'},
            {'p': '¿Cómo se escribe 15 en francés?', 'o': ['Quinze', 'Quatorze', 'Treize'], 'r': 'Quinze'},
            {'p': 'Para despedirse se dice...', 'o': ['Au revoir', 'Bonjour', 'S’il vous plaît'], 'r': 'Au revoir'},
            {'p': '¿Qué número es "douze"?', 'o': ['12', '2', '20'], 'r': '12'},
            {'p': '¿Cómo saludas por la tarde/noche?', 'o': ['Bonsoir', 'Bonne nuit', 'Salut'], 'r': 'Bonsoir'},
            {'p': 'Si digo "Ça va ?", respondes:', 'o': ['Ça va bien', 'Je m’appelle Anne', 'Merci'], 'r': 'Ça va bien'},
            {'p': '¿Cómo se dice el número 8?', 'o': ['Huit', 'Sept', 'Neuf'], 'r': 'Huit'},
            {'p': '¿Qué es "Monsieur"?', 'o': ['Señor', 'Señora', 'Niño'], 'r': 'Señor'},
            {'p': 'Número 20 en francés:', 'o': ['Vingt', 'Dix', 'Trente'], 'r': 'Vingt'}
        ]
    },
    'U2': {
        'titulo': 'Ma famille (Être/Avoir)',
        'preguntas': [
            {'p': '¿Cómo se dice "Yo tengo"?', 'o': ['J’ai', 'Je suis', 'Tu as'], 'r': 'J’ai'},
            {'p': '¿Qué significa "Mère"?', 'o': ['Madre', 'Padre', 'Hermana'], 'r': 'Madre'},
            {'p': 'Para decir "Yo soy" usamos:', 'o': ['Je suis', 'Il est', 'J’ai'], 'r': 'Je suis'},
            {'p': '¿Quién es "le grand-père"?', 'o': ['El abuelo', 'El tío', 'El primo'], 'r': 'El abuelo'},
            {'p': '¿Cómo se dice "Hermana"?', 'o': ['Sœur', 'Frère', 'Fille'], 'r': 'Sœur'},
            {'p': 'Verbo Être: "Tu ___"', 'o': ['es', 'as', 'suis'], 'r': 'es'},
            {'p': '¿Qué significa "Frère"?', 'o': ['Hermano', 'Hijo', 'Padre'], 'r': 'Hermano'},
            {'p': 'Para preguntar la edad: "Quel ___ as-tu?"', 'o': ['âge', 'nom', 'famille'], 'r': 'âge'},
            {'p': '¿Cómo se dice "Padre"?', 'o': ['Père', 'Papier', 'Grand-mère'], 'r': 'Père'},
            {'p': '"Ils sont" significa...', 'o': ['Ellos son', 'Ellos tienen', 'Nosotros somos'], 'r': 'Ellos son'}
        ]
    },
    'U3': {
        'titulo': 'Couleurs et Vêtements',
        'preguntas': [
            {'p': '¿De qué color es el cielo?', 'o': ['Bleu', 'Rouge', 'Vert'], 'r': 'Bleu'},
            {'p': '¿Qué es "une jupe"?', 'o': ['Una falda', 'Un pantalón', 'Una camisa'], 'r': 'Une jupe'},
            {'p': 'El color "Jaune" es...', 'o': ['Amarillo', 'Blanco', 'Negro'], 'r': 'Amarillo'},
            {'p': '¿Cómo se dice "Rojo"?', 'o': ['Rouge', 'Rose', 'Rousse'], 'r': 'Rouge'},
            {'p': '¿Qué prenda es "un manteau"?', 'o': ['Un abrigo', 'Un zapato', 'Un gorro'], 'r': 'Un abrigo'},
            {'p': 'Color de la hierba:', 'o': ['Vert', 'Violet', 'Orange'], 'r': 'Vert'},
            {'p': '¿Qué son "des chaussures"?', 'o': ['Zapatos', 'Calcetines', 'Guantes'], 'r': 'Zapatos'},
            {'p': 'Blanco en francés:', 'o': ['Blanc', 'Noir', 'Gris'], 'r': 'Blanc'},
            {'p': '¿Qué es "un pull"?', 'o': ['Un jersey', 'Una gorra', 'Un bañador'], 'r': 'Un jersey'},
            {'p': 'Rosa en francés se dice:', 'o': ['Rose', 'Rouge', 'Roux'], 'r': 'Rose'}
        ]
    },
    'U4': {
        'titulo': 'La Classe (Objetos)',
        'preguntas': [
            {'p': '¿Qué es "un stylo"?', 'o': ['Bolígrafo', 'Lápiz', 'Goma'], 'r': 'Bolígrafo'},
            {'p': 'Mochila se dice...', 'o': ['Sac à dos', 'Trousse', 'Cahier'], 'r': 'Sac à dos'},
            {'p': '¿Qué guardas en "la trousse"?', 'o': ['Le crayon', 'Le lit', 'Le vélo'], 'r': 'Le crayon'},
            {'p': '¿Qué significa "une gomme"?', 'o': ['Una goma', 'Una regla', 'Un pegamento'], 'r': 'Una goma'},
            {'p': 'Libro se dice...', 'o': ['Livre', 'Cahier', 'Papier'], 'r': 'Livre'},
            {'p': '¿Qué es "une chaise"?', 'o': ['Una silla', 'Una mesa', 'Una pizarra'], 'r': 'Una silla'},
            {'p': 'Para escribir usamos...', 'o': ['Un crayon', 'Une fenêtre', 'Une porte'], 'r': 'Un crayon'},
            {'p': '¿Qué es "un tableau"?', 'o': ['Pizarra', 'Cuaderno', 'Sacapuntas'], 'r': 'Pizarra'},
            {'p': 'Cuaderno en francés:', 'o': ['Cahier', 'Classeur', 'Feuille'], 'r': 'Cahier'},
            {'p': '¿Dónde se sienta el alumno?', 'o': ['Sur la chaise', 'Sous la table', 'Dans le sac'], 'r': 'Sur la chaise'}
        ]
    },
    'U5': {
        'titulo': 'Jours et Mois (El tiempo)',
        'preguntas': [
            {'p': '¿Qué día es "Lundi"?', 'o': ['Lunes', 'Martes', 'Domingo'], 'r': 'Lunes'},
            {'p': '¿Cómo se dice Sábado?', 'o': ['Samedi', 'Dimanche', 'Vendredi'], 'r': 'Samedi'},
            {'p': '¿Cuál es el primer mes del año?', 'o': ['Janvier', 'Février', 'Mars'], 'r': 'Janvier'},
            {'p': 'Diciembre en francés:', 'o': ['Décembre', 'Novembre', 'Octobre'], 'r': 'Décembre'},
            {'p': '¿Qué significa "Demain"?', 'o': ['Mañana', 'Hoy', 'Ayer'], 'r': 'Mañana'},
            {'p': '¿Cómo se dice "Hoy"?', 'o': ['Aujourd’hui', 'Après', 'Avant'], 'r': 'Aujourd’hui'},
            {'p': 'Día después del miércoles:', 'o': ['Jeudi', 'Mardi', 'Samedi'], 'r': 'Jeudi'},
            {'p': 'Mes de las flores (Mayo):', 'o': ['Mai', 'Mars', 'Moi'], 'r': 'Mai'},
            {'p': '¿Qué mes es "Août"?', 'o': ['Agosto', 'Abril', 'Junio'], 'r': 'Agosto'},
            {'p': '¿Cuántos días tiene "une semaine"?', 'o': ['Sept', 'Six', 'Dix'], 'r': 'Sept'}
        ]
    },
    'U6': {
        'titulo': 'La Maison (Habitaciones)',
        'preguntas': [
            {'p': '¿Dónde dormimos?', 'o': ['La chambre', 'La cuisine', 'Le garage'], 'r': 'La chambre'},
            {'p': '¿Dónde se cocina?', 'o': ['La cuisine', 'Le salón', 'La douche'], 'r': 'La cuisine'},
            {'p': '¿Qué es "un lit"?', 'o': ['Una cama', 'Una mesa', 'Un armario'], 'r': 'Una cama'},
            {'p': 'Salón en francés:', 'o': ['Salon', 'Salle de séjour', 'Ambos'], 'r': 'Ambos'},
            {'p': '¿Dónde nos lavamos?', 'o': ['La salle de bains', 'Le jardin', 'Le grenier'], 'r': 'La salle de bains'},
            {'p': '¿Qué es "une fenêtre"?', 'o': ['Ventana', 'Puerta', 'Pared'], 'r': 'Ventana'},
            {'p': '¿Cómo se dice mesa?', 'o': ['Table', 'Tapis', 'Télé'], 'r': 'Table'},
            {'p': 'Jardín en francés:', 'o': ['Jardin', 'Forêt', 'Parc'], 'r': 'Jardin'},
            {'p': '¿Qué es "un escalier"?', 'o': ['Escalera', 'Espejo', 'Escritorio'], 'r': 'Escalera'},
            {'p': 'Puerta en francés:', 'o': ['Porte', 'Pont', 'Poste'], 'r': 'Porte'}
        ]
    },
    'U7': {
        'titulo': 'La Nourriture (Comida)',
        'preguntas': [
            {'p': '¿Qué es "le pain"?', 'o': ['Pan', 'Pino', 'Vino'], 'r': 'Pan'},
            {'p': 'Carne en francés:', 'o': ['Viande', 'Poisson', 'Poulet'], 'r': 'Viande'},
            {'p': '¿Cómo se dice leche?', 'o': ['Lait', 'Eau', 'Jus'], 'r': 'Lait'},
            {'p': '¿Qué significa "Le petit déjeuner"?', 'o': ['Desayuno', 'Comida', 'Cena'], 'r': 'Desayuno'},
            {'p': 'Queso en francés:', 'o': ['Fromage', 'Fraise', 'Frite'], 'r': 'Fromage'},
            {'p': '¿Qué es "un œuf"?', 'o': ['Un huevo', 'Un ojo', 'Un buey'], 'r': 'Un huevo'},
            {'p': 'Pescado en francés:', 'o': ['Poisson', 'Poison', 'Boisson'], 'r': 'Poisson'},
            {'p': '¿Qué significa "Manger"?', 'o': ['Comer', 'Beber', 'Cantar'], 'r': 'Comer'},
            {'p': 'Agua en francés:', 'o': ['Eau', 'Lait', 'Vin'], 'r': 'Eau'},
            {'p': '¿Qué son "des frites"?', 'o': ['Patatas fritas', 'Frutas', 'Flanes'], 'r': 'Patatas fritas'}
        ]
    },
    'U8': {
        'titulo': 'Le Marché (Frutas y Números)',
        'preguntas': [
            {'p': '¿Qué es "une pomme"?', 'o': ['Manzana', 'Pera', 'Plátano'], 'r': 'Manzana'},
            {'p': 'Fresa en francés:', 'o': ['Fraise', 'Framboise', 'Fruit'], 'r': 'Fraise'},
            {'p': '¿Cómo se dice plátano?', 'o': ['Banane', 'Ananas', 'Orange'], 'r': 'Banane'},
            {'p': 'Número 30:', 'o': ['Trente', 'Treize', 'Trance'], 'r': 'Trente'},
            {'p': 'Número 50:', 'o': ['Cinquante', 'Cinq', 'Quinze'], 'r': 'Cinquante'},
            {'p': '¿Qué es "une orange"?', 'o': ['Naranja', 'Oreja', 'Oveja'], 'r': 'Naranja'},
            {'p': '¿Cómo se dice 100?', 'o': ['Cent', 'Sang', 'Sans'], 'r': 'Cent'},
            {'p': 'Pera en francés:', 'o': ['Poire', 'Pomme', 'Pêche'], 'r': 'Poire'},
            {'p': '¿Qué es "le marché"?', 'o': ['El mercado', 'La marcha', 'El martes'], 'r': 'El mercado'},
            {'p': 'Número 40:', 'o': ['Quarante', 'Quatorze', 'Cinquante'], 'r': 'Quarante'}
        ]
    }
}

def iniciar_examen(message, bot, unidad_id):
    """Lógica para enviar las preguntas al usuario"""
    unidad = TEMARIO.get(unidad_id)
    preguntas = random.sample(unidad['preguntas'], 10) # Siempre 10 preguntas aleatorias
    
    for idx, p in enumerate(preguntas):
        markup = types.InlineKeyboardMarkup()
        botones = [types.InlineKeyboardButton(opt, callback_data=f"r_{'ok' if opt == p['r'] else 'no'}") for opt in p['o']]
        markup.add(*botones)
        bot.send_message(message.chat.id, f"Pregunta {idx+1}: {p['p']}", reply_markup=markup)
