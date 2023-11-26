"""
Realizar un programa que lea desde teclado un número entero positivo y lo
convierta a binario utilizando recursividad.
"""

def decToBin(n):
    num = ''
    if(n == 0 or n == 1):
        num += str(n)
    else:
        num += ( decToBin(n//2) + str(n%2))
    
    return num

print(decToBin(10))