"""
    Escribe un programa que, a partir de los lados de un rectángulo, calcule su
    área y perímetro y los muestre por pantalla.
"""

# Pedir la longitud de la base
base = float(input('Dime la base del rectángulo\n'))
# Pedir la longitud de la altura
altura = float(input('Dime la altura del rectángulo\n'))


# Al ser un cálculo muy simple usar una lambda es más rápido que definir una función
area = lambda b, h : b * h


# Mostrar el resultado por pantalla
print(f'El área del rectángulo de base {base} y altura {altura} es {area(base, altura)}')
