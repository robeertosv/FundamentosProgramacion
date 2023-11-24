"""Programar un procedimiento recursivo que compruebe si un cierto número se
encuentra o no en una lista."""

lista = [1,2,3,4,5]

def isInList(lista:list, num:int):
    #Mirar si el primer elemento de la lista es el numero, si no, volver a ejecutar con el primer elemento de la lista
    inList = None
    if(len(lista) != 0):
        if(lista[0] == num):
            print(f"El {num} está en la lista {lista}")
            inList = True
        else:
            print(f"El {num}, no es el primer elemento de la lista: {lista}")
            inList = isInList(lista[1:], num)
    else:
        print(f"El {num} no estaba en la lista")
        inList =  False
    return inList

print(isInList(lista, 2))