"""
Clase base Vehiculo.
Representa un vehículo genérico del sistema.
"""

class Vehiculo:
    def __init__(self, placa: str, ubicacion: int):
        self.placa = placa
        self.ubicacion = ubicacion  # distancia en km

    # Método que será sobrescrito (polimorfismo)
    def obtener_estado(self):
        return "Vehículo genérico"