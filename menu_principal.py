import tkinter as tk
from tkinter import messagebox
import os
import json
from datetime import datetime

# Variables globales
ventana_menu = None

# === FUNCIONES DE PROGRESO ===
def guardar_progreso(materia, unidad, puntuacion, examenes_completados):
    """Guarda progreso del usuario"""
    progreso = {
        "materia": materia,
        "unidad": unidad,
        "puntuacion": puntuacion,
        "examenes_completados": examenes_completados,
        "fecha": datetime.now().strftime("%d/%m/%Y %H:%M"),
        "total_preguntas": 0
    }
    
    with open("progreso.json", "w", encoding="utf-8") as f:
        json.dump(progreso, f, ensure_ascii=False, indent=2)
    print(f"💾 Progreso guardado: {materia} U{unidad}")

def cargar_progreso():
    """Carga progreso anterior"""
    if os.path.exists("progreso.json"):
        try:
            with open("progreso.json", "r", encoding="utf-8") as f:
                return json.load(f)
        except:
            return None
    return None

# === FUNCIONES DE NAVEGACIÓN ===
def abrir_materia(materia):
    """Abre archivo de materia específica"""
    try:
        if materia == "mates":
            import mates
            ventana_menu.destroy()
            mates.main()
        elif materia == "lengua":
            import lengua
            ventana_menu.destroy()
            lengua.main()
        elif materia == "ciencias":
            import ciencias
            ventana_menu.destroy()
            ciencias.main()
        elif materia == "ingles":
            import ingles
            ventana_menu.destroy()
            ingles.main()
        elif materia == "frances":
            import frances
            ventana_menu.destroy()
            frances.main()
    except ImportError:
        messagebox.showerror("Error", f"❌ No se encuentra {materia}.py")

def continuar_progreso(progreso):
    """Continúa desde donde lo dejó"""
    materia = progreso['materia']
    abrir_materia(materia)

def salir_app():
    """Cierra aplicación"""
    if messagebox.askyesno("Salir", "¿Seguro que quieres salir?"):
        ventana_menu.destroy()

