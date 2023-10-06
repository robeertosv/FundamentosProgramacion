"""
Programa una función que permita determinar si un determinado carácter es una
vocal o no, utilizando la construcción if-elif. Repite el ejercicio utilizando esta
vez el operador booleano or y observa las diferencias.
"""

def is_vocal(x:str)->bool:
    return True if x == 'a' or x == 'e' or x == 'i' or x == 'o' or x == 'u' else False

x = input('Introduce un carácter: ')
print(is_vocal(x))