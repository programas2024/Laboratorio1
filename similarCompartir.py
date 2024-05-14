import webbrowser
import time

class Compartir:
    def __init__(self):
        self._cancion_actual = None

    def get_cancion_actual(self):
        return self._cancion_actual

    def set_cancion_actual(self, cancion):
        self._cancion_actual = cancion

    def abrir_whatsapp_web(self, mensaje):
        # Construye el mensaje que se enviará
        mensaje_whatsapp = f"Estoy escuchando '{self._cancion_actual}' en el reproductor de música. {mensaje}"

        # Crea la URL de WhatsApp Web con el mensaje predefinido
        url_whatsapp = f"https://web.whatsapp.com/send?text={mensaje_whatsapp}"

        # Abre WhatsApp Web en un navegador predeterminado
        webbrowser.open_new_tab(url_whatsapp)

    def compartir_whatsapp(self):
        if self._cancion_actual:
            # Abre WhatsApp Web
            self.abrir_whatsapp_web("Selecciona el contacto y envía este mensaje.")
            # Espera 10 segundos para que el usuario seleccione el contacto y escriba el mensaje
            time.sleep(10)
        else:
            print("No hay canción actual para compartir")
