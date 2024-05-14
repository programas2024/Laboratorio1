import tkinter as tk
from tkinter import messagebox, ttk

class VentanaCrearCarpeta:
    def __init__(self, master, reproductor):
        self.master = master
        self.reproductor = reproductor  # Referencia al reproductor de música
        self.master.title("Crear Carpeta")
        
        
        self.canvas = tk.Canvas(self.master, bg="white", width=400, height=320)
        self.canvas.pack()

        # Etiqueta y campo de entrada para el nombre de la carpeta
        self.label_nombre = tk.Label(self.canvas, text="Nombre de la carpeta:")
        self.label_nombre.place(x=10, y=10)
        self.entry_nombre = tk.Entry(self.canvas)
        self.entry_nombre.place(x=150, y=10, width=120)

        # Etiqueta y marco de texto para la descripción
        self.label_descripcion = tk.Label(self.canvas, text="Descripción:")
        self.label_descripcion.place(x=10, y=40)
        self.text_descripcion = tk.Text(self.canvas, width=20, height=5)
        self.text_descripcion.place(x=150, y=40)

        # Etiqueta y menú desplegable para la capacidad
        self.label_capacidad = tk.Label(self.canvas, text="Capacidad:")
        self.label_capacidad.place(x=10, y=120)
        self.combo_capacidad = ttk.Combobox(self.canvas, values=[i for i in range(51)], state="readonly")
        self.combo_capacidad.current(0)  # Valor predeterminado
        self.combo_capacidad.place(x=150, y=120, width=120)

        # Botón para crear la carpeta
        self.btn_crear = tk.Button(self.canvas, text="Crear Carpeta", command=self.crear_carpeta)
        self.btn_crear.place(x=80, y=160)

        # Botón para descartar la acción
        self.btn_descartar = tk.Button(self.canvas, text="Descartar", command=self.descartar_accion)
        self.btn_descartar.place(x=180, y=160)

    def crear_carpeta(self):
        nombre = self.entry_nombre.get()
        descripcion = self.text_descripcion.get("1.0", tk.END)
        capacidad = self.combo_capacidad.get()

        # Aquí puedes implementar la lógica para crear la carpeta con los datos proporcionados
        # Por ahora, simplemente mostraremos los datos en un mensaje de alerta
        messagebox.showinfo("Carpeta Creada", f"Nombre: {nombre}\nDescripción: {descripcion}\nCapacidad: {capacidad}")

        # Llamar a la función para actualizar la lista de carpetas en el reproductor de música
        self.reproductor.actualizar_lista_carpetas(nombre)

    def descartar_accion(self):
        self.master.destroy()