"""
Programar, haciendo uso de la recursividad, una función en Python que
permita obtener el término de orden n de la sucesión de Fibonacci
"""

def fibonacci(n):
    sol = 0
    if n == 0 or n == 1:
        sol = n
    else:
        sol = fibonacci(n-1)+fibonacci(n-2)
        
    return sol

print(fibonacci(8))