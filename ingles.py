  import random

# TEMARIO INGLÉS 5º (Edelvives FanFest - CEIP Las Encinas)
# 10 preguntas por examen / 3 modelos por unidad
TEMARIO = {
    'U1_ING': {
        'titulo': 'Unit 1: My Day & Free Time',
        'examenes': [
            [ # Examen 1
                {'p': 'How do you say "levantarse"?', 'o': ['Get up', 'Go up'], 'r': 'Get up'},
                {'p': 'I ___ my teeth every morning.', 'o': ['brush', 'wash'], 'r': 'brush'},
                {'p': 'What is "desayunar"?', 'o': ['Have breakfast', 'Have dinner'], 'r': 'Have breakfast'},
                {'p': 'She ___ to school at 8:30.', 'o': ['goes', 'go'], 'r': 'goes'},
                {'p': 'How do you say "ducharse"?', 'o': ['Have a shower', 'Take a bath'], 'r': 'Have a shower'},
                {'p': 'I ___ my homework in the afternoon.', 'o': ['do', 'make'], 'r': 'do'},
                {'p': 'What is "cenar"?', 'o': ['Have dinner', 'Have lunch'], 'r': 'Have dinner'},
                {'p': 'He ___ TV after school.', 'o': ['watches', 'watch'], 'r': 'watches'},
                {'p': 'How do you say "peinarse"?', 'o': ['Comb my hair', 'Wash my hair'], 'r': 'Comb my hair'},
                {'p': 'I ___ to bed at 10 o\'clock.', 'o': ['go', 'goes'], 'r': 'go'}
            ],
            [ # Examen 2
                {'p': 'Does he play football? Yes, he ___.', 'o': ['does', 'do'], 'r': 'does'},
                {'p': 'I ___ play video games on Mondays.', 'o': ['don\'t', 'doesn\'t'], 'r': 'don\'t'},
                {'p': 'What time is it? (6:30)', 'o': ['Half past six', 'Quarter past six'], 'r': 'Half past six'},
                {'p': 'She ___ (listen) to music.', 'o': ['listens', 'listen'], 'r': 'listens'},
                {'p': 'How do you say "siempre"?', 'o': ['Always', 'Never'], 'r': 'Always'},
                {'p': 'How do you say "a veces"?', 'o': ['Sometimes', 'Usually'], 'r': 'Sometimes'},
                {'p': 'We ___ (have) lunch at the canteen.', 'o': ['have', 'has'], 'r': 'have'},
                {'p': 'Does she like dancing? No, she ___.', 'o': ['doesn\'t', 'don\'t'], 'r': 'doesn\'t'},
                {'p': 'What is "merendar"?', 'o': ['Have a snack', 'Have breakfast'], 'r': 'Have a snack'},
                {'p': 'Do they study English? Yes, they ___.', 'o': ['do', 'does'], 'r': 'do'}
            ],
            [ # Examen 3
                {'p': 'What is "entrenar"?', 'o': ['Train', 'Play'], 'r': 'Train'},
                {'p': 'My brother ___ (wash) the car.', 'o': ['washes', 'wash'], 'r': 'washes'},
                {'p': 'What is "temprano"?', 'o': ['Early', 'Late'], 'r': 'Early'},
                {'p': 'I ___ (not like) pizza.', 'o': ['don\'t like', 'doesn\'t like'], 'r': 'don\'t like'},
                {'p': 'How do you say "nunca"?', 'o': ['Never', 'Often'], 'r': 'Never'},
                {'p': 'What is "hacer la cama"?', 'o': ['Make the bed', 'Do the bed'], 'r': 'Make the bed'},
                {'p': 'She ___ (get up) at seven.', 'o': ['gets up', 'get up'], 'r': 'gets up'},
                {'p': 'What is "llegar tarde"?', 'o': ['Be late', 'Be early'], 'r': 'Be late'},
                {'p': 'Do you live in Alfacar? Yes, I ___.', 'o': ['do', 'am'], 'r': 'do'},
                {'p': 'What is "leer un libro"?', 'o': ['Read a book', 'Write a book'], 'r': 'Read a book'}
            ]
        ]
    },
    'U2_ING': {
        'titulo': 'Unit 2: Food & Health',
        'examenes': [
            [ # Examen 1
                {'p': 'How do you say "manzanas"?', 'o': ['Apples', 'Pears'], 'r': 'Apples'},
                {'p': 'Is "milk" countable or uncountable?', 'o': ['Uncountable', 'Countable'], 'r': 'Uncountable'},
                {'p': 'I would like ___ orange.', 'o': ['an', 'a'], 'r': 'an'},
                {'p': 'There is ___ water in the bottle.', 'o': ['some', 'any'], 'r': 'some'},
                {'p': 'Are there ___ eggs?', 'o': ['any', 'some'], 'r': 'any'},
                {'p': 'What is "zanahoria"?', 'o': ['Carrot', 'Potato'], 'r': 'Carrot'},
                {'p': 'How do you say "saludable"?', 'o': ['Healthy', 'Unhealthy'], 'r': 'Healthy'},
                {'p': 'What is "mantequilla"?', 'o': ['Butter', 'Cheese'], 'r': 'Butter'},
                {'p': 'I love ___ (eat) fruit.', 'o': ['eating', 'eat'], 'r': 'eating'},
                {'p': 'What is "pollo"?', 'o': ['Chicken', 'Fish'], 'r': 'Chicken'}
            ],
            [ # Examen 2
                {'p': 'I don\'t have ___ sugar.', 'o': ['any', 'some'], 'r': 'any'},
                {'p': 'How do you say "hambre"?', 'o': ['Hungry', 'Thirsty'], 'r': 'Hungry'},
                {'p': 'What is "aceite de oliva"?', 'o': ['Olive oil', 'Vinegar'], 'r': 'Olive oil'},
                {'p': 'A ___ of chocolate.', 'o': ['bar', 'glass'], 'r': 'bar'},
                {'p': 'A ___ of water.', 'o': ['glass', 'slice'], 'r': 'glass'},
                {'p': 'Is "banana" countable?', 'o': ['Yes', 'No'], 'r': 'Yes'},
                {'p': 'What is "arroz"?', 'o': ['Rice', 'Pasta'], 'r': 'Rice'},
                {'p': 'How do you say "sed"?', 'o': ['Thirsty', 'Hungry'], 'r': 'Thirsty'},
                {'p': 'There are ___ tomatoes.', 'o': ['some', 'any'], 'r': 'some'},
                {'p': 'A ___ of pizza.', 'o': ['slice', 'bottle'], 'r': 'slice'}
            ],
            [ # Examen 3
                {'p': 'What is "verduras"?', 'o': ['Vegetables', 'Fruit'], 'r': 'Vegetables'},
                {'p': 'Would you like ___ biscuit?', 'o': ['a', 'an'], 'r': 'a'},
                {'p': 'Is "honey" uncountable?', 'o': ['Yes', 'No'], 'r': 'Yes'},
                {'p': 'How do you say "comida basura"?', 'o': ['Junk food', 'Healthy food'], 'r': 'Junk food'},
                {'p': 'A ___ of milk.', 'o': ['bottle', 'packet'], 'r': 'bottle'},
                {'p': 'What is "sal"?', 'o': ['Salt', 'Sugar'], 'r': 'Salt'},
                {'p': 'There isn\'t ___ cheese.', 'o': ['any', 'some'], 'r': 'any'},
                {'p': 'How do you say "delicioso"?', 'o': ['Delicious', 'Disgusting'], 'r': 'Delicious'},
                {'p': 'What is "guisantes"?', 'o': ['Peas', 'Beans'], 'r': 'Peas'},
                {'p': 'I hate ___ (drink) soda.', 'o': ['drinking', 'drink'], 'r': 'drinking'}
            ]
        ]
    },
    'U3_ING': {
        'titulo': 'Unit 3: Places & My Town',
        'examenes': [
            [ # Examen 1
                {'p': 'Where can you buy books?', 'o': ['Bookshop', 'Library'], 'r': 'Bookshop'},
                {'p': 'Where do you borrow books?', 'o': ['Library', 'Bookshop'], 'r': 'Library'},
                {'p': 'Where do you see films?', 'o': ['Cinema', 'Museum'], 'r': 'Cinema'},
                {'p': 'The park is ___ the school and the shop.', 'o': ['between', 'next to'], 'r': 'between'},
                {'p': 'What is "ayuntamiento"?', 'o': ['Town Hall', 'Supermarket'], 'r': 'Town Hall'},
                {'p': 'Is there a park? Yes, there ___.', 'o': ['is', 'are'], 'r': 'is'},
                {'p': 'How do you say "enfrente de"?', 'o': ['Opposite', 'Behind'], 'r': 'Opposite'},
                {'p': 'Where do you see old things?', 'o': ['Museum', 'Park'], 'r': 'Museum'},
                {'p': 'How do you say "detrás"?', 'o': ['Behind', 'In front of'], 'r': 'Behind'},
                {'p': 'Where do you buy stamps?', 'o': ['Post office', 'Bank'], 'r': 'Post office'}
            ],
            [ # Examen 2
                {'p': 'Are there any shops? No, there ___.', 'o': ['aren\'t', 'isn\'t'], 'r': 'aren\'t'},
                {'p': 'What is "centro comercial"?', 'o': ['Shopping centre', 'Sports centre'], 'r': 'Shopping centre'},
                {'p': 'How do you say "al lado de"?', 'o': ['Next to', 'Under'], 'r': 'Next to'},
                {'p': 'Where do you keep money?', 'o': ['Bank', 'Hospital'], 'r': 'Bank'},
                {'p': 'The museum is ___ the corner.', 'o': ['on', 'in'], 'r': 'on'},
                {'p': 'What is "estación de tren"?', 'o': ['Train station', 'Bus stop'], 'r': 'Train station'},
                {'p': 'There ___ (be) a supermarket here.', 'o': ['is', 'are'], 'r': 'is'},
                {'p': 'How do you say "lejos"?', 'o': ['Far', 'Near'], 'r': 'Far'},
                {'p': 'How do you say "cerca"?', 'o': ['Near', 'Far'], 'r': 'Near'},
                {'p': 'Where do you buy bread?', 'o': ['Bakery', 'Butcher\'s'], 'r': 'Bakery'}
            ],
            [ # Examen 3
                {'p': 'Is there a hospital? No, there ___.', 'o': ['isn\'t', 'aren\'t'], 'r': 'isn\'t'},
                {'p': 'What is "polideportivo"?', 'o': ['Sports centre', 'School'], 'r': 'Sports centre'},
                {'p': 'How do you say "girar a la derecha"?', 'o': ['Turn right', 'Turn left'], 'r': 'Turn right'},
                {'p': 'How do you say "todo recto"?', 'o': ['Straight on', 'Cross'], 'r': 'Straight on'},
                {'p': 'Where can you see a doctor?', 'o': ['Hospital', 'Cinema'], 'r': 'Hospital'},
                {'p': 'Where do children study?', 'o': ['School', 'Park'], 'r': 'School'},
                {'p': 'Are there any parks? Yes, there ___.', 'o': ['are', 'is'], 'r': 'are'},
                {'p': 'What is "iglesia"?', 'o': ['Church', 'Castle'], 'r': 'Church'},
                {'p': 'How do you say "cruzar"?', 'o': ['Cross', 'Stop'], 'r': 'Cross'},
                {'p': 'What is "calle"?', 'o': ['Street', 'Road'], 'r': 'Street'}
            ]
        ]
    }
}    'U4_ING': {
        'titulo': 'Unit 4: Animals & Nature',
        'examenes': [
            [ # Examen 1: Comparativos
                {'p': 'A whale is ___ than a dolphin.', 'o': ['bigger', 'big'], 'r': 'bigger'},
                {'p': 'A cheetah is ___ than a lion.', 'o': ['faster', 'fastest'], 'r': 'faster'},
                {'p': 'What is "tiburón"?', 'o': ['Shark', 'Whale'], 'r': 'Shark'},
                {'p': 'How do you say "más lento que"?', 'o': ['slower than', 'slow than'], 'r': 'slower than'},
                {'p': 'What is "bosque"?', 'o': ['Forest', 'Beach'], 'r': 'Forest'},
                {'p': 'A giraffe is ___ than an elephant.', 'o': ['taller', 'tall'], 'r': 'taller'},
                {'p': 'How do you say "selva"?', 'o': ['Jungle', 'Mountain'], 'r': 'Jungle'},
                {'p': 'An eagle is ___ than a parrot.', 'o': ['stronger', 'strong'], 'r': 'stronger'},
                {'p': 'What is "desierto"?', 'o': ['Desert', 'River'], 'r': 'Desert'},
                {'p': 'A snake is ___ than a lizard.', 'o': ['longer', 'long'], 'r': 'longer'}
            ],
            [ # Examen 2: Superlativos
                {'p': 'The blue whale is the ___ animal.', 'o': ['biggest', 'bigger'], 'r': 'biggest'},
                {'p': 'The cheetah is the ___ land animal.', 'o': ['fastest', 'faster'], 'r': 'fastest'},
                {'p': 'What is "peligroso"?', 'o': ['Dangerous', 'Safe'], 'r': 'Dangerous'},
                {'p': 'How do you say "el más alto"?', 'o': ['the tallest', 'the taller'], 'r': 'the tallest'},
                {'p': 'Mount Everest is the ___ mountain.', 'o': ['highest', 'high'], 'r': 'highest'},
                {'p': 'What is "águila"?', 'o': ['Eagle', 'Owl'], 'r': 'Eagle'},
                {'p': 'The snail is the ___ animal.', 'o': ['slowest', 'slower'], 'r': 'slowest'},
                {'p': 'What is "océano"?', 'o': ['Ocean', 'Lake'], 'r': 'Ocean'},
                {'p': 'How do you say "pequeño"?', 'o': ['Small', 'Big'], 'r': 'Small'},
                {'p': 'What is "oso polar"?', 'o': ['Polar bear', 'Panda'], 'r': 'Polar bear'}
            ],
            [ # Examen 3: Mix
                {'p': 'Is a tiger faster than a cat?', 'o': ['Yes, it is', 'No, it isn\'t'], 'r': 'Yes, it is'},
                {'p': 'What is "río"?', 'o': ['River', 'Sea'], 'r': 'River'},
                {'p': 'How do you say "pesado"?', 'o': ['Heavy', 'Light'], 'r': 'Heavy'},
                {'p': 'The mosquito is the ___ animal.', 'o': ['smallest', 'smaller'], 'r': 'smallest'},
                {'p': 'What is "tierra"?', 'o': ['Land', 'Water'], 'r': 'Land'},
                {'p': 'Is an ant bigger than a spider?', 'o': ['No, it isn\'t', 'Yes, it is'], 'r': 'No, it isn\'t'},
                {'p': 'What is "pájaro"?', 'o': ['Bird', 'Fish'], 'r': 'Bird'},
                {'p': 'How do you say "más fuerte"?', 'o': ['stronger', 'strongest'], 'r': 'stronger'},
                {'p': 'What is "isla"?', 'o': ['Island', 'Coast'], 'r': 'Island'},
                {'p': 'Is the elephant the heaviest?', 'o': ['Yes, it is', 'No, it isn\'t'], 'r': 'Yes, it is'}
            ]
        ]
    }
}    'U4_ING': {
        'titulo': 'Unit 4: Animals & Nature',
        'examenes': [
            [ # Examen 1: Comparativos
                {'p': 'A whale is ___ than a dolphin.', 'o': ['bigger', 'big'], 'r': 'bigger'},
                {'p': 'A cheetah is ___ than a lion.', 'o': ['faster', 'fastest'], 'r': 'faster'},
                {'p': 'What is "tiburón"?', 'o': ['Shark', 'Whale'], 'r': 'Shark'},
                {'p': 'How do you say "más lento que"?', 'o': ['slower than', 'slow than'], 'r': 'slower than'},
                {'p': 'What is "bosque"?', 'o': ['Forest', 'Beach'], 'r': 'Forest'},
                {'p': 'A giraffe is ___ than an elephant.', 'o': ['taller', 'tall'], 'r': 'taller'},
                {'p': 'How do you say "selva"?', 'o': ['Jungle', 'Mountain'], 'r': 'Jungle'},
                {'p': 'An eagle is ___ than a parrot.', 'o': ['stronger', 'strong'], 'r': 'stronger'},
                {'p': 'What is "desierto"?', 'o': ['Desert', 'River'], 'r': 'Desert'},
                {'p': 'A snake is ___ than a lizard.', 'o': ['longer', 'long'], 'r': 'longer'}
            ],
            [ # Examen 2: Superlativos
                {'p': 'The blue whale is the ___ animal.', 'o': ['biggest', 'bigger'], 'r': 'biggest'},
                {'p': 'The cheetah is the ___ land animal.', 'o': ['fastest', 'faster'], 'r': 'fastest'},
                {'p': 'What is "peligroso"?', 'o': ['Dangerous', 'Safe'], 'r': 'Dangerous'},
                {'p': 'How do you say "el más alto"?', 'o': ['the tallest', 'the taller'], 'r': 'the tallest'},
                {'p': 'Mount Everest is the ___ mountain.', 'o': ['highest', 'high'], 'r': 'highest'},
                {'p': 'What is "águila"?', 'o': ['Eagle', 'Owl'], 'r': 'Eagle'},
                {'p': 'The snail is the ___ animal.', 'o': ['slowest', 'slower'], 'r': 'slowest'},
                {'p': 'What is "océano"?', 'o': ['Ocean', 'Lake'], 'r': 'Ocean'},
                {'p': 'How do you say "pequeño"?', 'o': ['Small', 'Big'], 'r': 'Small'},
                {'p': 'What is "oso polar"?', 'o': ['Polar bear', 'Panda'], 'r': 'Polar bear'}
            ],
            [ # Examen 3: Mix
                {'p': 'Is a tiger faster than a cat?', 'o': ['Yes, it is', 'No, it isn\'t'], 'r': 'Yes, it is'},
                {'p': 'What is "río"?', 'o': ['River', 'Sea'], 'r': 'River'},
                {'p': 'How do you say "pesado"?', 'o': ['Heavy', 'Light'], 'r': 'Heavy'},
                {'p': 'The mosquito is the ___ animal.', 'o': ['smallest', 'smaller'], 'r': 'smallest'},
                {'p': 'What is "tierra"?', 'o': ['Land', 'Water'], 'r': 'Land'},
                {'p': 'Is an ant bigger than a spider?', 'o': ['No, it isn\'t', 'Yes, it is'], 'r': 'No, it isn\'t'},
                {'p': 'What is "pájaro"?', 'o': ['Bird', 'Fish'], 'r': 'Bird'},
                {'p': 'How do you say "más fuerte"?', 'o': ['stronger', 'strongest'], 'r': 'stronger'},
                {'p': 'What is "isla"?', 'o': ['Island', 'Coast'], 'r': 'Island'},
                {'p': 'Is the elephant the heaviest?', 'o': ['Yes, it is', 'No, it isn\'t'], 'r': 'Yes, it is'}
            ]
        ]
    }
}

