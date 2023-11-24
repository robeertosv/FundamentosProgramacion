"""
Implementar un programa que dados dos números, calcule el producto de
forma recursiva. Los números a multiplicar deben ser leídos por teclado.
"""

def cumprod(n, times):
    prod = 0
    
    if times != 0:
        prod += n
        prod += cumprod(n, times-1)
    
    return prod

print(cumprod(2,3))