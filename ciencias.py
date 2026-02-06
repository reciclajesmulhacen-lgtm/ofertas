# ciencias.py - Edelvives FanFest Naturaleza 5 + Sociales 5

TEMARIO = {
    'U1': {
        'titulo': 'Seres vivos (Clasificación, ciclos vitales)',
        'examenes': [
            [
                {'p': '¿Qué tienen en común todos los seres vivos?', 'o': ['Nacen, crecen, se reproducen', 'Solo comen', 'Solo duermen'], 'r': 'Nacen, crecen, se reproducen'},
                {'p': '¿Qué animal es vertebrado?', 'o': ['Perro', 'Insecto', 'Medusa'], 'r': 'Perro'},
                {'p': '¿Qué planta hace fotosíntesis?', 'o': ['Todas las plantas verdes', 'Solo las flores', 'Solo los árboles'], 'r': 'Todas las plantas verdes'},
                {'p': 'En el ciclo de la mariposa, ¿qué viene después del huevo?', 'o': ['Oruga', 'Capullo', 'Mariposa'], 'r': 'Oruga'},
                {'p': 'Animal invertebrado ejemplo:', 'o': ['Araña', 'Pez', 'Pájaro'], 'r': 'Araña'},
                {'p': '¿Qué son los hongos?', 'o': ['Seres vivos que no son plantas ni animales', 'Plantas sin clorofila', 'Animales microscópicos'], 'r': 'Seres vivos que no son plantas ni animales'},
                {'p': 'Ciclo vital de la rana: ¿qué es el renacuajo?', 'o': ['Larva acuática', 'Adulto terrestre', 'Huevo'], 'r': 'Larva acuática'},
                {'p': 'Animal carnívoro come:', 'o': ['Carne', 'Plantas', 'Ambos'], 'r': 'Carne'},
                {'p': 'Planta herbívora NO existe, las plantas:', 'o': ['Hacen fotosíntesis', 'Comen carne', 'Beben sangre'], 'r': 'Hacen fotosíntesis'},
                {'p': '¿Qué es la metamorfosis?', 'o': ['Cambio de forma en el ciclo vital', 'Crecimiento sin cambios', 'Nacimiento directo'], 'r': 'Cambio de forma en el ciclo vital'}
            ],
            [
                {'p': '¿Cuál es omnívoro?', 'o': ['Oso', 'Aguila', 'Cocodrilo'], 'r': 'Oso'},
                {'p': 'Ciclo de la mariposa tiene ___ etapas', 'o': ['4', '3', '5'], 'r': '4'},
                {'p': 'Animal herbívoro ejemplo:', 'o': ['Vaca', 'León', 'Serpiente'], 'r': 'Vaca'},
                {'p': '¿Qué son las bacterias?', 'o': ['Microorganismos unicelulares', 'Plantas pequeñas', 'Animales minúsculos'], 'r': 'Microorganismos unicelulares'},
                {'p': 'En ciclo rana: renacuajo → ___ → rana', 'o': ['Patas', 'Cola', 'Branquias'], 'r': 'Patas'},
                {'p': '¿Qué clasificación es correcta?', 'o': ['Vertebrados: peces, aves, mamíferos', 'Vertebrados: plantas, hongos', 'Invertebrados: perros, pájaros'], 'r': 'Vertebrados: peces, aves, mamíferos'},
                {'p': 'Planta que NO hace fotosíntesis:', 'o': ['Hongos (no son plantas)', 'Pinos', 'Flores'], 'r': 'Hongos (no son plantas)'},
                {'p': 'Ciclo vital de pollo: huevo → ___ → pollo', 'o': ['Polluelo', 'Gallo', 'Nido'], 'r': 'Polluelo'},
                {'p': 'Microorganismos útiles ejemplo:', 'o': ['Lactobacilos (yogur)', 'Virus gripe', 'Hongos patógenos'], 'r': 'Lactobacilos (yogur)'},
                {'p': 'Animal que pasa por metamorfosis completa:', 'o': ['Mariposa', 'Perro', 'Pájaro'], 'r': 'Mariposa'}
            ],
            [
                {'p': '¿Qué come un herbívoro?', 'o': ['Plantas', 'Carne', 'Ambos'], 'r': 'Plantas'},
                {'p': 'Etapas ciclo mariposa (orden):', 'o': ['Huevo, oruga, capullo, mariposa', 'Mariposa, capullo, oruga, huevo', 'Oruga, mariposa, huevo, capullo'], 'r': 'Huevo, oruga, capullo, mariposa'},
                {'p': 'Ejemplo bacteria útil:', 'o': ['Yogur', 'Gripe', 'Sarna'], 'r': 'Yogur'},
                {'p': 'Animal ovíparo:', 'o': ['Gallina', 'Humano', 'Ballena'], 'r': 'Gallina'},
                {'p': 'Planta carnívora ejemplo:', 'o': ['Drosera', 'Pino', 'Rosa'], 'r': 'Drosera'},
                {'p': '¿Qué es un virus?', 'o': ['No es ser vivo, necesita célula para reproducirse', 'Bacteria muy pequeña', 'Hongos microscópicos'], 'r': 'No es ser vivo, necesita célula para reproducirse'},
                {'p': 'Ciclo vital humano: bebé → ___ → adulto', 'o': ['Niño', 'Anciano', 'Embarazo'], 'r': 'Niño'},
                {'p': 'Animal vivíparo ejemplo:', 'o': ['Gato', 'Cocodrilo', 'Pájaro'], 'r': 'Gato'},
                {'p': 'Reino fungi incluye:', 'o': ['Hongos, setas, levaduras', 'Plantas, árboles', 'Animales, insectos'], 'r': 'Hongos, setas, levaduras'},
                {'p': 'Metamorfosis incompleta ejemplo:', 'o': ['Saltamontes', 'Mariposa', 'Rana'], 'r': 'Saltamontes'}
            ]
        ]
    },

    'U2': {
        'titulo': 'Sistemas humanos (Digestivo, circulatorio, respiratorio)',
        'examenes': [
            [
                {'p': '¿Qué función tiene el estómago?', 'o': ['Digestir alimentos', 'Bombear sangre', 'Respirar'], 'r': 'Digestir alimentos'},
                {'p': 'Órgano que bombea sangre:', 'o': ['Corazón', 'Pulmón', 'Hígado'], 'r': 'Corazón'},
                {'p': '¿Dónde se intercambia oxígeno?', 'o': ['Pulmones', 'Estómago', 'Corazón'], 'r': 'Pulmones'},
                {'p': 'Orden digestión: boca → ___ → estómago', 'o': ['Esófago', 'Intestino', 'Hígado'], 'r': 'Esófago'},
                {'p': '¿Qué transporta la sangre?', 'o': ['Oxígeno y nutrientes', 'Aire', 'Alimentos'], 'r': 'Oxígeno y nutrientes'},
                {'p': 'Órgano respiratorio principal:', 'o': ['Pulmón', 'Corazón', 'Estómago'], 'r': 'Pulmón'},
                {'p': 'Intestino delgado función:', 'o': ['Absorber nutrientes', 'Bombear sangre', 'Filtrar aire'], 'r': 'Absorber nutrientes'},
                {'p': '¿Qué son las venas?', 'o': ['Llevan sangre al corazón', 'Llevan sangre desde corazón', 'Son pulmones'], 'r': 'Llevan sangre al corazón'},
                {'p': '¿Qué hacen los alvéolos?', 'o': ['Intercambian oxígeno y CO₂', 'Bombear sangre', 'Digieren comida'], 'r': 'Intercambian oxígeno y CO₂'},
                {'p': 'Hígado función principal:', 'o': ['Filtrar sangre, producir bilis', 'Respirar', 'Bombear'], 'r': 'Filtrar sangre, producir bilis'}
            ],
            [
                {'p': 'Órganos digestivos (orden): boca, ___ , estómago, intestino', 'o': ['esófago', 'pulmón', 'vena'], 'r': 'esófago'},
                {'p': 'Corazón tiene ___ cavidades', 'o': ['4', '2', '3'], 'r': '4'},
                {'p': '¿Qué entra por la tráquea?', 'o': ['Aire', 'Comida', 'Sangre'], 'r': 'Aire'},
                {'p': 'Intestino grueso absorbe:', 'o': ['Agua', 'Oxígeno', 'Nutrientes'], 'r': 'Agua'},
                {'p': 'Arterias llevan sangre:', 'o': ['Desde el corazón', 'Al corazón', 'Solo oxígeno'], 'r': 'Desde el corazón'},
                {'p': 'Diafragma función:', 'o': ['Ayuda a respirar', 'Digiere comida', 'Bombea sangre'], 'r': 'Ayuda a respirar'},
                {'p': 'Páncreas produce:', 'o': ['Insulina, enzimas digestivas', 'Sangre', 'Oxígeno'], 'r': 'Insulina, enzimas digestivas'},
                {'p': 'Bronquios están en:', 'o': ['Pulmones', 'Corazón', 'Estómago'], 'r': 'Pulmones'},
                {'p': 'Vaso sanguíneo más grande:', 'o': ['Aorta', 'Vena cava', 'Capilar'], 'r': 'Aorta'},
                {'p': 'Riocristalino NO es sistema humano, pertenece a:', 'o': ['Ojo', 'Digestivo', 'Respiratorio'], 'r': 'Ojo'}
            ],
            [
                {'p': '¿Qué digiere proteínas?', 'o': ['Jugo gástrico', 'Bilis', 'Insulina'], 'r': 'Jugo gástrico'},
                {'p': 'Pulmones se encuentran en la:', 'o': ['Cavidad torácica', 'Abdomen', 'Cabeza'], 'r': 'Cavidad torácica'},
                {'p': 'Corazón derecho bombea sangre a:', 'o': ['Pulmones', 'Cuerpo', 'Hígado'], 'r': 'Pulmones'},
                {'p': 'Hígado produce:', 'o': ['Bilis', 'Oxígeno', 'Sangre'], 'r': 'Bilis'},
                {'p': 'Capilares función:', 'o': ['Intercambio sustancias', 'Transporte rápido', 'Almacenamiento'], 'r': 'Intercambio sustancias'},
                {'p': 'Laringe función:', 'o': ['Voz y paso aire', 'Digiere comida', 'Filtra sangre'], 'r': 'Voz y paso aire'},
                {'p': 'Riñones filtran:', 'o': ['Sangre (sistema urinario)', 'Aire', 'Alimentos'], 'r': 'Sangre (sistema urinario)'},
                {'p': 'Glándulas salivales producen:', 'o': ['Saliva', 'Bilis', 'Jugo gástrico'], 'r': 'Saliva'},
                {'p': 'Ventrículo izquierdo bombea a:', 'o': ['Aorta (cuerpo)', 'Pulmones', 'Venas'], 'r': 'Aorta (cuerpo)'},
                {'p': 'Alvéolos rodeados por:', 'o': ['Capilares sanguíneos', 'Arterias grandes', 'Venas pulmonares'], 'r': 'Capilares sanguíneos'}
            ]
        ]
    },

    'U3': {
        'titulo': 'Energía (Renovables/no renovables)',
        'examenes': [
            [
                {'p': 'Energía solar es:', 'o': ['Renovable', 'No renovable', 'Química'], 'r': 'Renovable'},
                {'p': 'Energía del carbón es:', 'o': ['No renovable', 'Renovable', 'Eléctrica'], 'r': 'No renovable'},
                {'p': 'Energía eólica viene de:', 'o': ['Viento', 'Sol', 'Agua'], 'r': 'Viento'},
                {'p': 'Petróleo se tarda millones de años en:', 'o': ['Formarse', 'Quemarse', 'Transportarse'], 'r': 'Formarse'},
                {'p': 'Energía hidráulica usa:', 'o': ['Agua en movimiento', 'Carbón', 'Viento'], 'r': 'Agua en movimiento'},
                {'p': 'Energía geotérmica del:', 'o': ['Interior Tierra', 'Sol', 'Mar'], 'r': 'Interior Tierra'},
                {'p': 'Gas natural es:', 'o': ['No renovable', 'Renovable', 'Nuclear'], 'r': 'No renovable'},
                {'p': 'Biomasa ejemplo:', 'o': ['Madera, restos vegetales', 'Petróleo', 'Uranio'], 'r': 'Madera, restos vegetales'},
                {'p': 'Energía mareomotriz del:', 'o': ['Mareas mar', 'Sol', 'Viento'], 'r': 'Mareas mar'},
                {'p': 'Nuclear NO es renovable porque:', 'o': ['Uranio limitado', 'Sol ilimitado', 'Viento infinito'], 'r': 'Uranio limitado'}
            ],
            [
                {'p': 'Paneles solares captan:', 'o': ['Luz solar', 'Viento', 'Calor tierra'], 'r': 'Luz solar'},
                {'p': 'Molinos eólicos producen:', 'o': ['Electricidad', 'Calor', 'Combustible'], 'r': 'Electricidad'},
                {'p': 'Central nuclear usa:', 'o': ['Fisión uranio', 'Quema carbón', 'Paneles solares'], 'r': 'Fisión uranio'},
                {'p': 'Energía renovable ilimitada:', 'o': ['Solar', 'Petróleo', 'Carbón'], 'r': 'Solar'},
                {'p': 'Hidroeléctrica almacena agua en:', 'o': ['Presa', 'Pozo', 'Tanque'], 'r': 'Presa'},
                {'p': 'Combustibles fósiles son:', 'o': ['Carbón, petróleo, gas', 'Sol, viento, agua', 'Biomasa, nuclear'], 'r': 'Carbón, petróleo, gas'},
                {'p': 'Energía de la biomasa es:', 'o': ['Renovable', 'No renovable', 'Química'], 'r': 'Renovable'},
                {'p': 'Central térmica quema:', 'o': ['Carbón o gas', 'Uranio', 'Madera'], 'r': 'Carbón o gas'},
                {'p': 'Aerogenerador es:', 'o': ['Molino viento', 'Panel solar', 'Turbina agua'], 'r': 'Molino viento'},
                {'p': 'Energía no renovable se agota:', 'o': ['En siglos', 'En millones años', 'Nunca'], 'r': 'En siglos'}
            ],
            [
                {'p': 'Fotovoltaica convierte:', 'o': ['Luz → electricidad', 'Calor → luz', 'Viento → calor'], 'r': 'Luz → electricidad'},
                {'p': 'Central hidroeléctrica necesita:', 'o': ['Agua, salto altura', 'Carbón', 'Sol directo'], 'r': 'Agua, salto altura'},
                {'p': 'Uranio energía:', 'o': ['Nuclear', 'Química', 'Eléctrica'], 'r': 'Nuclear'},
                {'p': 'Ventaja energía solar:', 'o': ['Inagotable', 'Barata instalar', 'Contamina poco'], 'r': 'Inagotable'},
                {'p': 'Desventaja carbón:', 'o': ['Contamina mucho', 'Caro', 'Lento'], 'r': 'Contamina mucho'},
                {'p': 'Biogás produce:', 'o': ['Restos orgánicos', 'Sol', 'Viento'], 'r': 'Restos orgánicos'},
                {'p': 'Energía mareas:', 'o': ['Renovable', 'No renovable', 'Nuclear'], 'r': 'Renovable'},
                {'p': 'Transformador convierte:', 'o': ['Alta → baja tensión', 'DC → AC', 'Calor → electricidad'], 'r': 'Alta → baja tensión'},
                {'p': 'Parque eólico tiene:', 'o': ['Muchos aerogeneradores', 'Paneles solares', 'Presas'], 'r': 'Muchos aerogeneradores'},
                {'p': 'Combustible fósil más limpio:', 'o': ['Gas natural', 'Carbón', 'Petróleo'], 'r': 'Gas natural'}
            ]
        ]
    },

    'U4': {
        'titulo': 'Fuerzas (Gravedad, fricción, máquinas simples)',
        'examenes': [
            [
                {'p': 'Fuerza que atrae hacia la Tierra:', 'o': ['Gravedad', 'Fricción', 'Imán'], 'r': 'Gravedad'},
                {'p': 'Fricción se produce entre:', 'o': ['Superficies en contacto', 'Solo líquidos', 'Solo gases'], 'r': 'Superficies en contacto'},
                {'p': 'Palanca es máquina simple que:', 'o': ['Multiplica fuerza', 'Aumenta distancia', 'Cambia dirección'], 'r': 'Multiplica fuerza'},
                {'p': 'Polea sirve para:', 'o': ['Elevar cargas', 'Cortar', 'Girar'], 'r': 'Elevar cargas'},
                {'p': 'Fuerza de atracción entre imanes:', 'o': ['Magnética', 'Eléctrica', 'Gravitatoria'], 'r': 'Magnética'},
                {'p': 'Plano inclinado reduce:', 'o': ['Fuerza necesaria', 'Distancia', 'Peso'], 'r': 'Fuerza necesaria'},
                {'p': 'Fricción útil ejemplo:', 'o': ['Frenar coche', 'Deslizar hielo', 'Rodar rueda'], 'r': 'Frenar coche'},
                {'p': 'Gravedad en la Luna es:', 'o': ['Menor que en Tierra', 'Igual', 'Mayor'], 'r': 'Menor que en Tierra'},
                {'p': 'Cuerda tensa produce fuerza:', 'o': ['De tensión', 'Gravitatoria', 'Eléctrica'], 'r': 'De tensión'},
                {'p': 'Máquina simple NO es:', 'o': ['Motor eléctrico', 'Polea', 'Palanca'], 'r': 'Motor eléctrico'}
            ],
            [
                {'p': '¿Qué reduce la fricción?', 'o': ['Aceite, lubricante', 'Arena', 'Peso'], 'r': 'Aceite, lubricante'},
                {'p': 'Polea fija multiplica:', 'o': ['Dirección fuerza', 'Fuerza', 'Distancia'], 'r': 'Dirección fuerza'},
                {'p': 'Fuerza normal es:', 'o': ['Perpendicular superficie', 'Paralela', 'Oblicua'], 'r': 'Perpendicular superficie'},
                {'p': 'Cuña es máquina simple usada para:', 'o': ['Separar', 'Elevar', 'Girar'], 'r': 'Separar'},
                {'p': 'Peso es fuerza de:', 'o': ['Gravedad', 'Fricción', 'Imán'], 'r': 'Gravedad'},
                {'p': 'Polea móvil ventaja:', 'o': ['Multiplica fuerza', 'Aumenta distancia', 'Cambia dirección'], 'r': 'Multiplica fuerza'},
                {'p': 'Fricción en hielo es:', 'o': ['Muy baja', 'Muy alta', 'Nula'], 'r': 'Muy baja'},
                {'p': 'Rueda es aplicación de:', 'o': ['Plano inclinado', 'Palanca', 'Polea'], 'r': 'Plano inclinado'},
                {'p': 'Fuerza elástica ejemplo:', 'o': ['Goma elástica', 'Imán', 'Gravedad'], 'r': 'Goma elástica'},
                {'p': 'Tijeras son:', 'o': ['Doble cuña', 'Palanca', 'Polea'], 'r': 'Doble cuña'}
            ],
            [
                {'p': 'Gravedad universal atrae:', 'o': ['Entre masas', 'Solo Tierra', 'Solo imanes'], 'r': 'Entre masas'},
                {'p': 'Ventaja fricción en neumáticos:', 'o': ['Agarre carretera', 'Desgaste', 'Calor'], 'r': 'Agarre carretera'},
                {'p': 'Palanca de 1er grado: fulcro entre ___ y resistencia', 'o': ['Esfuerzo', 'Peso', 'Fuerza'], 'r': 'Esfuerzo'},
                {'p': 'Tornillo es:', 'o': ['Plano inclinado enrollado', 'Cuña', 'Palanca'], 'r': 'Plano inclinado enrollado'},
                {'p': 'Fuerza de flotación debe a:', 'o': ['Empuje líquido', 'Gravedad', 'Fricción'], 'r': 'Empuje líquido'},
                {'p': 'Máquina compuesta ejemplo:', 'o': ['Bicicleta', 'Polea simple', 'Palanca'], 'r': 'Bicicleta'},
                {'p': 'Coeficiente fricción depende de:', 'o': ['Materiales superficies', 'Solo peso', 'Solo velocidad'], 'r': 'Materiales superficies'},
                {'p': 'Polea con 3 cabos multiplica fuerza por:', 'o': ['3', '2', '4'], 'r': '3'},
                {'p': 'Fuerza centrífuga se siente al:', 'o': ['Girar rápido', 'Ir recto', 'Parar'], 'r': 'Girar rápido'},
                {'p': 'Destornillador usado como:', 'o': ['Palanca', 'Cuña', 'Polea'], 'r': 'Palanca'}
            ]
        ]
    },

    'U5': {
        'titulo': 'Sistema Solar (Planetas, rotación/traslación)',
        'examenes': [
            [
                {'p': '¿Cuántos planetas tiene el Sistema Solar?', 'o': ['8', '9', '7'], 'r': '8'},
                {'p': 'Planeta más cercano al Sol:', 'o': ['Mercurio', 'Venus', 'Tierra'], 'r': 'Mercurio'},
                {'p': 'Rotación de la Tierra produce:', 'o': ['Día y noche', 'Estaciones', 'Año'], 'r': 'Día y noche'},
                {'p': 'Traslación alrededor del Sol dura:', 'o': ['1 año', '24 horas', '1 mes'], 'r': '1 año'},
                {'p': 'Planeta con anillos:', 'o': ['Saturno', 'Júpiter', 'Urano'], 'r': 'Saturno'},
                {'p': 'Luna es satélite de:', 'o': ['Tierra', 'Marte', 'Júpiter'], 'r': 'Tierra'},
                {'p': 'Mayor planeta:', 'o': ['Júpiter', 'Saturno', 'Tierra'], 'r': 'Júpiter'},
                {'p': 'Eje Tierra inclinado produce:', 'o': ['Estaciones', 'Día/noche', 'Mareas'], 'r': 'Estaciones'},
                {'p': 'Planeta rojo:', 'o': ['Marte', 'Venus', 'Mercurio'], 'r': 'Marte'},
                {'p': 'Cometas tienen órbita:', 'o': ['Elíptica muy alargada', 'Circular', 'Parabólica'], 'r': 'Elíptica muy alargada'}
            ],
            [
                {'p': 'Venus es el planeta más:', 'o': ['Caliente', 'Frío', 'Lejano'], 'r': 'Caliente'},
                {'p': 'Asteroides están entre:', 'o': ['Marte y Júpiter', 'Tierra y Venus', 'Saturno y Urano'], 'r': 'Marte y Júpiter'},
                {'p': 'Sol contiene ___ % hidrógeno', 'o': ['Más del 70%', '50%', '10%'], 'r': 'Más del 70%'},
                {'p': 'Perihelio: distancia mínima al', 'o': ['Sol', 'Tierra', 'Luna'], 'r': 'Sol'},
                {'p': 'Afélio: distancia máxima al', 'o': ['Sol', 'Luna', 'Marte'], 'r': 'Sol'},
                {'p': 'Planeta con más lunas:', 'o': ['Júpiter', 'Saturno', 'Urano'], 'r': 'Júpiter'},
                {'p': 'Neptuno conocido por:', 'o': ['Vientos supersónicos', 'Anillos', 'Volcanes'], 'r': 'Vientos supersónicos'},
                {'p': 'Mercurio NO tiene:', 'o': ['Atmósfera', 'Rotación', 'Órbita'], 'r': 'Atmósfera'},
                {'p': 'Cinturón Kuiper contiene:', 'o': ['Plutón y objetos transneptunianos', 'Asteroides', 'Cometas'], 'r': 'Plutón y objetos transneptunianos'},
                {'p': 'Eclipse solar ocurre cuando Luna está entre:', 'o': ['Sol y Tierra', 'Tierra y Sol', 'Luna y Marte'], 'r': 'Sol y Tierra'}
            ],
            [
                {'p': 'Urano rota sobre su:', 'o': ['Lado (eje casi horizontal)', 'Polo vertical', 'Eje inclinado 45°'], 'r': 'Lado (eje casi horizontal)'},
                {'p': 'Tierra tarda 365 días en:', 'o': ['Traslación (año)', 'Rotación (día)', 'Órbita lunar'], 'r': 'Traslación (año)'},
                {'p': 'Satélites artificiales orbitan por:', 'o': ['Gravedad Tierra', 'Motores constantes', 'Imanes'], 'r': 'Gravedad Tierra'},
                {'p': 'Planeta enano ejemplo:', 'o': ['Plutón', 'Marte', 'Tierra'], 'r': 'Plutón'},
                {'p': 'Maremotos en planetas gaseosos por:', 'o': ['Gravedad lunas', 'Rotación rápida', 'Viento solar'], 'r': 'Gravedad lunas'},
                {'p': 'Sol masa representa ___ % Sistema Solar', 'o': ['99,8%', '50%', '80%'], 'r': '99,8%'},
                {'p': 'Órbita elíptica significa:', 'o': ['Distancia variable al Sol', 'Distancia constante', 'Sin órbita'], 'r': 'Distancia variable al Sol'},
                {'p': 'Fases lunares por:', 'o': ['Posición relativa Sol-Tierra-Luna', 'Rotación Tierra', 'Traslación Luna'], 'r': 'Posición relativa Sol-Tierra-Luna'},
                {'p': 'Cromósfera está en:', 'o': ['Sol (entre fotosfera y corona)', 'Tierra', 'Júpiter'], 'r': 'Sol (entre fotosfera y corona)'},
                {'p': 'Velocidad orbital Tierra:', 'o': ['30 km/s', '300 km/s', '3 km/s'], 'r': '30 km/s'}
            ]
        ]
    }
}

