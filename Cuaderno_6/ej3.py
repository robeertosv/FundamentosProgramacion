"""
Muy similar al anterior: Programar ahora un algoritmo recursivo que permita
hacer una división entera mediante restas sucesivas.
"""


def divider(dividendo:int, divisor:int)->int:
    
    if divisor == 0:
        print("No puedes dividir entre 0")
        
    if dividendo < divisor:
        return 0
    
    return 1 + divider(dividendo-divisor, divisor)

print(divider(30,6))