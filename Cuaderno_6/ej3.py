"""
Muy similar al anterior: Programar ahora un algoritmo recursivo que permita
hacer una división entera mediante restas sucesivas.
"""

def divider(dividendo:int, divisor:int)->float:
    if divisor == 0:
        raise ValueError("El divisor no puede ser 0")
    if divisor > dividendo:
        return 0
    return 1 + divider(dividendo-divisor, divisor)