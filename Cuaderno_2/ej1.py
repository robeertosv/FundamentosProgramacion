"""
Implementa una función "fuerza" que retorne el valor de la magnitud física
fuerza a partir de los valores de masa y aceleración recibidos como
parámetros. Construye después un programa probador especificando los
casos de prueba necesarios que muestre por pantalla el valor de la fuerza a
partir de una masa y aceleración dadas.

"""

def fuerza(masa, aceleracion):
    return masa * aceleracion

masa = float(input('Masa: '))
aceleracion = float(input('Aceleracion: '))

print(f"{masa}kg * {aceleracion} m/s^2 = {fuerza(masa, aceleracion)}N")