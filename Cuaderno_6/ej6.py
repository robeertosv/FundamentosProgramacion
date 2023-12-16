"""
Realizar una función recursiva que dado un número entero, cuente su número
de dígitos. 
"""

def counter(n, l):
    n = str(n)
    
    if len(n) == 0:
        return l
    else:
        return counter(n[:-1], l+1)
    
n = 50099

print(f'la longitud del numero {n} es de {counter(n, 0)}')