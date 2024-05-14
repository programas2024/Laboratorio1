import tkinter as tk
import psutil

class Bateria:
    def __init__(self, ventana):
        self.ventana = ventana
        self.estado = ""
        self.porcentaje = 0

        # Crear las imágenes para diferentes estados de la batería
        self.imagen_llena = tk.PhotoImage(file="imagenes\\bateria-llena.png")
        self.imagen_llenamedia = tk.PhotoImage(file="imagenes\\bateria.png")
        self.imagen_estado = tk.PhotoImage(file="imagenes\\estado bateria.png")
        self.imagen_vacia = tk.PhotoImage(file="imagenes\\bateria-vacia.png")

        # Crear etiqueta para mostrar el estado de la batería
        self.label_estado_bateria = tk.Label(self.ventana, image=self.imagen_estado, background="white")
        self.label_estado_bateria.place(x=850, y=20)

        # Crear tooltip para mostrar el porcentaje de la batería (inicialmente fuera de la ventana)
        self.tooltip_bateria = tk.Label(self.ventana, text="", background="white", relief="solid", borderwidth=1)
        self.tooltip_bateria.place(x=-1000, y=-1000)

        # Actualizar el estado de la batería cada segundo
        self.actualizar_estado_bateria()

        # Vincular eventos del ratón para mostrar y ocultar el tooltip
        self.label_estado_bateria.bind("<Enter>", self.mostrar_tooltip)
        self.label_estado_bateria.bind("<Leave>", self.ocultar_tooltip)

    def obtener_estado_bateria(self):
        estado_bateria = psutil.sensors_battery()
        if estado_bateria:
            self.estado = "Cargando" if estado_bateria.power_plugged else ""
            self.porcentaje = estado_bateria.percent
        else:
            self.estado = "Desconocido"
            self.porcentaje = -1

    def actualizar_estado_bateria(self):
        # Actualizar el estado de la batería
        self.obtener_estado_bateria()

        # Actualizar la imagen de la etiqueta según el porcentaje de la batería
        if self.porcentaje >= 90:
            self.label_estado_bateria.config(image=self.imagen_llena)
        elif 70 <= self.porcentaje < 90:
            self.label_estado_bateria.config(image=self.imagen_llenamedia)
        elif 50 <= self.porcentaje < 70:
            self.label_estado_bateria.config(image=self.imagen_estado)
        elif 0 <= self.porcentaje < 50:
            self.label_estado_bateria.config(image=self.imagen_vacia)

        # Actualizar el texto del tooltip
        self.tooltip_bateria.config(text=f" batería: {self.porcentaje}%")

        # Programar la próxima actualización después de 1 segundo
        self.ventana.after(1000, self.actualizar_estado_bateria)

    def mostrar_tooltip(self, event):
        # Mostrar el tooltip
        self.tooltip_bateria.place(x=700, y=20)

    def ocultar_tooltip(self, event):
        # Ocultar el tooltip
        self.tooltip_bateria.place(x=-1000, y=-1000)