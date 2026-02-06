# mates.py - Compatible con bot.py TELEGRAM
import tkinter as tk
from tkinter import messagebox
import json
import os
from datetime import datetime

# ================================
# TEMARIO (TU CÓDIGO ORIGINAL)
# ================================
TEMARIO = {
    'U1': {
        'titulo': 'Números hasta 1000 (descomposición, ordenación)',
        'examenes': [
            [
                {'p': 'Complete: 456 = 400 + ___ + 6', 'o': ['50', '40', '60'], 'r': '50'},
                {'p': '¿Cuál es mayor? 789 ___ 798', 'o': ['<', '>', '='], 'r': '<'},
                {'p': 'Ordena: 123, 132, ___', 'o': ['121', '122', '124'], 'r': '122'},
                {'p': 'Número anterior a 500:', 'o': ['499', '501', '490'], 'r': '499'},
                {'p': 'Número siguiente a 299:', 'o': ['300', '298', '299'], 'r': '300'},
                {'p': '345 en descomposición:', 'o': ['300+40+5', '300+45', '345'], 'r': '300+40+5'},
                {'p': '¿Cuál es par? ___', 'o': ['123', '124', '125'], 'r': '124'},
                {'p': 'Número redondo anterior a 678:', 'o': ['600', '700', '500'], 'r': '600'},
                {'p': 'Ordena de menor a mayor: 456, ___, 465', 'o': ['457', '455', '466'], 'r': '457'},
                {'p': 'Número primo: ___', 'o': ['17', '18', '20'], 'r': '17'}
            ],
            # ... resto de tus exámenes U1 (mantén igual) ...
            # Copia TODOS tus exámenes aquí igual que antes
            [{'p': 'Test pregunta', 'o': ['a', 'b', 'c'], 'r': 'a'}]
        ]
    },
    # ... resto de tus unidades U2-U8 (COPIA IGUAL que tienes) ...
    'U8': {
        'titulo': 'Áreas y perímetros',
        'examenes': [[{'p': 'Test', 'o': ['a', 'b', 'c'], 'r': 'a'}]]
    }
}

# ================================
# VARIABLES GLOBALES
# ================================
ventana = None
frame_contenido = None
materia_actual = "mates"
unidad_actual = "U1"
puntuacion_total = 0
examenes_completados = []

# ================================
# FUNCIONES NAVEGACIÓN Y PROGRESO
# ================================
def volver_menu_principal():
    """🔙 Vuelve a bot.py (menú Telegram)"""
    ventana.destroy()
    print("👋 Volviendo a menú principal...")

def guardar_progreso():
    """💾 Guarda progreso para Telegram"""
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
    messagebox.showinfo("✅ GUARDADO", f"Progreso guardado:\n📚 {materia_actual}\n🎯 U{unidad_actual}\n⭐ {puntuacion_total} pts")

def mostrar_unidad(unidad):
    """Muestra exámenes de unidad específica"""
    global unidad_actual, frame_contenido
    unidad_actual = unidad
    
    # Limpiar frame
    for widget in frame_contenido.winfo_children():
        widget.destroy()
    
    # Título unidad
    tk.Label(frame_contenido, 
             text=f"🎯 {TEMARIO[unidad]['titulo']}", 
             font=("Arial", 18, "bold"),
             bg="#f0f8ff", fg="#2c3e50").pack(pady=30)
    
    tk.Label(frame_contenido, 
             text="📝 ELIGE EXAMEN:", 
             font=("Arial", 14), 
             bg="#f0f8ff").pack(pady=(20,10))
    
    # 3 exámenes por unidad
    for i, examen in enumerate(TEMARIO[unidad]['examenes'], 1):
        tk.Button(frame_contenido,
                 text=f"📄 EXAMEN {i}",
                 command=lambda e=examen, u=unidad: iniciar_examen(e, u),
                 bg="#27ae60", fg="white",
                 font=("Arial", 14, "bold"),
                 padx=50, pady=15,
                 relief="raised", bd=4,
                 cursor="hand2").pack(pady=12)
    
    # Botón volver unidades
    tk.Button(frame_contenido,
             text="🔙 TODAS LAS UNIDADES",
             command=lambda: main(),
             bg="#95a5a6", fg="white",
             font=("Arial", 12, "bold"),
             padx=40, pady=12,
             relief="raised").pack(pady=25)

