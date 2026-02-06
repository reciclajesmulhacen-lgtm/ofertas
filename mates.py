import tkinter as tk
from tkinter import messagebox
import json

TEMARIO = {
    'U1': {'titulo': 'Números 1000', 'examenes': [[{'p':'test','o':['a','b'],'r':'a'}]]},
    'U2': {'titulo': 'Suma/resta', 'examenes': [[{'p':'test','o':['a','b'],'r':'a'}]]},
    'U3': {'titulo': 'Multiplicar', 'examenes': [[{'p':'test','o':['a','b'],'r':'a'}]]},
    'U4': {'titulo': 'División', 'examenes': [[{'p':'test','o':['a','b'],'r':'a'}]]},
    'U5': {'titulo': 'Fracciones', 'examenes': [[{'p':'test','o':['a','b'],'r':'a'}]]},
    'U6': {'titulo': 'Geometría', 'examenes': [[{'p':'test','o':['a','b'],'r':'a'}]]},
    'U7': {'titulo': 'Medidas', 'examenes': [[{'p':'test','o':['a','b'],'r':'a'}]]},
    'U8': {'titulo': 'Áreas', 'examenes': [[{'p':'test','o':['a','b'],'r':'a'}]]}
}

ventana = None
frame_contenido = None

def volver():
    messagebox.showinfo("ATRÁS", "¡BOTÓN ATRÁS FUNCIONA!")

def guardar():
    messagebox.showinfo("GUARDAR", "¡BOTÓN GUARDAR FUNCIONA!")

def main():
    global ventana, frame_contenido
    ventana = tk.Tk()
    ventana.title("🔢 MATES - DEBUG")
    ventana.geometry("900x700")
    ventana.configure(bg="lightblue")
    
    # HEADER GIGANTE ROJO
    header = tk.Frame(ventana, bg="RED", height=120)
    header.pack(fill="x")
    header.pack_propagate(False)
    
    tk.Label(header, text="🔢 MATEMÁTICAS 5º", font=("Arial", 24, "bold"), 
             bg="RED", fg="WHITE").pack(pady=20)
    
    # BOTÓN ATRÁS GIGANTE
    btn_atras = tk.Button(header, text="🔙 ←← ATRÁS ←←", font=("Arial", 20, "bold"),
                         bg="YELLOW", fg="BLACK", command=volver, height=3)
    btn_atras.pack(side="left", padx=20, pady=20)
    
    # BOTÓN GUARDAR GIGANTE  
    btn_guardar = tk.Button(header, text="💾 GUARDAR →→", font=("Arial", 20, "bold"),
                           bg="GREEN", fg="WHITE", command=guardar, height=3)
    btn_guardar.pack(side="right", padx=20, pady=20)
    
    # CONTENIDO
    frame_contenido = tk.Frame(ventana, bg="lightblue")
    frame_contenido.pack(fill="both", expand=True, padx=30, pady=20)
    
    tk.Label(frame_contenido, text="📚 UNIDADES", font=("Arial", 28, "bold"), 
             bg="lightblue", fg="darkblue").pack(pady=30)
    
    for unidad in ['U1','U2','U3','U4','U5','U6','U7','U8']:
        tk.Button(frame_contenido, text=f"U{unidad}", font=("Arial", 16, "bold"),
                 bg="orange", command=lambda u=unidad: print(f"Click {u}"),
                 height=3).pack(pady=10, fill="x")
    
    ventana.mainloop()

if __name__ == "__main__":
    main()
