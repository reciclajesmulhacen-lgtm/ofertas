import random

# TEMARIO COMPLETO (8 UNIDADES con 3 exámenes cada una)
TEMARIO = {
    'U1': {
        'titulo': 'Bonjour! (Saludos y Números)',
        'examenes': [
            [ # Examen 1
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
            ],
            [ # Examen 2
                {'p': '¿Cómo saludas por la mañana?', 'o': ['Bonjour', 'Bonsoir', 'Salut'], 'r': 'Bonjour'},
                {'p': '¿Qué significa "Au revoir"?', 'o': ['Adiós', 'Hola', 'Gracias'], 'r': 'Adiós'},
                {'p': '¿Qué número es "dix"?', 'o': ['10', '12', '1'], 'r': '10'},
                {'p': 'Cómo se escribe el número 5?', 'o': ['Cinq', 'Six', 'Sept'], 'r': 'Cinq'},
                {'p': '¿Cómo preguntas "¿Cómo te llamas?"', 'o': ['Comment tu t’appelles ?', 'Quel âge as-tu ?', 'Ça va ?'], 'r': 'Comment tu t’appelles ?'},
                {'p': '¿Qué significa "Merci"?', 'o': ['Gracias', 'De nada', 'Por favor'], 'r': 'Gracias'},
                {'p': '¿Qué número es "treize"?', 'o': ['13', '12', '3'], 'r': '13'},
                {'p': '¿Cómo se dice "Sí"?', 'o': ['Oui', 'Non', 'Salut'], 'r': 'Oui'},
                {'p': 'Número 1:', 'o': ['Un', 'Deux', 'Trois'], 'r': 'Un'},
                {'p': '¿Qué es "Madame"?', 'o': ['Señora', 'Señorita', 'Señor'], 'r': 'Señora'}
            ],
            [ # Examen 3
                {'p': '¿Cómo se dice "No"?', 'o': ['Non', 'Oui', 'Salut'], 'r': 'Non'},
                {'p': 'Número 2:', 'o': ['Deux', 'Trois', 'Un'], 'r': 'Deux'},
                {'p': '¿Qué significa "S’il vous plaît"?', 'o': ['Por favor', 'Gracias', 'De nada'], 'r': 'Por favor'},
                {'p': 'Número 3:', 'o': ['Trois', 'Quatre', 'Cinq'], 'r': 'Trois'},
                {'p': '¿Qué significa "À bientôt"?', 'o': ['Hasta pronto', 'Hasta luego', 'Adiós'], 'r': 'Hasta pronto'},
                {'p': 'Número 4:', 'o': ['Quatre', 'Cinq', 'Trois'], 'r': 'Quatre'},
                {'p': '¿Qué número es "sept"?', 'o': ['7', '8', '6'], 'r': '7'},
                {'p': '¿Qué número es "neuf"?', 'o': ['9', '8', '10'], 'r': '9'},
                {'p': '¿Qué número es "onze"?', 'o': ['11', '10', '12'], 'r': '11'},
                {'p': '¿Qué significa "De rien"?', 'o': ['De nada', 'Gracias', 'Por favor'], 'r': 'De nada'}
            ]
        ]
    },
    'U2': { # ... (Continúa con la estructura de examenes [ [], [], [] ] para U2 a U8)
        'titulo': 'Ma famille (Être/Avoir)',
        'examenes': [
            [ # Examen 1
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
            ],
            [], # Examen 2 vacío
            []  # Examen 3 vacío
        ]
    },
    'U3': { # ... (U3 a U8 solo con Examen 1 lleno por brevedad)
        'titulo': 'Couleurs et Vêtements',
         'examenes': [
            [{'p': '¿De qué color es el cielo?', 'o': ['Bleu', 'Rouge'], 'r': 'Bleu'}, {'p': '¿Qué es "une jupe"?', 'o': ['Una falda', 'Un pantalón'], 'r': 'Una falda'}, {'p': 'El color "Jaune" es...', 'o': ['Amarillo', 'Blanco'], 'r': 'Amarillo'}, {'p': '¿Cómo se dice "Rojo"?', 'o': ['Rouge', 'Rose'], 'r': 'Rouge'}, {'p': '¿Qué prenda es "un manteau"?', 'o': ['Un abrigo', 'Un zapato'], 'r': 'Un abrigo'}, {'p': 'Color de la hierba:', 'o': ['Vert', 'Violet'], 'r': 'Vert'}, {'p': '¿Qué son "des chaussures"?', 'o': ['Zapatos', 'Calcetines'], 'r': 'Zapatos'}, {'p': 'Blanco en francés:', 'o': ['Blanc', 'Noir'], 'r': 'Blanc'}, {'p': '¿Qué es "un pull"?', 'o': ['Un jersey', 'Una gorra'], 'r': 'Un jersey'}, {'p': 'Rosa en francés se dice:', 'o': ['Rose', 'Rouge'], 'r': 'Rose'}],
            [],[]
         ]
    },
    'U4': {
        'titulo': 'La Classe (Objetos)',
        'examenes': [
            [{'p': '¿Qué es "un stylo"?', 'o': ['Bolígrafo', 'Lápiz'], 'r': 'Bolígrafo'}, {'p': 'Mochila se dice...', 'o': ['Sac à dos', 'Trousse'], 'r': 'Sac à dos'}, {'p': '¿Qué guardas en "la trousse"?', 'o': ['Le crayon', 'Le lit'], 'r': 'Le crayon'}, {'p': '¿Qué significa "une gomme"?', 'o': ['Una goma', 'Una regla'], 'r': 'Una goma'}, {'p': 'Libro se dice...', 'o': ['Livre', 'Cahier'], 'r': 'Livre'}, {'p': '¿Qué es "une chaise"?', 'o': ['Una silla', 'Una mesa'], 'r': 'Una silla'}, {'p': 'Para escribir usamos...', 'o': ['Un crayon', 'Une fenêtre'], 'r': 'Un crayon'}, {'p': '¿Qué es "un tableau"?', 'o': ['Pizarra', 'Cuaderno'], 'r': 'Pizarra'}, {'p': 'Cuaderno en francés:', 'o': ['Cahier', 'Classeur'], 'r': 'Cahier'}, {'p': '¿Dónde se sienta el alumno?', 'o': ['Sur la chaise', 'Sous la table'], 'r': 'Sur la chaise'}],
            [],[]
        ]
    },
    'U5': {
        'titulo': 'Jours et Mois (El tiempo)',
        'examenes': [
            [{'p': '¿Qué día es "Lundi"?', 'o': ['Lunes', 'Martes'], 'r': 'Lunes'}, {'p': '¿Cómo se dice Sábado?', 'o': ['Samedi', 'Dimanche'], 'r': 'Samedi'}, {'p': '¿Cuál es el primer mes del año?', 'o': ['Janvier', 'Février'], 'r': 'Janvier'}, {'p': 'Diciembre en francés:', 'o': ['Décembre', 'Novembre'], 'r': 'Décembre'}, {'p': '¿Qué significa "Demain"?', 'o': ['Mañana', 'Hoy'], 'r': 'Mañana'}, {'p': '¿Cómo se dice "Hoy"?', 'o': ['Aujourd’hui', 'Après'], 'r': 'Aujourd’hui'}, {'p': 'Día después del miércoles:', 'o': ['Jeudi', 'Mardi'], 'r': 'Jeudi'}, {'p': 'Mes de las flores (Mayo):', 'o': ['Mai', 'Mars'], 'r': 'Mai'}, {'p': '¿Qué mes es "Août"?', 'o': ['Agosto', 'Abril'], 'r': 'Agosto'}, {'p': '¿Cuántos días tiene "une semaine"?', 'o': ['Sept', 'Six'], 'r': 'Sept'}],
            [],[]
        ]
    },
    'U6': {
        'titulo': 'La Maison (Habitaciones)',
        'examenes': [
            [{'p': '¿Dónde dormimos?', 'o': ['La chambre', 'La cuisine'], 'r': 'La chambre'}, {'p': '¿Dónde se cocina?', 'o': ['La cuisine', 'Le salón'], 'r': 'La cuisine'}, {'p': '¿Qué es "un lit"?', 'o': ['Una cama', 'Una mesa'], 'r': 'Una cama'}, {'p': 'Salón en francés:', 'o': ['Salon', 'Salle de séjour'], 'r': 'Salon'}, {'p': '¿Dónde nos lavamos?', 'o': ['La salle de bains', 'Le jardin'], 'r': 'La salle de bains'}, {'p': '¿Qué es "une fenêtre"?', 'o': ['Ventana', 'Puerta'], 'r': 'Ventana'}, {'p': '¿Cómo se dice mesa?', 'o': ['Table', 'Tapis'], 'r': 'Table'}, {'p': 'Jardín en francés:', 'o': ['Jardin', 'Forêt'], 'r': 'Jardin'}, {'p': '¿Qué es "un escalier"?', 'o': ['Escalera', 'Espejo'], 'r': 'Escalera'}, {'p': 'Puerta en francés:', 'o': ['Porte', 'Pont'], 'r': 'Porte'}],
            [],[]
        ]
    },
    'U7': {
        'titulo': 'La Nourriture (Comida)',
        'examenes': [
            [{'p': '¿Qué es "le pain"?', 'o': ['Pan', 'Pino'], 'r': 'Pan'}, {'p': 'Carne en francés:', 'o': ['Viande', 'Poisson'], 'r': 'Viande'}, {'p': '¿Cómo se dice leche?', 'o': ['Lait', 'Eau'], 'r': 'Lait'}, {'p': '¿Qué significa "Le petit déjeuner"?', 'o': ['Desayuno', 'Comida'], 'r': 'Desayuno'}, {'p': 'Queso en francés:', 'o': ['Fromage', 'Fraise'], 'r': 'Fromage'}, {'p': '¿Qué es "un œuf"?', 'o': ['Un huevo', 'Un ojo'], 'r': 'Un huevo'}, {'p': 'Pescado en francés:', 'o': ['Poisson', 'Poison'], 'r': 'Poisson'}, {'p': '¿Qué significa "Manger"?', 'o': ['Comer', 'Beber'], 'r': 'Comer'}, {'p': 'Agua en francés:', 'o': ['Eau', 'Lait'], 'r': 'Eau'}, {'p': '¿Qué son "des frites"?', 'o': ['Patatas fritas', 'Frutas'], 'r': 'Patatas fritas'}],
            [],[]
        ]
    },
    'U8': {
        'titulo': 'Le Marché (Frutas y Números)',
        'examenes': [
            [{'p': '¿Qué es "une pomme"?', 'o': ['Manzana', 'Pera'], 'r': 'Manzana'}, {'p': 'Fresa en francés:', 'o': ['Fraise', 'Framboise'], 'r': 'Fraise'}, {'p': '¿Cómo se dice plátano?', 'o': ['Banane', 'Ananas'], 'r': 'Banane'}, {'p': 'Número 30:', 'o': ['Trente', 'Treize'], 'r': 'Trente'}, {'p': 'Número 50:', 'o': ['Cinquante', 'Cinq'], 'r': 'Cinquante'}, {'p': '¿Qué es "une orange"?', 'o': ['Naranja', 'Oreja'], 'r': 'Naranja'}, {'p': '¿Cómo se dice 100?', 'o': ['Cent', 'Sang'], 'r': 'Cent'}, {'p': 'Pera en francés:', 'o': ['Poire', 'Pomme'], 'r': 'Poire'}, {'p': '¿Qué es "le marché"?', 'o': ['El mercado', 'La marcha'], 'r': 'El mercado'}, {'p': 'Número 40:', 'o': ['Quarante', 'Quatorze'], 'r': 'Quarante'}],
            [],[]
        ]
    }
}
