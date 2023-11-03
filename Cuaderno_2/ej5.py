"""
Escribe una función que determine si un punto de coordenadas en 2D está o
no sobre la circunferencia x2+y2=1000.

"""

import math


radio = math.sqrt(1000)  # Radio de la circunferencia centrada en (0, 0)


def distanciaAlCentro(x, y):
    # Teorema de Pitágoras para saber el modulo del vector que va de (0,0) a (x,y)
    return math.sqrt(x**2 + y**2)


def check(x, y):
    distancia = distanciaAlCentro(x, y)

    # Si el módulo del vector es mayor que el radio es porque el punto está fuera de la circunferencia
    if (distancia > radio):
        print(f"El punto ({x}, {y}) está fuera de la circunferencia")
    else:
        print(f"El punto ({x}, {y}) está dentro de la circunferencia")


x = float(input('Da un valor para x: '))
y = float(input('Da un valor para y: '))

check(x, y)
