import os

debug = []
for k in sorted(os.environ.keys()):
    if "TELEGRAM" in k or "RAILWAY" in k or "TOKEN" in k:
        debug.append(f"{k}={os.environ.get(k)}")

raise RuntimeError("DEBUG ENV -> " + " | ".join(debug))
