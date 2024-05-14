from tkinter import ttk
import tkinter as tk
import os

class SimilarBusqueda:
    def __init__(self, master, filtered_songs, play_selected_song_callback):
        try:
            self.master = master
            self.filtered_songs = filtered_songs
            self.play_selected_song_callback = play_selected_song_callback

            # Crear la ventana de búsqueda
            self.search_window = tk.Toplevel(master)
            self.search_window.title("Lista de Canciones Filtrada")

            self.list_canvas = tk.Canvas(self.search_window)
            self.list_canvas.pack(side=tk.LEFT, fill=tk.BOTH, expand=True)

            self.scrollbar = ttk.Scrollbar(self.search_window, orient=tk.VERTICAL, command=self.list_canvas.yview)
            self.scrollbar.pack(side=tk.RIGHT, fill=tk.Y)

            self.list_frame = tk.Frame(self.list_canvas)
            self.list_canvas.create_window((0, 0), window=self.list_frame, anchor=tk.NW)

            # Mostrar la lista de canciones filtradas
            self.show_filtered_song_list()

        except Exception as e:
            print("Error:", e)

    def show_filtered_song_list(self):
        try:
            for song in self.filtered_songs:
                song_name = os.path.basename(song)
                btn = tk.Button(self.list_frame, text=song_name, command=lambda s=song: self.play_selected_song_callback(s))
                btn.pack(fill=tk.X)  # Llenar horizontalmente
                # Agregar una casilla para agregar la canción como favorita
                tk.Checkbutton(self.list_frame, text="Agregar favorito").pack()

            self.list_frame.bind("<Configure>", lambda event, canvas=self.list_canvas: self.on_frame_configure(canvas))
            self.list_canvas.configure(yscrollcommand=self.scrollbar.set)

        except Exception as e:
            print("Error:", e)
