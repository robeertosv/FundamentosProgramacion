"""
Una aplicación leerá de teclado los valores necesarios para mostrar en
pantalla el área de un círculo, un cuadrado y un triángulo. No queremos
implementar la aplicación completa aún, sólo preparar los subprogramas de
que necesitaremos disponer para en un futuro construir la aplicación
(funciones que leen de teclado números y los validan, por una parte, y
funciones que hacen los cálculos de las distintas áreas, por otra). Nota: si lo
necesitas, utiliza como aproximación de П (pi) el valor de que proporciona la
biblioteca “math” de Python.
"""

import math

PI = math.pi

radio = float(input("Radio del círculo: "))
ht = float(input("Introduce la altura del triángulo: "))
bt = float(input("Introduce la base del triángulo: "))
l = float(input("Introduce el lado del cuadrado: "))

def areaCirulo(radius: float) -> float:
    return PI * (radius**2)


def areaTriangulo(base: float, altura: float) -> float:
    return 0.5 * base * altura


def areaCuadrado(lado: float) -> float:
    return lado**2