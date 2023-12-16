"""
Programar una función que dada una palabra, retorne la misma invertida
utilizando para ello recursividad. 

"""

p = 'roberto'

def inverter(palabra):
    if len(palabra) == 1:
        return palabra[-1]
    else:
        return palabra[-1] + inverter(palabra[:-1])

print(f'{p} al revés es {inverter(p)}')