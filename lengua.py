# lengua.py
TEMARIO = {
    'U1': {
        'titulo': '¡Por nuestra salud!',
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

    # ⚠️ U2 no estaba en el temario original, pero la añadimos para que el motor NO se rompa.
    'U2': {
        'titulo': 'Repaso y comprensión lectora',
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

# lengua.py - Unidades U4 a U8 completas
TEMARIO.update({
    'U4': {
        'titulo': 'Canal manualidades',
        'examenes': [
            [   # Examen 1
                {'p': '¿Qué tipo de palabras indican cantidad aproximada?', 'o': ['Indefinidos', 'Determinantes', 'Pronombres'], 'r': 'Indefinidos'},
                {'p': '¿Cuál es la función de un instructivo?', 'o': ['Dar pasos para realizar algo', 'Contar una historia', 'Expresar opinión'], 'r': 'Dar pasos para realizar algo'},
                {'p': 'Escribe la forma correcta: "Hecho ____ la tarea"', 'o': ['de', 'con', 'para'], 'r': 'de'},
                {'p': 'Selecciona el numeral que indica orden: primero, segundo...', 'o': ['Ordinales', 'Cardinales', 'Indefinidos'], 'r': 'Ordinales'},
                {'p': 'Palabra que indica un número exacto', 'o': ['Cardinal', 'Indefinido', 'Ordinal'], 'r': 'Cardinal'},
                {'p': 'Oración correcta para instrucciones', 'o': ['Corta la hoja con cuidado', 'La hoja está cortada', 'Me gusta cortar hojas'], 'r': 'Corta la hoja con cuidado'},
                {'p': 'Tipo de palabra que indica “algunos”', 'o': ['Indefinido', 'Determinante', 'Pronombre'], 'r': 'Indefinido'},
                {'p': 'Completa: “Para hacer el collage, necesitas ___ tijeras y pegamento”', 'o': ['unas', 'unos', 'la'], 'r': 'unas'},
                {'p': 'Numeral cardinal de 7', 'o': ['Siete', 'Séptimo', 'Varias'], 'r': 'Siete'},
                {'p': 'Selecciona el uso correcto de un instructivo', 'o': ['Seguir pasos para manualidades', 'Contar la historia de un libro', 'Dar tu opinión sobre un dibujo'], 'r': 'Seguir pasos para manualidades'}
            ],
            [   # Examen 2
                {'p': 'Tipo de numeral de “primero”', 'o': ['Ordinal', 'Cardinal', 'Indefinido'], 'r': 'Ordinal'},
                {'p': 'Palabra que indica cantidad exacta', 'o': ['Cardinal', 'Ordinal', 'Indefinido'], 'r': 'Cardinal'},
                {'p': 'Instrucción correcta: cortar papel', 'o': ['Corta el papel con tijeras', 'El papel se corta solo', 'Me gusta cortar papel'], 'r': 'Corta el papel con tijeras'},
                {'p': 'Indefinido que indica pocos', 'o': ['Algunos', 'Todos', 'Tres'], 'r': 'Algunos'},
                {'p': 'Ordinal de 5', 'o': ['Quinto', 'Cinco', 'Varias'], 'r': 'Quinto'},
                {'p': 'Completa: “____ materiales necesitas para el proyecto?”', 'o': ['Qué', 'Cuántos', 'Cómo'], 'r': 'Qué'},
                {'p': 'Usos de los numerales cardinales', 'o': ['Indican cantidad exacta', 'Indican posición', 'Indican instrucciones'], 'r': 'Indican cantidad exacta'},
                {'p': 'Selecciona la instrucción clara', 'o': ['Pinta la hoja de azul', 'La hoja es azul', 'Me gusta pintar'], 'r': 'Pinta la hoja de azul'},
                {'p': 'Palabra indefinida de cantidad', 'o': ['Varios', 'Dos', 'Primero'], 'r': 'Varios'},
                {'p': '¿Qué indica un numeral ordinal?', 'o': ['Orden o posición', 'Cantidad exacta', 'Cantidad aproximada'], 'r': 'Orden o posición'}
            ],
            [   # Examen 3
                {'p': 'Completa: “Necesito ____ tijeras para cortar”', 'o': ['unas', 'los', 'algunas'], 'r': 'unas'},
                {'p': 'Tipo de palabra que indica cantidad aproximada', 'o': ['Indefinido', 'Cardinal', 'Ordinal'], 'r': 'Indefinido'},
                {'p': 'Función principal de un instructivo', 'o': ['Indicar cómo hacer algo', 'Dar opinión', 'Contar una historia'], 'r': 'Indicar cómo hacer algo'},
                {'p': 'Ordinal de 3', 'o': ['Tercero', 'Tres', 'Algunos'], 'r': 'Tercero'},
                {'p': 'Numeral cardinal de 4', 'o': ['Cuatro', 'Cuarto', 'Pocos'], 'r': 'Cuatro'},
                {'p': 'Selecciona instrucción correcta', 'o': ['Dobla el papel a la mitad', 'El papel está doblado', 'Me gusta doblar papel'], 'r': 'Dobla el papel a la mitad'},
                {'p': 'Indefinido de cantidad grande', 'o': ['Muchos', 'Dos', 'Primero'], 'r': 'Muchos'},
                {'p': 'Usos de numerales ordinales', 'o': ['Indican posición', 'Indican cantidad exacta', 'Dan instrucciones'], 'r': 'Indican posición'},
                {'p': 'Completa: “Para la manualidad necesito ____ pegamento”', 'o': ['un poco de', 'mucho', 'tres'], 'r': 'un poco de'},
                {'p': 'Selecciona el numeral cardinal', 'o': ['Siete', 'Séptimo', 'Algunos'], 'r': 'Siete'}
            ]
        ]
    },
    'U5': {
        'titulo': 'Pasatiempo formal',
        'examenes': [
            [
                {'p': 'Selecciona la conjunción correcta: “Estudio mucho ____ apruebo los exámenes”', 'o': ['y', 'pero', 'porque'], 'r': 'y'},
                {'p': 'Preposición que indica dirección', 'o': ['hacia', 'sobre', 'en'], 'r': 'hacia'},
                {'p': 'Completa: “Voy ___ el parque”', 'o': ['al', 'a', 'en'], 'r': 'al'},
                {'p': 'Conjunción que une ideas contrarias', 'o': ['pero', 'y', 'o'], 'r': 'pero'},
                {'p': 'Selecciona la preposición correcta: “El libro está ___ la mesa”', 'o': ['sobre', 'hacia', 'entre'], 'r': 'sobre'},
                {'p': 'Completa: “Caminamos ___ la escuela”', 'o': ['hacia', 'sobre', 'en'], 'r': 'hacia'},
                {'p': 'Conjunción que indica causa', 'o': ['porque', 'pero', 'y'], 'r': 'porque'},
                {'p': 'Selecciona la preposición correcta: “El regalo está ___ la caja”', 'o': ['dentro de', 'sobre', 'al lado'], 'r': 'dentro de'},
                {'p': 'Completa: “Estudio mucho, ____ apruebo”', 'o': ['y', 'porque', 'pero'], 'r': 'y'},
                {'p': 'Conjunción que une palabras similares', 'o': ['y', 'o', 'pero'], 'r': 'y'}
            ],
            [
                {'p': 'Completa: “Voy ___ casa de mi abuela”', 'o': ['a', 'al', 'en'], 'r': 'a'},
                {'p': 'Conjunción que indica alternativa', 'o': ['o', 'y', 'pero'], 'r': 'o'},
                {'p': 'Selecciona la preposición correcta: “El cuaderno está ___ la mochila”', 'o': ['dentro de', 'sobre', 'debajo de'], 'r': 'dentro de'},
                {'p': 'Conjunción que indica oposición', 'o': ['pero', 'porque', 'y'], 'r': 'pero'},
                {'p': 'Completa: “Salgo ___ el colegio”', 'o': ['del', 'de', 'en'], 'r': 'del'},
                {'p': 'Selecciona la preposición de tiempo: “Llegamos ___ la tarde”', 'o': ['por', 'en', 'a'], 'r': 'en'},
                {'p': 'Conjunción de causa: “No fui a clase ___ estaba enfermo”', 'o': ['porque', 'y', 'pero'], 'r': 'porque'},
                {'p': 'Completa: “Estudio mucho, ____ saco buenas notas”', 'o': ['y', 'pero', 'o'], 'r': 'y'},
                {'p': 'Selecciona la preposición correcta: “El gato está ___ la silla”', 'o': ['debajo de', 'sobre', 'dentro de'], 'r': 'debajo de'},
                {'p': 'Conjunción que une ideas similares', 'o': ['y', 'pero', 'porque'], 'r': 'y'}
            ],
            [
                {'p': 'Completa: “Voy ___ la biblioteca”', 'o': ['a', 'al', 'en'], 'r': 'a'},
                {'p': 'Conjunción que indica consecuencia', 'o': ['por lo tanto', 'pero', 'y'], 'r': 'por lo tanto'},
                {'p': 'Selecciona la preposición correcta: “El lápiz está ___ la mesa”', 'o': ['sobre', 'en', 'bajo'], 'r': 'sobre'},
                {'p': 'Conjunción de contraste: “Estudié mucho, ____ no aprobé”', 'o': ['pero', 'porque', 'y'], 'r': 'pero'},
                {'p': 'Completa: “Salimos ___ la calle principal”', 'o': ['por', 'a', 'hacia'], 'r': 'por'},
                {'p': 'Preposición de lugar: “El perro duerme ___ la cama”', 'o': ['en', 'sobre', 'bajo'], 'r': 'en'},
                {'p': 'Conjunción que indica causa: “No vino a clase ___ estaba enfermo”', 'o': ['porque', 'pero', 'y'], 'r': 'porque'},
                {'p': 'Completa: “Estudia mucho, ____ obtiene buenas calificaciones”', 'o': ['y', 'pero', 'porque'], 'r': 'y'},
                {'p': 'Preposición que indica movimiento: “Vamos ___ el parque”', 'o': ['hacia', 'en', 'sobre'], 'r': 'hacia'},
                {'p': 'Conjunción que une palabras: “Pan ___ mantequilla”', 'o': ['y', 'pero', 'porque'], 'r': 'y'}
            ]
        ]
    }
})
# lengua.py - Unidades U1 a U3 completas
TEMARIO = {
    'U1': {
        'titulo': '¡Por nuestra salud!',
        'examenes': [
            [   # Examen 1
                {'p': 'Selecciona la forma correcta de la G o J en: "El ___ato es importante"', 'o': ['gato', 'jato', 'gato'], 'r': 'gato'},
                {'p': '¿Cuál es el objetivo principal de un anuncio?', 'o': ['Informar', 'Vender', 'Cantar'], 'r': 'Vender'},
                {'p': 'Completa: "El doctor nos dio ___ consejos para la salud"', 'o': ['buenos', 'bien', 'bueno'], 'r': 'buenos'},
                {'p': 'Selecciona la oración con G correcta', 'o': ['Pagué la cuenta', 'Pajé la cuenta', 'Pagé la cuenta'], 'r': 'Pagé la cuenta'},
                {'p': 'Elige la letra correcta: "El je___ de la selva"', 'o': ['fe', 'je', 'ge'], 'r': 'fe'},
                {'p': '¿Qué tipo de texto es un anuncio?', 'o': ['Persuasivo', 'Narrativo', 'Poético'], 'r': 'Persuasivo'},
                {'p': 'Completa: "Debemos ___ ejercicio regularmente"', 'o': ['hacer', 'hazer', 'aser'], 'r': 'hacer'},
                {'p': 'Selecciona la G correcta: "La j___ fue divertida"', 'o': ['ira', 'ira', 'era'], 'r': 'ira'},
                {'p': 'Elige la opción correcta: "Come frutas y ___ verduras"', 'o': ['verduras', 'verduras', 'verduras'], 'r': 'verduras'},
                {'p': 'Identifica la J correcta: "El niño ___uega en el parque"', 'o': ['juega', 'guega', 'jeuga'], 'r': 'juega'}
            ],
            [   # Examen 2
                {'p': '¿Qué se busca con un anuncio publicitario?', 'o': ['Vender un producto', 'Contar un cuento', 'Explicar un experimento'], 'r': 'Vender un producto'},
                {'p': 'Completa: "El médico ___ buenos hábitos"', 'o': ['recomienda', 'rekomienda', 'recomiendas'], 'r': 'recomienda'},
                {'p': 'Selecciona la palabra con G correcta', 'o': ['gente', 'jente', 'gente'], 'r': 'gente'},
                {'p': 'Identifica la letra correcta: "El je___ de la historia"', 'o': ['fe', 'je', 'ge'], 'r': 'je'},
                {'p': 'Oración con J correcta', 'o': ['El juez dictó la sentencia', 'El guez dictó la sentencia', 'El jeuz dictó la sentencia'], 'r': 'El juez dictó la sentencia'},
                {'p': 'Completa: "Es importante ___ una dieta equilibrada"', 'o': ['tener', 'tner', 'tenr'], 'r': 'tener'},
                {'p': 'Elige la opción correcta: "Los niños ___ a la escuela"', 'o': ['van', 'ban', 'van'], 'r': 'van'},
                {'p': '¿Qué tipo de texto es un anuncio?', 'o': ['Persuasivo', 'Narrativo', 'Expositivo'], 'r': 'Persuasivo'},
                {'p': 'Selecciona la J correcta: "El niño ___uega al fútbol"', 'o': ['juega', 'geua', 'jeuga'], 'r': 'juega'},
                {'p': 'Completa: "Debemos beber ___ agua"', 'o': ['mucha', 'muha', 'mucha'], 'r': 'mucha'}
            ],
            [   # Examen 3
                {'p': 'Selecciona la letra correcta: "La ma___ana es fría"', 'o': ['ñ', 'n', 'g'], 'r': 'ñ'},
                {'p': 'Completa: "El doctor recomienda ___ frutas"', 'o': ['comer', 'komer', 'comer'], 'r': 'comer'},
                {'p': 'Identifica la G correcta: "La gi___afa es alta"', 'o': ['r', 'f', 'g'], 'r': 'r'},  # Ejemplo simple
                {'p': 'Oración con J correcta', 'o': ['El jardinero cuida las flores', 'El gardinero cuida las flores', 'El jardineiro cuida las flores'], 'r': 'El jardinero cuida las flores'},
                {'p': '¿Cuál es el objetivo de un anuncio?', 'o': ['Vender', 'Informar', 'Narrar'], 'r': 'Vender'},
                {'p': 'Completa: "Es bueno ___ deporte"', 'o': ['hacer', 'aser', 'hazer'], 'r': 'hacer'},
                {'p': 'Selecciona la opción correcta: "Bebo ___ agua todos los días"', 'o': ['mucha', 'muha', 'mucho'], 'r': 'mucha'},
                {'p': 'Pronuncia correcta de G/J: "via___e"', 'o': ['ge', 'je', 'je'], 'r': 'je'},
                {'p': 'Completa: "El maestro ___ reglas de ortografía"', 'o': ['enseña', 'ensena', 'ensenia'], 'r': 'enseña'},
                {'p': 'Identifica la palabra con G correcta: "girar"', 'o': ['girar', 'jirar', 'girar'], 'r': 'girar'}
            ]
        ]
    },
    'U3': {
        'titulo': 'Versoladas',
        'examenes': [
            [
                {'p': '¿Qué tipo de determinante es “este”?', 'o': ['Demostrativo', 'Posesivo', 'Indefinido'], 'r': 'Demostrativo'},
                {'p': 'Selecciona el determinante correcto: “___ casa es grande”', 'o': ['Esta', 'Ese', 'Algun'], 'r': 'Esta'},
                {'p': 'Completa: "Voy a ver ___ amigos"', 'o': ['mis', 'míos', 'mi'], 'r': 'mis'},
                {'p': 'Identifica el determinante: "Aquel libro es interesante"', 'o': ['Aquel', 'Libro', 'Es'], 'r': 'Aquel'},
                {'p': 'Selecciona el determinante adecuado: "No tengo ___ tiempo"', 'o': ['mucho', 'muchos', 'mucha'], 'r': 'mucho'},
                {'p': 'Completa: "He comprado ___ manzanas"', 'o': ['unas', 'unos', 'una'], 'r': 'unas'},
                {'p': 'Tipo de determinante: "su mochila"', 'o': ['Posesivo', 'Demostrativo', 'Indefinido'], 'r': 'Posesivo'},
                {'p': 'Completa: "___ personas vinieron"', 'o': ['Algunas', 'Algunos', 'Unas'], 'r': 'Algunas'},
                {'p': 'Selecciona el determinante correcto: "No conozco ___ niños"', 'o': ['esos', 'aquellos', 'algunos'], 'r': 'algunos'},
                {'p': 'Tipo de determinante: "mi libro"', 'o': ['Posesivo', 'Demostrativo', 'Indefinido'], 'r': 'Posesivo'}
            ],
            [
                {'p': 'Determinate: “este lápiz es mío”', 'o': ['Demostrativo', 'Posesivo', 'Indefinido'], 'r': 'Demostrativo'},
                {'p': 'Completa: "___ perro es de Juan"', 'o': ['Ese', 'Este', 'Aquel'], 'r': 'Ese'},
                {'p': 'Selecciona determinante: "Veo ___ casas"', 'o': ['unas', 'unos', 'algunas'], 'r': 'unas'},
                {'p': 'Tipo de determinante: "su hermano"', 'o': ['Posesivo', 'Demostrativo', 'Indefinido'], 'r': 'Posesivo'},
                {'p': 'Completa: "No tengo ___ ideas"', 'o': ['ninguna', 'alguna', 'muchas'], 'r': 'ninguna'},
                {'p': 'Determinante: "aquel edificio"', 'o': ['Demostrativo', 'Posesivo', 'Indefinido'], 'r': 'Demostrativo'},
                {'p': 'Completa: "He visto ___ libros"', 'o': ['algunos', 'unas', 'un'], 'r': 'algunos'},
                {'p': 'Tipo: "mi casa"', 'o': ['Posesivo', 'Demostrativo', 'Indefinido'], 'r': 'Posesivo'},
                {'p': 'Completa: "___ estudiantes aprobaron"', 'o': ['Todos', 'Algunos', 'Muchos'], 'r': 'Algunos'},
                {'p': 'Selecciona: "su mochila"', 'o': ['Posesivo', 'Demostrativo', 'Indefinido'], 'r': 'Posesivo'}
            ],
            [
                {'p': 'Determinante: “aquel día fue especial”', 'o': ['Demostrativo', 'Posesivo', 'Indefinido'], 'r': 'Demostrativo'},
                {'p': 'Completa: "___ casa es grande"', 'o': ['Esta', 'Ese', 'Algun'], 'r': 'Esta'},
                {'p': 'Tipo de determinante: "mis amigos"', 'o': ['Posesivo', 'Demostrativo', 'Indefinido'], 'r': 'Posesivo'},
                {'p': 'Selecciona el determinante: "unos niños corren"', 'o': ['Indefinido', 'Demostrativo', 'Posesivo'], 'r': 'Indefinido'},
                {'p': 'Completa: "___ mochila es tuya"', 'o': ['Esa', 'Su', 'Esta'], 'r': 'Su'},
                {'p': 'Determinante: "algunas chicas"', 'o': ['Indefinido', 'Posesivo', 'Demostrativo'], 'r': 'Indefinido'},
                {'p': 'Tipo: "mi cuaderno"', 'o': ['Posesivo', 'Demostrativo', 'Indefinido'], 'r': 'Posesivo'},
                {'p': 'Completa: "___ días fueron maravillosos"', 'o': ['Esos', 'Unos', 'Algunos'], 'r': 'Esos'},
                {'p': 'Selecciona el determinante: "su hermano mayor"', 'o': ['Posesivo', 'Demostrativo', 'Indefinido'], 'r': 'Posesivo'},
                {'p': 'Completa: "___ personas vinieron a la fiesta"', 'o': ['Algunas', 'Todos', 'Muchos'], 'r': 'Algunas'}
            ]
        ]
    }
}
