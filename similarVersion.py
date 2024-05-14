import tkinter as tk
from Similartooltip import SimilarTooltip

class similarversion:
    def __init__(self, parent):
        self.parent = parent
        self.ventana = tk.Toplevel(parent)
        self.ventana.title("Versión")
        self.ventana.geometry("500x600")
        
        self.ventana.transient(parent)  # Establece la ventana principal como el padre
        self.ventana.grab_set()  # Bloquea el foco en esta ventana

        self.canvas = tk.Canvas(self.ventana, bg="white", width=500, height=600)
        self.canvas.pack()

        self.imagen4= tk.PhotoImage(file="imagenes/salida.png")

        version_label = tk.Label(self.canvas, text="Versión 0.0.9", font=("Arial", 14), background="white")
        version_label.place(x=240, y=20, anchor="center")

        creadores_label = tk.Label(self.canvas, text="Creadores:" ,font=("Arial", 14), background="white")
        creadores_label.place(x=240, y=50, anchor="center")

        creadores_label = tk.Label(self.canvas, text="Juan Sebastian Molina Diaz y Jhonnatan Ceron Amariles", font=("Arial", 12), background="white")
        creadores_label.place(x=240, y=90, anchor="center")

        creadores_label = tk.Label(self.canvas, text="Contactos:" ,font=("Arial", 14), background="white")
        creadores_label.place(x=240, y=130, anchor="center")

        creadores_label = tk.Label(self.canvas, text="juan.esteban.molina@correounivalle.edu.co", font=("Arial", 12), background="white")
        creadores_label.place(x=240, y=170, anchor="center")

        creadores_label = tk.Label(self.canvas, text="jhonnatan.ceron@correounivalle.edu.co", font=("Arial", 12), background="white")
        creadores_label.place(x=240, y=210, anchor="center")

        creadores_label = tk.Label(self.canvas, text="Descripcion", font=("Arial", 14), background="white")
        creadores_label.place(x=240, y=250, anchor="center")

        creadores_label = tk.Label(self.canvas, text="Esta aplicacion esta diseñada para llevar tu ritmo en tu dia", font=("Arial", 12), background="white")
        creadores_label.place(x=240, y=290, anchor="center")

        creadores_label = tk.Label(self.canvas, text="escucha lo que quieras con toda la seguridad y confianza", font=("Arial", 12), background="white")
        creadores_label.place(x=240, y=330, anchor="center")

        creadores_label = tk.Label(self.canvas, text="Cuenta  con variedad de opciones para tus gustos  ", font=("Arial", 12), background="white")
        creadores_label.place(x=240, y=370, anchor="center")

        creadores_label = tk.Label(self.canvas, text="sera tu acompañante de cada dia.   ", font=("Arial", 12), background="white")
        creadores_label.place(x=240, y=410, anchor="center")

        creadores_label = tk.Label(self.canvas, text="Proximamente   ", font=("Arial", 14), background="white")
        creadores_label.place(x=240, y=450, anchor="center")

        creadores_label = tk.Label(self.canvas, text="Mejoramiento de la barra de progreso,compartir en facebook ,instagram etc  ", font=("Arial", 10), background="white")
        creadores_label.place(x=240, y=490, anchor="center")

        cerrar_boton = tk.Button(self.canvas, text="Cerrar",image=self.imagen4,border=0,background="white", command=self.cerrar)
        cerrar_boton.place(x=240, y=550, anchor="center")
        SimilarTooltip(cerrar_boton,"Salir de version")


    def cerrar(self):
        self.ventana.destroy()



