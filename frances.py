# frances.py - Difusión Clic Clac 1

TEMARIO = {
    'U1': {
        'titulo': 'Bonjour! (Saludos, presentación, números 1-20)',
        'examenes': [
            [
                {'p': '¿Cómo se dice "Hola"?', 'o': ['Bonjour', 'Au revoir', 'Salut'], 'r': 'Bonjour'},
                {'p': '¿Cómo se dice "Adiós"?', 'o': ['Au revoir', 'Bonjour', 'Merci'], 'r': 'Au revoir'},
                {'p': '"Je m'appelle Ana" significa:', 'o': ['Me llamo Ana', 'Tengo 10 años', '¿Cómo te llamas?'], 'r': 'Me llamo Ana'},
                {'p': 'Número 5 en francés:', 'o': ['cinq', 'six', 'quatre'], 'r': 'cinq'},
                {'p': '¿Cómo se dice " informal hola"?', 'o': ['Salut', 'Bonjour', 'Au revoir'], 'r': 'Salut'},
                {'p': '"Comment t'appelles-tu?" significa:', 'o': ['¿Cómo te llamas?', '¿Cuántos años tienes?', 'Adiós'], 'r': '¿Cómo te llamas?'},
                {'p': 'Número 10:', 'o': ['dix', 'neuf', 'onze'], 'r': 'dix'},
                {'p': '¿Cómo se dice "Gracias"?', 'o': ['Merci', 'S'il vous plaît', 'De rien'], 'r': 'Merci'},
                {'p': 'Número 3:', 'o': ['trois', 'deux', 'quatre'], 'r': 'trois'},
                {'p': '"Bonjour, je m'appelle Paul" es:', 'o': ['Hola, me llamo Paul', 'Adiós, tengo 10 años', 'Hola, ¿cómo estás?'], 'r': 'Hola, me llamo Paul'}
            ],
            [
                {'p': 'Número 15:', 'o': ['quinze', 'seize', 'quatorze'], 'r': 'quinze'},
                {'p': '"Au revoir!" significa:', 'o': ['¡Hasta luego!', '¡Hola!', '¡Gracias!'], 'r': '¡Hasta luego!'},
                {'p': '¿Cómo se dice "¿Cómo estás?"', 'o': ['Comment ça va?', 'Comment t'appelles-tu?', 'J"ai dix ans'], 'r': 'Comment ça va?'},
                {'p': 'Número 7:', 'o': ['sept', 'six', 'huit'], 'r': 'sept'},
                {'p': '"Salut!" es saludo:', 'o': ['Informal', 'Formal', 'De despedida'], 'r': 'Informal'},
                {'p': 'Número 12:', 'o': ['douze', 'onze', 'treize'], 'r': 'douze'},
                {'p': '"De rien" significa:', 'o': ['De nada', 'Por favor', 'Gracias'], 'r': 'De nada'},
                {'p': 'Número 1:', 'o': ['un', 'deux', 'une'], 'r': 'un'},
                {'p': '"S"il vous plaît" es:', 'o': ['Por favor', 'Gracias', 'Adiós'], 'r': 'Por favor'},
                {'p': 'Número 20:', 'o': ['vingt', 'dix-neuf', 'vingt-et-un'], 'r': 'vingt'}
            ],
            [
                {'p': 'Completa: "Bonjour, ___ m'appelle Marie"', 'o': ['je', 'tu', 'il'], 'r': 'je'},
                {'p': 'Número 8:', 'o': ['huit', 'sept', 'neuf'], 'r': 'huit'},
                {'p': '"Comment allez-vous?" es saludo:', 'o': ['Formal', 'Informal', 'De noche'], 'r': 'Formal'},
                {'p': 'Número 16:', 'o': ['seize', 'quinze', 'dix-sept'], 'r': 'seize'},
                {'p': '"À bientôt!" significa:', 'o': ['¡Hasta pronto!', '¡Hola!', '¡Adiós!'], 'r': '¡Hasta pronto!'},
                {'p': 'Número 4:', 'o': ['quatre', 'cinq', 'trois'], 'r': 'quatre'},
                {'p': '"Pardon" se usa para:', 'o': ['Disculpar', 'Saludar', 'Despedir'], 'r': 'Disculpar'},
                {'p': 'Número 18:', 'o': ['dix-huit', 'dix-sept', 'dix-neuf'], 'r': 'dix-huit'},
                {'p': 'Saludo de noche:', 'o': ['Bonsoir', 'Bonjour', 'Bonne nuit'], 'r': 'Bonsoir'},
                {'p': 'Número 2:', 'o': ['deux', 'un', 'trois'], 'r': 'deux'}
            ]
        ]
    },

    'U2': {
        'titulo': 'Ma famille (Être/avoir, edades, nacionalidad)',
        'examenes': [
            [
                {'p': 'Verbo ÊTRE: "Yo ___ español"', 'o': ['suis', 'es', 'ai'], 'r': 'suis'},
                {'p': '"Tengo 10 años" es:', 'o': ['J"ai dix ans', 'Je suis dix ans', 'J"ai dix'], 'r': 'J"ai dix ans'},
                {'p': '"Mi madre" es:', 'o': ['ma mère', 'mon père', 'ma soeur'], 'r': 'ma mère'},
                {'p': 'Verbo AVOIR: "Tú ___ un frère"', 'o': ['as', 'ai', 'a'], 'r': 'as'},
                {'p': '"Soy francés" es:', 'o': ['Je suis français', 'J"ai français', 'Je français'], 'r': 'Je suis français'},
                {'p': '"Mi hermano" es:', 'o': ['mon frère', 'ma soeur', 'mon père'], 'r': 'mon frère'},
                {'p': 'Verbo ÊTRE: "Ellos ___ content"', 'o': ['sont', 'es', 'ai'], 'r': 'sont'},
                {'p': '"Tengo 12 años": J"___ douze ans"', 'o': ['ai', 'suis', 'es'], 'r': 'ai'},
                {'p': '"Española" (femenino):', 'o': ['espagnole', 'espagnol', 'espagne'], 'r': 'espagnole'},
                {'p': '"Mi padre" es:', 'o': ['mon père', 'ma mère', 'mon frère'], 'r': 'mon père'}
            ],
            [
                {'p': 'Verbo ÊTRE: "Tú ___ petite"', 'o': ['es', 'suis', 'sommes'], 'r': 'es'},
                {'p': '"Mi hermana" es:', 'o': ['ma soeur', 'mon frère', 'mon père'], 'r': 'ma soeur'},
                {'p': 'Verbo AVOIR: "Él ___ un chat"', 'o': ['a', 'ai', 'as'], 'r': 'a'},
                {'p': '"Tengo 8 años": J"___ huit ans"', 'o': ['ai', 'suis', 'es'], 'r': 'ai'},
                {'p': '"Soy andaluz": Je ___ andalou"', 'o': ['suis', 'ai', 'es'], 'r': 'suis'},
                {'p': 'Verbo ÊTRE: "Nosotros ___ étudiants"', 'o': ['sommes', 'suis', 'es'], 'r': 'sommes'},
                {'p': '"Mi abuelo" es:', 'o': ['mon grand-père', 'ma grand-mère', 'mon cousin'], 'r': 'mon grand-père'},
                {'p': 'Verbo AVOIR: "Nosotros ___ des chiens"', 'o': ['avons', 'ai', 'as'], 'r': 'avons'},
                {'p': '"Tengo 15 años": J"___ quinze ans"', 'o': ['ai', 'suis', 'es'], 'r': 'ai'},
                {'p': '"Granadina" (femenino):', 'o': ['granadine', 'granadin', 'granada'], 'r': 'granadine'}
            ],
            [
                {'p': 'Verbo ÊTRE: "Ella ___ grande"', 'o': ['est', 'suis', 'sommes'], 'r': 'est'},
                {'p': '"Mi primo" es:', 'o': ['mon cousin', 'ma cousine', 'mon oncle'], 'r': 'mon cousin'},
                {'p': '"Soy de Alfacar": Je ___ d"Alfacar"', 'o': ['suis', 'ai', 'es'], 'r': 'suis'},
                {'p': 'Verbo AVOIR: "Ellos ___ des livres"', 'o': ['ont', 'ai', 'as'], 'r': 'ont'},
                {'p': '"Mi abuela" es:', 'o': ['ma grand-mère', 'mon grand-père', 'ma tante'], 'r': 'ma grand-mère'},
                {'p': 'Verbo ÊTRE: "Vosotros ___ contents"', 'o': ['êtes', 'suis', 'sommes'], 'r': 'êtes'},
                {'p': '"Tengo 11 años": J"___ onze ans"', 'o': ['ai', 'suis', 'es'], 'r': 'ai'},
                {'p': '"Mi tío" es:', 'o': ['mon oncle', 'ma tante', 'mon père'], 'r': 'mon oncle'},
                {'p': 'Verbo AVOIR: "Ella ___ neuf ans"', 'o': ['a', 'ai', 'as'], 'r': 'a'},
                {'p': '"Soy del colegio Las Encinas": Je ___ du collège Las Encinas"', 'o': ['suis', 'ai', 'es'], 'r': 'suis'}
            ]
        ]
    },

    'U3': {
        'titulo': 'Couleurs (Colores, ropa básica)',
        'examenes': [
            [
                {'p': 'Rojo en francés:', 'o': ['rouge', 'bleu', 'vert'], 'r': 'rouge'},
                {'p': '"T-shirt" es:', 'o': ['un tee-shirt', 'un pantalon', 'une chemise'], 'r': 'un tee-shirt'},
                {'p': 'Azul:', 'o': ['bleu', 'jaune', 'rouge'], 'r': 'bleu'},
                {'p': 'Verde:', 'o': ['vert', 'violet', 'orange'], 'r': 'vert'},
                {'p': '"Pantalón":', 'o': ['un pantalon', 'une jupe', 'un pull'], 'r': 'un pantalon'},
                {'p': 'Amarillo:', 'o': ['jaune', 'blanc', 'noir'], 'r': 'jaune'},
                {'p': 'Naranja:', 'o': ['orange', 'rose', 'gris'], 'r': 'orange'},
                {'p': '"Falda":', 'o': ['une jupe', 'un short', 'une robe'], 'r': 'une jupe'},
                {'p': 'Blanco:', 'o': ['blanc', 'noir', 'marron'], 'r': 'blanc'},
                {'p': 'Negro:', 'o': ['noir', 'rouge', 'bleu'], 'r': 'noir'}
            ],
            [
                {'p': 'Rosa:', 'o': ['rose', 'violet', 'vert'], 'r': 'rose'},
                {'p': '"Camisa":', 'o': ['une chemise', 'un pull', 'un manteau'], 'r': 'une chemise'},
                {'p': 'Marrón:', 'o': ['marron', 'jaune', 'gris'], 'r': 'marron'},
                {'p': '"Jersey":', 'o': ['un pull', 'une écharpe', 'un chapeau'], 'r': 'un pull'},
                {'p': 'Gris:', 'o': ['gris', 'blanc', 'noir'], 'r': 'gris'},
                {'p': 'Morado:', 'o': ['violet', 'rose', 'orange'], 'r': 'violet'},
                {'p': '"Vestido":', 'o': ['une robe', 'un jean', 'une jupe'], 'r': 'une robe'},
                {'p': '"Zapatos":', 'o': ['des chaussures', 'un chapeau', 'une écharpe'], 'r': 'des chaussures'},
                {'p': '"Sombrero":', 'o': ['un chapeau', 'une casquette', 'des lunettes'], 'r': 'un chapeau'},
                {'p': '"Calcetines":', 'o': ['des chaussettes', 'des gants', 'une ceinture'], 'r': 'des chaussettes'}
            ],
            [
                {'p': '"Bufanda":', 'o': ['une écharpe', 'un pull', 'une chemise'], 'r': 'une écharpe'},
                {'p': 'Colores primarios:', 'o': ['rouge, jaune, bleu', 'vert, orange, violet', 'blanc, noir, gris'], 'r': 'rouge, jaune, bleu'},
                {'p': '"Vaqueros":', 'o': ['un jean', 'une jupe', 'un short'], 'r': 'un jean'},
                {'p': '"Guantes":', 'o': ['des gants', 'des chaussettes', 'une écharpe'], 'r': 'des gants'},
                {'p': '"Tengo una camiseta roja": J"ai un tee-shirt ___"', 'o': ['rouge', 'bleu', 'vert'], 'r': 'rouge'},
                {'p': '"Gafas":', 'o': ['des lunettes', 'un chapeau', 'des chaussures'], 'r': 'des lunettes'},
                {'p': '"Tengo un jersey azul": J"ai un pull ___"', 'o': ['bleu', 'rouge', 'jaune'], 'r': 'bleu'},
                {'p': '"Cinturón":', 'o': ['une ceinture', 'une écharpe', 'des gants'], 'r': 'une ceinture'},
                {'p': 'Colores compuestos ejemplo:', 'o': ['orange, violet, marron', 'rouge, bleu, jaune', 'blanc, noir'], 'r': 'orange, violet, marron'},
                {'p': '"Tengo pantalones negros": J"ai un pantalon ___"', 'o': ['noir', 'blanc', 'vert'], 'r': 'noir'}
            ]
        ]
    },

    'U4': {
        'titulo': 'Classe (Objetos escolares, preposiciones)',
        'examenes': [
            [
                {'p': '"Cuaderno":', 'o': ['un cahier', 'un livre', 'un stylo'], 'r': 'un cahier'},
                {'p': 'El libro está ___ la mesa (encima):', 'o': ['sur', 'dans', 'sous'], 'r': 'sur'},
                {'p': '"Lápiz":', 'o': ['un crayon', 'une gomme', 'un taille-crayon'], 'r': 'un crayon'},
                {'p': 'La silla está ___ la mesa (debajo):', 'o': ['sous', 'sur', 'devant'], 'r': 'sous'},
                {'p': '"Regla":', 'o': ['une règle', 'un cahier', 'un stylo'], 'r': 'une règle'},
                {'p': '"El boli está ___ el estuche" (dentro):', 'o': ['dans', 'sur', 'derrière'], 'r': 'dans'},
                {'p': '"Borrador":', 'o': ['une gomme', 'un crayon', 'une règle'], 'r': 'une gomme'},
                {'p': '"La pizarra está ___ la clase" (frente):', 'o': ['devant', 'dans', 'sous'], 'r': 'devant'},
                {'p': '"Sacapuntas":', 'o': ['un taille-crayon', 'un cahier', 'une gomme'], 'r': 'un taille-crayon'},
                {'p': '"La silla está ___ la mesa" (detrás):', 'o': ['derrière', 'sur', 'dans'], 'r': 'derrière'}
            ],
            [
                {'p': '"Libro":', 'o': ['un livre', 'un cahier', 'un stylo'], 'r': 'un livre'},
                {'p': '"El pupitre está ___ la pared" (al lado):', 'o': ['à côté de', 'sur', 'sous'], 'r': 'à côté de'},
                {'p': '"Pegamento":', 'o': ['de la colle', 'un crayon', 'une règle'], 'r': 'de la colle'},
                {'p': '"La mochila está ___ el suelo" (encima):', 'o': ['sur', 'sous', 'dans'], 'r': 'sur'},
                {'p': '"Calculadora":', 'o': ['une calculatrice', 'un cahier', 'un taille-crayon'], 'r': 'une calculatrice'},
                {'p': '"El profesor está ___ los alumnos" (frente):', 'o': ['devant', 'derrière', 'à côté de'], 'r': 'devant'},
                {'p': '"Carpeta":', 'o': ['une pochette', 'un livre', 'une gomme'], 'r': 'une pochette'},
                {'p': '"Los libros están ___ la estantería" (dentro):', 'o': ['dans', 'sur', 'sous'], 'r': 'dans'},
                {'p': '"Compás":', 'o': ['un compas', 'une règle', 'un crayon'], 'r': 'un compas'},
                {'p': '"La ventana está ___ la clase" (al lado):', 'o': ['à côté de', 'devant', 'derrière'], 'r': 'à côté de'}
            ],
            [
                {'p': '"Diccionario":', 'o': ['un dictionnaire', 'un cahier', 'une calculatrice'], 'r': 'un dictionnaire'},
                {'p': '"El gato está ___ la silla" (encima):', 'o': ['sur', 'sous', 'dans'], 'r': 'sur'},
                {'p': '"Goma de borrar":', 'o': ['une gomme', 'un stylo', 'une règle'], 'r': 'une gomme'},
                {'p': '"La puerta está ___ la clase" (detrás):', 'o': ['derrière', 'devant', 'à côté de'], 'r': 'derrière'},
                {'p': '"Atlas":', 'o': ['un atlas', 'un livre', 'un cahier'], 'r': 'un atlas'},
                {'p': '"Los lápices están ___ la caja" (dentro):', 'o': ['dans', 'sur', 'sous'], 'r': 'dans'},
                {'p': '"Tijeras":', 'o': ['des ciseaux', 'une règle', 'un crayon'], 'r': 'des ciseaux'},
                {'p': '"El reloj está ___ la pared" (encima):', 'o': ['sur', 'dans', 'sous'], 'r': 'sur'},
                {'p': '"Pupitre":', 'o': ['un pupitre', 'une chaise', 'un tableau'], 'r': 'un pupitre'},
                {'p': '"La silla está ___ el profesor" (al lado):', 'o': ['à côté de', 'devant', 'derrière'], 'r': 'à côté de'}
            ]
        ]
    },

    'U5': {
        'titulo': 'Jours/mois (Días, meses, fecha)',
        'examenes': [
            [
                {'p': 'Lunes:', 'o': ['lundi', 'mardi', 'mercredi'], 'r': 'lundi'},
                {'p': 'Enero:', 'o': ['janvier', 'février', 'mars'], 'r': 'janvier'},
                {'p': '"Hoy es lunes": Aujourd"hui, c"est ___', 'o': ['lundi', 'mardi', 'jeudi'], 'r': 'lundi'},
                {'p': 'Martes:', 'o': ['mardi', 'lundi', 'mercredi'], 'r': 'mardi'},
                {'p': 'Marzo:', 'o': ['mars', 'avril', 'mai'], 'r': 'mars'},
                {'p': 'Miércoles:', 'o': ['mercredi', 'jeudi', 'vendredi'], 'r': 'mercredi'},
                {'p': 'Mayo:', 'o': ['mai', 'juin', 'juillet'], 'r': 'mai'},
                {'p': '"¿Qué día es hoy?": Quel jour ___-t-on?', 'o': ['on est', 'on a', 'on va'], 'r': 'on est'},
                {'p': 'Jueves:', 'o': ['jeudi', 'mercredi', 'samedi'], 'r': 'jeudi'},
                {'p': '"Es 15 de febrero": On est le ___ février', 'o': ['quinze', 'seize', 'quatorze'], 'r': 'quinze'}
            ],
            [
                {'p': 'Viernes:', 'o': ['vendredi', 'jeudi', 'samedi'], 'r': 'vendredi'},
                {'p': 'Junio:', 'o': ['juin', 'juillet', 'août'], 'r': 'juin'},
                {'p': 'Sábado:', 'o': ['samedi', 'dimanche', 'vendredi'], 'r': 'samedi'},
                {'p': 'Agosto:', 'o': ['août', 'septembre', 'octobre'], 'r': 'août'},
                {'p': 'Domingo:', 'o': ['dimanche', 'samedi', 'lundi'], 'r': 'dimanche'},
                {'p': 'Noviembre:', 'o': ['novembre', 'octobre', 'décembre'], 'r': 'novembre'},
                {'p': '"Hoy es miércoles": Aujourd"hui on est ___', 'o': ['mercredi', 'mardi', 'jeudi'], 'r': 'mercredi'},
                {'p': '"Es 5 de mayo": C"est le ___ mai', 'o': ['cinq', 'six', 'quatre'], 'r': 'cinq'},
                {'p': '"¿Qué mes es?": On est en ___?', 'o': ['quel mois', 'quel jour', 'quelle date'], 'r': 'quel mois'},
                {'p': 'Diciembre:', 'o': ['décembre', 'novembre', 'janvier'], 'r': 'décembre'}
            ],
            [
                {'p': '"Es lunes 10": Lundi ___', 'o': ['dix', 'onze', 'douze'], 'r': 'dix'},
                {'p': 'Abril:', 'o': ['avril', 'mars', 'mai'], 'r': 'avril'},
                {'p': '"¿Qué fecha es hoy?": Quelle ___ est-on?', 'o': ['date', 'jour', 'mois'], 'r': 'date'},
                {'p': 'Julio:', 'o': ['juillet', 'juin', 'août'], 'r': 'juillet'},
                {'p': '"Hoy es viernes 20": Aujourd"hui c"est vendredi ___', 'o': ['vingt', 'dix-neuf', 'vingt-et-un'], 'r': 'vingt'},
                {'p': 'Octubre:', 'o': ['octobre', 'septembre', 'novembre'], 'r': 'octobre'},
                {'p': 'Septiembre:', 'o': ['septembre', 'août', 'octobre'], 'r': 'septembre'},
                {'p': '"Es 3 de marzo": Le ___ mars', 'o': ['trois', 'deux', 'quatre'], 'r': 'trois'},
                {'p': '"Fin de semana":', 'o': ['samedi et dimanche', 'lundi et mardi', 'mercredi et jeudi'], 'r': 'samedi et dimanche'},
                {'p': '"Es 25 de diciembre": Le vingt-cinq ___', 'o': ['décembre', 'novembre', 'octobre'], 'r': 'décembre'}
            ]
        ]
    },

    'U6': {
        'titulo': 'Maison (Habitaciones, muebles)',
        'examenes': [
            [
                {'p': '"Habitaciones":', 'o': ['la chambre, la cuisine', 'la rue, la ville', 'l"école, la classe'], 'r': 'la chambre, la cuisine'},
                {'p': '"Cama":', 'o': ['un lit', 'une chaise', 'une table'], 'r': 'un lit'},
                {'p': '"Cocina":', 'o': ['la cuisine', 'la chambre', 'la salle de bain'], 'r': 'la cuisine'},
                {'p': '"Silla":', 'o': ['une chaise', 'un lit', 'un canapé'], 'r': 'une chaise'},
                {'p': '"Baño":', 'o': ['la salle de bain', 'la cuisine', 'le salon'], 'r': 'la salle de bain'},
                {'p': '"Mesa":', 'o': ['une table', 'une chaise', 'un lit'], 'r': 'une table'},
                {'p': '"Salón/comedor":', 'o': ['le salon', 'la chambre', 'la cuisine'], 'r': 'le salon'},
                {'p': '"Sofá":', 'o': ['un canapé', 'une chaise', 'un lit'], 'r': 'un canapé'},
                {'p': '"Dormitorio":', 'o': ['la chambre', 'la salle de bain', 'la cuisine'], 'r': 'la chambre'},
                {'p': '"Armario":', 'o': ['une armoire', 'une table', 'un canapé'], 'r': 'une armoire'}
            ],
            [
                {'p': '"Lavabo":', 'o': ['un lavabo', 'une baignoire', 'une douche'], 'r': 'un lavabo'},
                {'p': '"Comedor":', 'o': ['la salle à manger', 'la chambre', 'la cuisine'], 'r': 'la salle à manger'},
                {'p': '"Lámpara":', 'o': ['une lampe', 'une table', 'une chaise'], 'r': 'une lampe'},
                {'p': '"Nevera":', 'o': ['un frigo', 'un four', 'un micro-ondes'], 'r': 'un frigo'},
                {'p': '"Cuadro":', 'o': ['un tableau', 'une lampe', 'un tapis'], 'r': 'un tableau'},
                {'p': '"Alfombra":', 'o': ['un tapis', 'une chaise', 'une table'], 'r': 'un tapis'},
                {'p': '"Pasillo":', 'o': ['le couloir', 'la chambre', 'le salon'], 'r': 'le couloir'},
                {'p': '"Estufa":', 'o': ['un four', 'un frigo', 'un lave-vaisselle'], 'r': 'un four'},
                {'p': '"Espejo":', 'o': ['un miroir', 'une lampe', 'un tableau'], 'r': 'un miroir'},
                {'p': '"Jardín":', 'o': ['le jardin', 'la cuisine', 'la chambre'], 'r': 'le jardin'}
            ],
            [
                {'p': '"Microondas":', 'o': ['un micro-ondes', 'un frigo', 'un four'], 'r': 'un micro-ondes'},
                {'p': '"Lavavajillas":', 'o': ['un lave-vaisselle', 'une machine à laver', 'un sèche-linge'], 'r': 'un lave-vaisselle'},
                {'p': '"Lavadora":', 'o': ['une machine à laver', 'un frigo', 'un four'], 'r': 'une machine à laver'},
                {'p': '"Televisión":', 'o': ['la télévision', 'la radio', 'l"ordinateur'], 'r': 'la télévision'},
                {'p': '"Ordenador":', 'o': ['l"ordinateur', 'le téléphone', 'la télé'], 'r': 'l"ordinateur'},
                {'p': '"Teléfono":', 'o': ['le téléphone', 'l"ordinateur', 'la télévision'], 'r': 'le téléphone'},
                {'p': '"Ventana":', 'o': ['la fenêtre', 'la porte', 'le mur'], 'r': 'la fenêtre'},
                {'p': '"Puerta":', 'o': ['la porte', 'la fenêtre', 'le plafond'], 'r': 'la porte'},
                {'p': '"Pared":', 'o': ['le mur', 'la porte', 'la fenêtre'], 'r': 'le mur'},
                {'p': '"Techo":', 'o': ['le plafond', 'le mur', 'la fenêtre'], 'r': 'le plafond'}
            ]
        ]
    },

    'U7': {
        'titulo': 'Nourriture (Comida, partitivos du/de la)',
        'examenes': [
            [
                {'p': '"Pan":', 'o': ['du pain', 'de la viande', 'du fromage'], 'r': 'du pain'},
                {'p': '"Manzana":', 'o': ['une pomme', 'du pain', 'de la viande'], 'r': 'une pomme'},
                {'p': '"Agua":', 'o': ['de l"eau', 'du lait', 'de la soupe'], 'r': 'de l"eau'},
                {'p': '"Carne":', 'o': ['de la viande', 'du pain', 'une pomme'], 'r': 'de la viande'},
                {'p': '"Leche":', 'o': ['du lait', 'de l"eau', 'de la viande'], 'r': 'du lait'},
                {'p': '"Queso":', 'o': ['du fromage', 'du pain', 'une pomme'], 'r': 'du fromage'},
                {'p': '"Sopa":', 'o': ['de la soupe', 'du lait', 'de l"eau'], 'r': 'de la soupe'},
                {'p': '"Naranja":', 'o': ['une orange', 'du pain', 'de la viande'], 'r': 'une orange'},
                {'p': '"Mantequilla":', 'o': ['du beurre', 'du fromage', 'de la soupe'], 'r': 'du beurre'},
                {'p': '"Huevos":', 'o': ['des oeufs', 'du lait', 'une pomme'], 'r': 'des oeufs'}
            ],
            [
                {'p': '"Arroz":', 'o': ['du riz', 'de la viande', 'une pomme'], 'r': 'du riz'},
                {'p': '"Pescado":', 'o': ['du poisson', 'du pain', 'de l"eau'], 'r': 'du poisson'},
                {'p': '"Plátano":', 'o': ['une banane', 'du fromage', 'de la soupe'], 'r': 'une banane'},
                {'p': '"Zumo":', 'o': ['du jus', 'du lait', 'de la viande'], 'r': 'du jus'},
                {'p': '"Patatas":', 'o': ['des pommes de terre', 'du riz', 'une orange'], 'r': 'des pommes de terre'},
                {'p': '"Tomate":', 'o': ['une tomate', 'du pain', 'de l"eau'], 'r': 'une tomate'},
                {'p': '"Yogur":', 'o': ['un yaourt', 'du fromage', 'de la soupe'], 'r': 'un yaourt'},
                {'p': '"Aceite":', 'o': ['de l"huile', 'du beurre', 'du lait'], 'r': 'de l"huile'},
                {'p': '"Perejil":', 'o': ['du persil', 'des pommes de terre', 'une banane'], 'r': 'du persil'},
                {'p': '"Galletas":', 'o': ['des biscuits', 'du riz', 'de la viande'], 'r': 'des biscuits'}
            ],
            [
                {'p': '"¿Quieres pan?": Veux-tu ___ pain?', 'o': ['du', 'de la', 'des'], 'r': 'du'},
                {'p': '"¿Hay leche?": Y a-t-il ___ lait?', 'o': ['du', 'de la', 'de l"'], 'r': 'du'},
                {'p': '"No hay agua": Il n"y a pas ___ eau', 'o': ['d"eau', 'de l"eau', 'du eau'], 'r': 'd"eau'},
                {'p': '"Quiero carne": Je veux ___ viande', 'o': ['de la', 'du', 'des'], 'r': 'de la'},
                {'p': '"Hay queso": Il y a ___ fromage', 'o': ['du', 'de la', 'de l"'], 'r': 'du'},
                {'p': '"No hay sopa": Il n"y a pas ___ soupe', 'o': ['de la', 'du', 'des'], 'r': 'de la'},
                {'p': '"¿Hay naranjas?": Y a-t-il ___ oranges?', 'o': ['des', 'du', 'de la'], 'r': 'des'},
                {'p': '"Quiero mantequilla": Je veux ___ beurre', 'o': ['du', 'de la', 'des'], 'r': 'du'},
                {'p': '"Hay huevos": Il y a ___ oeufs', 'o': ['des', 'du', 'de la'], 'r': 'des'},
                {'p': '"No hay arroz": Il n"y a pas ___ riz', 'o': ['de', 'du', 'des'], 'r': 'de'}
            ]
        ]
    },

    'U8': {
        'titulo': 'Marché (Frutas, números 20-100)',
        'examenes': [
            [
                {'p': 'Número 25:', 'o': ['vingt-cinq', 'vingt-quatre', 'vingt-six'], 'r': 'vingt-cinq'},
                {'p': '"Fresa":', 'o': ['une fraise', 'une cerise', 'une framboise'], 'r': 'une fraise'},
                {'p': 'Número 30:', 'o': ['trente', 'vingt-neuf', 'trente-et-un'], 'r': 'trente'},
                {'p': '"Melocotón":', 'o': ['une pêche', 'une poire', 'une pomme'], 'r': 'une pêche'},
                {'p': 'Número 40:', 'o': ['quarante', 'trente-neuf', 'quarante-deux'], 'r': 'quarante'},
                {'p': '"Piña":', 'o': ['un ananas', 'une orange', 'une banane'], 'r': 'un ananas'},
                {'p': 'Número 50:', 'o': ['cinquante', 'quarante-neuf', 'cinquante-et-un'], 'r': 'cinquante'},
                {'p': '"Limón":', 'o': ['un citron', 'une lime', 'un pamplemousse'], 'r': 'un citron'},
                {'p': 'Número 60:', 'o': ['soixante', 'cinquante-neuf', 'soixante-dix'], 'r': 'soixante'},
                {'p': '"Sandía":', 'o': ['une pastèque', 'une melon', 'une fraise'], 'r': 'une pastèque'}
            ],
            [
                {'p': 'Número 70:', 'o': ['soixante-dix', 'soixante-neuf', 'quatre-vingts'], 'r': 'soixante-dix'},
                {'p': '"Uvas":', 'o': ['des raisins', 'des fraises', 'des cerises'], 'r': 'des raisins'},
                {'p': 'Número 80:', 'o': ['quatre-vingts', 'soixante-dix-neuf', 'quatre-vingt-un'], 'r': 'quatre-vingts'},
                {'p': '"Ciruela":', 'o': ['une prune', 'une pêche', 'une poire'], 'r': 'une prune'},
                {'p': 'Número 90:', 'o': ['quatre-vingt-dix', 'quatre-vingt-neuf', 'quatre-vingt-onze'], 'r': 'quatre-vingt-dix'},
                {'p': '"Melón":', 'o': ['un melon', 'une pastèque', 'un ananas'], 'r': 'un melon'},
                {'p': 'Número 100:', 'o': ['cent', 'quatre-vingt-dix-neuf', 'cent-un'], 'r': 'cent'},
                {'p': '"Cereza":', 'o': ['une cerise', 'une fraise', 'un raisin'], 'r': 'une cerise'},
                {'p': '"¿Cuánto cuesta?":', 'o': ['Combien ça coûte?', 'Où est-ce?', 'C"est combien?'], 'r': 'Combien ça coûte?'},
                {'p': '"Dos manzanas": Deux ___', 'o': ['pommes', 'pomme', 'poma'], 'r': 'pommes'}
            ],
            [
                {'p': 'Número 21:', 'o': ['vingt-et-un', 'vingt-deux', 'vingt'], 'r': 'vingt-et-un'},
                {'p': '"Frambuesa":', 'o': ['une framboise', 'une fraise', 'une mûre'], 'r': 'une framboise'},
                {'p': 'Número 35:', 'o': ['trente-cinq', 'trente-quatre', 'trente-six'], 'r': 'trente-cinq'},
                {'p': '"Pera":', 'o': ['une poire', 'une pomme', 'une prune'], 'r': 'une poire'},
                {'p': '"Tres naranjas": Trois ___', 'o': ['oranges', 'orange', 'orango'], 'r': 'oranges'},
                {'p': 'Número 45:', 'o': ['quarante-cinq', 'quarante-quatre', 'quarante-six'], 'r': 'quarante-cinq'},
                {'p': '"Mango":', 'o': ['un mango', 'une mangue', 'un ananas'], 'r': 'un mango'},
                {'p': '"¿Esto cuánto es?": C"est ___ euros?', 'o': ['combien', 'quel', 'où'], 'r': 'combien'},
                {'p': 'Número 55:', 'o': ['cinquante-cinq', 'cinquante-quatre', 'cinquante-six'], 'r': 'cinquante-cinq'},
                {'p': '"Moras":', 'o': ['des mûres', 'des raisins', 'des fraises'], 'r': 'des mûres'}
            ]
        ]
    }
}
