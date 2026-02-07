# validar.py
import importlib
from colorama import init, Fore, Style

# Inicializa colorama
init(autoreset=True)

# Archivos de materias
archivos = ["mates", "lengua", "ingles", "frances", "ciencias"]

resumen = {}

for mat in archivos:
    try:
        mod = importlib.import_module(mat)
    except Exception as e:
        print(f"{Fore.RED}❌ No se pudo cargar {mat}.py: {e}")
        continue

    if not hasattr(mod, "TEMARIO"):
        print(f"{Fore.RED}❌ {mat}.py no contiene la variable TEMARIO")
        continue

    total_preguntas = 0
    errores = []
    temario = mod.TEMARIO

    # Recorre cada unidad como diccionario
    for uni_key, unidad_data in temario.items():
        examenes = unidad_data.get("examenes", [])
        for ex_idx, examen in enumerate(examenes):
            # examen es una lista de preguntas directamente
            for preg_idx, preg in enumerate(examen):
                total_preguntas += 1
                # Chequeo de claves
                faltantes = [k for k in ("p", "o", "r") if k not in preg]
                if faltantes:
                    errores.append(f"❌ Unidad {uni_key} Examen {ex_idx+1} Pregunta {preg_idx+1}: faltan claves {faltantes}")
                    continue
                # Validación de respuesta correcta
                if preg['r'] not in preg['o']:
                    errores.append(
                        f"❌ Unidad {uni_key} Examen {ex_idx+1} Pregunta {preg_idx+1}: respuesta '{preg['r']}' no está en opciones {preg['o']}"
                    )

    if errores:
        print(f"{Fore.YELLOW}--- Errores en {mat} ---")
        for err in errores:
            print(f"{Fore.RED}{err}")
    else:
        print(f"{Fore.GREEN}✅ {mat}: {total_preguntas} preguntas verificadas correctamente")

    resumen[mat] = {"total": total_preguntas, "errores": len(errores)}

# --- Resumen final ---
print(f"\n{Fore.CYAN}=== RESUMEN FINAL ===")
for mat, data in resumen.items():
    if data['errores'] == 0:
        print(f"{Fore.GREEN}✅ {mat}: {data['total']} preguntas correctas")
    else:
        print(f"{Fore.RED}❌ {mat}: {data['errores']} errores de {data['total']} preguntas")
