"""

Reprograma lo hecho en el ejercicio 2 para reutilizar el validador de enteros del
ejercicio 3. Obviamente, tendrás que seguir validando que los valores de hora y
minutos se encuentran en el rango correcto.

"""
import ej3 as checker

import math

def converter(horas:str, minutos:str)->str:
        horas = int(horas)
        minutos = int(minutos)
        if(checker.validar_entero(horas) and checker.validar_entero(minutos)):
            if(horas < 24 or horas > 0 or minutos < 59 or minutos > 0):
                if(horas < 12):
                    return str(horas) + ":" + str(minutos) + "AM"
                else:
                    return str(horas-12) + ":" + str(minutos) + "PM" 
        return "Error"

horas = input("Horas: ")
minutos = input("Minutos: ")

print(converter(horas, minutos))