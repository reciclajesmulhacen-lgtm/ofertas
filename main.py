import os

print("==== VARIABLES DISPONIBLES ====")
for k in sorted(os.environ.keys()):
    if "TELEGRAM" in k or "RAILWAY" in k or "TOKEN" in k:
        print(k, "=", os.environ.get(k))

print("==== FIN ====")

raise RuntimeError("PARADO A PROPÓSITO (solo para debug)")
