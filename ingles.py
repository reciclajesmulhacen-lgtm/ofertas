   import random

# TEMARIO MACMILLAN STEPS INTO ENGLISH 5º
TEMARIO = {
    'U1': {
        'titulo': 'Hello! (Numbers & Colors)',
        'examenes': [
            [ # EXAMEN 1 (Añade aquí hasta 10 preguntas)
                {'p': 'How do you say 75?', 'o': ['Seventy-five', 'Sixty-five'], 'r': 'Seventy-five'},
                {'p': 'What color is a lemon?', 'o': ['Yellow', 'Purple'], 'r': 'Yellow'}
            ],
            [ # EXAMEN 2
                {'p': 'How do you spell 100?', 'o': ['One hundred', 'One thousand'], 'r': 'One hundred'},
                {'p': 'What color do you get mixing blue and red?', 'o': ['Purple', 'Green'], 'r': 'Purple'}
            ],
            [ # EXAMEN 3
                {'p': 'Which number is "Thirteen"?', 'o': ['13', '30'], 'r': '13'},
                {'p': 'The color of the grass is...', 'o': ['Green', 'Blue'], 'r': 'Green'}
            ]
        ]
    },
    'U2': {
        'titulo': 'Family (Have got / To be)',
        'examenes': [
            [ # EXAMEN 1
                {'p': 'My mother\'s brother is my...', 'o': ['Uncle', 'Aunt'], 'r': 'Uncle'},
                {'p': 'Complete: I ___ got a sister.', 'o': ['have', 'has'], 'r': 'have'}
            ],
            [ # EXAMEN 2
                {'p': 'My father\'s mother is my...', 'o': ['Grandmother', 'Grandfather'], 'r': 'Grandmother'},
                {'p': 'Complete: She ___ 10 years old.', 'o': ['is', 'are'], 'r': 'is'}
            ],
            [ # EXAMEN 3
                {'p': 'How do you say "Primo"?', 'o': ['Cousin', 'Brother'], 'r': 'Cousin'},
                {'p': 'Complete: They ___ got a dog.', 'o': ['have', 'has'], 'r': 'have'}
            ]
        ]
    },
    'U3': {
        'titulo': 'House (There is/are)',
        'examenes': [
            [ # EXAMEN 1
                {'p': 'Where do you cook?', 'o': ['Kitchen', 'Bedroom'], 'r': 'Kitchen'},
                {'p': 'Complete: There ___ a sofa in the living room.', 'o': ['is', 'are'], 'r': 'is'}
            ],
            [ # EXAMEN 2
                {'p': 'Where do you sleep?', 'o': ['Bedroom', 'Garden'], 'r': 'Bedroom'},
                {'p': 'Complete: There ___ two chairs in the room.', 'o': ['are', 'is'], 'r': 'are'}
            ],
            [ # EXAMEN 3
                {'p': 'How do you say "Espejo"?', 'o': ['Mirror', 'Window'], 'r': 'Mirror'},
                {'p': 'Where is the shower?', 'o': ['Bathroom', 'Kitchen'], 'r': 'Bathroom'}
            ]
        ]
    },
    'U4': {
        'titulo': 'Food (Like / Some & Any)',
        'examenes': [
            [ # EXAMEN 1
                {'p': 'Complete: I like ___ apples.', 'o': ['some', 'any'], 'r': 'some'},
                {'p': 'Do you like broccoli? No, I ___.', 'o': ['don\'t', 'doesn\'t'], 'r': 'don\'t'}
            ],
            [ # EXAMEN 2
                {'p': 'Complete: Is there ___ milk?', 'o': ['any', 'some'], 'r': 'any'},
                {'p': 'What is "Chicken"?', 'o': ['Pollo', 'Pescado'], 'r': 'Pollo'}
            ],
            [ # EXAMEN 3
                {'p': 'Complete: She ___ oranges.', 'o': ['likes', 'like'], 'r': 'likes'},
                {'p': 'What is "Watermelon"?', 'o': ['Sandía', 'Melón'], 'r': 'Sandía'}
            ]
        ]
    },
    'U5': {
        'titulo': 'School (Present Simple)',
        'examenes': [
            [ # EXAMEN 1
                {'p': 'What time is it? 08:00', 'o': ['It\'s eight o\'clock', 'It\'s half past eight'], 'r': 'It\'s eight o\'clock'},
                {'p': 'Complete: I ___ to school at 9:00.', 'o': ['go', 'goes'], 'r': 'go'}
            ],
            [ # EXAMEN 2
                {'p': 'What time is it? 07:30', 'o': ['It\'s half past seven', 'It\'s seven o\'clock'], 'r': 'It\'s half past seven'},
                {'p': 'Complete: He ___ homework every day.', 'o': ['does', 'do'], 'r': 'does'}
            ],
            [ # EXAMEN 3
                 {'p': 'Complete: We ___ English on Mondays.', 'o': ['have', 'has'], 'r': 'have'},
                 {'p': 'What is "Maths"?', 'o': ['Matemáticas', 'Francés'], 'r': 'Matemáticas'}
            ]
        ]
    },
    'U6': {
        'titulo': 'Animals (Comparatives)',
        'examenes': [
            [ # EXAMEN 1
                {'p': 'An elephant is ___ than a mouse.', 'o': ['bigger', 'smaller'], 'r': 'bigger'},
                {'p': 'A giraffe is ___ than a dog.', 'o': ['taller', 'shorter'], 'r': 'taller'}
            ],
            [ # EXAMEN 2
                {'p': 'A cheetah is ___ than a turtle.', 'o': ['faster', 'slower'], 'r': 'faster'},
                {'p': 'Which animal can fly?', 'o': ['Bird', 'Lion'], 'r': 'Bird'}
            ],
            [ # EXAMEN 3
                 {'p': 'A mouse is ___ than a cat.', 'o': ['smaller', 'bigger'], 'r': 'smaller'},
                 {'p': 'A lion is ___ than a cat.', 'o': ['more dangerous', 'smaller'], 'r': 'more dangerous'}
            ]
        ]
    },
    'U7': {
        'titulo': 'Clothes (Present Continuous)',
        'examenes': [
            [ # EXAMEN 1
                {'p': 'Complete: I am ___ a blue T-shirt.', 'o': ['wearing', 'wear'], 'r': 'wearing'},
                {'p': 'What are "Shoes"?', 'o': ['Zapatos', 'Pantalones'], 'r': 'Zapatos'}
            ],
            [ # EXAMEN 2
                {'p': 'Complete: She ___ wearing a red dress.', 'o': ['is', 'are'], 'r': 'is'},
                {'p': 'What is a "Hat"?', 'o': ['Sombrero', 'Bufanda'], 'r': 'Sombrero'}
            ],
            [ # EXAMEN 3
                 {'p': 'Complete: They ___ wearing coats.', 'o': ['are', 'is'], 'r': 'are'},
                 {'p': 'When do you wear a "Swimsuit"?', 'o': ['In summer', 'In winter'], 'r': 'In summer'}
            ]
        ]
    },
    'U8': {
        'titulo': 'Routines (Sequence words)',
        'examenes': [
            [ # EXAMEN 1
                {'p': '___, I get up. Then, I have breakfast.', 'o': ['First', 'Finally'], 'r': 'First'},
                {'p': 'What is "Brush your teeth"?', 'o': ['Lavarse los dientes', 'Peinarse'], 'r': 'Lavarse los dientes'}
            ],
            [ # EXAMEN 2
                {'p': '___ school, I go to the park.', 'o': ['After', 'Before'], 'r': 'After'},
                {'p': 'What is "Go to bed"?', 'o': ['Irse a dormir', 'Levantarse'], 'r': 'Irse a dormir'}
            ],
            [ # EXAMEN 3
                 {'p': 'I have a shower ___ I go to bed.', 'o': ['before', 'after'], 'r': 'before'},
                 {'p': 'I watch TV, and ___, I go to sleep.', 'o': ['finally', 'first'], 'r': 'finally'}
            ]
        ]
    }
}
