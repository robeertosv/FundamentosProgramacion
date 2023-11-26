"""
Programar una función que dada una palabra, retorne la misma invertida
utilizando para ello recursividad. 
"""

def palindromo(palabra):
    contador = 0
    contador += len(palabra)
    lista = []
    if(contador == 0):
        return palabra
    else:
        lista.append(palabra[-1])
        palabra = palabra[-1:]
        palabra = palindromo(palabra)
    
    return lista

palindromo("roberto")