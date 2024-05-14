import tkinter as tk

class similarvolumen:
    def __init__(self, ventana, pygame_mixer):
        self.ventana = ventana
        self.pygame_mixer = pygame_mixer

        # Crear un lienzo para mostrar la imagen de sonido o sin sonido
        self.canvas = tk.Canvas(self.ventana, bg="black", width=120, height=50,border=0,background="white")
        self.canvas.place(x=600, y=555)

        # Crear una barra de desplazamiento horizontal para el volumen
        self.slider_volumen = tk.Scale(self.ventana, from_=0, to=100, orient=tk.HORIZONTAL, label="", command=self.cambiar_volumen)
        self.slider_volumen.set(50)  # Establecer el volumen inicial al 50%
       
        # Configurar el estilo del botón de volumen
        self.slider_volumen.config(bg="white", troughcolor="lightgray", highlightbackground="black", bd=2, relief=tk.RIDGE)

        # Posicionar el botón de volumen en la ventana
        self.slider_volumen.place(x=640, y=560, height=50, width=120)

        # Cargar las imágenes de sonido y sin sonido
        self.sonido_img = tk.PhotoImage(file="imagenes/sonido.png")
        self.sin_sonido_img = tk.PhotoImage(file="imagenes/sin-sonido.png")

        # Mostrar la imagen de sonido por defecto
        self.imagen_sonido = self.canvas.create_image(0, 0, anchor=tk.NW, image=self.sonido_img)

        # Vincular eventos de entrada y salida del cursor para cambiar el cursor
        self.slider_volumen.bind("<Enter>", self.cambiar_cursor)
        self.slider_volumen.bind("<Leave>", self.cambiar_cursor)

    def cambiar_volumen(self, valor):
        # Convertir el valor del control deslizante al rango 0-1 (normalizar)
        volumen_normalizado = float(valor) / 100
        # Ajustar el volumen para que sea más alto
        volumen_ajustado = volumen_normalizado * 1.5  # Multiplicar por un factor para ajustar el volumen
        # Establecer el volumen de pygame
        self.pygame_mixer.music.set_volume(volumen_ajustado)

        # Cambiar la imagen según el volumen
        if int(valor) > 0:
            self.canvas.itemconfig(self.imagen_sonido, image=self.sonido_img)
        else:
            self.canvas.itemconfig(self.imagen_sonido, image=self.sin_sonido_img)

    def cambiar_cursor(self, event):
        # Cambiar el cursor al entrar o salir del control deslizante de volumen
        if event.type == tk.EventType.Enter:
            self.ventana.config(cursor="hand2")
        elif event.type == tk.EventType.Leave:
            self.ventana.config(cursor="")
