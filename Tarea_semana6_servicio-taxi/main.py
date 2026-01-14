"""
Programa principal del sistema de taxis.
"""

from modelos.taxi import Taxi
from servicios.gestor_taxi import buscar_taxi_disponible

def main():
    print("======= SERVICIO DE TAXI LATA=======")

    # Taxis registrados en el sistema
    taxis = [
        Taxi("ABC-1223", 5, True),
        Taxi("DEF-4576", 10, False),
        Taxi("GHI-7890", 7, True)
    ]

    direccion = input("Ingrese su dirección de referencia: ")
    ubicacion_usuario = int(input("Ingrese su ubicación(en km aproximado): "))

    taxi = buscar_taxi_disponible(taxis, ubicacion_usuario)

    if taxi:
        print("\n ===Taxi Asignado===:")
        print("Placa:", taxi.placa)
        print("Estado:", taxi.obtener_estado())
        print("Distancia aproximada:", abs(taxi.ubicacion - ubicacion_usuario), "km")
    else:
        print("\n LO SENTIMOS, NO hay taxis disponibles en este momento.")

if __name__ == "__main__":
    main()
