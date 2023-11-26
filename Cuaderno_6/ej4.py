"""
Programar, haciendo uso de la recursividad, una función en Python que
permita obtener el término de orden n de la sucesión de Fibonacci 
"""

def fibonacci(n):
    if n == 0 or n == 1:
        return 1
    return fibonacci(n-1) + fibonacci(n-2)

print(fibonacci(5))