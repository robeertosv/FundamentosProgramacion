"""
Una lista de enteros original debe utilizarse para generar dos listas, una con los
números pares de la original ordenados ascendentemente y otra con los impares
ordenados descendentemente. La generación de las 2 listas debe hacerse a
medida que se recorre la original, es decir, se toma un número de la original, se
decide a qué lista (pares o impares) debe ir, y se inserta ordenado en la misma
de acuerdo con el criterio de la lista (ascendente o descendente). 
"""
original = [1,2,3,4,5,6,7,8,9,10]

def clasificador(lista):
    pares = []
    impares = []
    
    for i in range(len(lista)):
        if(lista[i] % 2 == 0):
            pares.append(lista[i])
        else:
            impares.append(lista[i])
    
    impares = impares[::-1]
    
    return pares, impares

print(clasificador(original))