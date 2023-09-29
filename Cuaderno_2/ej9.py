"""
Un número complejo es un número de la forma a+bi, donde a y b son
números reales y el valor de i es √-1 . Las cuatro operaciones aritméticas
básicas sobre números complejos se definen como:

• Suma: (a+bi)+(c+di)=(a+c)+(b+d)i
• Resta: (a+bi)-(c+di)=(a-c)+(b-d)i
• Producto: (a+bi)*(c+di)=(ac-bd)+(ad+bc)i
• División: (a+bi)/(c+di) = ((ac+bd)/(c2+d2)) + ((bc-ad)/(c2+d2))i, suponiendo c2+d2<>0

Programa funciones para cada una de las operaciones descritas con sus
respectivos probadores y prepara una biblioteca con ellos. Construye los
probadores que muestren por pantalla el resultado de las operaciones
reseñadas. No utilices datos de tipo complejo, sino que deberás simularlos
programando los complejos utilizando como coeficientes (a,b,c y d) valores
de tipo real.

"""

# Función para sumar dos números complejos
def suma_complejos(a, b, c, d):
    real_part = a + c
    imag_part = b + d
    return (real_part, imag_part)

# Función para restar dos números complejos
def resta_complejos(a, b, c, d):
    real_part = a - c
    imag_part = b - d
    return (real_part, imag_part)

# Función para multiplicar dos números complejos
def multiplicacion_complejos(a, b, c, d):
    real_part = (a * c) - (b * d)
    imag_part = (a * d) + (b * c)
    return (real_part, imag_part)

# Función para dividir dos números complejos
def division_complejos(a, b, c, d):
    if (c == 0 and d == 0):
        print("El denominador no puede ser cero.")
    
    denominador = c**2 + d**2
    real_part = ((a * c) + (b * d)) / denominador
    imag_part = ((b * c) - (a * d)) / denominador
    return (real_part, imag_part)

# Probador para las funciones
def probar_operaciones():
    a = float(input("Ingrese la parte real de número complejo A: "))
    b = float(input("Ingrese la parte imaginaria de número complejo A: "))
    c = float(input("Ingrese la parte real de número complejo B: "))
    d = float(input("Ingrese la parte imaginaria de número complejo B: "))
    
    resultado_suma = suma_complejos(a, b, c, d)
    resultado_resta = resta_complejos(a, b, c, d)
    resultado_multiplicacion = multiplicacion_complejos(a, b, c, d)
    
    try:
        resultado_division = division_complejos(a, b, c, d)
        print(f"Suma: {resultado_suma}")
        print(f"Resta: {resultado_resta}")
        print(f"Multiplicación: {resultado_multiplicacion}")
        print(f"División: {resultado_division}")
    except ValueError as e:
        print(e)

# Ejecutar el probador
probar_operaciones()
