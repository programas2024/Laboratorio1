import tkinter as tk
from Similartooltip import SimilarTooltip
class similarayuida:
    def __init__(self, master):
        self.master = master
        self.ventana_emergente = tk.Toplevel(master)
        self.ventana_emergente.title("Ayuda")
        self.ventana_emergente.geometry("1200x700")
        self.ventana_emergente.resizable(False, False)

        self.lienzo = tk.Canvas(self.ventana_emergente, bg="white", width=1200, height=700)
        self.lienzo.pack()

        # Cargar la imagen
        self.imagen = tk.PhotoImage(file="imagenes/ayuda.png")
        self.imagen1 = tk.PhotoImage(file="imagenes/cheque.png")


        # Dibujar la imagen en el lienzo
        self.lienzo.create_image(0, 0, anchor=tk.NW, image=self.imagen)

        self.btn_aceptar = tk.Button(self.ventana_emergente, text="Aceptar",compound="left",image=self.imagen1,border=0,background="white", command=self.cerrar_ventana)
        self.btn_aceptar.place(relx=0.5, rely=0.9, anchor="center")

        SimilarTooltip(self.btn_aceptar,"Aceptar la ayuda")

    def cerrar_ventana(self):
        self.ventana_emergente.destroy()

