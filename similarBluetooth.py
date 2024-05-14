import os

class BluetoothManager:
    def abrir_panel_bluetooth(self):
        os.system("bthprops.cpl")

    def conectar_dispositivo(self, direccion_mac):
        # No se puede conectar directamente desde Python en Windows
        print("No se puede conectar directamente a dispositivos Bluetooth en Windows desde Python.")