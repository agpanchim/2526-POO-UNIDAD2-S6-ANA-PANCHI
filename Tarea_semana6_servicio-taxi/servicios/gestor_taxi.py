"""
Gestión del servicio de taxis.
"""

def buscar_taxi_disponible(taxis, ubicacion_usuario):
    taxi_cercano = None
    menor_distancia = 9999

    for taxi in taxis:
        if taxi.esta_disponible():
            distancia = abs(taxi.ubicacion - ubicacion_usuario)
            if distancia < menor_distancia:
                menor_distancia = distancia
                taxi_cercano = taxi

    return taxi_cercano