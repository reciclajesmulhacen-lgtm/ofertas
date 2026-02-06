import json
import os
from datetime import datetime

# VARIABLES GLOBALES
ventana = None
frame_contenido = None
materia_actual = "mates"
unidad_actual = "U1"
puntuacion_total = 0
examenes_completados = []

# 🔙 FUNCIÓN VOLVER A boy.py
def volver_menu_principal():
    """Vuelve a boy.py"""
    ventana.destroy()
    import boy
    boy.main()

# 💾 FUNCIÓN GUARDAR PROGRESO
def guardar_progreso():
    """Guarda progreso actual"""
    global puntuacion_total, unidad_actual, examenes_completados
    progreso = {
        "materia": materia_actual,
        "unidad": unidad_actual,
        "puntuacion": puntuacion_total,
        "examenes_completados": examenes_completados,
        "fecha": datetime.now().strftime("%d/%m/%Y %H:%M"),
        "total_preguntas": 0
    }
    with open("progreso.json", "w", encoding="utf-8") as f:
        json.dump(progreso, f, ensure_ascii=False, indent=2)
    print("✅ Progreso guardado!")



TEMARIO = {
    'U1': {
        'titulo': 'Números hasta 1.000.000 (Leer/escribir, valor posicional)',
        'examenes': [
            [
                {'p': '¿Cuántas centenas hay en 5.432?', 'o': ['5', '43', '432'], 'r': '5'},
                {'p': 'Escribe en letras: 7.890', 'o': ['siete mil ochocientos noventa', 'siete ochenta y noventa', 'siete mil noventa'], 'r': 'siete mil ochocientos noventa'},
                {'p': '¿Cuál es el valor de las 3 en 34.567?', 'o': ['3.000', '300', '30'], 'r': '3.000'},
                {'p': 'Ordena: 12.345, 12.354, 12.435', 'o': ['12.345, 12.354, 12.435', '12.435, 12.354, 12.345', '12.354, 12.345, 12.435'], 'r': '12.345, 12.354, 12.435'},
                {'p': 'Completa: 89.XXX tiene ___ millares', 'o': ['89', '8', '9'], 'r': '89'},
                {'p': '¿Qué número es mayor? 456.789 ___ 456.798', 'o': ['>', '<', '='], 'r': '>'},
                {'p': 'Escribe: OCHENTA Y CUATRO MIL', 'o': ['84.000', '8.400', '84.000'], 'r': '84.000'},
                {'p': 'Valor posicional del 6 en 267.891', 'o': ['600', '6.000', '60.000'], 'r': '60.000'},
                {'p': 'Completa el desglose: 34.567 = ___ millares + 4 centenas', 'o': ['34.000', '34.500', '30.000'], 'r': '34.000'},
                {'p': '¿Cuál está ordenado correctamente?', 'o': ['123, 132, 213', '213, 132, 123', '132, 123, 213'], 'r': '123, 132, 213'}
            ],
            [
                {'p': '¿Cuántos millares en 98.765?', 'o': ['98', '9', '987'], 'r': '98'},
                {'p': 'Escribe en números: CUARENTA Y DOS MIL', 'o': ['42.000', '4.200', '42.000'], 'r': '42.000'},
                {'p': 'Valor del 9 en 19.234', 'o': ['9.000', '900', '90'], 'r': '9.000'},
                {'p': '¿Cuál es menor? 567.890 ___ 567.809', 'o': ['>', '<', '='], 'r': '<'},
                {'p': 'Completa: 123.456 = 100.000 + ___ + 3.000 + 400 + 50 + 6', 'o': ['20.000', '23.000', '2.000'], 'r': '20.000'},
                {'p': 'Escribe: NOVENTA Y SIETE MIL', 'o': ['97.000', '9.700', '97.000'], 'r': '97.000'},
                {'p': '¿Cuántas unidades de millar en 456.789?', 'o': ['456', '45', '4'], 'r': '456'},
                {'p': 'Ordena de menor a mayor: 100.000, 10.000, 1.000', 'o': ['1.000, 10.000, 100.000', '100.000, 10.000, 1.000', '10.000, 1.000, 100.000'], 'r': '1.000, 10.000, 100.000'},
                {'p': 'Valor posicional del 2 en 321.000', 'o': ['200.000', '20.000', '2.000'], 'r': '200.000'},
                {'p': 'Completa: En 78.912 el dígito de las decenas es', 'o': ['1', '90', '12'], 'r': '1'}
            ],
            [
                {'p': 'Escribe: SESENTA Y TRES MIL CUATROCIENTOS', 'o': ['63.400', '6.340', '63.400'], 'r': '63.400'},
                {'p': '¿Cuántas centenas en 987.654?', 'o': ['6', '65', '654'], 'r': '6'},
                {'p': '¿Qué número sigue?: 234.567, 234.568, ___', 'o': ['234.569', '234.678', '234.570'], 'r': '234.569'},
                {'p': 'Valor del 5 en 543.210', 'o': ['5.000', '500', '50'], 'r': '5.000'},
                {'p': 'Completa el desglose: 999.999 = 900.000 + ___ + 9.000 + 900 + 90 + 9', 'o': ['90.000', '99.000', '9.000'], 'r': '90.000'},
                {'p': '¿Cuál es mayor? 123.456 ___ 123.465', 'o': ['>', '<', '='], 'r': '<'},
                {'p': 'Escribe en letras: 500.000', 'o': ['quinientos mil', 'cinco mil', 'cincuenta mil'], 'r': 'quinientos mil'},
                {'p': '¿Cuántos millares hay en 1.000.000?', 'o': ['1.000', '100', '10'], 'r': '1.000'},
                {'p': 'Valor posicional del 8 en 180.000', 'o': ['8.000', '80.000', '800.000'], 'r': '80.000'},
                {'p': 'Ordena: 99.999, 100.000, 99.998', 'o': ['99.998, 99.999, 100.000', '100.000, 99.999, 99.998', '99.999, 99.998, 100.000'], 'r': '99.998, 99.999, 100.000'}
            ]
        ]
    },

    'U2': {
        'titulo': 'Operaciones naturales (Suma/resta/multiplicación/división)',
        'examenes': [
            [
                {'p': 'Resuelve: 456 + 789 =', 'o': ['1.245', '1.235', '1.255'], 'r': '1.245'},
                {'p': 'Resuelve: 1.234 - 567 =', 'o': ['667', '677', '657'], 'r': '667'},
                {'p': 'Multiplica: 23 × 4 =', 'o': ['92', '82', '102'], 'r': '92'},
                {'p': 'Divide: 84 ÷ 7 =', 'o': ['12', '11', '13'], 'r': '12'},
                {'p': '¿Cuánto es 999 + 1?', 'o': ['1.000', '998', '1.001'], 'r': '1.000'},
                {'p': 'Resuelve: 456 × 2 =', 'o': ['912', '902', '922'], 'r': '912'},
                {'p': 'Resta: 1.000 - 456 =', 'o': ['544', '554', '534'], 'r': '544'},
                {'p': 'Divide: 96 ÷ 8 =', 'o': ['12', '10', '14'], 'r': '12'},
                {'p': 'Multiplica: 45 × 3 =', 'o': ['135', '145', '125'], 'r': '135'},
                {'p': 'Suma: 2.345 + 3.456 =', 'o': ['5.801', '5.811', '5.791'], 'r': '5.801'}
            ],
            [
                {'p': 'Resuelve: 567 + 432 =', 'o': ['999', '989', '1.009'], 'r': '999'},
                {'p': 'Multiplica: 12 × 12 =', 'o': ['144', '132', '156'], 'r': '144'},
                {'p': 'Resta: 876 - 234 =', 'o': ['642', '652', '632'], 'r': '642'},
                {'p': 'Divide: 144 ÷ 12 =', 'o': ['12', '14', '10'], 'r': '12'},
                {'p': 'Suma con llevada: 598 + 457 =', 'o': ['1.055', '1.045', '1.065'], 'r': '1.055'},
                {'p': 'Multiplica: 25 × 4 =', 'o': ['100', '90', '110'], 'r': '100'},
                {'p': 'Resta con préstamo: 1.000 - 777 =', 'o': ['223', '233', '213'], 'r': '223'},
                {'p': 'Divide: 72 ÷ 9 =', 'o': ['8', '7', '9'], 'r': '8'},
                {'p': 'Multiplica: 67 × 2 =', 'o': ['134', '124', '144'], 'r': '134'},
                {'p': 'Suma: 999 + 999 =', 'o': ['1.998', '2.000', '1.988'], 'r': '1.998'}
            ],
            [
                {'p': 'Resuelve: 3.456 + 2.543 =', 'o': ['5.999', '5.989', '6.009'], 'r': '5.999'},
                {'p': 'Multiplica: 34 × 3 =', 'o': ['102', '94', '112'], 'r': '102'},
                {'p': 'Resta: 5.000 - 2.345 =', 'o': ['2.655', '2.645', '2.665'], 'r': '2.655'},
                {'p': 'Divide: 180 ÷ 12 =', 'o': ['15', '12', '18'], 'r': '15'},
                {'p': 'Suma: 1.234 + 5.566 =', 'o': ['6.800', '6.790', '6.810'], 'r': '6.800'},
                {'p': 'Multiplica: 89 × 2 =', 'o': ['178', '188', '168'], 'r': '178'},
                {'p': 'Divide: 250 ÷ 5 =', 'o': ['50', '45', '55'], 'r': '50'},
                {'p': 'Resta: 987 - 654 =', 'o': ['333', '343', '323'], 'r': '333'},
                {'p': 'Multiplica: 56 × 3 =', 'o': ['168', '158', '178'], 'r': '168'},
                {'p': 'Suma: 4.567 + 5.432 =', 'o': ['9.999', '10.000', '9.989'], 'r': '9.999'}
            ]
        ]
    },

    'U3': {
        'titulo': 'Decimales (Suma/resta/comparar decimales)',
        'examenes': [
            [
                {'p': 'Suma: 2,3 + 1,7 =', 'o': ['4,0', '3,9', '4,1'], 'r': '4,0'},
                {'p': 'Resta: 5,8 - 2,4 =', 'o': ['3,4', '3,3', '3,5'], 'r': '3,4'},
                {'p': '¿Cuál es mayor? 1,23 ___ 1,32', 'o': ['>', '<', '='], 'r': '<'},
                {'p': 'Suma: 0,45 + 0,55 =', 'o': ['1,00', '0,99', '1,01'], 'r': '1,00'},
                {'p': 'Completa: 3,___ + 4,2 = 8,5', 'o': ['5,3', '4,3', '5,2'], 'r': '4,3'},
                {'p': 'Ordena: 2,5; 2,05; 2,50', 'o': ['2,05; 2,5; 2,50', '2,50; 2,5; 2,05', '2,5; 2,05; 2,50'], 'r': '2,05; 2,5; 2,50'},
                {'p': 'Resta: 7,99 - 3,50 =', 'o': ['4,49', '4,59', '4,39'], 'r': '4,49'},
                {'p': '¿Cuál es menor? 0,9 ___ 0,89', 'o': ['>', '<', '='], 'r': '<'},
                {'p': 'Suma: 1,25 + 2,75 =', 'o': ['4,00', '3,99', '4,01'], 'r': '4,00'},
                {'p': 'Escribe con coma: 2 + 0,5 + 0,3', 'o': ['2,8', '2,83', '2,35'], 'r': '2,8'}
            ],
            [
                {'p': 'Suma: 4,56 + 3,44 =', 'o': ['8,00', '7,99', '8,01'], 'r': '8,00'},
                {'p': 'Resta: 9,87 - 4,32 =', 'o': ['5,55', '5,45', '5,65'], 'r': '5,55'},
                {'p': '¿Cuál es mayor? 3,09 ___ 3,90', 'o': ['>', '<', '='], 'r': '>'},
                {'p': 'Suma: 2,99 + 3,01 =', 'o': ['6,00', '5,99', '6,01'], 'r': '6,00'},
                {'p': 'Ordena de menor a mayor: 1,2; 1,02; 1,20', 'o': ['1,02; 1,2; 1,20', '1,20; 1,2; 1,02', '1,2; 1,02; 1,20'], 'r': '1,02; 1,2; 1,20'},
                {'p': 'Resta: 10,00 - 6,75 =', 'o': ['3,25', '3,35', '3,15'], 'r': '3,25'},
                {'p': 'Completa: 1,___ + 2,4 = 4,0', 'o': ['2,6', '2,5', '2,7'], 'r': '2,6'},
                {'p': '¿Cuál es igual? 2,50 ___ 2,5', 'o': ['>', '<', '='], 'r': '='},
                {'p': 'Suma: 0,89 + 0,11 =', 'o': ['1,00', '0,99', '1,01'], 'r': '1,00'},
                {'p': 'Resta: 8,90 - 4,45 =', 'o': ['4,45', '4,35', '4,55'], 'r': '4,45'}
            ],
            [
                {'p': 'Suma: 12,34 + 7,66 =', 'o': ['20,00', '19,99', '20,01'], 'r': '20,00'},
                {'p': 'Resta: 15,99 - 9,23 =', 'o': ['6,76', '6,66', '6,86'], 'r': '6,76'},
                {'p': '¿Cuál es mayor? 4,01 ___ 4,10', 'o': ['>', '<', '='], 'r': '>'},
                {'p': 'Suma: 5,49 + 4,51 =', 'o': ['10,00', '9,99', '10,01'], 'r': '10,00'},
                {'p': 'Ordena: 0,9; 0,89; 0,98', 'o': ['0,89; 0,9; 0,98', '0,98; 0,9; 0,89', '0,9; 0,89; 0,98'], 'r': '0,89; 0,9; 0,98'},
                {'p': 'Resta: 20,00 - 13,57 =', 'o': ['6,43', '6,53', '6,33'], 'r': '6,43'},
                {'p': '¿Cuál es menor? 2,99 ___ 3,0', 'o': ['>', '<', '='], 'r': '>'},
                {'p': 'Suma: 9,98 + 0,02 =', 'o': ['10,00', '9,99', '10,01'], 'r': '10,00'},
                {'p': 'Completa: 7,___ - 2,3 = 4,9', 'o': ['7,2', '7,1', '7,3'], 'r': '7,2'},
                {'p': 'Resta: 100,00 - 67,89 =', 'o': ['32,11', '32,21', '32,01'], 'r': '32,11'}
            ]
        ]
    },

    'U4': {
        'titulo': 'Fracciones comunes (1/2, 1/4, equivalentes)',
        'examenes': [
            [
                {'p': '¿Cuánto es la mitad de 16?', 'o': ['8', '4', '12'], 'r': '8'},
                {'p': '¿Cuánto es 1/4 de 20?', 'o': ['5', '4', '10'], 'r': '5'},
                {'p': 'Marca la fracción equivalente a 1/2:', 'o': ['2/4', '1/3', '1/4'], 'r': '2/4'},
                {'p': 'Completa: 1/2 de 24 =', 'o': ['12', '6', '8'], 'r': '12'},
                {'p': '¿Cuál es 1/4 de 16?', 'o': ['4', '8', '2'], 'r': '4'},
                {'p': '¿Qué fracción es igual a 1/2?', 'o': ['3/6', '1/3', '2/5'], 'r': '3/6'},
                {'p': 'Mitad de 30:', 'o': ['15', '10', '20'], 'r': '15'},
                {'p': '1/4 de 12:', 'o': ['3', '4', '6'], 'r': '3'},
                {'p': '¿Cuál es equivalente a 1/4?', 'o': ['2/8', '1/2', '3/12'], 'r': '2/8'},
                {'p': 'Completa: 1/2 = ___/8', 'o': ['4', '2', '6'], 'r': '4'}
            ],
            [
                {'p': 'Mitad de 18:', 'o': ['9', '6', '12'], 'r': '9'},
                {'p': '1/4 de 28:', 'o': ['7', '14', '4'], 'r': '7'},
                {'p': '¿Cuál es equivalente a 1/2?', 'o': ['4/8', '2/3', '3/5'], 'r': '4/8'},
                {'p': '1/4 de 36:', 'o': ['9', '12', '18'], 'r': '9'},
                {'p': 'Mitad de 40:', 'o': ['20', '10', '30'], 'r': '20'},
                {'p': '¿Qué es igual a 1/4?', 'o': ['3/12', '1/2', '2/6'], 'r': '3/12'},
                {'p': '1/2 de 50:', 'o': ['25', '10', '30'], 'r': '25'},
                {'p': '1/4 de 24:', 'o': ['6', '8', '12'], 'r': '6'},
                {'p': 'Completa: 1/2 = ___/10', 'o': ['5', '2', '10'], 'r': '5'},
                {'p': '¿Cuál es equivalente a 1/4?', 'o': ['1/4', '1/2', '1/8'], 'r': '1/4'}
            ],
            [
                {'p': 'Mitad de 32:', 'o': ['16', '8', '24'], 'r': '16'},
                {'p': '1/4 de 40:', 'o': ['10', '20', '5'], 'r': '10'},
                {'p': '¿Cuál es igual a 1/2?', 'o': ['5/10', '1/3', '2/4'], 'r': '5/10'},
                {'p': '1/4 de 32:', 'o': ['8', '16', '4'], 'r': '8'},
                {'p': 'Mitad de 28:', 'o': ['14', '7', '21'], 'r': '14'},
                {'p': '¿Qué fracción equivale a 1/4?', 'o': ['5/20', '1/2', '3/8'], 'r': '5/20'},
                {'p': '1/2 de 36:', 'o': ['18', '12', '24'], 'r': '18'},
                {'p': '1/4 de 44:', 'o': ['11', '22', '4'], 'r': '11'},
                {'p': 'Completa: 1/4 = ___/12', 'o': ['3', '6', '4'], 'r': '3'},
                {'p': '¿Cuál es la mitad representada como fracción?', 'o': ['1/2', '1/4', '3/4'], 'r': '1/2'}
            ]
        ]
    },

    'U5': {
        'titulo': 'Geometría plana (Polígonos, perímetro)',
        'examenes': [
            [
                {'p': '¿Cuántos lados tiene un triángulo?', 'o': ['3', '4', '5'], 'r': '3'},
                {'p': '¿Cuántos lados tiene un cuadrado?', 'o': ['4', '3', '6'], 'r': '4'},
                {'p': 'Perímetro de un cuadrado de lado 5 cm:', 'o': ['20 cm', '10 cm', '15 cm'], 'r': '20 cm'},
                {'p': '¿Qué polígono tiene 5 lados?', 'o': ['Pentágono', 'Hexágono', 'Triángulo'], 'r': 'Pentágono'},
                {'p': 'Perímetro de un rectángulo 3×6 cm:', 'o': ['18 cm', '9 cm', '24 cm'], 'r': '18 cm'},
                {'p': '¿Cuántos lados tiene un hexágono?', 'o': ['6', '5', '8'], 'r': '6'},
                {'p': 'Perímetro de triángulo con lados 4, 5, 6 cm:', 'o': ['15 cm', '10 cm', '20 cm'], 'r': '15 cm'},
                {'p': '¿Qué figura tiene todos los lados iguales?', 'o': ['Cuadrado', 'Rectángulo', 'Triángulo'], 'r': 'Cuadrado'},
                {'p': 'Perímetro de pentágono regular lado 2 cm:', 'o': ['10 cm', '5 cm', '12 cm'], 'r': '10 cm'},
                {'p': '¿Cuántos vértices tiene un cuadrilátero?', 'o': ['4', '3', '5'], 'r': '4'}
            ],
            [
                {'p': 'Perímetro de rectángulo 4×8 cm:', 'o': ['24 cm', '12 cm', '32 cm'], 'r': '24 cm'},
                {'p': '¿Qué polígono tiene 8 lados?', 'o': ['Octágono', 'Heptágono', 'Pentágono'], 'r': 'Octágono'},
                {'p': 'Perímetro de cuadrado lado 7 cm:', 'o': ['28 cm', '14 cm', '21 cm'], 'r': '28 cm'},
                {'p': '¿Cuántos lados tiene un rectángulo?', 'o': ['4', '3', '5'], 'r': '4'},
                {'p': 'Perímetro de triángulo 5, 5, 5 cm:', 'o': ['15 cm', '10 cm', '20 cm'], 'r': '15 cm'},
                {'p': '¿Qué figura tiene 4 lados pero no todos iguales?', 'o': ['Rectángulo', 'Cuadrado', 'Triángulo'], 'r': 'Rectángulo'},
                {'p': 'Perímetro de pentágono regular lado 3 cm:', 'o': ['15 cm', '10 cm', '18 cm'], 'r': '15 cm'},
                {'p': '¿Cuántos vértices tiene un pentágono?', 'o': ['5', '4', '6'], 'r': '5'},
                {'p': 'Perímetro de rectángulo 5×10 cm:', 'o': ['30 cm', '15 cm', '25 cm'], 'r': '30 cm'},
                {'p': '¿Qué polígono tiene 7 lados?', 'o': ['Heptágono', 'Hexágono', 'Octágono'], 'r': 'Heptágono'}
            ],
            [
                {'p': 'Perímetro de cuadrado lado 6 cm:', 'o': ['24 cm', '12 cm', '18 cm'], 'r': '24 cm'},
                {'p': '¿Cuántos lados tiene un triángulo?', 'o': ['3', '4', '6'], 'r': '3'},
                {'p': 'Perímetro de rectángulo 2×9 cm:', 'o': ['22 cm', '11 cm', '18 cm'], 'r': '22 cm'},
                {'p': '¿Qué es el perímetro?', 'o': ['Suma de todos los lados', 'Número de lados', 'Área interior'], 'r': 'Suma de todos los lados'},
                {'p': 'Perímetro de pentágono regular lado 4 cm:', 'o': ['20 cm', '16 cm', '24 cm'], 'r': '20 cm'},
                {'p': '¿Cuántos vértices tiene un hexágono?', 'o': ['6', '5', '8'], 'r': '6'},
                {'p': 'Perímetro de triángulo 3, 4, 5 cm:', 'o': ['12 cm', '10 cm', '15 cm'], 'r': '12 cm'},
                {'p': '¿Qué figura tiene 4 lados y 4 ángulos rectos?', 'o': ['Rectángulo', 'Triángulo', 'Pentágono'], 'r': 'Rectángulo'},
                {'p': 'Perímetro de cuadrado lado 9 cm:', 'o': ['36 cm', '18 cm', '27 cm'], 'r': '36 cm'},
                {'p': '¿Cuántos lados tiene un octágono?', 'o': ['8', '7', '6'], 'r': '8'}
            ]
        ]
    },

    'U6': {
        'titulo': 'Medidas (Perímetro/área, conversiones)',
        'examenes': [
            [
                {'p': '¿Cuántos cm en 1 m?', 'o': ['100', '10', '1.000'], 'r': '100'},
                {'p': 'Área de cuadrado lado 4 cm:', 'o': ['16 cm²', '8 cm²', '20 cm²'], 'r': '16 cm²'},
                {'p': 'Convierte 2 m a cm:', 'o': ['200 cm', '20 cm', '2.000 cm'], 'r': '200 cm'},
                {'p': 'Perímetro de rectángulo 3×5 cm:', 'o': ['16 cm', '8 cm', '15 cm'], 'r': '16 cm'},
                {'p': 'Área de rectángulo 2×6 cm:', 'o': ['12 cm²', '8 cm²', '24 cm²'], 'r': '12 cm²'},
                {'p': 'Convierte 300 cm a m:', 'o': ['3 m', '30 m', '0,3 m'], 'r': '3 m'},
                {'p': '¿Cuántos mm en 1 cm?', 'o': ['10', '100', '1.000'], 'r': '10'},
                {'p': 'Área de cuadrado lado 5 cm:', 'o': ['25 cm²', '10 cm²', '20 cm²'], 'r': '25 cm²'},
                {'p': 'Convierte 1,5 m a cm:', 'o': ['150 cm', '15 cm', '1.500 cm'], 'r': '150 cm'},
                {'p': 'Perímetro de triángulo 4, 4, 4 cm:', 'o': ['12 cm', '8 cm', '16 cm'], 'r': '12 cm'}
            ],
            [
                {'p': 'Área de rectángulo 4×7 cm:', 'o': ['28 cm²', '11 cm²', '44 cm²'], 'r': '28 cm²'},
                {'p': 'Convierte 450 cm a m:', 'o': ['4,5 m', '45 m', '0,45 m'], 'r': '4,5 m'},
                {'p': '¿Cuántos cm en 3 m?', 'o': ['300 cm', '30 cm', '3.000 cm'], 'r': '300 cm'},
                {'p': 'Área de cuadrado lado 6 cm:', 'o': ['36 cm²', '12 cm²', '24 cm²'], 'r': '36 cm²'},
                {'p': 'Perímetro de rectángulo 5×8 cm:', 'o': ['26 cm', '13 cm', '40 cm'], 'r': '26 cm'},
                {'p': 'Convierte 25 cm a mm:', 'o': ['250 mm', '25 mm', '2.500 mm'], 'r': '250 mm'},
                {'p': 'Área de rectángulo 3×9 cm:', 'o': ['27 cm²', '12 cm²', '36 cm²'], 'r': '27 cm²'},
                {'p': 'Convierte 2,5 m a cm:', 'o': ['250 cm', '25 cm', '2.500 cm'], 'r': '250 cm'},
                {'p': 'Perímetro de cuadrado lado 7 cm:', 'o': ['28 cm', '14 cm', '49 cm'], 'r': '28 cm'},
                {'p': '¿Qué mide el área?', 'o': ['cm²', 'cm', 'm'], 'r': 'cm²'}
            ],
            [
                {'p': 'Área de rectángulo 6×6 cm:', 'o': ['36 cm²', '12 cm²', '72 cm²'], 'r': '36 cm²'},
                {'p': 'Convierte 1.200 cm a m:', 'o': ['12 m', '1,2 m', '120 m'], 'r': '12 m'},
                {'p': 'Perímetro de rectángulo 4×10 cm:', 'o': ['28 cm', '14 cm', '40 cm'], 'r': '28 cm'},
                {'p': 'Área de cuadrado lado 8 cm:', 'o': ['64 cm²', '16 cm²', '32 cm²'], 'r': '64 cm²'},
                {'p': 'Convierte 75 cm a mm:', 'o': ['750 mm', '75 mm', '7.500 mm'], 'r': '750 mm'},
                {'p': 'Área de rectángulo 5×7 cm:', 'o': ['35 cm²', '12 cm²', '70 cm²'], 'r': '35 cm²'},
                {'p': 'Convierte 4 m a cm:', 'o': ['400 cm', '40 cm', '4.000 cm'], 'r': '400 cm'},
                {'p': 'Perímetro de triángulo 5, 5, 6 cm:', 'o': ['16 cm', '12 cm', '20 cm'], 'r': '16 cm'},
                {'p': '¿Cuántos mm en 1 m?', 'o': ['1.000', '100', '10'], 'r': '1.000'},
                {'p': 'Área de cuadrado lado 3 cm:', 'o': ['9 cm²', '6 cm²', '12 cm²'], 'r': '9 cm²'}
            ]
        ]
    },

    'U7': {
        'titulo': 'Porcentajes (25%, 50%, 10% de cantidad)',
        'examenes': [
            [
                {'p': '¿Qué es el 50% de 100?', 'o': ['50', '25', '10'], 'r': '50'},
                {'p': '¿Qué es el 25% de 80?', 'o': ['20', '40', '10'], 'r': '20'},
                {'p': '¿Qué es el 10% de 50?', 'o': ['5', '10', '25'], 'r': '5'},
                {'p': '50% de 60:', 'o': ['30', '15', '20'], 'r': '30'},
                {'p': '25% de 40:', 'o': ['10', '20', '5'], 'r': '10'},
                {'p': '10% de 200:', 'o': ['20', '10', '50'], 'r': '20'},
                {'p': '50% es lo mismo que:', 'o': ['1/2', '1/4', '1/10'], 'r': '1/2'},
                {'p': '25% de 100:', 'o': ['25', '50', '10'], 'r': '25'},
                {'p': '10% de 90:', 'o': ['9', '18', '45'], 'r': '9'},
                {'p': '50% de 80:', 'o': ['40', '20', '16'], 'r': '40'}
            ],
            [
                {'p': '25% de 60:', 'o': ['15', '30', '20'], 'r': '15'},
                {'p': '10% de 300:', 'o': ['30', '15', '60'], 'r': '30'},
                {'p': '50% de 90:', 'o': ['45', '25', '18'], 'r': '45'},
                {'p': '25% es lo mismo que:', 'o': ['1/4', '1/2', '1/10'], 'r': '1/4'},
                {'p': '10% de 70:', 'o': ['7', '14', '35'], 'r': '7'},
                {'p': '50% de 120:', 'o': ['60', '30', '24'], 'r': '60'},
                {'p': '25% de 200:', 'o': ['50', '25', '100'], 'r': '50'},
                {'p': '10% es lo mismo que:', 'o': ['1/10', '1/4', '1/2'], 'r': '1/10'},
                {'p': '50% de 150:', 'o': ['75', '37', '50'], 'r': '75'},
                {'p': '25% de 120:', 'o': ['30', '60', '12'], 'r': '30'}
            ],
            [
                {'p': '10% de 400:', 'o': ['40', '20', '80'], 'r': '40'},
                {'p': '50% de 70:', 'o': ['35', '17', '28'], 'r': '35'},
                {'p': '25% de 80:', 'o': ['20', '40', '16'], 'r': '20'},
                {'p': '10% de 150:', 'o': ['15', '30', '75'], 'r': '15'},
                {'p': '50% de 200:', 'o': ['100', '50', '20'], 'r': '100'},
                {'p': '25% de 36:', 'o': ['9', '18', '12'], 'r': '9'},
                {'p': '10% de 80:', 'o': ['8', '16', '40'], 'r': '8'},
                {'p': '50% de 44:', 'o': ['22', '11', '44'], 'r': '22'},
                {'p': '25% de 92:', 'o': ['23', '46', '18'], 'r': '23'},
                {'p': '¿Qué porcentaje es la mitad?', 'o': ['50%', '25%', '10%'], 'r': '50%'}
            ]
        ]
    },

    'U8': {
        'titulo': 'Estadística (Gráficos barras, media/moda)',
        'examenes': [
            [
                {'p': 'En un gráfico de barras, el eje vertical representa:', 'o': ['Cantidad', 'Nombres', 'Colores'], 'r': 'Cantidad'},
                {'p': 'Datos: 2, 3, 3, 4. La moda es:', 'o': ['3', '2', '4'], 'r': '3'},
                {'p': 'Media de: 10, 20, 30', 'o': ['20', '15', '25'], 'r': '20'},
                {'p': '¿Qué muestra un gráfico de barras?', 'o': ['Comparación de datos', 'Suma total', 'Porcentajes'], 'r': 'Comparación de datos'},
                {'p': 'Datos: 5, 5, 6, 7. La moda es:', 'o': ['5', '6', '7'], 'r': '5'},
                {'p': 'Media de: 4, 6, 8', 'o': ['6', '5', '7'], 'r': '6'},
                {'p': '¿Qué es la moda?', 'o': ['Número que más se repite', 'Suma de todos', 'Promedio'], 'r': 'Número que más se repite'},
                {'p': 'Media de: 1, 2, 3, 4', 'o': ['2,5', '2', '3'], 'r': '2,5'},
                {'p': 'Datos: 10, 10, 20, 30. Moda:', 'o': ['10', '20', '30'], 'r': '10'},
                {'p': 'Gráfico de barras sirve para:', 'o': ['Comparar cantidades', 'Medir áreas', 'Calcular porcentajes'], 'r': 'Comparar cantidades'}
            ],
            [
                {'p': 'Datos: 7, 7, 8, 9, 9. ¿Cuál es la moda?', 'o': ['7 y 9', '8', '7'], 'r': '7 y 9'},
                {'p': 'Media de: 12, 14, 16', 'o': ['14', '13', '15'], 'r': '14'},
                {'p': 'En un gráfico de barras, las barras más altas indican:', 'o': ['Mayor cantidad', 'Menor cantidad', 'Igual cantidad'], 'r': 'Mayor cantidad'},
                {'p': 'Datos: 3, 4, 4, 5. Moda:', 'o': ['4', '3', '5'], 'r': '4'},
                {'p': 'Media de: 20, 30, 40, 50', 'o': ['35', '30', '40'], 'r': '35'},
                {'p': '¿Qué es la media?', 'o': ['Promedio de los datos', 'Máximo valor', 'Dato más frecuente'], 'r': 'Promedio de los datos'},
                {'p': 'Datos: 1, 2, 2, 3, 3, 3. Moda:', 'o': ['3', '2', '1'], 'r': '3'},
                {'p': 'Media de: 5, 10, 15', 'o': ['10', '8', '12'], 'r': '10'},
                {'p': 'Gráfico de barras: barra azul 15, roja 20. ¿Cuál es mayor?', 'o': ['Roja', 'Azul', 'Iguales'], 'r': 'Roja'},
                {'p': 'Datos sin moda: 1, 2, 3, 4', 'o': ['No hay moda', '1', '4'], 'r': 'No hay moda'}
            ],
            [
                {'p': 'Media de: 8, 12, 16, 20', 'o': ['14', '12', '16'], 'r': '14'},
                {'p': 'Datos: 6, 6, 7, 8, 9. Moda:', 'o': ['6', '7', '9'], 'r': '6'},
                {'p': 'En gráfico barras: lunes 5, martes 8. ¿Cuál más?', 'o': ['Martes', 'Lunes', 'Iguales'], 'r': 'Martes'},
                {'p': 'Media de: 2, 4, 6, 8, 10', 'o': ['6', '5', '7'], 'r': '6'},
                {'p': 'Datos: 11, 12, 12, 13. Moda:', 'o': ['12', '11', '13'], 'r': '12'},
                {'p': '¿Qué mide la altura de las barras?', 'o': ['Cantidad o frecuencia', 'Nombre de categoría', 'Color'], 'r': 'Cantidad o frecuencia'},
                {'p': 'Media de: 100, 200, 300', 'o': ['200', '150', '250'], 'r': '200'},
                {'p': 'Datos: 4, 5, 5, 6, 6, 6. ¿Cuál moda?', 'o': ['6', '5', '4'], 'r': '6'},
                {'p': 'Media de 3 números iguales (5, 5, 5):', 'o': ['5', '3', '15'], 'r': '5'},
                {'p': 'Gráfico barras compara:', 'o': ['Diferentes categorías', 'Solo un dato', 'Áreas'], 'r': 'Diferentes categorías'}
            ]
        ]
    }
}
