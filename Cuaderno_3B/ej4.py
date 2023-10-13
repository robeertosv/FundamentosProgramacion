"""
Escribe un programa que lea una serie de números enteros hasta que se
introduzca el número -9999, y cuente el total de números introducidos, el total de
valores positivos y el total de valores negativos (no consideres el cero ni positivo ni
negativo). Reutiliza la función que hayas diseñado en el Ejercicio 1 para validar tus
entradas

"""
from ej1 import is_int

def clasificador()->tuple:
    num = None
    cantidad = 0
    positivos = 0
    negativos = 0  
    
    while num != -9999:
        num = input("Introduce un número: ")
        if(is_int(num)):
            num = int(num)
            cantidad += 1
            if(num > 0):
                positivos += 1
            else:
                negativos += 1
        
    return (cantidad, positivos, negativos)

print(clasificador())