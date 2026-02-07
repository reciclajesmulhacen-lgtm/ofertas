# validar.py
import importlib

# Archivos de materias
archivos = ["mates", "lengua", "ingles", "frances", "ciencias"]

for mat in archivos:
    try:
        mod = importlib.import_module(mat)
    except Exception as e:
        print(f"❌ No se pudo cargar {mat}.py: {e}")
        continue

    if not hasattr(mod, "TEMARIO"):
        print(f"❌ {mat}.py no contiene la variable TEMARIO")
        continue

    total_preguntas = 0
    errores = []
    temario = mod.TEMARIO

    for uni_idx, unidad in enumerate(temario):
        exámenes = unidad.get("examenes", [])
        for ex_idx, examen in enumerate(exámenes):
            preguntas = examen.get("preguntas", [])
            for preg_idx, preg in enumerate(preguntas):
                total_preguntas += 1
                keys_faltantes = [k for k in ("p","o","r") if k not in preg]
                if keys_faltantes:
                    errores.append(f"❌ {mat} - Unidad {uni_idx+1} Examen {ex_idx+1} Pregunta {preg_idx+1}: faltan claves {keys_faltantes}")
                    continue
                if preg['r'] not in preg['o']:
                    errores.append(f"❌ {mat} - Unidad {uni_idx+1} Examen {ex_idx+1} Pregunta {preg_idx+1}: respuesta '{preg['r']}' no está en opciones {preg['o']}")

    if errores:
        for err in errores: print(err)
    else:
        print(f"✅ {mat}: {total_preguntas} preguntas verificadas correctamente")
