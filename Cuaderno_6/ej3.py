"""
Muy similar al anterior: Programar ahora un algoritmo recursivo que permita
hacer una división entera mediante restas sucesivas.
"""

def cumdiv(dividendo, divisor):
    resultado = None
    if dividendo < divisor:
        resultado = 0
    else:
        resultado =  1 + cumdiv(dividendo-divisor, divisor)
    return resultado
print(cumdiv(10,2))