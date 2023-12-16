"""
Muy similar al anterior: Programar ahora un algoritmo recursivo que permita
hacer una división entera mediante restas sucesivas.
"""

def cumdiv(a,b, i):
    
    if a == 0:
        return i
    else:
        return cumdiv(a-b, b, i+1) 

print(cumdiv(27,3, 0))