"""
Modifica la función anterior permitiendo que las listas sean desiguales. Los
elementos sobrantes de la lista más larga se añadirán al final de la lista
resultante. 
"""
l1 = [1,2,3,4]
l2 = [1,2,3,4,5,6]

def suma(l1, l2):
    l3 = []

    lista_mas_corta = l1 if len(l2) > len(l1) else l2
    lista_mas_larga = l1 if len(l1) > len(l2) else l2

    for i in range(len(lista_mas_corta)):
        l3.append(l1[i] + l2[i])
    
    for i in range(len(l3), len(lista_mas_larga)):
        l3.append(lista_mas_larga[i])
    
    return l3
    
print(suma(l1, l2))
