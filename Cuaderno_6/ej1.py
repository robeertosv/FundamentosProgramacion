"""Programar un procedimiento recursivo que compruebe si un cierto número se
encuentra o no en una lista."""

lista = [1,2,3,4,5,6]    
def checker(lista, n, pos):
    if len(lista)-1 > pos:
        if lista[pos] == n:
            return True
        else:
            return checker(lista, n, pos+1)
   
print(checker(lista, 41, 0))