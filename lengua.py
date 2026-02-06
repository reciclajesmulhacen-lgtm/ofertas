# lengua.py

TEMARIO = {
    'U1': {
        'titulo': '¡Por nuestra salud! (Anuncios, G/J)',
        'examenes': [
            [
                {'p': '¿Qué tipo de texto es un anuncio?', 'o': ['Narrativo', 'Persuasivo', 'Poético'], 'r': 'Persuasivo'},
                {'p': '¿Para qué sirve principalmente un anuncio?', 'o': ['Para vender o convencer', 'Para contar un cuento', 'Para explicar una receta'], 'r': 'Para vender o convencer'},
                {'p': 'Completa con la palabra correcta: "Es importante ___ agua"', 'o': ['beber', 'bever', 'veber'], 'r': 'beber'},
                {'p': 'Elige la forma correcta: "El niño ___uega en el parque"', 'o': ['juega', 'guega', 'jeuga'], 'r': 'juega'},
                {'p': '¿Cuál está bien escrita?', 'o': ['jirafa', 'girafa', 'jirrafa'], 'r': 'jirafa'},
                {'p': 'Completa: "Me duele la ___arganta"', 'o': ['g', 'j', 'h'], 'r': 'g'},
                {'p': '¿Qué parte NO suele aparecer en un anuncio?', 'o': ['Eslogan', 'Precio', 'Personajes de un cuento'], 'r': 'Personajes de un cuento'},
                {'p': 'Elige la correcta: "El ___efe del hospital"', 'o': ['jefe', 'gefe', 'jefe'], 'r': 'jefe'},
                {'p': '¿Cuál está bien escrita?', 'o': ['ejercicio', 'egercicio', 'ejerzicio'], 'r': 'ejercicio'},
                {'p': 'En un anuncio, el eslogan es…', 'o': ['Una frase corta que se recuerda', 'Una receta', 'Un poema largo'], 'r': 'Una frase corta que se recuerda'}
            ],
            [
                {'p': '¿Qué texto intenta convencerte de comprar algo?', 'o': ['Un anuncio', 'Un cuento', 'Una carta'], 'r': 'Un anuncio'},
                {'p': 'Elige la palabra correcta: "Hoy ___emos fruta"', 'o': ['comemos', 'komemos', 'comeemos'], 'r': 'comemos'},
                {'p': '¿Cuál está bien escrita?', 'o': ['viaje', 'viage', 'biaje'], 'r': 'viaje'},
                {'p': 'Completa: "El ___ugo de naranja"', 'o': ['j', 'g', 'h'], 'r': 'j'},
                {'p': '¿Qué palabra lleva J?', 'o': ['juguete', 'guguete', 'jugete'], 'r': 'juguete'},
                {'p': '¿Qué palabra lleva G?', 'o': ['gimnasio', 'jimnasio', 'gimnazio'], 'r': 'gimnasio'},
                {'p': 'Un anuncio suele tener…', 'o': ['Imagen y texto', 'Solo números', 'Solo poemas'], 'r': 'Imagen y texto'},
                {'p': 'Elige la correcta: "Mi ___ente es amable"', 'o': ['gente', 'jente', 'guente'], 'r': 'gente'},
                {'p': 'Completa: "El médico me dio un ___arabe"', 'o': ['j', 'g', 'h'], 'r': 'j'},
                {'p': '¿Cuál es el objetivo del anuncio?', 'o': ['Convencer', 'Dormir', 'Asustar'], 'r': 'Convencer'}
            ],
            [
                {'p': '¿Qué palabra está bien escrita?', 'o': ['jardín', 'gardín', 'jardin'], 'r': 'jardín'},
                {'p': 'Completa: "Me gusta el ___ugo de manzana"', 'o': ['j', 'g', 'h'], 'r': 'j'},
                {'p': 'Elige la correcta: "Hago e___ercicio"', 'o': ['j', 'g', 'h'], 'r': 'j'},
                {'p': '¿Cuál está bien escrita?', 'o': ['girar', 'jirrar', 'girrar'], 'r': 'girar'},
                {'p': 'Un anuncio intenta…', 'o': ['Convencer', 'Narrar una aventura', 'Contar un chiste'], 'r': 'Convencer'},
                {'p': 'Completa: "El ___efe del equipo"', 'o': ['j', 'g', 'h'], 'r': 'j'},
                {'p': '¿Cuál palabra es correcta?', 'o': ['gente', 'jente', 'guente'], 'r': 'gente'},
                {'p': 'Completa: "Voy de via___e"', 'o': ['j', 'g', 'h'], 'r': 'j'},
                {'p': '¿Qué palabra lleva G?', 'o': ['gimnasia', 'jimnasia', 'gimnacia'], 'r': 'gimnasia'},
                {'p': 'Un eslogan es…', 'o': ['Una frase corta y pegadiza', 'Una carta larga', 'Un texto científico'], 'r': 'Una frase corta y pegadiza'}
            ]
        ]
    },

    # U2 no está en tu tabla-resumen, pero FanFest U2 es "Arte sonoro" (adverbios, descripciones, polisemia, coma).[web:243]
    # Aquí la dejamos como repaso general/comprensión para no romper el bot.
    'U2': {
        'titulo': 'Arte sonoro (Repaso y comprensión)',
        'examenes': [
            [
                {'p': '¿Qué es un párrafo?', 'o': ['Un grupo de oraciones sobre una idea', 'Una palabra suelta', 'Una letra'], 'r': 'Un grupo de oraciones sobre una idea'},
                {'p': '¿Qué suele llevar un texto para ser más claro?', 'o': ['Títulos y puntos', 'Solo dibujos', 'Solo números'], 'r': 'Títulos y puntos'},
                {'p': '¿Cuál es una oración?', 'o': ['Hoy voy al parque.', 'Parque', 'Hoy'], 'r': 'Hoy voy al parque.'},
                {'p': '¿Qué signo se usa al final de una pregunta?', 'o': ['¿ ?', '.'], 'r': '¿ ?'},
                {'p': '¿Cuál es un texto narrativo?', 'o': ['Un cuento', 'Un anuncio', 'Un horario'], 'r': 'Un cuento'},
                {'p': '¿Cuál es un texto expositivo?', 'o': ['Un texto que explica', 'Un poema', 'Un chiste'], 'r': 'Un texto que explica'},
                {'p': '¿Qué palabra está bien escrita?', 'o': ['higiene', 'ijiene', 'hijiene'], 'r': 'higiene'},
                {'p': '¿Qué es la idea principal?', 'o': ['Lo más importante del texto', 'La última palabra', 'Un dibujo'], 'r': 'Lo más importante del texto'},
                {'p': '¿Qué es un título?', 'o': ['El nombre del texto', 'Un punto', 'Una letra'], 'r': 'El nombre del texto'},
                {'p': '¿Qué ayuda a entender un texto?', 'o': ['Leer despacio', 'Leer sin mirar', 'No leer'], 'r': 'Leer despacio'}
            ],
            [
                {'p': '¿Qué es una descripción?', 'o': ['Explicar cómo es algo', 'Vender un producto', 'Hacer cuentas'], 'r': 'Explicar cómo es algo'},
                {'p': '¿Qué es una narración?', 'o': ['Contar hechos', 'Explicar reglas', 'Dar precios'], 'r': 'Contar hechos'},
                {'p': '¿Cuál es un sinónimo de “bonito”?', 'o': ['Hermoso', 'Feo', 'Triste'], 'r': 'Hermoso'},
                {'p': '¿Cuál es un antónimo de “rápido”?', 'o': ['Lento', 'Ligero', 'Ágil'], 'r': 'Lento'},
                {'p': '¿Qué signo se usa al final de una frase?', 'o': ['Punto', 'Coma', 'Dos puntos'], 'r': 'Punto'},
                {'p': '¿Qué signo se usa para separar elementos?', 'o': ['Coma', 'Punto', 'Interrogación'], 'r': 'Coma'},
                {'p': '¿Qué palabra está bien escrita?', 'o': ['gente', 'jente', 'guente'], 'r': 'gente'},
                {'p': '¿Qué es un diálogo?', 'o': ['Conversación', 'Un mapa', 'Una tabla'], 'r': 'Conversación'},
                {'p': '¿Qué hace un narrador?', 'o': ['Cuenta la historia', 'Vende', 'Dibuja'], 'r': 'Cuenta la historia'},
                {'p': '¿Qué es un personaje?', 'o': ['Quien aparece en la historia', 'Un punto', 'Un título'], 'r': 'Quien aparece en la historia'}
            ],
            [
                {'p': '¿Qué es una instrucción?', 'o': ['Un paso para hacer algo', 'Un cuento', 'Un anuncio'], 'r': 'Un paso para hacer algo'},
                {'p': '¿Qué palabra es un verbo?', 'o': ['correr', 'mesa', 'azul'], 'r': 'correr'},
                {'p': '¿Qué palabra es un sustantivo?', 'o': ['niño', 'cantar', 'rápido'], 'r': 'niño'},
                {'p': '¿Qué palabra es un adjetivo?', 'o': ['alto', 'casa', 'comer'], 'r': 'alto'},
                {'p': '¿Qué es un párrafo?', 'o': ['Un grupo de oraciones', 'Una letra', 'Un dibujo'], 'r': 'Un grupo de oraciones'},
                {'p': '¿Qué es una oración?', 'o': ['Una frase con sentido', 'Una palabra', 'Un número'], 'r': 'Una frase con sentido'},
                {'p': '¿Qué signo se usa en una exclamación?', 'o': ['¡ !', '.'], 'r': '¡ !'},
                {'p': '¿Qué es un resumen?', 'o': ['Lo más importante en pocas palabras', 'Un anuncio', 'Una lista de precios'], 'r': 'Lo más importante en pocas palabras'},
                {'p': '¿Qué ayuda a ordenar ideas?', 'o': ['Párrafos', 'Borrar', 'Gritar'], 'r': 'Párrafos'},
                {'p': '¿Qué es un tema?', 'o': ['De qué trata el texto', 'Un dibujo', 'Un punto'], 'r': 'De qué trata el texto'}
            ]
        ]
    },

    'U3': {
        'titulo': 'Versoladas (Determinantes)',
        'examenes': [
            [
                {'p': '¿Qué tipo de determinante es “este”?', 'o': ['Demostrativo', 'Posesivo', 'Indefinido'], 'r': 'Demostrativo'},
                {'p': 'Completa: "___ casa es grande"', 'o': ['Esta', 'Mi', 'Algunas'], 'r': 'Esta'},
                {'p': 'Completa: "Voy con ___ amigos"', 'o': ['mis', 'míos', 'mi'], 'r': 'mis'},
                {'p': '¿Cuál es un determinante posesivo?', 'o': ['mi', 'este', 'algunas'], 'r': 'mi'},
                {'p': '¿Cuál es un determinante demostrativo?', 'o': ['ese', 'mi', 'ninguno'], 'r': 'ese'},
                {'p': 'Completa: "No tengo ___ tiempo"', 'o': ['mucho', 'muchos', 'muchas'], 'r': 'mucho'},
                {'p': 'Completa: "He comprado ___ manzanas"', 'o': ['unas', 'unos', 'una'], 'r': 'unas'},
                {'p': '¿Qué tipo es “algunas”?', 'o': ['Indefinido', 'Demostrativo', 'Posesivo'], 'r': 'Indefinido'},
                {'p': 'Completa: "___ libro es tuyo"', 'o': ['Ese', 'Mi', 'Unas'], 'r': 'Ese'},
                {'p': '¿Cuál es un determinante?', 'o': ['aquella', 'correr', 'rápido'], 'r': 'aquella'}
            ],
            [
                {'p': '¿Qué determinante es posesivo?', 'o': ['su', 'aquel', 'unos'], 'r': 'su'},
                {'p': 'Completa: "___ perro ladra"', 'o': ['Ese', 'Muchos', 'Algunas'], 'r': 'Ese'},
                {'p': 'Completa: "Tengo ___ lápices"', 'o': ['unos', 'este', 'mi'], 'r': 'unos'},
                {'p': '¿Qué determinante es demostrativo?', 'o': ['aquel', 'mi', 'muchas'], 'r': 'aquel'},
                {'p': 'Completa: "No quiero ___ galletas"', 'o': ['ningunas', 'ese', 'mi'], 'r': 'ningunas'},
                {'p': 'Completa: "___ mochila es roja"', 'o': ['Mi', 'Este', 'Unas'], 'r': 'Mi'},
                {'p': '¿Qué tipo es “estos”?', 'o': ['Demostrativo', 'Posesivo', 'Indefinido'], 'r': 'Demostrativo'},
                {'p': '¿Qué tipo es “mis”?', 'o': ['Posesivo', 'Demostrativo', 'Indefinido'], 'r': 'Posesivo'},
                {'p': 'Completa: "___ niños juegan"', 'o': ['Algunos', 'Mi', 'Este'], 'r': 'Algunos'},
                {'p': '¿Cuál es un determinante indefinido?', 'o': ['muchos', 'ese', 'mi'], 'r': 'muchos'}
            ],
            [
                {'p': 'Completa: "___ día fue genial"', 'o': ['Aquel', 'Mi', 'Unas'], 'r': 'Aquel'},
                {'p': '¿Qué tipo es “mi”?', 'o': ['Posesivo', 'Demostrativo', 'Indefinido'], 'r': 'Posesivo'},
                {'p': '¿Qué tipo es “esa”?', 'o': ['Demostrativo', 'Posesivo', 'Indefinido'], 'r': 'Demostrativo'},
                {'p': 'Completa: "He visto ___ coches"', 'o': ['algunos', 'este', 'mi'], 'r': 'algunos'},
                {'p': 'Completa: "___ mochila es tuya"', 'o': ['Esa', 'Mi', 'Unos'], 'r': 'Esa'},
                {'p': '¿Cuál es un determinante?', 'o': ['estos', 'saltar', 'bonito'], 'r': 'estos'},
                {'p': 'Completa: "___ casa es de Ana"', 'o': ['Su', 'Aquel', 'Unas'], 'r': 'Su'},
                {'p': '¿Qué tipo es “unas”?', 'o': ['Indefinido', 'Demostrativo', 'Posesivo'], 'r': 'Indefinido'},
                {'p': 'Completa: "___ libros son nuevos"', 'o': ['Estos', 'Mi', 'Unas'], 'r': 'Estos'},
                {'p': '¿Qué tipo es “su”?', 'o': ['Posesivo', 'Demostrativo', 'Indefinido'], 'r': 'Posesivo'}
            ]
        ]
    }
}

