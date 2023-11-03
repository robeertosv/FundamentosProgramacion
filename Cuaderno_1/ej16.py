"""
16. Haz un programa que pida al usuario dos textos (cadenas de caracteres) y
los muestre en pantalla en orden alfabético. Pruébalo también introduciendo
cadenas de caracteres que sean numéricas, por ejemplo 99 y 102 y razona
sobre la salida producida.

"""
str1 = input("Dime una palabra: ")
str2 = input("Dime otra palabra: ")

palabras = []
palabras.append(str1)
palabras.append(str2)

palabras.sort()
print(f"Las palabras en orden alfabético quedan así: {palabras}")


int1 = input('Dime un número: ')
int2 = input('Dime otro número: ')

numeros = []
numeros.append(int1)
numeros.append(int2)
numeros.sort()

print(f"Los numeros en orden alfabético quedan así: {numeros}")

"""
    Si es capaz de ordenar palabras, en cambio los numeros no los ordena, ya que no se puede ordenar un numero alfabeticamente
"""