def iniciar_examen(examen, unidad):
    """Inicia examen (simulado - adaptar a tu código)"""
    messagebox.showinfo("EXAMEN", f"Iniciando examen U{unidad}\n{len(examen)} preguntas\n¡Empezar!")

# ================================
# MAIN - INTERFAZ COMPLETA
# ================================
def main():
    global ventana, frame_contenido
    
    # Configurar ventana
    ventana = tk.Tk()
    ventana.title("🔢 MATEMÁTICAS 5º PRIMARIA - Compatible con Telegram Bot")
    ventana.geometry("900x800")
    ventana.configure(bg="#f0f8ff")
    ventana.resizable(False, False)
    
    # === HEADER SUPERIOR ===
    header = tk.Frame(ventana, bg="#2c3e50", height=90)
    header.pack(fill="x")
    header.pack_propagate(False)
    
    # Título materia
    tk.Label(header, 
             text="🔢 MATEMÁTICAS 5º PRIMARIA", 
             font=("Arial", 16, "bold"), 
             bg="#2c3e50", fg="white").pack(side="left", padx=30, pady=28)
    
    # BOTÓN 🔙 VOLVER A BOT TELEGRAM
    tk.Button(header,
             text="🔙 VOLVER BOT TELEGRAM",
             command=volver_menu_principal,
             bg="#e74c3c", fg="white",
             font=("Arial", 13, "bold"),
             relief="raised", bd=4,
             padx=25, pady=10,
             cursor="hand2").pack(side="left", padx=15, pady=23)
    
    # BOTÓN 💾 GUARDAR PROGRESO
    tk.Button(header,
             text="💾 GUARDAR PROGRESO",
             command=guardar_progreso,
             bg="#28a745", fg="white",
             font=("Arial", 13, "bold"),
             relief="raised", bd=4,
             padx=25, pady=10,
             cursor="hand2").pack(side="right", padx=25, pady=23)
    
    # === CONTENIDO PRINCIPAL ===
    frame_contenido = tk.Frame(ventana, bg="#f0f8ff")
    frame_contenido.pack(fill="both", expand=True, padx=40, pady=30)
    
    # Título principal
    titulo = tk.Label(frame_contenido, 
                     text="📚 ELIGE TU UNIDAD", 
                     font=("Arial", 22, "bold"),
                     bg="#f0f8ff", fg="#2c3e50")
    titulo.pack(pady=35)
    
    # Frame unidades
    frame_unidades = tk.Frame(frame_contenido, bg="#f0f8ff")
    frame_unidades.pack(pady=25)
    
    # Botones U1-U8
    for unidad in ['U1', 'U2', 'U3', 'U4', 'U5', 'U6', 'U7', 'U8']:
        titulo_unidad = TEMARIO[unidad]['titulo'][:35] + "..." if len(TEMARIO[unidad]['titulo']) > 35 else TEMARIO[unidad]['titulo']
        btn = tk.Button(frame_unidades,
                       text=f"📖 U{unidad} - {titulo_unidad}",
                       command=lambda u=unidad: mostrar_unidad(u),
                       bg="#3498db", fg="white",
                       font=("Arial", 13, "bold"),
                       relief="raised", bd=4,
                       padx=35, pady=16,
                       cursor="hand2",
                       width=40,
                       height=2)
        btn.pack(pady=12, padx=25, fill="x")
    
    # Información inferior
    info_frame = tk.Frame(frame_contenido, bg="#f0f8ff")
    info_frame.pack(pady=30)
    
    tk.Label(info_frame,
            text="💡 Usa 'GUARDAR PROGRESO' para salvar tu avance", 
            font=("Arial", 11), bg="#f0f8ff", fg="#7f8c8d").pack()
    tk.Label(info_frame,
            text="⭐ Puntuación actual: 0 puntos", 
            font=("Arial", 11, "bold"), bg="#f0f8ff", fg="#27ae60").pack()
    
    ventana.mainloop()

if __name__ == "__main__":
    main()
