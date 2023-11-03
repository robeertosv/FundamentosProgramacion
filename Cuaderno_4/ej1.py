"""
Escribir una función que sume dos listas de enteros de igual longitud y retorne
otra lista que contenga la suma de las originales elemento a elemento. 
"""
l1 = [1,2,3,4]
l2 = [1,2,3,4]

def suma(l1, l2): 
    l3 = []

    for i in range(len(l1)):
        l3.append(l1[i] + l2[i])
    return l3

print(suma(l1, l2))