# Ciencias Sociales FanFest 5 (temas transversales)
TEMARIO.update({
    'Social1': {
        'titulo': 'Continentes y población',
        'examenes': [
            [
                {'p': 'Continente más poblado:', 'o': ['Asia', 'África', 'Europa'], 'r': 'Asia'},
                {'p': 'Cuántos continentes:', 'o': ['7', '6', '5'], 'r': '7'},
                {'p': 'País más poblado mundo:', 'o': ['China', 'India', 'EEUU'], 'r': 'China'},
                {'p': 'España pertenece a:', 'o': ['Europa', 'África', 'Asia'], 'r': 'Europa'},
                {'p': 'Océano más grande:', 'o': ['Pacífico', 'Atlántico', 'Índico'], 'r': 'Pacífico'},
                {'p': 'Andalucía comunidad:', 'o': ['Autónoma', 'Provincial', 'Municipal'], 'r': 'Autónoma'},
                {'p': 'Alfacar provincia:', 'o': ['Granada', 'Málaga', 'Sevilla'], 'r': 'Granada'},
                {'p': 'Capital España:', 'o': ['Madrid', 'Barcelona', 'Sevilla'], 'r': 'Madrid'},
                {'p': 'Capital Granada:', 'o': ['Granada', 'Alfacar', 'Motril'], 'r': 'Granada'},
                {'p': 'Población mundial aprox.:', 'o': ['8.000 millones', '5.000 millones', '10.000 millones'], 'r': '8.000 millones'}
            ]
        ]
    },
    'Social2': {
        'titulo': 'Economía y transportes',
        'examenes': [
            [
                {'p': 'Producto primario ejemplo:', 'o': ['Trigo', 'Coche', 'Profesor'], 'r': 'Trigo'},
                {'p': 'Producto industrial ejemplo:', 'o': ['Televisor', 'Tomate', 'Pescado'], 'r': 'Televisor'},
                {'p': 'Servicio ejemplo:', 'o': ['Médico', 'Leche', 'Zapatos'], 'r': 'Médico'},
                {'p': 'Transporte terrestre:', 'o': ['Tren', 'Avión', 'Barco'], 'r': 'Tren'},
                {'p': 'Moneda España:', 'o': ['Euro', 'Peseta', 'Dólar'], 'r': 'Euro'},
                {'p': 'Comercio internacional usa:', 'o': ['Barcos, aviones', 'Solo camiones', 'Solo trenes'], 'r': 'Barcos, aviones'},
                {'p': 'Agricultura es:', 'o': ['Primaria', 'Industrial', 'Servicio'], 'r': 'Primaria'},
                {'p': 'Aeropuerto es transporte:', 'o': ['Aéreo', 'Marítimo', 'Terrestre'], 'r': 'Aéreo'},
                {'p': 'Fábrica produce:', 'o': ['Productos industriales', 'Servicios', 'Agricultura'], 'r': 'Productos industriales'},
                {'p': 'Número emergencias España:', 'o': ['112', '911', '061'], 'r': '112'}
            ]
        ]
    },
    'Social3': {
        'titulo': 'Tiempo histórico',
        'examenes': [
            [
                {'p': 'Calendario tiene ___ días:', 'o': ['365', '360', '300'], 'r': '365'},
                {'p': 'Año bisiesto tiene:', 'o': ['366 días', '365 días', '364 días'], 'r': '366 días'},
                {'p': 'Edad Antigua termina con:', 'o': ['Caída Imperio Romano', 'Descubrimiento América', 'Revolución Industrial'], 'r': 'Caída Imperio Romano'},
                {'p': 'Historia Granada: Alhambra construida por:', 'o': ['Nazaríes', 'Reyes Católicos', 'Romanos'], 'r': 'Nazaríes'},
                {'p': 'Mes con 31 días ejemplo:', 'o': ['Enero', 'Febrero', 'Abril'], 'r': 'Enero'},
                {'p': 'Edad Media entre:', 'o': ['Caída Roma - Descubrimiento América', 'Prehistoria - Edad Antigua', 'Edad Moderna - Contemporánea'], 'r': 'Caída Roma - Descubrimiento América'},
                {'p': 'Año 2026 es:', 'o': ['Siglo XXI', 'Siglo XX', 'Siglo XIX'], 'r': 'Siglo XXI'},
                {'p': 'Semana tiene ___ días:', 'o': ['7', '6', '8'], 'r': '7'},
                {'p': 'Alfacar historia famosa:', 'o': ['Federico García Lorca', 'Colón', 'Torquemada'], 'r': 'Federico García Lorca'},
                {'p': 'Década son ___ años:', 'o': ['10', '100', '1.000'], 'r': '10'}
            ]
        ]
    }
})
