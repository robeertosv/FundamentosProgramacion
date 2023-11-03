"""
Python permite dar valores por defecto en la definición de un subprograma.
Documéntate y estudia cómo se hace esto. Para ello, ten en cuenta que la
presión es mucho más estable que la temperatura. Nota: Este ejercicio
pretende mostrarte que con la implementación de valores por defecto ya no
te harían falta los dos ejercicios anteriores. 

"""

def calculaAB(a=0,b=0):
    return a+b

print(calculaAB()) # 0 + 0 = 0
print(calculaAB(1)) # 1 + 0 = 0
print(calculaAB(1,4)) # 1 + 4 = 5