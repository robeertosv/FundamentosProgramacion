"""
Programar una función que dada una palabra, retorne la misma invertida
utilizando para ello recursividad
"""

def inverter(word:str)->str:
    r = ''
    if(len(word) != 0):
        r += word[-1]
        r += inverter(word.rstrip(word[-1]))
    return r

print(inverter('roberto'))