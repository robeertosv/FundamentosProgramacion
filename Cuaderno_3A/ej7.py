"""
Programa una función que permita determinar si un determinado carácter es una
vocal o no, utilizando la construcción if-elif. Repite el ejercicio utilizando esta
vez el operador booleano or y observa las diferencias.
"""

vocales = ['a', 'e', 'i', 'o', 'u']
is_vocal = lambda x: True if x in vocales else False

x = input('Introduce un carácter: ')
print(is_vocal(x))