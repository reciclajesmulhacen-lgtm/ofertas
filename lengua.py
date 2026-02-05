import random

# TEMARIO LENGUA CASTELLANA 5º (Edelvives FanFest - Fiel al libro)
TEMARIO = {
    'U1_LEN': {
        'titulo': '¡Por nuestra salud! (G/J y el Párrafo)',
        'examenes': [
            [{'p': 'Según el libro, ¿cómo se escriben las palabras que terminan en -aje y -eje?', 'o': ['Con J', 'Con G'], 'r': 'Con J'}, {'p': '¿Qué unidad de texto está formada por un conjunto de oraciones sobre una misma idea?', 'o': ['El párrafo', 'El eslogan'], 'r': 'El párrafo'}, {'p': 'Las palabras que empiezan por eje- (ejemplo, ejercicio) se escriben con...', 'o': ['J', 'G'], 'r': 'J'}],
            [{'p': '¿Qué signo de puntuación se usa para separar dos párrafos distintos?', 'o': ['Punto y aparte', 'Punto y seguido'], 'r': 'Punto y aparte'}, {'p': '¿Se escriben con G las palabras que empiezan por gest- (gestión, gesticular)?', 'o': ['Sí', 'No'], 'r': 'Sí'}, {'p': '¿Cuál es la función comunicativa de los anuncios según la U1?', 'o': ['Convencer al receptor', 'Entretener al lector'], 'r': 'Convencer al receptor'}],
            [{'p': '¿Qué letra llevan las palabras que terminan en -jero/a (extranjero, consejera)?', 'o': ['J', 'G'], 'r': 'J'}, {'p': '¿Cómo se llama la frase corta y memorable de un anuncio?', 'o': ['Eslogan', 'Cuerpo'], 'r': 'Eslogan'}, {'p': 'Las formas verbales cuyos infinitivos no tienen G ni J (decir -> dije) se escriben con...', 'o': ['J', 'G'], 'r': 'J'}]
        ]
    },
    'U3_LEN': {
        'titulo': 'Versoladas (Los Determinantes)',
        'examenes': [
            [{'p': '¿Qué clase de palabras acompañan al sustantivo para concretarlo?', 'o': ['Determinantes', 'Conjunciones'], 'r': 'Determinantes'}, {'p': '¿Cuáles son los artículos determinados?', 'o': ['el, la, los, las', 'un, una, unos, unas'], 'r': 'el, la, los, las'}, {'p': '¿Qué indican los determinantes posesivos?', 'o': ['Pertenencia o posesión', 'Distancia'], 'r': 'Pertenencia o posesión'}],
            [{'p': '¿"Esa" y "esos" son demostrativos de qué distancia?', 'o': ['Media', 'Cercanía'], 'r': 'Media'}, {'p': 'En la frase "Nuestros amigos", ¿qué tipo de determinante es "Nuestros"?', 'o': ['Posesivo', 'Artículo'], 'r': 'Posesivo'}, {'p': '¿Los determinantes concuerdan siempre con el sustantivo en...?', 'o': ['Género y número', 'Solo en número'], 'r': 'Género y número'}],
            [{'p': '¿Cuál es un demostrativo de lejanía?', 'o': ['Aquel', 'Este'], 'r': 'Aquel'}, {'p': '¿Qué artículo se usa para sustantivos femeninos que empiezan por "a" tónica (ej: águila)?', 'o': ['El', 'La'], 'r': 'El'}, {'p': '¿"Tus" es un posesivo de un solo poseedor?', 'o': ['Sí', 'No'], 'r': 'Sí'}]
        ]
    },
    'U4_LEN': {
        'titulo': 'Canal manualidades (Numerales e Indefinidos)',
        'examenes': [
            [{'p': '¿Qué numerales indican orden (primero, segundo...)?', 'o': ['Ordinales', 'Cardinales'], 'r': 'Ordinales'}, {'p': '¿Qué indican los determinantes indefinidos?', 'o': ['Cantidad imprecisa', 'Cantidad exacta'], 'r': 'Cantidad imprecisa'}, {'p': '¿En qué parte de un texto instructivo aparecen los materiales?', 'o': ['Lista de materiales', 'Procedimiento'], 'r': 'Lista de materiales'}],
            [{'p': '¿"Varios" y "algunas" son determinantes de qué tipo?', 'o': ['Indefinidos', 'Numerales'], 'r': 'Indefinidos'}, {'p': '¿Cómo se escribe el numeral ordinal de 10?', 'o': ['Décimo', 'Diezavo'], 'r': 'Décimo'}, {'p': '¿Qué tipo de texto explica cómo hacer algo paso a paso?', 'o': ['Instructivo', 'Leyenda'], 'r': 'Instructivo'}],
            [{'p': '¿Cuál es un numeral cardinal?', 'o': ['Cien', 'Centésimo'], 'r': 'Cien'}, {'p': '¿"Pocos" es un determinante indefinido?', 'o': ['Sí', 'No'], 'r': 'Sí'}, {'p': '¿Los verbos en los textos instructivos suelen estar en...?', 'o': ['Imperativo o Infinitivo', 'Pasado'], 'r': 'Imperativo o Infinitivo'}]
        ]
    }
}

    }
}
import random

