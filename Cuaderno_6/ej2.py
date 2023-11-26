"""
Implementar un programa que dados dos números, calcule el producto de
forma recursiva. Los números a multiplicar deben ser leídos por teclado.

NOTA: no puede utilizar el operador de multiplicación así que utilice sumas.
"""

def cumprod(num:float, times:int)->float:
    suma = 0
    
    if times != 0:
        suma += num
        suma += cumprod(num, times-1)
    
    return suma

print(cumprod(4, 3))