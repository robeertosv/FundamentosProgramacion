"""
Programar, haciendo uso de la recursividad, una función en Python que
permita obtener el término de orden n de la sucesión de Fibonacci

"""

def fibonacci(n):
    if n-1 == 1 or n-1 == 0:
        return 1
    else:
        return fibonacci(n-2) + fibonacci(n-1)

print(fibonacci(9))