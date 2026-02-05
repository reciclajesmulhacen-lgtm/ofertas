# estadisticas.py

import json
import os
from datetime import date

ARCHIVO = "resultados.json"

def registrar_resultado(usuario_id, unidad, examen_num, respuestas_usuario, TEMARIO):
    """
    Registra los resultados de un examen para un usuario específico.
    """
    # Crear archivo si no existe
    if not os.path.exists(ARCHIVO):
        with open(ARCHIVO, "w") as f:
            json.dump({}, f)

    # Cargar datos existentes
    with open(ARCHIVO, "r") as f:
        data = json.load(f)

    # Clave única por usuario + unidad + examen
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
            fallos.append(idx + 1)

    data[key]["aciertos"] = aciertos
    data[key]["fallos"] = fallos
    data[key]["historial"].append(str(date.today()))

    # Guardar de nuevo en el archivo JSON
    with open(ARCHIVO, "w") as f:
        json.dump(data, f, indent=2)

    return {"aciertos": aciertos, "fallos": fallos, "intentos": data[key]["intentos"]}


def ver_estadisticas(usuario_id, unidad, examen_num):
    """
    Devuelve un texto con las estadísticas de un examen de un usuario.
    """
    if not os.path.exists(ARCHIVO):
        return "No hay estadísticas todavía."

    with open(ARCHIVO, "r") as f:
        data = json.load(f)

    key = f"{usuario_id}_{unidad}_{examen_num}"
    if key not in data:
        return "No hay estadísticas para este examen."

    info = data[key]
    texto = (
        f"Intentos: {info['intentos']}\n"
        f"Aciertos: {info['aciertos']}\n"
        f"Fallos: {info['fallos']}\n"
        f"Historial de fechas: {info['historial']}"
    )
    return texto
