# Escriba un programa debidamente modularizado y documentado que genere una secuencia de
# 100 números naturales aleatorios entre -1 y 1000 y calcule la suma de los que son múltiplos de 17. 

import random

def generator()->int:
    """Genera un integer entre el -1 y el 1000"""
    return random.randint(-1, 1000)

def isMultplipleOf17(n:int)->bool:
    """
    Función que recibe un integer como parámetro y comprueba si es múltiplo de 17. 
    Devuelve True si lo es. False si no lo es
    """
    return n % 17 == 0

def sumatory()->int:
    total = 0
    
    for i in range(100):
        num = generator()
        if(isMultplipleOf17(num)):
            total += num
    
    return total

print(sumatory())