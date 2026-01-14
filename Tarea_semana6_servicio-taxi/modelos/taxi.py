"""
Clase Taxi.
Hereda de Vehiculo.
"""

from modelos.vehiculo import Vehiculo

class Taxi(Vehiculo):
    def __init__(self, placa: str, ubicacion: int, disponible: bool):
        super().__init__(placa, ubicacion)
        self.__disponible = disponible  # Encapsulación

    # Getter
    def esta_disponible(self):
        return self.__disponible

    # Setter
    def cambiar_disponibilidad(self, estado: bool):
        self.__disponible = estado

    # Polimorfismo: sobrescritura
    def obtener_estado(self):
        if self.__disponible:
            return "Taxi disponible"
        else:
            return "Taxi no disponible"