"""
Programar un procedimiento recursivo que compruebe si un cierto número se
encuentra o no en una lista.
"""

lista = [1,2,3,4,5,6]

def checker(lista:list, num:int)->bool:
    isInList = False
    if(len(lista) != 0):
        if lista[0] == num:
            isInList = True
        else:
            isInList = False
            isInList = checker(lista[1:], num)
            
    return isInList

print(checker(lista, 15))