import tkinter as tk

class SimilarAjustes:
    def __init__(self, master):
        self.master = master
        self.ajustes_window = None  # Variable para almacenar la ventana emergente

    def toggle_modo_oscuro(self):
        if self.master.cget("bg") == "white":
            self.master.configure(bg="black")
            self.label_song.config(bg="black", fg="white")
            self.label_song1.config(bg="black", fg="white")
            self.label_time.config(bg="white", fg="black")
            self.label_duration.config(bg="white", fg="black")
            self.canvas.config(bg="black")
        else:
            self.master.configure(bg="white")
            self.label_song.config(bg="white", fg="black")
            self.label_song1.config(bg="white", fg="black")
            self.label_time.config(bg="lightblue", fg="black")
            self.label_duration.config(bg="lightblue", fg="black")
            self.canvas.config(bg="white")

    def toggle_modo_agua(self):
        if self.master.cget("bg") == "white":
            self.master.configure(bg="lightblue")
            self.label_song.config(bg="lightblue", fg="black")
            self.label_song1.config(bg="lightblue", fg="black")
            self.label_time.config(bg="lightblue", fg="black")
            self.label_duration.config(bg="lightblue", fg="black")
            self.canvas.config(bg="white")
        else:
            self.master.configure(bg="white")
            self.label_song.config(bg="white", fg="black")
            self.label_song1.config(bg="white", fg="black")
            self.label_time.config(bg="lightblue", fg="black")
            self.label_duration.config(bg="lightblue", fg="black")
            self.canvas.config(bg="white")

    def botones(self):
        self.ajustes_window = tk.Toplevel(self.master)  # Crear la ventana emergente
        self.ajustes_window.title("Ajustes")

        # Crear los botones para seleccionar el modo
        btn_oscuro = tk.Button(self.ajustes_window, text="Modo Oscuro", command=self.toggle_modo_oscuro)
        btn_agua = tk.Button(self.ajustes_window, text="Modo Agua", command=self.toggle_modo_agua)
        btn_oscuro.pack()
        btn_agua.pack()


        

    

   