import tkinter as tk

class SimilarAtajos:
    def __init__(self, master):
        self.master = master

    def mostrar_atajos(self):
        # Crear una ventana emergente para mostrar los atajos
        self.atajos_window = tk.Toplevel(self.master)
        self.atajos_window.title("Atajos de Teclado")
        self.atajos_window.resizable(False, False)

        # Crear un marco para contener los atajos
        atajos_frame = tk.Frame(self.atajos_window)
        atajos_frame.pack(padx=10, pady=10)

        # Lista de atajos con su descripción
        atajos = [
            ("Ctrl + Z", "Cargar música"),
            ("Ctrl + Y", "Mostrar ajustes"),
            ("Ctrl + F", "Reproducir/Pausar"),
            ("Ctrl + H", "Siguiente canción"),
            ("Ctrl + X", "Canción anterior"),
            ("Ctrl + spc", "Mostrar ayuda")
        ]

        # Mostrar los atajos en la ventana emergente
        for idx, (atajo, descripcion) in enumerate(atajos):
            tk.Label(atajos_frame, text=atajo, font=("Arial", 10, "bold")).grid(row=idx, column=0, sticky="w")
            tk.Label(atajos_frame, text=descripcion, font=("Arial", 10)).grid(row=idx, column=1, sticky="w")

        # Botón para cerrar la ventana emergente
        btn_cerrar = tk.Button(self.atajos_window, text="Cerrar", command=self.atajos_window.destroy)
        btn_cerrar.pack(pady=10)
