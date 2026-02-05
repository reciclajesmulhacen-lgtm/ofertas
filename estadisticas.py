# estadisticas.py

import json
import os
from datetime import date

ARCHIVO = "resultados.json"

def registrar_resultado(usuario_id, unidad, examen_num, respuestas_usuario, TEMARIO):
    # Crea el archivo si no existe
    if not os.path.exists(ARCHIVO):
        with open(ARCHIVO, "w") as f:
            json.dump({}, f)

    # Carga los datos existentes
    with open(ARCHIVO, "r") as f:
        data = json.load(f)

    # Clave única por usuario y examen
    key = f"{usuario_id}_{unidad}_{examen_num}"
    if key not in data:
        data[key] = {
            "intentos": 0,
            "aciertos": 0,
            "fallos": [],
            "historial": []
        }

    data[key]["intentos"] += 1
    aciertos = 0
    fallos = []

    for idx, r in enumerate(respuestas_usuario):
        if r != "INCORRECTA":
            aciertos += 1
        else:
            fallos.append(idx+1)

    data[key]["aciertos"] = aciertos
    data[key]["fallos"] = fallos
    data[key]["historial"].append(str(date.today()))

    # Guarda los datos
    with open(ARCHIVO, "w") as f:
        json.dump(data, f, indent=2)

    return {"aciertos": aciertos, "fallos": fallos, "intentos": dat
