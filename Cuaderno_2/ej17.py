"""
Se dice que un gas está en condiciones ideales cuando está a 1 atmosfera de
presión y 0ºC, es decir 273, 15ºK. Escribe una función que determine si un
cierto gas se encuentra en condiciones ideales.

"""

def isIdeal(p:float, t:float)->bool:
    """
    p tiene que introducirse en atmosferas y t en ºC
    """
    return True if p==1 and t==0 else False

print(isIdeal(1,0))