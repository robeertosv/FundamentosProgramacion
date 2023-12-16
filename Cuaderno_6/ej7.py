"""
Realizar un programa que lea desde teclado un número entero positivo y lo
convierta a binario utilizando recursividad.
"""

def toBin(n):
    if n == 0:
        return ''
    else:
        return toBin(n // 2) + str(n % 2)

n = 5

print(f'El número {n} en binario es {toBin(n)}')