# === VENTANA PRINCIPAL ===
def main():
    global ventana_menu
    
    # Crear ventana principal
    ventana_menu = tk.Tk()
    ventana_menu.title("🎓 APP EXÁMENES 5º PRIMARIA")
    ventana_menu.geometry("550x700")
    ventana_menu.resizable(False, False)
    ventana_menu.configure(bg="#f0f8ff")
    
    # Icono y centro pantalla
    ventana_menu.iconify()
    ventana_menu.update()
    ventana_menu.deiconify()
    
    # === TÍTULO PRINCIPAL ===
    titulo = tk.Label(
        ventana_menu,
        text="🎓 EXAMENES 5º PRIMARIA",
        font=("Arial", 24, "bold"),
        bg="#f0f8ff",
        fg="#2c3e50"
    )
    titulo.pack(pady=30)
    
    # === MOSTRAR PROGRESO ===
    progreso = cargar_progreso()
    if progreso:
        frame_progreso = tk.Frame(ventana_menu, bg="#d4edda", relief="ridge", bd=2)
        frame_progreso.pack(pady=15, padx=20, fill="x")
        
        tk.Label(
            frame_progreso,
            text=f"📊 PROGRESO GUARDADO",
            font=("Arial", 12, "bold"),
            bg="#d4edda",
            fg="#155724"
        ).pack(pady=5)
        
        tk.Label(
            frame_progreso,
            text=f"📚 {progreso['materia'].upper()}: U{progreso['unidad']} | {progreso['puntuacion']} pts",
            font=("Arial", 11),
            bg="#d4edda",
            fg="#155724"
        ).pack()
        
        tk.Label(
            frame_progreso,
            text=f"📅 {progreso['fecha']}",
            font=("Arial", 9),
            bg="#d4edda",
            fg="#6c757d"
        ).pack(pady=(0,10))
        
        # Botón CONTINUAR
        btn_continuar = tk.Button(
            frame_progreso,
            text="➤ CONTINUAR AQUÍ",
            command=lambda: continuar_progreso(progreso),
            bg="#28a745",
            fg="white",
            font=("Arial", 12, "bold"),
            relief="raised",
            bd=3,
            padx=20,
            pady=5,
            cursor="hand2"
        )
        btn_continuar.pack(pady=10)
    
    # === SEPARADOR ===
    separador = tk.Frame(ventana_menu, height=2, bg="#bdc3c7")
    separador.pack(fill="x", padx=20, pady=20)
    
    # === BOTONES DE MATERIAS ===
    frame_botones = tk.Frame(ventana_menu, bg="#f0f8ff")
    frame_botones.pack(pady=20)
    
    # MATES
    btn_mates = tk.Button(
        frame_botones,
        text="🔢 MATEMÁTICAS\n(Mochila Ligera 5)",
        command=lambda: abrir_materia("mates"),
        bg="#3498db",
        fg="white",
        font=("Arial", 14, "bold"),
        relief="raised",
        bd=4,
        padx=30,
        pady=15,
        cursor="hand2"
    )
    btn_mates.pack(pady=10, padx=50, fill="x")
    
    # LENGUA
    btn_lengua = tk.Button(
        frame_botones,
        text="📖 LENGUA\n(Santillana 5)",
        command=lambda: abrir_materia("lengua"),
        bg="#e74c3c",
        fg="white",
        font=("Arial", 14, "bold"),
        relief="raised",
        bd=4,
        padx=30,
        pady=15,
        cursor="hand2"
    )
    btn_lengua.pack(pady=10, padx=50, fill="x")
    
    # CIENCIAS
    btn_ciencias = tk.Button(
        frame_botones,
        text="🧪 CIENCIAS\n(Santillana 5)",
        command=lambda: abrir_materia("ciencias"),
        bg="#f39c12",
        fg="white",
        font=("Arial", 14, "bold"),
        relief="raised",
        bd=4,
        padx=30,
        pady=15,
        cursor="hand2"
    )
    btn_ciencias.pack(pady=10, padx=50, fill="x")
    
    # INGLÉS
    btn_ingles = tk.Button(
        frame_botones,
        text="🇬🇧 INGLÉS\n(Macmillan Steps 5)",
        command=lambda: abrir_materia("ingles"),
        bg="#9b59b6",
        fg="white",
        font=("Arial", 14, "bold"),
        relief="raised",
        bd=4,
        padx=30,
        pady=15,
        cursor="hand2"
    )
    btn_ingles.pack(pady=10, padx=50, fill="x")
    
    # FRANCÉS
    btn_frances = tk.Button(
        frame_botones,
        text="🇫🇷 FRANCÉS\n(Clic Clac 1)",
        command=lambda: abrir_materia("frances"),
        bg="#1abc9c",
        fg="white",
        font=("Arial", 14, "bold"),
        relief="raised",
        bd=4,
        padx=30,
        pady=15,
        cursor="hand2"
    )
    btn_frances.pack(pady=10, padx=50, fill="x")
    
    # === BOTONES INFERIORES ===
    frame_inferior = tk.Frame(ventana_menu, bg="#f0f8ff")
    frame_inferior.pack(side="bottom", pady=30)
    
    # Botón REINICIAR PROGRESO
    btn_reiniciar = tk.Button(
        frame_inferior,
        text="🔄 REINICIAR PROGRESO",
        command=lambda: reiniciar_progreso(),
        bg="#95a5a6",
        fg="white",
        font=("Arial", 10, "bold"),
        relief="raised",
        bd=3
    )
    btn_reiniciar.pack(side="left", padx=10)
    
    # Botón SALIR
    btn_salir = tk.Button(
        frame_inferior,
        text="❌ SALIR",
        command=salir_app,
        bg="#e74c3c",
        fg="white",
        font=("Arial", 10, "bold"),
        relief="raised",
        bd=3
    )
    btn_salir.pack(side="right", padx=10)
    
    ventana_menu.mainloop()

def reiniciar_progreso():
    """Borra archivo de progreso"""
    if os.path.exists("progreso.json"):
        if messagebox.askyesno("Confirmar", "¿Borrar TODO el progreso?"):
            os.remove("progreso.json")
            messagebox.showinfo("Listo", "✅ Progreso reiniciado")
            main()  # Recarga menú
    else:
        messagebox.showinfo("Info", "No hay progreso guardado")

# INICIAR APP
if __name__ == "__main__":
    main()
