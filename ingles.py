# ingles.py - Macmillan Steps into English 5

TEMARIO = {
    'U1': {
        'titulo': 'Hello! (Name/age, numbers 1-100, colors)',
        'examenes': [
            [
                {'p': "What's your name?", 'o': ["My name's Anna", "I'm fine", "I'm ten"], 'r': "My name's Anna"},
                {'p': 'How old are you?', 'o': ["I'm ten", "ten years", "My name's Tom"], 'r': "I'm ten"},
                {'p': 'Numbers: 15 + 5 =', 'o': ['twenty', 'fifteen', 'ten'], 'r': 'twenty'},
                {'p': 'What color is the sky?', 'o': ['blue', 'red', 'green'], 'r': 'blue'},
                {'p': 'How do you spell "red"?', 'o': ['R-E-D', 'R-D-E', 'RED'], 'r': 'R-E-D'},
                {'p': 'Complete: "Hello, I ___ Anna"', 'o': ["'m", 'am', 'are'], 'r': "'m"},
                {'p': 'Number: "fifty" es', 'o': ['50', '15', '5'], 'r': '50'},
                {'p': 'Color del sol:', 'o': ['yellow', 'blue', 'black'], 'r': 'yellow'},
                {'p': '¿Cuánto es 20 - 10?', 'o': ['ten', 'twenty', 'eleven'], 'r': 'ten'},
                {'p': 'My favorite color is', 'o': ['green', 'Greenn', 'greens'], 'r': 'green'}
            ],
            [
                {'p': 'Complete: "___ name is Tom"', 'o': ['My', 'I', 'Me'], 'r': 'My'},
                {'p': 'How old is she?', 'o': ["She's eight", 'She eight', 'She is eight years'], 'r': "She's eight"},
                {'p': 'Numbers: 30 + 20 =', 'o': ['fifty', 'thirty', 'forty'], 'r': 'fifty'},
                {'p': 'What color is grass?', 'o': ['green', 'blue', 'yellow'], 'r': 'green'},
                {'p': 'Spell "blue":', 'o': ['B-L-U-E', 'B-U-L-E', 'BLUE'], 'r': 'B-L-U-E'},
                {'p': 'Hello! I ___ nine years old', 'o': ["'m", 'am', 'are'], 'r': "'m"},
                {'p': '"78" se dice:', 'o': ['seventy-eight', 'eighteen', 'seventeen'], 'r': 'seventy-eight'},
                {'p': 'Color de la nieve:', 'o': ['white', 'black', 'red'], 'r': 'white'},
                {'p': '25 + 25 =', 'o': ['fifty', 'twenty-five', 'fifty-five'], 'r': 'fifty'},
                {'p': 'What color are your eyes?', 'o': ['brown', 'Brown', 'browm'], 'r': 'brown'}
            ],
            [
                {'p': "What's ___ name?", 'o': ['your', 'you', 'yours'], 'r': 'your'},
                {'p': 'How many? 100 - 50 =', 'o': ['fifty', 'hundred', 'zero'], 'r': 'fifty'},
                {'p': 'Apple color:', 'o': ['red', 'blue', 'green'], 'r': 'red'},
                {'p': 'Complete: "I ___ twelve"', 'o': ["'m", 'is', 'are'], 'r': "'m"},
                {'p': 'Number: "sixty-five"', 'o': ['65', '56', '15'], 'r': '65'},
                {'p': 'Banana color:', 'o': ['yellow', 'green', 'orange'], 'r': 'yellow'},
                {'p': 'Spell "green":', 'o': ['G-R-E-E-N', 'G-R-E-E-N-N', 'GREEN'], 'r': 'G-R-E-E-N'},
                {'p': '10 + 10 + 10 =', 'o': ['thirty', 'twenty', 'ten'], 'r': 'thirty'},
                {'p': 'What color is orange?', 'o': ['orange', 'red', 'yellow'], 'r': 'orange'},
                {'p': 'My ___ is green', 'o': ['T-shirt', 'T-shirrt', 'Tshirt'], 'r': 'T-shirt'}
            ]
        ]
    },

    'U2': {
        'titulo': 'Family (To be, have got, possessives)',
        'examenes': [
            [
                {'p': 'Complete: "She ___ my sister"', 'o': ['is', 'am', 'are'], 'r': 'is'},
                {'p': 'I ___ got a dog', 'o': ['have', 'has', 'am'], 'r': 'have'},
                {'p': 'This is ___ book', 'o': ['my', 'mine', 'me'], 'r': 'my'},
                {'p': 'They ___ my brothers', 'o': ['are', 'is', 'am'], 'r': 'are'},
                {'p': 'She ___ got blue eyes', 'o': ['has', 'have', 'am'], 'r': 'has'},
                {'p': "That's ___ father", 'o': ['his', 'he', 'him'], 'r': 'his'},
                {'p': 'We ___ in the park', 'o': ['are', 'is', 'am'], 'r': 'are'},
                {'p': 'This is ___ cat', 'o': ['your', 'you', 'yours'], 'r': 'your'},
                {'p': 'He ___ got a bike', 'o': ['has', 'have', 'am'], 'r': 'has'},
                {'p': 'You ___ my friend', 'o': ['are', 'is', 'am'], 'r': 'are'}
            ],
            [
                {'p': 'Complete: "___ got a brother"', 'o': ['I have', 'I has', 'Me have'], 'r': 'I have'},
                {'p': 'It ___ my ball', 'o': ['is', 'are', 'am'], 'r': 'is'},
                {'p': 'This is ___ house', 'o': ['her', 'she', 'hers'], 'r': 'her'},
                {'p': 'They ___ got cars', 'o': ['have', 'has', 'are'], 'r': 'have'},
                {'p': 'My sister ___ tall', 'o': ['is', 'are', 'am'], 'r': 'is'},
                {'p': 'We ___ got a cat', 'o': ['have', 'has', 'am'], 'r': 'have'},
                {'p': 'That ___ your bag', 'o': ['is', 'are', 'am'], 'r': 'is'},
                {'p': 'He ___ my uncle', 'o': ['is', 'are', 'am'], 'r': 'is'},
                {'p': 'This is ___ pen', 'o': ['our', 'us', 'ours'], 'r': 'our'},
                {'p': 'You ___ got glasses', 'o': ['have', 'has', 'is'], 'r': 'have'}
            ],
            [
                {'p': 'Complete: "___ my parents"', 'o': ['These are', 'This are', 'This is'], 'r': 'These are'},
                {'p': 'She ___ got long hair', 'o': ['has', 'have', 'is'], 'r': 'has'},
                {'p': 'That is ___ car', 'o': ['their', 'them', 'they'], 'r': 'their'},
                {'p': 'I ___ happy', 'o': ['am', 'is', 'are'], 'r': 'am'},
                {'p': 'We ___ got two dogs', 'o': ['have', 'has', 'are'], 'r': 'have'},
                {'p': 'My brother ___ short', 'o': ['is', 'are', 'am'], 'r': 'is'},
                {'p': 'This ___ my cousin', 'o': ['is', 'are', 'am'], 'r': 'is'},
                {'p': 'They ___ my grandparents', 'o': ['are', 'is', 'am'], 'r': 'are'},
                {'p': 'You ___ got a nice smile', 'o': ['have', 'has', 'are'], 'r': 'have'},
                {'p': 'It ___ our house', 'o': ['is', 'are', 'am'], 'r': 'is'}
            ]
        ]
    },

    'U3': {
        'titulo': 'House (There is/are, furniture)',
        'examenes': [
            [
                {'p': 'Complete: "There ___ a bed in my room"', 'o': ['is', 'are', 'have'], 'r': 'is'},
                {'p': 'There ___ two chairs', 'o': ['are', 'is', 'have'], 'r': 'are'},
                {'p': 'Furniture: "sofa"', 'o': ['Living room', 'Kitchen', 'Bedroom'], 'r': 'Living room'},
                {'p': 'There ___ a table in the kitchen', 'o': ['is', 'are', 'have'], 'r': 'is'},
                {'p': 'There ___ three books', 'o': ['are', 'is', 'have'], 'r': 'are'},
                {'p': '"Wardrobe" significa:', 'o': ['Armario', 'Silla', 'Mesa'], 'r': 'Armario'},
                {'p': 'There ___ a lamp on the table', 'o': ['is', 'are', 'have'], 'r': 'is'},
                {'p': '"Bed" es para:', 'o': ['Dormir', 'Cocinar', 'Estudiar'], 'r': 'Dormir'},
                {'p': 'There ___ four windows', 'o': ['are', 'is', 'have'], 'r': 'are'},
                {'p': '"Carpet" significa:', 'o': ['Alfombra', 'Cuadro', 'Espejo'], 'r': 'Alfombra'}
            ],
            [
                {'p': 'Complete: "There ___ a TV in the living room"', 'o': ['is', 'are', 'have'], 'r': 'is'},
                {'p': 'There ___ some pictures', 'o': ['are', 'is', 'have'], 'r': 'are'},
                {'p': '"Cupboard" es:', 'o': ['Armario cocina', 'Cama', 'Sofá'], 'r': 'Armario cocina'},
                {'p': 'There ___ a mirror in the bathroom', 'o': ['is', 'are', 'have'], 'r': 'is'},
                {'p': 'There ___ two cats', 'o': ['are', 'is', 'have'], 'r': 'are'},
                {'p': '"Curtains" significa:', 'o': ['Cortinas', 'Alfombras', 'Sillas'], 'r': 'Cortinas'},
                {'p': 'There ___ a computer', 'o': ['is', 'are', 'have'], 'r': 'is'},
                {'p': 'There ___ some flowers', 'o': ['are', 'is', 'have'], 'r': 'are'},
                {'p': '"Drawer" es:', 'o': ['Cajón', 'Puerta', 'Ventana'], 'r': 'Cajón'},
                {'p': 'There ___ a clock on the wall', 'o': ['is', 'are', 'have'], 'r': 'is'}
            ],
            [
                {'p': 'There ___ some books on the shelf', 'o': ['are', 'is', 'have'], 'r': 'are'},
                {'p': '"Rug" significa:', 'o': ['Alfombra pequeña', 'Mesa', 'Lámpara'], 'r': 'Alfombra pequeña'},
                {'p': 'There ___ a fridge in the kitchen', 'o': ['is', 'are', 'have'], 'r': 'is'},
                {'p': 'There ___ three chairs', 'o': ['are', 'is', 'have'], 'r': 'are'},
                {'p': '"Bookshelf" es:', 'o': ['Estantería', 'Cama', 'Sofá'], 'r': 'Estantería'},
                {'p': 'There ___ a dog under the table', 'o': ['is', 'are', 'have'], 'r': 'is'},
                {'p': 'There ___ some apples', 'o': ['are', 'is', 'have'], 'r': 'are'},
                {'p': '"Cushion" significa:', 'o': ['Cojín', 'Almohada', 'Manta'], 'r': 'Cojín'},
                {'p': 'There ___ a window in the bedroom', 'o': ['is', 'are', 'have'], 'r': 'is'},
                {'p': 'There ___ two sofas', 'o': ['are', 'is', 'have'], 'r': 'are'}
            ]
        ]
    },

    'U4': {
        'titulo': 'Food (Some/any, can, like/don"t like)',
        'examenes': [
            [
                {'p': 'Complete: "I like apples. I ___ bananas"', 'o': ["don't like", 'not like', 'no like'], 'r': "don't like"},
                {'p': 'There ___ some milk', 'o': ['is', 'are', 'have'], 'r': 'is'},
                {'p': 'I ___ swim', 'o': ['can', 'like', 'have'], 'r': 'can'},
                {'p': 'Is there ___ water?', 'o': ['any', 'some', 'a'], 'r': 'any'},
                {'p': 'I like ___ pizza', 'o': ['some', 'any', 'a'], 'r': 'some'},
                {'p': 'She ___ play tennis', 'o': ['can', 'like', 'have'], 'r': 'can'},
                {'p': 'There aren"t ___ oranges', 'o': ['any', 'some', 'a'], 'r': 'any'},
                {'p': 'Do you like ___ ice cream?', 'o': ['any', 'some', 'a'], 'r': 'any'},
                {'p': 'I don"t like ___ spinach', 'o': ['any', 'some', 'a'], 'r': 'any'},
                {'p': 'He ___ run fast', 'o': ['can', 'like', 'have'], 'r': 'can'}
            ],
            [
                {'p': 'Complete: "There ___ any bread"', 'o': ["isn't", 'aren"t', 'not'], 'r': "isn't"},
                {'p': 'I ___ dance', 'o': ['can', 'like', 'have'], 'r': 'can'},
                {'p': 'There ___ some eggs', 'o': ['are', 'is', 'have'], 'r': 'are'},
                {'p': 'Do you like coffee? No, I ___', 'o': ["don't", 'not', 'no'], 'r': "don't"},
                {'p': 'Is there ___ cheese?', 'o': ['any', 'some', 'a'], 'r': 'any'},
                {'p': 'We ___ play football', 'o': ['can', 'like', 'have'], 'r': 'can'},
                {'p': 'I like ___ cake', 'o': ['some', 'any', 'a'], 'r': 'some'},
                {'p': 'There aren"t ___ cookies', 'o': ['any', 'some', 'a'], 'r': 'any'},
                {'p': 'She doesn"t like ___ fish', 'o': ['any', 'some', 'a'], 'r': 'any'},
                {'p': 'They ___ sing', 'o': ['can', 'like', 'have'], 'r': 'can'}
            ],
            [
                {'p': 'There ___ some water in the fridge', 'o': ['is', 'are', 'have'], 'r': 'is'},
                {'p': 'I don"t like ___ olives', 'o': ['any', 'some', 'a'], 'r': 'any'},
                {'p': 'Can you ___?', 'o': ['swim', 'like swimming', 'have swim'], 'r': 'swim'},
                {'p': 'There ___ any juice', 'o': ["isn't", 'aren"t', 'not'], 'r': "isn't"},
                {'p': 'I like ___ chocolate', 'o': ['some', 'any', 'a'], 'r': 'some'},
                {'p': 'He can"t ___ guitar', 'o': ['play the', 'play', 'playing'], 'r': 'play the'},
                {'p': 'Is there ___ rice?', 'o': ['any', 'some', 'a'], 'r': 'any'},
                {'p': 'We don"t like ___ carrots', 'o': ['any', 'some', 'a'], 'r': 'any'},
                {'p': 'There ___ some bread', 'o': ['is', 'are', 'have'], 'r': 'is'},
                {'p': 'She ___ ride a bike', 'o': ['can', 'like', 'have'], 'r': 'can'}
            ]
        ]
    },

    'U5': {
        'titulo': 'School (Present Simple, time, frequency)',
        'examenes': [
            [
                {'p': 'Complete: "I ___ to school every day"', 'o': ['go', 'goes', 'going'], 'r': 'go'},
                {'p': 'She ___ at 8:00', 'o': ['gets up', 'get up', 'getting up'], 'r': 'gets up'},
                {'p': 'What time ___ it?', 'o': ['is', 'are', 'do'], 'r': 'is'},
                {'p': 'I ___ play tennis', 'o': ['always', 'never', 'sometimes'], 'r': 'always'},
                {'p': 'He ___ TV in the evening', 'o': ['watches', 'watch', 'watching'], 'r': 'watches'},
                {'p': "It's ___ o'clock", 'o': ['three', 'thirty', 'quarter'], 'r': 'three'},
                {'p': 'We ___ at 3:00', 'o': ['finish', 'finishes', 'finishing'], 'r': 'finish'},
                {'p': 'She ___ homework', 'o': ['sometimes does', 'sometimes do', 'do sometimes'], 'r': 'sometimes does'},
                {'p': 'They ___ football after school', 'o': ['play', 'plays', 'playing'], 'r': 'play'},
                {'p': "It's half ___ six", 'o': ['past', 'to', 'quarter'], 'r': 'past'}
            ],
            [
                {'p': 'Complete: "My brother ___ games"', 'o': ['plays', 'play', 'playing'], 'r': 'plays'},
                {'p': 'What time do you ___ lunch?', 'o': ['have', 'has', 'having'], 'r': 'have'},
                {'p': 'I ___ go to the park', 'o': ['usually', 'never', 'always'], 'r': 'usually'},
                {'p': 'It"s ___ to ten', 'o': ['quarter', 'half', 'twenty'], 'r': 'quarter'},
                {'p': 'She ___ English', 'o': ['studies', 'study', 'studying'], 'r': 'studies'},
                {'p': 'We ___ at 7:00', 'o': ['get up', 'gets up', 'getting up'], 'r': 'get up'},
                {'p': 'He ___ pizza', 'o': ['never eats', 'never eat', 'eats never'], 'r': 'never eats'},
                {'p': 'They ___ to music', 'o': ['listen', 'listens', 'listening'], 'r': 'listen'},
                {'p': "It's ___ past two", 'o': ['half', 'quarter', 'twenty'], 'r': 'half'},
                {'p': 'My parents ___ at 11:00', 'o': ['go to bed', 'goes to bed', 'going'], 'r': 'go to bed'}
            ],
            [
                {'p': 'I ___ my teeth three times a day', 'o': ['brush', 'brushes', 'brushing'], 'r': 'brush'},
                {'p': 'What time ___ your bus?', 'o': ['does', 'do', 'is'], 'r': 'does'},
                {'p': 'She ___ TV', 'o': ['sometimes watches', 'sometimes watch', 'watch sometimes'], 'r': 'sometimes watches'},
                {'p': "It's quarter ___ three", 'o': ['to', 'past', 'half'], 'r': 'to'},
                {'p': 'We ___ at school from 9 to 3', 'o': ['are', 'is', 'have'], 'r': 'are'},
                {'p': 'He ___ breakfast at 8:00', 'o': ['has', 'have', 'having'], 'r': 'has'},
                {'p': 'They ___ early on Saturdays', 'o': ['don"t get up', 'doesn"t get up', 'not get up'], 'r': 'don"t get up'},
                {'p': 'I ___ my friends every weekend', 'o': ['visit', 'visits', 'visiting'], 'r': 'visit'},
                {'p': 'School ___ at 3:00', 'o': ['finishes', 'finish', 'finishing'], 'r': 'finishes'},
                {'p': "It's twenty ___ four", 'o': ['past', 'to', 'half'], 'r': 'past'}
            ]
        ]
    },

    'U6': {
        'titulo': 'Animals (Comparatives, prepositions)',
        'examenes': [
            [
                {'p': 'Elephant is ___ animal', 'o': ['bigger than', 'big than', 'biggest'], 'r': 'bigger than'},
                {'p': 'The cat is ___ the table', 'o': ['under', 'on', 'in'], 'r': 'under'},
                {'p': 'This bird is ___ that bird', 'o': ['smaller', 'small', 'smallest'], 'r': 'smaller'},
                {'p': 'The dog is ___ the chair', 'o': ['behind', 'under', 'on'], 'r': 'behind'},
                {'p': 'Lion is ___ tiger', 'o': ['bigger than a', 'big than', 'biggest than'], 'r': 'bigger than a'},
                {'p': 'The fish is ___ the bowl', 'o': ['in', 'on', 'under'], 'r': 'in'},
                {'p': 'This snake is ___ that snake', 'o': ['longer than', 'long than', 'longest'], 'r': 'longer than'},
                {'p': 'The ball is ___ the sofa', 'o': ['behind', 'in', 'on'], 'r': 'behind'},
                {'p': 'Horse is ___ donkey', 'o': ['faster than a', 'fast than', 'fastest'], 'r': 'faster than a'},
                {'p': 'The book is ___ the bed', 'o': ['under', 'on', 'in'], 'r': 'under'}
            ],
            [
                {'p': 'My house is ___ your house', 'o': ['bigger than', 'big than', 'biggest'], 'r': 'bigger than'},
                {'p': 'The picture is ___ the wall', 'o': ['on', 'under', 'behind'], 'r': 'on'},
                {'p': 'This car is ___ that car', 'o': ['faster than', 'fast than', 'fastest'], 'r': 'faster than'},
                {'p': 'The lamp is ___ the table', 'o': ['on', 'under', 'in'], 'r': 'on'},
                {'p': 'Rabbit is ___ mouse', 'o': ['bigger than a', 'big than', 'biggest'], 'r': 'bigger than a'},
                {'p': 'The keys are ___ the drawer', 'o': ['in', 'on', 'under'], 'r': 'in'},
                {'p': 'This book is ___ that book', 'o': ['thicker than', 'thick than', 'thickest'], 'r': 'thicker than'},
                {'p': 'The cat is ___ the box', 'o': ['in', 'on', 'under'], 'r': 'in'},
                {'p': 'Apple is ___ orange', 'o': ['smaller than an', 'small than', 'smallest'], 'r': 'smaller than an'},
                {'p': 'The TV is ___ the shelf', 'o': ['on', 'in', 'under'], 'r': 'on'}
            ],
            [
                {'p': 'My dog is ___ your dog', 'o': ['bigger than', 'big than', 'biggest'], 'r': 'bigger than'},
                {'p': 'The clock is ___ the wall', 'o': ['on', 'under', 'behind'], 'r': 'on'},
                {'p': 'This fish is ___ that fish', 'o': ['smaller than', 'small than', 'smallest'], 'r': 'smaller than'},
                {'p': 'The plate is ___ the table', 'o': ['on', 'under', 'in'], 'r': 'on'},
                {'p': 'Tiger is ___ lion', 'o': ['bigger than a', 'big than', 'biggest'], 'r': 'bigger than a'},
                {'p': 'The pen is ___ the bag', 'o': ['in', 'on', 'under'], 'r': 'in'},
                {'p': 'This river is ___ that river', 'o': ['longer than', 'long than', 'longest'], 'r': 'longer than'},
                {'p': 'The bird is ___ the tree', 'o': ['in', 'on', 'under'], 'r': 'in'},
                {'p': 'Summer is ___ winter', 'o': ['hotter than', 'hot than', 'hottest'], 'r': 'hotter than'},
                {'p': 'The painting is ___ the door', 'o': ['next to', 'on', 'under'], 'r': 'next to'}
            ]
        ]
    },

    'U7': {
        'titulo': 'Clothes (Present Continuous, shopping)',
        'examenes': [
            [
                {'p': 'Complete: "I ___ a T-shirt"', 'o': ['am wearing', 'wear', 'wears'], 'r': 'am wearing'},
                {'p': 'How much ___ these shoes?', 'o': ['do ... cost', 'does ... cost', 'is ... cost'], 'r': 'do ... cost'},
                {'p': 'She ___ jeans', 'o': ['is wearing', 'wear', 'wears'], 'r': 'is wearing'},
                {'p': 'How much is the shirt?', 'o': ['It"s ten euros', 'Ten euros', 'It ten euros'], 'r': 'It"s ten euros'},
                {'p': 'They ___ football', 'o': ['are playing', 'play', 'plays'], 'r': 'are playing'},
                {'p': '"Dress" significa:', 'o': ['Vestido', 'Pantalón', 'Camisa'], 'r': 'Vestido'},
                {'p': 'I ___ a blue sweater', 'o': ['am wearing', 'wear', 'wears'], 'r': 'am wearing'},
                {'p': 'How much ___ this hat?', 'o': ['does ... cost', 'do ... cost', 'is ... cost'], 'r': 'does ... cost'},
                {'p': 'We ___ TV now', 'o': ['are watching', 'watch', 'watches'], 'r': 'are watching'},
                {'p': '"Sweater" es:', 'o': ['Jersey', 'Zapatos', 'Sombrero'], 'r': 'Jersey'}
            ],
            [
                {'p': 'He ___ a red jacket', 'o': ['is wearing', 'wear', 'wears'], 'r': 'is wearing'},
                {'p': 'Excuse me, ___ are the T-shirts?', 'o': ['where', 'how much', 'what color'], 'r': 'where'},
                {'p': 'Look! They ___ basketball', 'o': ['are playing', 'play', 'plays'], 'r': 'are playing'},
                {'p': 'The trousers ___ twenty euros', 'o': ['are', 'is', 'have'], 'r': 'are'},
                {'p': 'She ___ her homework', 'o': ['is doing', 'do', 'does'], 'r': 'is doing'},
                {'p': '"Scarf" significa:', 'o': ['Bufanda', 'Guantes', 'Calcetines'], 'r': 'Bufanda'},
                {'p': 'What color ___ your shoes?', 'o': ['are', 'is', 'have'], 'r': 'are'},
                {'p': 'I ___ a green skirt', 'o': ['am wearing', 'wear', 'wears'], 'r': 'am wearing'},
                {'p': 'How much ___ that dress?', 'o': ['does ... cost', 'do ... cost', 'is ... cost'], 'r': 'does ... cost'},
                {'p': 'They ___ in the park', 'o': ['are running', 'run', 'runs'], 'r': 'are running'}
            ],
            [
                {'p': 'Complete: "___ wearing a hat"', 'o': ['He"s', 'He wear', 'He wears'], 'r': 'He"s'},
                {'p': 'The jacket ___ fifteen euros', 'o': ['costs', 'cost', 'are'], 'r': 'costs'},
                {'p': 'Look! She ___ a book', 'o': ['is reading', 'read', 'reads'], 'r': 'is reading'},
                {'p': '"Trainers" significa:', 'o': ['Zapatillas deportivas', 'Botas', 'Sandalias'], 'r': 'Zapatillas deportivas'},
                {'p': 'We ___ blue T-shirts', 'o': ['are wearing', 'wear', 'wears'], 'r': 'are wearing'},
                {'p': 'Where ___ the changing room?', 'o': ['is', 'are', 'have'], 'r': 'is'},
                {'p': 'I ___ shopping now', 'o': ['am going', 'go', 'goes'], 'r': 'am going'},
                {'p': 'These socks ___ five euros', 'o': ['are', 'is', 'cost'], 'r': 'are'},
                {'p': 'He ___ a black coat', 'o': ['is wearing', 'wear', 'wears'], 'r': 'is wearing'},
                {'p': 'What ___ you wearing?', 'o': ['are', 'is', 'have'], 'r': 'are'}
            ]
        ]
    },

    'U8': {
        'titulo': 'Routines (Daily routines, sequence words)',
        'examenes': [
            [
                {'p': 'Complete: "First, I ___ up"', 'o': ['get', 'get up', 'gets up'], 'r': 'get up'},
                {'p': 'Then, I ___ my teeth', 'o': ['brush', 'get', 'wash'], 'r': 'brush'},
                {'p': 'After that, I ___ breakfast', 'o': ['have', 'get', 'go'], 'r': 'have'},
                {'p': 'Finally, I ___ to school', 'o': ['go', 'get', 'brush'], 'r': 'go'},
                {'p': 'What do you do ___ the morning?', 'o': ['in', 'on', 'at'], 'r': 'in'},
                {'p': 'I ___ TV in the evening', 'o': ['watch', 'get up', 'brush'], 'r': 'watch'},
                {'p': 'Before school, I ___ my face', 'o': ['wash', 'watch', 'go'], 'r': 'wash'},
                {'p': 'Sequence: 1st, 2nd, 3rd, ___', 'o': ['4th', '3rd', '5th'], 'r': '4th'},
                {'p': 'I ___ dinner at 8:00', 'o': ['have', 'get', 'brush'], 'r': 'have'},
                {'p': 'After dinner, I ___ my homework', 'o': ['do', 'get up', 'watch'], 'r': 'do'}
            ],
            [
                {'p': 'First I wake ___, then I ___', 'o': ['up / shower', 'up / get up', 'on / shower'], 'r': 'up / shower'},
                {'p': 'I ___ to bed at 10:00', 'o': ['go', 'get', 'brush'], 'r': 'go'},
                {'p': 'Before lunch, I ___ my hands', 'o': ['wash', 'watch', 'do'], 'r': 'wash'},
                {'p': 'What"s next? First ___, then breakfast', 'o': ['get up', 'go to bed', 'brush teeth'], 'r': 'get up'},
                {'p': 'I ___ lunch at 2:00', 'o': ['have', 'get', 'go'], 'r': 'have'},
                {'p': 'After school, I ___ a snack', 'o': ['have', 'get up', 'brush'], 'r': 'have'},
                {'p': '"Next" significa:', 'o': ['Después', 'Primero', 'Finalmente'], 'r': 'Después'},
                {'p': 'I ___ games with my friends', 'o': ['play', 'get', 'wash'], 'r': 'play'},
                {'p': 'Finally, before sleeping, I ___ a story', 'o': ['read', 'get up', 'have'], 'r': 'read'},
                {'p': 'My routine: wake up, ___, breakfast, school', 'o': ['get dressed', 'go to bed', 'play games'], 'r': 'get dressed'}
            ],
            [
                {'p': 'Complete routine: First ___, then shower, then ___', 'o': ['wake up / breakfast', 'go to bed / dinner', 'play / sleep'], 'r': 'wake up / breakfast'},
                {'p': 'I ___ at 7:00 every morning', 'o': ['get up', 'go to bed', 'have dinner'], 'r': 'get up'},
                {'p': 'After that, I ___ my uniform', 'o': ['put on', 'take off', 'wash'], 'r': 'put on'},
                {'p': 'I ___ the bus at 8:00', 'o': ['catch', 'cook', 'read'], 'r': 'catch'},
                {'p': '"Get dressed" significa:', 'o': ['Vestirse', 'Desvestirse', 'Dormir'], 'r': 'Vestirse'},
                {'p': 'Evening routine: dinner, ___, bed', 'o': ['homework / go to', 'play football / get up', 'breakfast / school'], 'r': 'homework / go to'},
                {'p': 'I ___ a bath in the evening', 'o': ['have', 'get', 'play'], 'r': 'have'},
                {'p': 'Before bed, I ___ my teeth again', 'o': ['brush', 'wash', 'play'], 'r': 'brush'},
                {'p': 'Weekends I ___ later', 'o': ['get up', 'go to school', 'have breakfast'], 'r': 'get up'},
                {'p': 'Complete: wake up → get dressed → ___ → school', 'o': ['have breakfast', 'play games', 'go to bed'], 'r': 'have breakfast'}
            ]
        ]
    }
}
