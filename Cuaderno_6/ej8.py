"""
Calcular la suma de los números pares entre 0 y n de manera recursiva.
"""

def sumEven(n):
    if(n == 0):
        return 0
    else:
        if(n%2 == 0):
            return n + sumEven(n-1)
        else:
            return sumEven(n-1)
        
print(sumEven(10))