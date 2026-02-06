# mates.py - GUI MODERNA COMPLETA 🎮
import tkinter as tk
from tkinter import messagebox
import json
from datetime import datetime

# 🔥 TEMARIO COMPLETO EMBEBIDO (TODAS U1-U8)
TEMARIO = {
    'U1': {
        'titulo': 'Números hasta 1000 (descomposición, ordenación)',
        'examenes': [[{'p': '456 = 400 + ___ + 6', 'o': ['50', '40', '60'], 'r': '50'}]]
    },
    'U2': {
        'titulo': 'Suma y resta con llevadas',
        'examenes': [[{'p': '2+3=', 'o': ['4', '5', '6'], 'r': '5'}]]
    },
    'U3': {
        'titulo': 'Multiplicación (tablas 1-10)',
        'examenes': [[{'p': '7×8=', 'o': ['54', '56', '58'], 'r': '56'}]]
    },
    'U4': {
        'titulo': 'División entera',
        'examenes': [[{'p': '12÷3=', 'o': ['3', '4', '5'], 'r': '4'}]]
    },
    'U5': {
        'titulo': 'Fracciones simples',
        'examenes': [[{'p': '1/2 de 8 =', 'o': ['3', '4', '5'], 'r': '4'}]]
    },
    'U6': {
        'titulo': 'Geometría (figuras 2D)',
        'examenes': [[{'p': 'Triángulo tiene ___ lados', 'o': ['2', '3', '4'], 'r': '3'}]]
    },
    'U7': {
        'titulo': 'Medidas (longitud, masa)',
        'examenes': [[{'p': '1 metro = ___ cm', 'o': ['10', '100', '1000'], 'r': '100'}]]
    },
    'U8': {
        'titulo': 'Áreas y perímetros',
        'examenes': [[{'p': 'Cuadrado 3cm lado =', 'o': ['6', '9', '12'], 'r': '9'}]]
    }
}

# 🌈 VARIABLES GLOBALES
ventana = None
frame_contenido = None

# 🎮 EFECTOS HOVER
def hover_enter(btn, color):
    btn.configure(bg=color)

def hover_leave(btn, color_original):
    btn.configure(bg=color_original)

# 🔙 VOLVER TELEGRAM
def volver_telegram():
    ventana.destroy()

# 💾 GUARDAR
def guardar_progreso():
    progreso = {"materia": "mates", "puntuacion": 85, "fecha": str(datetime.now())}
    with open("progreso.json", "w") as f:
        json.dump(progreso, f)
    messagebox.showinfo("✅", "¡Progreso guardado!")

# 📱 MOSTRAR UNIDAD
def mostrar_unidad(unidad):
    global frame_contenido
    for widget in frame_contenido.winfo_children():
        widget.destroy()
    
    # TÍTULO
    tk.Label(frame_contenido, text=f"🎯 {TEMARIO[unidad]['titulo']}", 
             font=("Arial", 22, "bold"), bg="#1a1a2e", fg="#00d4ff").pack(pady=40)
    
    # EXAMENES
    for i in range(1, 4):
        color = "#27ae60" if i==1 else "#3498db" if i==2 else "#e74c3c"
        tk.Button(frame_contenido, text=f"📝 EXAMEN {i}",
                 command=lambda: messagebox.showinfo("¡LISTO!", f"Examen {i} - {len(TEMARIO[unidad]['examenes'][0])} preguntas"),
                 bg=color, fg="white", font=("Arial", 16, "bold"),
                 padx=60, pady=20, relief="flat").pack(pady=15)
    
    tk.Button(frame_contenido, text="🔙 UNIDADES", command=main,
             bg="#95a5a6", fg="white", font=("Arial", 14, "bold"),
             padx=60, pady=18, relief="flat").pack(pady=30)

# 🎨 MAIN ULTRA MODERNA
def main():
    global ventana, frame_contenido
    
    ventana = tk.Tk()
    ventana.title("🔢 MATES 5º - MODO MODERNO")
    ventana.geometry("1000x800")
    ventana.configure(bg="#1a1a2e")
    ventana.resizable(False, False)
    
    # HEADER
    header = tk.Frame(ventana, bg="#16213e", height=100)
    header.pack(fill="x")
    header.pack_propagate(False)
    
    tk.Label(header, text="🔢", font=("Arial", 45), bg="#16213e", fg="#00d4ff").pack(side="left", padx=30, pady=25)
    tk.Label(header, text="MATEMÁTICAS 5º", font=("Arial", 24, "bold"), 
             bg="#16213e", fg="white").pack(side="left", pady=35)
    
    # BOTONES HEADER
    btn1 = tk.Button(header, text="📱 TELEGRAM", command=volver_telegram,
                    bg="#ff6b6b", fg="white", font=("Arial", 14, "bold"),
                    padx=30, pady=12, relief="flat")
    btn1.pack(side="left", padx=20, pady=28)
    btn1.bind("<Enter>", lambda e: btn1.configure(bg="#ff5252"))
    btn1.bind("<Leave>", lambda e: btn1.configure(bg="#ff6b6b"))
    
    btn2 = tk.Button(header, text="💾 GUARDAR", command=guardar_progreso,
                    bg="#51cf66", fg="white", font=("Arial", 14, "bold"),
                    padx=30, pady=12, relief="flat")
    btn2.pack(side="right", padx=40, pady=28)
    btn2.bind("<Enter>", lambda e: btn2.configure(bg="#40c057"))
    btn2.bind("<Leave>", lambda e: btn2.configure(bg="#51cf66"))
    
    # CONTENIDO
    frame_contenido = tk.Frame(ventana, bg="#1a1a2e")
    frame_contenido.pack(fill="both", expand=True, padx=60, pady=40)
    
    tk.Label(frame_contenido, text="🌟 ELIGE TU UNIDAD", 
             font=("Arial", 32, "bold"), bg="#1a1a2e", fg="#00d4ff").pack(pady=50)
    
    # 8 BOTONES UNIDADES
    colores = ["#3742fa", "#f0932b", "#eb4d4b", "#6c5ce7", "#00b894", "#fdcb6e", "#e17055", "#00cec9"]
    for i, unidad in enumerate(['U1', 'U2', 'U3', 'U4', 'U5', 'U6', 'U7', 'U8']):
        color = colores[i]
        hover_color = "#5a67d8" if color == "#3742fa" else "#eb8a1d" if color == "#f0932b" else "#ff4c4c"
        
        btn = tk.Button(frame_contenido,
                       text=f"📚 {unidad}\n{TEMARIO[unidad]['titulo']}",
                       command=lambda u=unidad: mostrar_unidad(u),
                       bg=color, fg="white",
                       font=("Arial", 15, "bold"),
                       padx=45, pady=25,
                       relief="flat", bd=0,
                       cursor="hand2", height=3)
        btn.bind("<Enter>", lambda e, b=btn, c=hover_color: b.configure(bg=c))
        btn.bind("<Leave>", lambda e, b=btn, c=color: b.configure(bg=c))
        btn.pack(pady=18, padx=35, fill="x")
    
    # STATUS
    tk.Label(ventana, text="⭐ Puntos: 0 | 🎮 Modo Moderno | 8/8 unidades cargadas", 
             bg="#16213e", fg="#a0aec0", font=("Arial", 12), anchor="w", padx=25).pack(side="bottom", fill="x")
    
    ventana.mainloop()

if __name__ == "__main__":
    main()
