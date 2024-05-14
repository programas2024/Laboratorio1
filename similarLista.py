from tkinter import ttk
import tkinter as tk
import os

class SimilarLista:
    def __init__(self, master, song_list, play_selected_song_callback):
        self.master = master
        self.song_list = song_list
        self.play_selected_song_callback = play_selected_song_callback

        # Crear la ventana de la lista de canciones
        self.list_window = tk.Toplevel(master)
        self.list_window.title("Lista de Canciones")
        self.list_window.geometry("500x300")  # Establecer tamaño específico
        self.list_window.minsize(300, 200)  # Establecer tamaño mínimo
        

        self.list_canvas = tk.Canvas(self.list_window)
        self.list_canvas.pack(side=tk.LEFT, fill=tk.BOTH, expand=True)

        self.scrollbar = ttk.Scrollbar(self.list_window, orient=tk.VERTICAL, command=self.list_canvas.yview)
        self.scrollbar.pack(side=tk.RIGHT, fill=tk.Y)

        self.list_frame = tk.Frame(self.list_canvas)
        self.list_canvas.create_window((0, 0), window=self.list_frame, anchor=tk.NW)

        # Obtener la longitud máxima de las canciones para ajustar el ancho de los botones
        self.max_song_length = max(len(os.path.basename(song)) for song in self.song_list)

        # Mostrar la lista de canciones
        self.show_song_list()

    def show_song_list(self):
        for song in self.song_list:
            song_name = os.path.basename(song)
            btn = tk.Button(self.list_frame, text=song_name, command=lambda s=song: self.play_selected_song_callback(s))
            btn.pack(fill=tk.X)  # Llenar horizontalmente
            # Ajustar el ancho de los botones para que coincidan con la longitud máxima de la canción
            btn.config(width=self.max_song_length)
            # Agregar una casilla para agregar la canción como favorita
            tk.Checkbutton(self.list_frame, text="Agregar favorito").pack()