"""
Implementar un programa que dados dos números, calcule el producto de
forma recursiva. Los números a multiplicar deben ser leídos por teclado.
NOTA: no puede utilizar el operador de multiplicación así que utilice sumas.
"""

def cumprod(a,b):
    
    if b == 0:
        return 0
    else:
        return a + cumprod(a, b-1)
    
print(cumprod(3,2))