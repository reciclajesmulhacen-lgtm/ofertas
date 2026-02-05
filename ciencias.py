import random

# TEMARIO CIENCIAS NATURALES Y SOCIALES 5º (Edelvives FanFest)
TEMARIO = {
    'U1_NAT': {
        'titulo': 'Seres Vivos (Clasificación y Ciclos)',
        'examenes': [
            # Examen 1
            [
                {'p': '¿Cuál es la unidad más pequeña de un ser vivo?', 'o': ['La célula', 'El tejido', 'El órgano'], 'r': 'La célula'},
                {'p': 'Los seres vivos que fabrican su propio alimento son...', 'o': ['Autótrofos', 'Heterótrofos'], 'r': 'Autótrofos'},
                {'p': '¿A qué reino pertenece el moho?', 'o': ['Plantas', 'Hongos (Fungi)', 'Animales'], 'r': 'Hongos (Fungi)'},
                {'p': '¿Las bacterias son organismos...?', 'o': ['Unicelulares', 'Pluricelulares'], 'r': 'Unicelulares'},
                {'p': 'Las tres funciones vitales son nutrición, relación y...', 'o': ['Reproducción', 'Digestión', 'Sueño'], 'r': 'Reproducción'},
                {'p': '¿Qué instrumento usamos para ver células?', 'o': ['Telescopio', 'Microscopio', 'Lupa'], 'r': 'Microscopio'},
                {'p': 'Los animales que comen otros animales son...', 'o': ['Herbívoros', 'Carnívoros'], 'r': 'Carnívoros'},
                {'p': '¿En qué reino incluirías a una ameba?', 'o': ['Protoctistas', 'Moneras', 'Plantas'], 'r': 'Protoctistas'},
                {'p': '¿Las plantas realizan la fotosíntesis?', 'o': ['Sí', 'No'], 'r': 'Sí'},
                {'p': 'Un conjunto de células del mismo tipo forma un...', 'o': ['Órgano', 'Tejido', 'Sistema'], 'r': 'Tejido'}
            ],
            # Examen 2
            [
                {'p': '¿Qué reino no tiene núcleo definido en sus células?', 'o': ['Moneras', 'Hongos', 'Plantas'], 'r': 'Moneras'},
                {'p': 'La fotosíntesis ocurre gracias a la...', 'o': ['Clorofila', 'Sangre', 'Tierra'], 'r': 'Clorofila'},
                {'p': '¿Los hongos se desplazan?', 'o': ['Sí', 'No'], 'r': 'No'},
                {'p': '¿Qué expulsan las plantas durante la fotosíntesis?', 'o': ['Dióxido de carbono', 'Oxígeno'], 'r': 'Oxígeno'},
                {'p': 'Los seres que consumen materia orgánica son...', 'o': ['Heterótrofos', 'Autótrofos'], 'r': 'Heterótrofos'},
                {'p': '¿Una levadura es un hongo?', 'o': ['Sí', 'No'], 'r': 'Sí'},
                {'p': '¿Qué parte de la célula contiene el material genético?', 'o': ['Núcleo', 'Citoplasma', 'Membrana'], 'r': 'Núcleo'},
                {'p': '¿Las algas pertenecen al reino...?', 'o': ['Protoctistas', 'Plantas'], 'r': 'Protoctistas'},
                {'p': '¿Los virus se consideran seres vivos plenos?', 'o': ['Sí', 'No'], 'r': 'No'},
                {'p': '¿El reino animal es autótrofo?', 'o': ['Sí', 'No'], 'r': 'No'}
            ],
            # Examen 3
            [
                {'p': '¿Qué envuelve y protege a la célula?', 'o': ['Membrana', 'Núcleo', 'Orgánulos'], 'r': 'Membrana'},
                {'p': 'Los organismos pluricelulares tienen...', 'o': ['Una célula', 'Muchas células'], 'r': 'Muchas células'},
                {'p': '¿De dónde obtienen energía las plantas?', 'o': ['Del sol', 'De otros animales'], 'r': 'Del sol'},
                {'p': '¿Los champiñones hacen la fotosíntesis?', 'o': ['Sí', 'No'], 'r': 'No'},
                {'p': '¿A qué reino pertenecen las algas pardas?', 'o': ['Protoctistas', 'Plantas'], 'r': 'Protoctistas'},
                {'p': '¿Qué función permite tener descendencia?', 'o': ['Relación', 'Reproducción'], 'r': 'Reproducción'},
                {'p': '¿Los protozoos viven en ambientes húmedos?', 'o': ['Sí', 'No'], 'r': 'Sí'},
                {'p': '¿El citoplasma es líquido?', 'o': ['Sí', 'No'], 'r': 'Sí'},
                {'p': '¿Un árbol es un ser pluricelular?', 'o': ['Sí', 'No'], 'r': 'Sí'},
                {'p': '¿Las bacterias pueden ser beneficiosas?', 'o': ['Sí', 'No'], 'r': 'Sí'}
            ]
        ]
    },
    'U2_NAT': {
        'titulo': 'Sistemas Humanos (Digestivo, Circulatorio, Respiratorio)',
        'examenes': [
            # Examen 1
            [
                {'p': '¿Dónde empieza la digestión?', 'o': ['Boca', 'Estómago', 'Esófago'], 'r': 'Boca'},
                {'p': '¿Qué gas absorbemos al respirar?', 'o': ['Nitrógeno', 'Oxígeno'], 'r': 'Oxígeno'},
                {'p': '¿Qué órgano bombea la sangre?', 'o': ['Pulmones', 'Corazón', 'Hígado'], 'r': 'Corazón'},
                {'p': 'Los vasos que llevan sangre desde el corazón son...', 'o': ['Venas', 'Arterias'], 'r': 'Arterias'},
                {'p': '¿Dónde se absorben los nutrientes?', 'o': ['Intestino Delgado', 'Intestino Grueso'], 'r': 'Intestino Delgado'},
                {'p': '¿Cómo se llaman los sacos donde ocurre el intercambio de gases?', 'o': ['Alvéolos', 'Bronquios'], 'r': 'Alvéolos'},
                {'p': '¿Qué líquido ayuda a digerir en el estómago?', 'o': ['Jugos gástricos', 'Saliva'], 'r': 'Jugos gástricos'},
                {'p': 'La sangre está formada por plasma, plaquetas, glóbulos blancos y...', 'o': ['Glóbulos rojos', 'Músculos'], 'r': 'Glóbulos rojos'},
                {'p': '¿Qué tubo conecta la boca con el estómago?', 'o': ['Esófago', 'Tráquea'], 'r': 'Esófago'},
                {'p': '¿Qué función elimina desechos de la sangre?', 'o': ['Excreción', 'Digestión'], 'r': 'Excreción'}
            ],
            # Examen 2 (Misma lógica...)
            [
                {'p': '¿Qué músculo ayuda a los pulmones a moverse?', 'o': ['Bíceps', 'Diafragma'], 'r': 'Diafragma'},
                {'p': '¿Dónde se forman las heces?', 'o': ['Intestino Grueso', 'Estómago'], 'r': 'Intestino Grueso'},
                {'p': '¿Qué células defienden el cuerpo?', 'o': ['Glóbulos rojos', 'Glóbulos blancos'], 'r': 'Glóbulos blancos'},
                {'p': 'Las venas llevan la sangre...', 'o': ['Hacia el corazón', 'Fuera del corazón'], 'r': 'Hacia el corazón'},
                {'p': '¿Cómo se llama la mezcla de comida y saliva?', 'o': ['Bolo alimenticio', 'Quimo'], 'r': 'Bolo alimenticio'},
                {'p': '¿Qué órgano produce la bilis?', 'o': ['Hígado', 'Páncreas'], 'r': 'Hígado'},
                {'p': '¿Cuántas cavidades tiene el corazón humano?', 'o': ['2', '4', '3'], 'r': '4'},
                {'p': 'La tráquea se divide en dos...', 'o': ['Bronquios', 'Venas'], 'r': 'Bronquios'},
                {'p': '¿Qué plaquetas ayudan a cerrar heridas?', 'o': ['Plaquetas', 'Plasma'], 'r': 'Plaquetas'},
                {'p': '¿El aire entra por las fosas nasales?', 'o': ['Sí', 'No'], 'r': 'Sí'}
            ],
            # Examen 3
            [
                {'p': '¿Qué sistema transporta oxígeno y nutrientes?', 'o': ['Circulatorio', 'Respiratorio'], 'r': 'Circulatorio'},
                {'p': '¿Qué órgano filtra la sangre para crear orina?', 'o': ['Riñones', 'Pulmones'], 'r': 'Riñones'},
                {'p': '¿Cuál es el camino del aire tras la faringe?', 'o': ['Laringe', 'Estómago'], 'r': 'Laringe'},
                {'p': '¿Qué gas expulsamos al espirar?', 'o': ['Dióxido de carbono', 'Oxígeno'], 'r': 'Dióxido de carbono'},
                {'p': '¿Cómo se llama el movimiento del corazón cuando se contrae?', 'o': ['Sístole', 'Diástole'], 'r': 'Sístole'},
                {'p': '¿Y cuándo se relaja?', 'o': ['Diástole', 'Sístole'], 'r': 'Diástole'},
                {'p': '¿Los capilares son vasos sanguíneos muy finos?', 'o': ['Sí', 'No'], 'r': 'Sí'},
                {'p': '¿El páncreas interviene en la digestión?', 'o': ['Sí', 'No'], 'r': 'Sí'},
                {'p': '¿La saliva contiene enzimas?', 'o': ['Sí', 'No'], 'r': 'Sí'},
                {'p': '¿Es importante beber agua para el sistema excretor?', 'o': ['Sí', 'No'], 'r': 'Sí'}
            ]
        ]
    },
    'U3_NAT': {
        'titulo': 'Energía (Renovables y No Renovables)',
        'examenes': [
            # Examen 1
            [
                {'p': '¿Qué energía viene del Sol?', 'o': ['Solar', 'Eólica', 'Hidráulica'], 'r': 'Solar'},
                {'p': '¿El petróleo es renovable?', 'o': ['Sí', 'No'], 'r': 'No'},
                {'p': '¿Qué energía usa el viento?', 'o': ['Eólica', 'Térmica'], 'r': 'Eólica'},
                {'p': '¿La leña es un ejemplo de...?', 'o': ['Biomasa', 'Energía nuclear'], 'r': 'Biomasa'},
                {'p': '¿Qué energía se obtiene del agua en movimiento?', 'o': ['Hidráulica', 'Química'], 'r': 'Hidráulica'},
                {'p': '¿El carbón es un combustible fósil?', 'o': ['Sí', 'No'], 'r': 'Sí'},
                {'p': '¿Qué energía usamos al encender una bombilla?', 'o': ['Eléctrica', 'Sonora'], 'r': 'Eléctrica'},
                {'p': '¿La energía se crea o se transforma?', 'o': ['Se crea', 'Se transforma'], 'r': 'Se transforma'},
                {'p': '¿El calor es energía...?', 'o': ['Térmica', 'Luminosa'], 'r': 'Térmica'},
                {'p': '¿Cuál contamina más?', 'o': ['Energía solar', 'Combustibles fósiles'], 'r': 'Combustibles fósiles'}
            ],
            # Examen 2
            [
                {'p': '¿Qué energía tienen los alimentos?', 'o': ['Química', 'Mecánica'], 'r': 'Química'},
                {'p': '¿El gas natural es inagotable?', 'o': ['Sí', 'No'], 'r': 'No'},
                {'p': '¿Cómo se llama la energía del interior de la Tierra?', 'o': ['Geotérmica', 'Solar'], 'r': 'Geotérmica'},
                {'p': '¿Las placas fotovoltaicas producen...?', 'o': ['Electricidad', 'Viento'], 'r': 'Electricidad'},
                {'p': 'Un objeto que se mueve tiene energía...', 'o': ['Mecánica', 'Nuclear'], 'r': 'Mecánica'},
                {'p': '¿El uranio es para energía...?', 'o': ['Nuclear', 'Eólica'], 'r': 'Nuclear'},
                {'p': '¿La energía renovable se agota?', 'o': ['Sí', 'No'], 'r': 'No'},
                {'p': '¿Qué produce un altavoz?', 'o': ['Energía sonora', 'Energía química'], 'r': 'Energía sonora'},
                {'p': '¿Ahorrar energía ayuda al planeta?', 'o': ['Sí', 'No'], 'r': 'Sí'},
                {'p': '¿La gasolina viene del petróleo?', 'o': ['Sí', 'No'], 'r': 'Sí'}
            ],
            # Examen 3
            [
                {'p': '¿Qué es una fuente de energía?', 'o': ['Un recurso natural', 'Una máquina'], 'r': 'Un recurso natural'},
                {'p': '¿El viento es una fuente renovable?', 'o': ['Sí', 'No'], 'r': 'Sí'},
                {'p': '¿Qué energía tiene una pila?', 'o': ['Química', 'Térmica'], 'r': 'Química'},
                {'p': '¿El transporte gasta mucha energía?', 'o': ['Sí', 'No'], 'r': 'Sí'},
                {'p': '¿Qué energía produce un radiador?', 'o': ['Térmica', 'Eólica'], 'r': 'Térmica'},
                {'p': '¿Los molinos modernos se llaman aerogeneradores?', 'o': ['Sí', 'No'], 'r': 'Sí'},
                {'p': '¿El sol se apagará pronto?', 'o': ['Sí', 'No'], 'r': 'No'},
                {'p': '¿La energía puede almacenarse en baterías?', 'o': ['Sí', 'No'], 'r': 'Sí'},
                {'p': '¿Quemar basura para obtener calor es biomasa?', 'o': ['Sí', 'No'], 'r': 'Sí'},
                {'p': '¿Las mareas dan energía mareomotriz?', 'o': ['Sí', 'No'], 'r': 'Sí'}
            ]
        ]
    },
    'U4_NAT': {
        'titulo': 'Fuerzas (Gravedad y Máquinas)',
        'examenes': [
            # Examen 1
            [
                {'p': '¿Qué fuerza nos atrae hacia el suelo?', 'o': ['Gravedad', 'Magnetismo', 'Fricción'], 'r': 'Gravedad'},
                {'p': '¿Qué fuerza frena un objeto al rozar?', 'o': ['Rozamiento/Fricción', 'Gravedad'], 'r': 'Rozamiento/Fricción'},
                {'p': '¿Cuál es una máquina simple?', 'o': ['Polea', 'Coche', 'Ordenador'], 'r': 'Polea'},
                {'p': '¿Qué parte de la palanca es donde apoyamos?', 'o': ['Punto de apoyo', 'Carga'], 'r': 'Punto de apoyo'},
                {'p': '¿Un imán usa fuerza...?', 'o': ['Magnética', 'Eléctrica'], 'r': 'Magnética'},
                {'p': '¿Qué máquina es una rampa?', 'o': ['Plano inclinado', 'Palanca'], 'r': 'Plano inclinado'},
                {'p': '¿El peso es una fuerza?', 'o': ['Sí', 'No'], 'r': 'Sí'},
                {'p': '¿Qué máquina usa una rueda con surco?', 'o': ['Polea', 'Tornillo'], 'r': 'Polea'},
                {'p': '¿Las fuerzas pueden deformar objetos?', 'o': ['Sí', 'No'], 'r': 'Sí'},
                {'p': '¿Quién descubrió la gravedad?', 'o': ['Newton', 'Einstein'], 'r': 'Newton'}
            ],
            # Examen 2
            [
                {'p': '¿Qué máquina es un martillo al sacar clavos?', 'o': ['Palanca', 'Polea'], 'r': 'Palanca'},
                {'p': '¿La fuerza se mide en...?', 'o': ['Newtons', 'Kilos'], 'r': 'Newtons'},
                {'p': '¿Una bicicleta es una máquina...?', 'o': ['Compuesta', 'Simple'], 'r': 'Compuesta'},
                {'p': '¿Qué fuerza hace que floten los barcos?', 'o': ['Flotabilidad', 'Gravedad'], 'r': 'Flotabilidad'},
                {'p': '¿El motor es una parte de máquinas complejas?', 'o': ['Sí', 'No'], 'r': 'Sí'},
                {'p': '¿Qué reduce el rozamiento?', 'o': ['Aceite/Lubricante', 'Arena'], 'r': 'Aceite/Lubricante'},
                {'p': '¿Un muelle es un objeto elástico?', 'o': ['Sí', 'No'], 'r': 'Sí'},
                {'p': '¿La distancia influye en la gravedad?', 'o': ['Sí', 'No'], 'r': 'Sí'},
                {'p': '¿Una tijera son dos palancas?', 'o': ['Sí', 'No'], 'r': 'Sí'},
                {'p': '¿Qué máquina simple es un pomo de puerta?', 'o': ['Torno/Rueda', 'Palanca'], 'r': 'Torno/Rueda'}
            ],
            # Examen 3
            [
                {'p': '¿La masa y el peso son lo mismo?', 'o': ['No', 'Sí'], 'r': 'No'},
                {'p': '¿Dónde pesarías menos?', 'o': ['En la Luna', 'En la Tierra'], 'r': 'En la Luna'},
                {'p': '¿Qué máquina es un hacha?', 'o': ['Cuña', 'Polea'], 'r': 'Cuña'},
                {'p': '¿Las máquinas nos ahorran tiempo y esfuerzo?', 'o': ['Sí', 'No'], 'r': 'Sí'},
                {'p': '¿Un engranaje son ruedas dentadas?', 'o': ['Sí', 'No'], 'r': 'Sí'},
                {'p': '¿La fuerza de contacto requiere tocar el objeto?', 'o': ['Sí', 'No'], 'r': 'Sí'},
                {'p': '¿La gravedad actúa a distancia?', 'o': ['Sí', 'No'], 'r': 'Sí'},
                {'p': '¿Un interruptor es parte de un circuito?', 'o': ['Sí', 'No'], 'r': 'Sí'},
                {'p': '¿El plástico es conductor?', 'o': ['No', 'Sí'], 'r': 'No'},
                {'p': '¿El cobre es conductor?', 'o': ['Sí', 'No'], 'r': 'Sí'}
            ]
        ]
    },
    'U5_NAT': {
        'titulo': 'Sistema Solar (Planetas y Movimientos)',
        'examenes': [
            # Examen 1
            [
                {'p': '¿Cuál es el centro del Sistema Solar?', 'o': ['El Sol', 'La Tierra'], 'r': 'El Sol'},
                {'p': '¿Qué movimiento da lugar a las estaciones?', 'o': ['Traslación', 'Rotación'], 'r': 'Traslación'},
                {'p': '¿Cuál es el planeta más grande?', 'o': ['Júpiter', 'Saturno'], 'r': 'Júpiter'},
                {'p': '¿Qué planeta tiene anillos muy visibles?', 'o': ['Saturno', 'Marte'], 'r': 'Saturno'},
                {'p': '¿Cuántos planetas hay en nuestro sistema?', 'o': ['8', '9', '7'], 'r': '8'},
                {'p': '¿Qué planeta es el "planeta rojo"?', 'o': ['Marte', 'Venus'], 'r': 'Marte'},
                {'p': '¿La Luna es un...?', 'o': ['Satélite', 'Planeta'], 'r': 'Satélite'},
                {'p': '¿Qué movimiento da lugar al día y la noche?', 'o': ['Rotación', 'Traslación'], 'r': 'Rotación'},
                {'p': '¿Cuál es el planeta más cercano al Sol?', 'o': ['Mercurio', 'Tierra'], 'r': 'Mercurio'},
                {'p': '¿En qué galaxia estamos?', 'o': ['Vía Láctea', 'Andrómeda'], 'r': 'Vía Láctea'}
            ],
            # Examen 2
            [
                {'p': '¿Cuánto tarda la Tierra en dar una vuelta al Sol?', 'o': ['365 días', '24 horas'], 'r': '365 días'},
                {'p': '¿Cuál es el planeta más frío?', 'o': ['Neptuno', 'Venus'], 'r': 'Neptuno'},
                {'p': '¿Venus es el planeta más caluroso?', 'o': ['Sí', 'No'], 'r': 'Sí'},
                {'p': '¿Qué son los asteroides?', 'o': ['Rocas espaciales', 'Bolas de gas'], 'r': 'Rocas espaciales'},
                {'p': '¿La Tierra es un planeta rocoso?', 'o': ['Sí', 'No'], 'r': 'Sí'},
                {'p': '¿Qué forma tiene la órbita de los planetas?', 'o': ['Elíptica', 'Cuadrada'], 'r': 'Elíptica'},
                {'p': '¿Cómo se llama cuando la Luna tapa al Sol?', 'o': ['Eclipse', 'Marea'], 'r': 'Eclipse'},
                {'p': '¿Urano gira de lado?', 'o': ['Sí', 'No'], 'r': 'Sí'},
                {'p': '¿Plutón se considera ahora planeta enano?', 'o': ['Sí', 'No'], 'r': 'Sí'},
                {'p': '¿El Sol es una estrella?', 'o': ['Sí', 'No'], 'r': 'Sí'}
            ],
            # Examen 3
            [
                {'p': '¿Qué capa de aire rodea la Tierra?', 'o': ['Atmósfera', 'Hidrosfera'], 'r': 'Atmósfera'},
                {'p': '¿La Tierra es el tercer planeta desde el Sol?', 'o': ['Sí', 'No'], 'r': 'Sí'},
                {'p': '¿Cómo se llaman los planetas de gas?', 'o': ['Gigantes gaseosos', 'Rocosos'], 'r': 'Gigantes gaseosos'},
                {'p': '¿La Luna brilla con luz propia?', 'o': ['No, refleja al Sol', 'Sí'], 'r': 'No, refleja al Sol'},
                {'p': '¿Qué planeta está entre la Tierra y Mercurio?', 'o': ['Venus', 'Marte'], 'r': 'Venus'},
                {'p': '¿Cuánto tarda la Tierra en rotar sobre sí misma?', 'o': ['24 horas', '12 horas'], 'r': '24 horas'},
                {'p': '¿Hay agua líquida en la Tierra?', 'o': ['Sí', 'No'], 'r': 'Sí'},
                {'p': '¿Qué fuerza mantiene a los planetas en órbita?', 'o': ['Gravedad', 'Viento'], 'r': 'Gravedad'},
                {'p': '¿Los cometas tienen colas de hielo y polvo?', 'o': ['Sí', 'No'], 'r': 'Sí'},
                {'p': '¿El ser humano ha pisado la Luna?', 'o': ['Sí', 'No'], 'r': 'Sí'}
            ]
        ]
    },
    'U_SOCIALES': {
        'titulo': 'Sociales (Continentes, Población y Economía)',
        'examenes': [
            # Examen 1
            [
                {'p': '¿En qué continente está España?', 'o': ['Europa', 'África', 'Asia'], 'r': 'Europa'},
                {'p': '¿Cuál es el continente más poblado?', 'o': ['Asia', 'América'], 'r': 'Asia'},
                {'p': '¿Qué sector económico incluye la agricultura?', 'o': ['Primario', 'Secundario', 'Terciario'], 'r': 'Primario'},
                {'p': '¿Qué sector incluye las fábricas?', 'o': ['Secundario', 'Primario'], 'r': 'Secundario'},
                {'p': '¿Qué sector es el turismo y el comercio?', 'o': ['Terciario', 'Primario'], 'r': 'Terciario'},
                {'p': '¿Cómo se llama cuando la gente llega a un país para vivir?', 'o': ['Inmigración', 'Emigración'], 'r': 'Inmigración'},
                {'p': '¿Cuál es el océano más grande?', 'o': ['Pacífico', 'Atlántico'], 'r': 'Pacífico'},
                {'p': '¿Cuántos continentes hay?', 'o': ['6', '5', '7'], 'r': '6'},
                {'p': '¿Qué es la población activa?', 'o': ['Gente que puede trabajar', 'Niños y jubilados'], 'r': 'Gente que puede trabajar'},
                {'p': '¿Qué mide la natalidad?', 'o': ['Número de nacimientos', 'Número de muertes'], 'r': 'Número de nacimientos'}
            ],
            # Examen 2
            [
                {'p': '¿Qué continente es una gran isla?', 'o': ['Oceanía', 'África'], 'r': 'Oceanía'},
                {'p': '¿Dónde está el río Amazonas?', 'o': ['América del Sur', 'Asia'], 'r': 'América del Sur'},
                {'p': '¿Qué sector es la ganadería?', 'o': ['Primario', 'Terciario'], 'r': 'Primario'},
                {'p': '¿Qué es el padrón?', 'o': ['Registro de vecinos', 'Un tipo de barco'], 'r': 'Registro de vecinos'},
                {'p': '¿La Antártida está poblada permanentemente?', 'o': ['No', 'Sí'], 'r': 'No'},
                {'p': '¿Qué sector es la educación y sanidad?', 'o': ['Terciario', 'Secundario'], 'r': 'Terciario'},
                {'p': '¿Qué es la densidad de población?', 'o': ['Habitantes por km2', 'Total de habitantes'], 'r': 'Habitantes por km2'},
                {'p': '¿El comercio es una actividad del sector...?', 'o': ['Terciario', 'Primario'], 'r': 'Terciario'},
                {'p': '¿Un artesano pertenece al sector...?', 'o': ['Secundario', 'Primario'], 'r': 'Secundario'},
                {'p': '¿Qué es el crecimiento natural?', 'o': ['Natalidad menos Mortalidad', 'Inmigrantes'], 'r': 'Natalidad menos Mortalidad'}
            ],
            # Examen 3
            [
                {'p': '¿Qué cordillera está entre Europa y Asia?', 'o': ['Urales', 'Himalaya'], 'r': 'Urales'},
                {'p': '¿Qué océano baña las costas de España?', 'o': ['Atlántico', 'Índico'], 'r': 'Atlántico'},
                {'p': '¿La minería es sector...?', 'o': ['Primario', 'Secundario'], 'r': 'Primario'},
                {'p': '¿Qué es el transporte multimodal?', 'o': ['Usa varios medios', 'Usa solo uno'], 'r': 'Usa varios medios'},
                {'p': '¿Cómo se llama la salida de personas de su país?', 'o': ['Emigración', 'Inmigración'], 'r': 'Emigración'},
                {'p': '¿Qué es el desarrollo sostenible?', 'o': ['Cuidar recursos para el futuro', 'Gastar mucho'], 'r': 'Cuidar recursos para el futuro'},
                {'p': '¿Qué continente tiene el desierto del Sáhara?', 'o': ['África', 'Oceanía'], 'r': 'África'},
                {'p': '¿Qué sector transforma materias primas?', 'o': ['Secundario', 'Terciario'], 'r': 'Secundario'},
                {'p': '¿España tiene una población envejecida?', 'o': ['Sí', 'No'], 'r': 'Sí'},
                {'p': '¿La mayoría de españoles trabaja en el sector...?', 'o': ['Terciario', 'Primario'], 'r': 'Terciario'}
            ]
        ]
    }
}