# TEMARIO LENGUA CASTELLANA 5º (Edelvives FanFest - CEIP Las Encinas)
# Estructura: 3 Exámenes por Unidad / 3 Preguntas por Examen
TEMARIO = {
    'U1_LEN': {
        'titulo': '¡Por nuestra salud! (G/J y el Párrafo)',
        'examenes': [
            [{'p': '¿Cómo se escriben las palabras que terminan en -aje y -eje?', 'o': ['Con J', 'Con G'], 'r': 'Con J'}, {'p': '¿Qué unidad de texto está formada por oraciones sobre una misma idea?', 'o': ['El párrafo', 'El eslogan'], 'r': 'El párrafo'}, {'p': 'Las palabras que empiezan por eje- (ejemplo) se escriben con...', 'o': ['J', 'G'], 'r': 'J'}],
            [{'p': '¿Qué punto se usa para separar dos párrafos diferentes?', 'o': ['Punto y aparte', 'Punto y seguido'], 'r': 'Punto y aparte'}, {'p': '¿Se escriben con G las palabras que empiezan por gest-?', 'o': ['Sí', 'No'], 'r': 'Sí'}, {'p': '¿Cuál es la función principal de un anuncio publicitario?', 'o': ['Convencer al receptor', 'Contar una historia'], 'r': 'Convencer al receptor'}],
            [{'p': '¿Qué letra llevan las palabras que terminan en -jero/a?', 'o': ['J', 'G'], 'r': 'J'}, {'p': '¿Cómo se llama la frase corta y llamativa de un anuncio?', 'o': ['Eslogan', 'Cuerpo del texto'], 'r': 'Eslogan'}, {'p': 'Las formas verbales cuyos infinitivos no tienen G ni J se escriben con...', 'o': ['J', 'G'], 'r': 'J'}]
        ]
    },
    'U3_LEN': {
        'titulo': 'Versoladas (Los Determinantes)',
        'examenes': [
            [{'p': '¿Qué palabras acompañan al nombre para concretarlo?', 'o': ['Determinantes', 'Adjetivos'], 'r': 'Determinantes'}, {'p': '¿Cuáles son los artículos determinados?', 'o': ['el, la, los, las', 'un, una, unos, unas'], 'r': 'el, la, los, las'}, {'p': '¿Qué indican los determinantes posesivos?', 'o': ['Pertenencia', 'Cercanía'], 'r': 'Pertenencia'}],
            [{'p': '¿"Esa" y "esos" son demostrativos de qué distancia?', 'o': ['Media', 'Lejanía'], 'r': 'Media'}, {'p': 'En "Nuestros libros", ¿qué tipo de determinante es "Nuestros"?', 'o': ['Posesivo', 'Artículo'], 'r': 'Posesivo'}, {'p': '¿Los determinantes concuerdan con el nombre en...?', 'o': ['Género y número', 'Solo género'], 'r': 'Género y número'}],
            [{'p': '¿Cuál es un demostrativo de lejanía?', 'o': ['Aquel', 'Este'], 'r': 'Aquel'}, {'p': '¿Qué artículo se usa para "águila" (femenino con A tónica)?', 'o': ['El', 'La'], 'r': 'El'}, {'p': '¿"Tus" es un posesivo de un solo poseedor?', 'o': ['Sí', 'No'], 'r': 'Sí'}]
        ]
    },
    'U4_LEN': {
        'titulo': 'Canal manualidades (Numerales e Indefinidos)',
        'examenes': [
            [{'p': '¿Qué numerales indican orden (primero, segundo...)?', 'o': ['Ordinales', 'Cardinales'], 'r': 'Ordinales'}, {'p': '¿Qué indican los determinantes indefinidos?', 'o': ['Cantidad imprecisa', 'Cantidad exacta'], 'r': 'Cantidad imprecisa'}, {'p': '¿Dónde aparecen los materiales en un texto instructivo?', 'o': ['Lista de materiales', 'Procedimiento'], 'r': 'Lista de materiales'}],
            [{'p': '¿"Varios" y "algunas" son determinantes de qué tipo?', 'o': ['Indefinidos', 'Numerales'], 'r': 'Indefinidos'}, {'p': '¿Cómo se escribe el numeral ordinal de 10?', 'o': ['Décimo', 'Diezavo'], 'r': 'Décimo'}, {'p': '¿Qué texto explica cómo hacer algo paso a paso?', 'o': ['Instructivo', 'Noticia'], 'r': 'Instructivo'}],
            [{'p': '¿Cuál es un numeral cardinal?', 'o': ['Cien', 'Centésimo'], 'r': 'Cien'}, {'p': '¿"Pocos" es un determinante indefinido?', 'o': ['Sí', 'No'], 'r': 'Sí'}, {'p': 'Los verbos en manualidades suelen estar en...', 'o': ['Imperativo o Infinitivo', 'Pasado'], 'r': 'Imperativo o Infinitivo'}]
        ]
    },
    'U5_LEN': {
        'titulo': 'Pasatiempo formal (Enlaces)',
        'examenes': [
            [{'p': '¿Qué palabras unen palabras u oraciones que dependen entre sí?', 'o': ['Preposiciones', 'Sustantivos'], 'r': 'Preposiciones'}, {'p': '¿Cuál es una conjunción copulativa?', 'o': ['y, e, ni', 'o, u'], 'r': 'y, e, ni'}, {'p': '¿Las preposiciones cambian de género o número?', 'o': ['No, son invariables', 'Sí'], 'r': 'No, son invariables'}],
            [{'p': '¿"Pero" y "aunque" son conjunciones de qué tipo?', 'o': ['Adversativas', 'Disyuntivas'], 'r': 'Adversativas'}, {'p': '¿Qué preposición indica lugar o destino?', 'o': ['A', 'De'], 'r': 'A'}, {'p': '¿Las conjunciones disyuntivas (o, u) indican elección?', 'o': ['Sí', 'No'], 'r': 'Sí'}],
            [{'p': 'Completa la lista: a, ante, bajo, cabe, con...', 'o': ['contra', 'porque'], 'r': 'contra'}, {'p': '¿Cuál es la función de los enlaces?', 'o': ['Unir palabras', 'Describir nombres'], 'r': 'Unir palabras'}, {'p': '¿"Hacia" es una preposición?', 'o': ['Sí', 'No'], 'r': 'Sí'}]
        ]
    },
    'U6_LEN': {
        'titulo': 'Aires de leyenda (El Verbo)',
        'examenes': [
            [{'p': '¿Qué parte del verbo aporta el significado?', 'o': ['Raíz', 'Desinencia'], 'r': 'Raíz'}, {'p': '¿Qué modo indica una orden o ruego?', 'o': ['Imperativo', 'Indicativo'], 'r': 'Imperativo'}, {'p': '¿"Vivir" pertenece a qué conjugación?', 'o': ['Tercera (-ir)', 'Segunda (-er)'], 'r': 'Tercera (-ir)'}],
            [{'p': '¿Qué modo expresa deseos, dudas o posibilidades?', 'o': ['Subjuntivo', 'Indicativo'], 'r': 'Subjuntivo'}, {'p': '¿"Caminábamos" es un tiempo...?', 'o': ['Pasado', 'Futuro'], 'r': 'Pasado'}, {'p': 'Las terminaciones que indican persona y número son las...', 'o': ['Desinencias', 'Raíces'], 'r': 'Desinencias'}],
            [{'p': '¿El modo indicativo expresa acciones reales?', 'o': ['Sí', 'No'], 'r': 'Sí'}, {'p': '¿Cuál es la raíz de "jugábamos"?', 'o': ['jug-', 'juga-'], 'r': 'jug-'}, {'p': '¿"Comeré" está en primera persona singular?', 'o': ['Sí', 'No'], 'r': 'Sí'}]
        ]
    },
    'U7_LEN': {
        'titulo': 'Voces del mundo (Expositivos)',
        'examenes': [
            [{'p': '¿Qué es una familia de palabras?', 'o': ['Palabras con misma raíz', 'Palabras que riman'], 'r': 'Palabras con misma raíz'}, {'p': '¿Un texto expositivo debe ser objetivo?', 'o': ['Sí', 'No'], 'r': 'Sí'}, {'p': '¿Cuál es la raíz común de pan, panadero y panadería?', 'o': ['pan', 'pana'], 'r': 'pan'}],
            [{'p': '¿Qué tipo de texto explica un tema de forma clara?', 'o': ['Expositivo', 'Poema'], 'r': 'Expositivo'}, {'p': '¿"Florero" pertenece a la familia de "flor"?', 'o': ['Sí', 'No'], 'r': 'Sí'}, {'p': 'En un texto expositivo, ¿se usan opiniones personales?', 'o': ['No, solo hechos', 'Sí, muchas'], 'r': 'No, solo hechos'}],
            [{'p': 'Identifica la palabra intrusa en la familia "mar":', 'o': ['Martillo', 'Maremoto'], 'r': 'Martillo'}, {'p': '¿Dónde solemos encontrar textos expositivos?', 'o': ['Enciclopedias', 'Libros de chistes'], 'r': 'Enciclopedias'}, {'p': '¿"Submarino" es de la familia de "mar"?', 'o': ['Sí', 'No'], 'r': 'Sí'}]
        ]
    },
    'U8_LEN': {
        'titulo': 'Correspondencia (Pronombres)',
        'examenes': [
            [{'p': '¿Qué palabras sustituyen al nombre para no repetirlo?', 'o': ['Pronombres personales', 'Adjetivos'], 'r': 'Pronombres personales'}, {'p': '¿Cuáles son los pronombres de 1ª persona?', 'o': ['Yo, nosotros/as', 'Tú, vosotros/as'], 'r': 'Yo, nosotros/as'}, {'p': '¿"Ellos" es un pronombre de qué persona?', 'o': ['Tercera', 'Segunda'], 'r': 'Tercera'}],
            [{'p': '¿Qué pronombre sustituye a "María y tú"?', 'o': ['Vosotras', 'Ellas'], 'r': 'Vosotras'}, {'p': '¿"Él" lleva tilde cuando es pronombre?', 'o': ['Sí', 'No'], 'r': 'Sí'}, {'p': '¿"Me, te, se, nos, os" son también pronombres?', 'o': ['Sí', 'No'], 'r': 'Sí'}],
            [{'p': '¿Cuál es el pronombre de 2ª persona singular?', 'o': ['Tú / Usted', 'Él'], 'r': 'Tú / Usted'}, {'p': '¿"Nosotros" es plural?', 'o': ['Sí', 'No'], 'r': 'Sí'}, {'p': 'En "Ellas vienen", ¿qué palabra es el pronombre?', 'o': ['Ellas', 'Vienen'], 'r': 'Ellas'}]
        ]
    }
}