# Unidades U4–U8 según FanFest 5 [web:243]
TEMARIO.update({
    'U4': {
        'titulo': 'Canal manualidades (Determinantes numerales e indefinidos, instructivos)',
        'examenes': [
            [
                {'p': '¿Qué tipo de palabras indican cantidad aproximada?', 'o': ['Indefinidos', 'Pronombres', 'Adjetivos'], 'r': 'Indefinidos'},
                {'p': '¿Cuál es la función de un texto instructivo?', 'o': ['Dar pasos para realizar algo', 'Contar una historia', 'Describir un lugar'], 'r': 'Dar pasos para realizar algo'},
                {'p': 'Selecciona el numeral que indica orden: primero, segundo...', 'o': ['Ordinales', 'Cardinales', 'Indefinidos'], 'r': 'Ordinales'},
                {'p': 'Palabra que indica un número exacto', 'o': ['Cardinal', 'Indefinido', 'Ordinal'], 'r': 'Cardinal'},
                {'p': '¿Cuál es un numeral cardinal?', 'o': ['tres', 'tercero', 'algunos'], 'r': 'tres'},
                {'p': 'Completa: "He pegado ___ fotos en la cartulina"', 'o': ['tres', 'varias', 'primera'], 'r': 'tres'},
                {'p': 'Tipo de palabra que indica “algunos”', 'o': ['Indefinido', 'Cardinal', 'Ordinal'], 'r': 'Indefinido'},
                {'p': 'Completa: "Para el experimento necesito ___ vasos de agua"', 'o': ['dos', 'primero', 'algunos'], 'r': 'dos'},
                {'p': '¿Qué indica un numeral ordinal?', 'o': ['Orden o posición', 'Cantidad aproximada', 'Cantidad exacta'], 'r': 'Orden o posición'},
                {'p': 'Instrucción bien escrita', 'o': ['Recorta las figuras con cuidado', 'Las figuras están recortadas', 'Me gusta recortar'], 'r': 'Recorta las figuras con cuidado'}
            ],
            [
                {'p': 'Ordinal de 5', 'o': ['quinto', 'cinco', 'varios'], 'r': 'quinto'},
                {'p': 'Cardinal de la cantidad 7', 'o': ['siete', 'séptimo', 'algunos'], 'r': 'siete'},
                {'p': 'Completa: "Pega ___ trozos de papel de colores"', 'o': ['varios', 'primero', 'tres'], 'r': 'varios'},
                {'p': '¿Qué tipo de texto explica pasos a seguir?', 'o': ['Instructivo', 'Narrativo', 'Poético'], 'r': 'Instructivo'},
                {'p': 'Completa: "Colorea las piezas en el ___ paso"', 'o': ['segundo', 'dos', 'varios'], 'r': 'segundo'},
                {'p': '¿Cuál es un indefinido?', 'o': ['muchos', 'tres', 'quinto'], 'r': 'muchos'},
                {'p': 'Completa: "En la receta usamos ___ huevos"', 'o': ['tres', 'tercero', 'varios'], 'r': 'tres'},
                {'p': 'Instrucción clara para un vídeo-tutorial', 'o': ['Primero, enciende la cámara', 'Me gustan los vídeos', 'El vídeo es bonito'], 'r': 'Primero, enciende la cámara'},
                {'p': '¿Qué tipo de determinante es "dos"?', 'o': ['Numeral cardinal', 'Numeral ordinal', 'Indefinido'], 'r': 'Numeral cardinal'},
                {'p': '¿Qué tipo de determinante es "varios"?', 'o': ['Indefinido', 'Numeral cardinal', 'Demostrativo'], 'r': 'Indefinido'}
            ],
            [
                {'p': 'Completa: "Corta la cartulina en ___ partes iguales"', 'o': ['cuatro', 'cuartos', 'varios'], 'r': 'cuatro'},
                {'p': 'Completa: "En el ___ paso pegamos las fotos"', 'o': ['tercer', 'tres', 'algunos'], 'r': 'tercer'},
                {'p': '¿Qué palabra indica cantidad aproximada?', 'o': ['algunos', 'dos', 'segundo'], 'r': 'algunos'},
                {'p': '¿Qué tipo de texto es una receta de cocina?', 'o': ['Instructivo', 'Lírico', 'Teatral'], 'r': 'Instructivo'},
                {'p': 'Completa: "He usado ___ colores diferentes"', 'o': ['muchos', 'cuatro', 'segundo'], 'r': 'muchos'},
                {'p': '¿Qué tipo de determinante es "primero"?', 'o': ['Numeral ordinal', 'Numeral cardinal', 'Indefinido'], 'r': 'Numeral ordinal'},
                {'p': 'Completa: "Para la manualidad necesito ___ pegamento"', 'o': ['un poco de', 'tres', 'quinto'], 'r': 'un poco de'},
                {'p': '¿Qué indica un numeral cardinal?', 'o': ['Cantidad exacta', 'Orden', 'Lugar'], 'r': 'Cantidad exacta'},
                {'p': 'Instrucción correcta', 'o': ['Dobla la hoja por la mitad', 'La hoja está doblada', 'Me gusta doblar hojas'], 'r': 'Dobla la hoja por la mitad'},
                {'p': 'Selecciona el numeral cardinal', 'o': ['cuatro', 'cuarto', 'varios'], 'r': 'cuatro'}
            ]
        ]
    },

    'U5': {
        'titulo': 'Pasatiempo formal (Preposiciones, conjunciones, interjecciones)',
        'examenes': [
            [
                {'p': 'Selecciona la conjunción correcta: "Estudio mucho ____ apruebo los exámenes"', 'o': ['y', 'pero', 'porque'], 'r': 'y'},
                {'p': 'Preposición que indica dirección', 'o': ['hacia', 'sobre', 'en'], 'r': 'hacia'},
                {'p': 'Completa: "Voy ___ el parque"', 'o': ['al', 'a', 'en'], 'r': 'al'},
                {'p': 'Conjunción que une ideas contrarias', 'o': ['pero', 'y', 'o'], 'r': 'pero'},
                {'p': 'Selecciona la preposición correcta: "El libro está ___ la mesa"', 'o': ['sobre', 'hacia', 'entre'], 'r': 'sobre'},
                {'p': 'Conjunción que indica causa', 'o': ['porque', 'pero', 'y'], 'r': 'porque'},
                {'p': '¿Cuál es una interjección?', 'o': ['¡Ay!', 'porque', 'sobre'], 'r': '¡Ay!'},
                {'p': 'Completa: "Caminamos ___ la escuela"', 'o': ['hacia', 'sobre', 'en'], 'r': 'hacia'},
                {'p': 'Selecciona la conjunción que une palabras similares', 'o': ['y', 'o', 'pero'], 'r': 'y'},
                {'p': 'Preposición de lugar: "El gato está ___ la silla"', 'o': ['debajo de', 'porque', 'y'], 'r': 'debajo de'}
            ],
            [
                {'p': 'Completa: "Voy ___ casa de mi abuela"', 'o': ['a', 'al', 'en'], 'r': 'a'},
                {'p': 'Conjunción que indica alternativa', 'o': ['o', 'y', 'pero'], 'r': 'o'},
                {'p': 'Selecciona la preposición correcta: "El cuaderno está ___ la mochila"', 'o': ['dentro de', 'sobre', 'delante de'], 'r': 'dentro de'},
                {'p': 'Conjunción que indica oposición', 'o': ['pero', 'porque', 'y'], 'r': 'pero'},
                {'p': 'Preposición de tiempo: "Llegamos ___ la tarde"', 'o': ['por', 'en', 'a'], 'r': 'por'},
                {'p': '¿Cuál es una interjección de sorpresa?', 'o': ['¡Oh!', 'hacia', 'porque'], 'r': '¡Oh!'},
                {'p': 'Completa: "Salgo ___ el colegio"', 'o': ['del', 'de', 'en'], 'r': 'del'},
                {'p': 'Conjunción de causa: "No fui a clase ___ estaba enfermo"', 'o': ['porque', 'y', 'pero'], 'r': 'porque'},
                {'p': 'Completa: "Estudio mucho, ____ saco buenas notas"', 'o': ['y', 'pero', 'o'], 'r': 'y'},
                {'p': 'Preposición correcta: "El regalo está ___ la caja"', 'o': ['dentro de', 'sobre', 'encima de'], 'r': 'dentro de'}
            ],
            [
                {'p': 'Completa: "Vamos ___ el parque"', 'o': ['hacia', 'en', 'sobre'], 'r': 'hacia'},
                {'p': 'Conjunción que indica consecuencia', 'o': ['por lo tanto', 'pero', 'y'], 'r': 'por lo tanto'},
                {'p': 'Preposición de lugar: "El perro duerme ___ la cama"', 'o': ['en', 'sobre', 'bajo'], 'r': 'en'},
                {'p': 'Conjunción de contraste: "Estudié mucho, ____ no aprobé"', 'o': ['pero', 'porque', 'y'], 'r': 'pero'},
                {'p': '¿Cuál es una interjección de alegría?', 'o': ['¡Hurra!', 'porque', 'entre'], 'r': '¡Hurra!'},
                {'p': 'Completa: "Salimos ___ la calle principal"', 'o': ['por', 'a', 'hacia'], 'r': 'por'},
                {'p': 'Conjunción que une palabras: "Pan ___ mantequilla"', 'o': ['y', 'pero', 'porque'], 'r': 'y'},
                {'p': 'Preposición correcta: "El lápiz está ___ la mesa"', 'o': ['sobre', 'de', 'por'], 'r': 'sobre'},
                {'p': 'Conjunción que indica elección', 'o': ['o', 'y', 'porque'], 'r': 'o'},
                {'p': 'Preposición que indica origen: "Viene ___ Granada"', 'o': ['de', 'a', 'en'], 'r': 'de'}
            ]
        ]
    },

    'U6': {
        'titulo': 'Aires de leyenda (El verbo, formas verbales)',
        'examenes': [
            [
                {'p': '¿Qué es un verbo?', 'o': ['Una acción o estado', 'Un objeto', 'Una cualidad'], 'r': 'Una acción o estado'},
                {'p': 'Selecciona el verbo en esta oración: "Luis corre rápido"', 'o': ['Luis', 'corre', 'rápido'], 'r': 'corre'},
                {'p': 'Completa: "Mañana nosotros ___ al cine"', 'o': ['iremos', 'iremosos', 'voy'], 'r': 'iremos'},
                {'p': '¿En qué tiempo está el verbo?: "Yo canté"', 'o': ['Pasado', 'Presente', 'Futuro'], 'r': 'Pasado'},
                {'p': '¿En qué persona está "nosotros jugamos"?', 'o': ['1.ª persona del plural', '2.ª del singular', '3.ª del plural'], 'r': '1.ª persona del plural'},
                {'p': 'Completa: "Ellos ___ una leyenda"', 'o': ['cuentan', 'cuenta', 'contamos'], 'r': 'cuentan'},
                {'p': 'Infinitivo de "corremos"', 'o': ['correr', 'corriendo', 'corrío'], 'r': 'correr'},
                {'p': '¿Cuál es un verbo en infinitivo?', 'o': ['saltar', 'salté', 'salta'], 'r': 'saltar'},
                {'p': 'Completa: "Yo ___ un cuento de miedo"', 'o': ['leo', 'lees', 'leemos'], 'r': 'leo'},
                {'p': 'Verbo en futuro: ', 'o': ['viajaré', 'viajé', 'viajo'], 'r': 'viajaré'}
            ],
            [
                {'p': '¿Qué parte del verbo cambia según la persona y tiempo?', 'o': ['Desinencia', 'Raíz', 'Sustantivo'], 'r': 'Desinencia'},
                {'p': '¿Cuál es la raíz de "cantamos"?', 'o': ['cant-', 'amos', 'canta'], 'r': 'cant-'},
                {'p': 'Verbo en presente: ', 'o': ['corro', 'corrí', 'correré'], 'r': 'corro'},
                {'p': 'Completa: "Tú ___ muy rápido"', 'o': ['corres', 'corro', 'corren'], 'r': 'corres'},
                {'p': '¿En qué tiempo está "viviremos"?', 'o': ['Futuro', 'Presente', 'Pasado'], 'r': 'Futuro'},
                {'p': '¿En qué persona está "él juega"?', 'o': ['3.ª del singular', '1.ª del plural', '2.ª del singular'], 'r': '3.ª del singular'},
                {'p': 'Infinitivo de "miraron"', 'o': ['mirar', 'mirando', 'mirado'], 'r': 'mirar'},
                {'p': 'Completa: "Nosotros ___ una leyenda esta noche"', 'o': ['leeremos', 'leo', 'lees'], 'r': 'leeremos'},
                {'p': 'Verbo en pasado: ', 'o': ['comí', 'como', 'comeré'], 'r': 'comí'},
                {'p': '¿Cuál es un verbo?', 'o': ['nadar', 'nube', 'alto'], 'r': 'nadar'}
            ],
            [
                {'p': 'Completa: "Ellas ___ a la puerta del castillo"', 'o': ['llamaron', 'llaman', 'llamarán'], 'r': 'llamaron'},
                {'p': '¿Qué es el tiempo verbal?', 'o': ['Momento de la acción', 'Lugar de la acción', 'Personaje'], 'r': 'Momento de la acción'},
                {'p': '¿En qué tiempo está "yo escribo"?', 'o': ['Presente', 'Pasado', 'Futuro'], 'r': 'Presente'},
                {'p': 'Verbo en 3.ª persona plural', 'o': ['cantan', 'cantas', 'canto'], 'r': 'cantan'},
                {'p': 'Completa: "Nosotros ___ la leyenda del dragón"', 'o': ['contamos', 'contáis', 'contaré'], 'r': 'contamos'},
                {'p': 'Infinitivo de "soñaban"', 'o': ['soñar', 'soñado', 'soñó'], 'r': 'soñar'},
                {'p': 'Verbo en futuro: ', 'o': ['leeré', 'leí', 'leo'], 'r': 'leeré'},
                {'p': 'Completa: "Ella ___ muchas historias"', 'o': ['conoce', 'conocen', 'conoces'], 'r': 'conoce'},
                {'p': '¿Qué indica la persona verbal?', 'o': ['Quién realiza la acción', 'Dónde ocurre', 'Cuándo ocurre'], 'r': 'Quién realiza la acción'},
                {'p': '¿Cuál es un verbo relacionado con leyendas?', 'o': ['contar', 'castillo', 'héroe'], 'r': 'contar'}
            ]
        ]
    },

    'U7': {
        'titulo': 'Voces del mundo (Familia de palabras, textos expositivos, lenguas)',
        'examenes': [
            [
                {'p': '¿Qué es una familia de palabras?', 'o': ['Palabras con la misma raíz', 'Palabras de otro idioma', 'Palabras inventadas'], 'r': 'Palabras con la misma raíz'},
                {'p': '¿Cuál NO pertenece a la familia de "mar"?', 'o': ['marino', 'marinero', 'mariposa'], 'r': 'mariposa'},
                {'p': 'Familia de palabras de "pan":', 'o': ['pan, panadero, panadería', 'pan, mano, panda', 'pan, pena, pana'], 'r': 'pan, panadero, panadería'},
                {'p': '¿Qué es un texto expositivo?', 'o': ['Un texto que explica', 'Un texto que convence', 'Un texto que cuenta una historia'], 'r': 'Un texto que explica'},
                {'p': 'Completa: "El español, el francés y el inglés son..."', 'o': ['lenguas', 'países', 'personas'], 'r': 'lenguas'},
                {'p': '¿Qué es un dialecto?', 'o': ['Variedad de una lengua', 'Idioma inventado', 'Lengua secreta'], 'r': 'Variedad de una lengua'},
                {'p': '¿Qué lengua se habla en España?', 'o': ['Castellano', 'Chino', 'Japonés'], 'r': 'Castellano'},
                {'p': '¿Qué lengua se usa en los signos para personas sordas?', 'o': ['Lengua de signos', 'Lengua musical', 'Lengua antigua'], 'r': 'Lengua de signos'},
                {'p': '¿Qué hace un texto expositivo?', 'o': ['Explica un tema', 'Cuenta una leyenda', 'Vende un producto'], 'r': 'Explica un tema'},
                {'p': '¿Qué palabra pertenece a la familia de "flor"?', 'o': ['florero', 'flotar', 'flaco'], 'r': 'florero'}
            ],
            [
                {'p': '¿Cuál pertenece a la familia de "sol"?', 'o': ['soleado', 'silla', 'sal'], 'r': 'soleado'},
                {'p': '¿Qué es la raíz de una palabra?', 'o': ['La parte que no cambia', 'El final', 'La tilde'], 'r': 'La parte que no cambia'},
                {'p': 'Familia de "luz":', 'o': ['luz, luminoso, alumbrar', 'luz, luna, loma', 'luz, lujo, lucha'], 'r': 'luz, luminoso, alumbrar'},
                {'p': 'Un texto expositivo sirve para...', 'o': ['informar', 'asustar', 'reír'], 'r': 'informar'},
                {'p': '¿Qué es una lengua?', 'o': ['Un sistema de comunicación', 'Un país', 'Un deporte'], 'r': 'Un sistema de comunicación'},
                {'p': '¿Cuál es una lengua?', 'o': ['inglés', 'Europa', 'Granada'], 'r': 'inglés'},
                {'p': '¿Qué se hace en una exposición oral?', 'o': ['Explicar un tema ante otros', 'Dormir', 'Cantar siempre'], 'r': 'Explicar un tema ante otros'},
                {'p': '¿Qué palabra pertenece a la familia de "tiempo"?', 'o': ['temporal', 'templar', 'timbre'], 'r': 'temporal'},
                {'p': '¿Qué lengua se habla en Francia?', 'o': ['francés', 'alemán', 'italiano'], 'r': 'francés'},
                {'p': '¿Qué lengua se habla en Reino Unido?', 'o': ['inglés', 'árabe', 'latín'], 'r': 'inglés'}
            ],
            [
                {'p': '¿Cuál NO pertenece a la familia de "leer"?', 'o': ['lector', 'lectura', 'letra'], 'r': 'letra'},
                {'p': 'Familia de "nación":', 'o': ['nación, nacional, nacionalidad', 'nación, nacer, naciendo', 'nación, noche, nicho'], 'r': 'nación, nacional, nacionalidad'},
                {'p': 'Un texto expositivo debe ser...', 'o': ['claro y ordenado', 'misterioso', 'confuso'], 'r': 'claro y ordenado'},
                {'p': '¿Qué es la lengua de signos?', 'o': ['Lengua visual con las manos', 'Lengua escrita en libros', 'Lengua secreta'], 'r': 'Lengua visual con las manos'},
                {'p': '¿Qué palabra pertenece a la familia de "historia"?', 'o': ['historiador', 'histérico', 'histeria'], 'r': 'historiador'},
                {'p': '¿Qué se utiliza en una exposición en vídeo?', 'o': ['imagen y voz', 'solo música', 'solo texto'], 'r': 'imagen y voz'},
                {'p': '¿Qué lengua se habla en Italia?', 'o': ['italiano', 'portugués', 'ruso'], 'r': 'italiano'},
                {'p': '¿Qué palabra pertenece a la familia de "mar"?', 'o': ['marea', 'malo', 'mármol'], 'r': 'marea'},
                {'p': '¿Qué es una comunidad lingüística?', 'o': ['Personas que comparten una lengua', 'Personas que comparten deporte', 'Personas que comparten ropa'], 'r': 'Personas que comparten una lengua'},
                {'p': '¿Qué tipo de texto explica un tema sobre animales?', 'o': ['Expositivo', 'Lírico', 'Teatral'], 'r': 'Expositivo'}
            ]
        ]
    },

    'U8': {
        'titulo': 'Correspondencia entre tú y yo (Pronombres personales, cartas y correos)',
        'examenes': [
            [
                {'p': '¿Qué es un pronombre personal?', 'o': ['Palabra que sustituye al nombre', 'Nombre de una persona', 'Un adjetivo'], 'r': 'Palabra que sustituye al nombre'},
                {'p': '¿Cuál es un pronombre personal?', 'o': ['yo', 'casa', 'bonito'], 'r': 'yo'},
                {'p': 'Completa: "___ voy al parque"', 'o': ['Yo', 'Casa', 'Libro'], 'r': 'Yo'},
                {'p': '¿Cuál NO es pronombre personal?', 'o': ['árbol', 'tú', 'nosotros'], 'r': 'árbol'},
                {'p': '¿Qué pronombre sustituye a "María"?', 'o': ['ella', 'nosotros', 'tú'], 'r': 'ella'},
                {'p': '¿Qué pronombre sustituye a "Juan y yo"?', 'o': ['nosotros', 'ellos', 'él'], 'r': 'nosotros'},
                {'p': '¿Qué tipo de texto es una carta?', 'o': ['Texto de correspondencia', 'Texto teatral', 'Texto poético'], 'r': 'Texto de correspondencia'},
                {'p': 'Parte de la carta donde va el saludo', 'o': ['encabezamiento', 'despedida', 'firma'], 'r': 'encabezamiento'},
                {'p': 'Parte final de la carta donde te despides', 'o': ['despedida', 'cuerpo', 'dirección'], 'r': 'despedida'},
                {'p': '¿Qué se escribe en un correo electrónico?', 'o': ['Asunto y mensaje', 'Solo dibujos', 'Solo números'], 'r': 'Asunto y mensaje'}
            ],
            [
                {'p': '¿Cuál es un pronombre personal de 2.ª persona del singular?', 'o': ['tú', 'yo', 'ellos'], 'r': 'tú'},
                {'p': '¿Cuál es un pronombre de 3.ª persona del plural?', 'o': ['ellos', 'nosotros', 'tú'], 'r': 'ellos'},
                {'p': 'Completa: "___ somos amigos"', 'o': ['Nosotros', 'Él', 'Ella'], 'r': 'Nosotros'},
                {'p': 'En una carta, ¿dónde se cuenta lo que quieres decir?', 'o': ['En el cuerpo', 'En la fecha', 'En la firma'], 'r': 'En el cuerpo'},
                {'p': '¿Qué se pone en la firma de una carta?', 'o': ['El nombre de quien la escribe', 'La dirección', 'La fecha'], 'r': 'El nombre de quien la escribe'},
                {'p': '¿Qué abreviatura es correcta?', 'o': ['Sr.', 'Señ.', 'Sn.'], 'r': 'Sr.'},
                {'p': '¿Qué significan las siglas "DNI"?', 'o': ['Documento Nacional de Identidad', 'Día Nacional Infantil', 'Datos Nacionales Internet'], 'r': 'Documento Nacional de Identidad'},
                {'p': 'Completa: "___ te escribo para contarte..."', 'o': ['Te', 'Nos', 'Le'], 'r': 'Te'},
                {'p': '¿Qué pronombre usamos para "Ana y tú"?', 'o': ['vosotros', 'ellos', 'él'], 'r': 'vosotros'},
                {'p': '¿Qué diferencia a una carta formal?', 'o': ['Lenguaje más respetuoso', 'Muchos dibujos', 'No tiene saludo'], 'r': 'Lenguaje más respetuoso'}
            ],
            [
                {'p': '¿Cuál es un pronombre personal de 1.ª persona plural?', 'o': ['nosotros', 'ellos', 'ella'], 'r': 'nosotros'},
                {'p': '¿Cuál es un pronombre de 3.ª persona singular?', 'o': ['él', 'tú', 'yo'], 'r': 'él'},
                {'p': 'Completa: "___ vais al colegio"', 'o': ['Vosotros', 'Ellos', 'Él'], 'r': 'Vosotros'},
                {'p': 'En un correo electrónico, el campo "Para" indica...', 'o': ['el destinatario', 'el remitente', 'la firma'], 'r': 'el destinatario'},
                {'p': 'En una carta, ¿dónde se pone la fecha?', 'o': ['Arriba a la derecha', 'En la firma', 'En el cuerpo'], 'r': 'Arriba a la derecha'},
                {'p': '¿Qué es una abreviatura?', 'o': ['Forma corta de una palabra', 'Un dibujo', 'Un número'], 'r': 'Forma corta de una palabra'},
                {'p': '¿Qué es una sigla?', 'o': ['Palabra formada por iniciales', 'Un cuento', 'Un saludo'], 'r': 'Palabra formada por iniciales'},
                {'p': 'Completa: "___ escriben muy bien"', 'o': ['Ellos', 'Yo', 'Tú'], 'r': 'Ellos'},
                {'p': '¿Qué lenguaje usamos con amigos?', 'o': ['Más informal o coloquial', 'Muy formal siempre', 'Solo en cartas'], 'r': 'Más informal o coloquial'},
                {'p': '¿Qué lenguaje usamos en una carta al director del colegio?', 'o': ['Lenguaje formal', 'Lenguaje de chat', 'Lenguaje secreto'], 'r': 'Lenguaje formal'}
            ]
        ]
    }
})
