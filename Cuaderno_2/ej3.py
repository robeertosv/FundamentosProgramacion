"""
La Tasa de Interés Efectivo Anual (TIEA) es función de la tasa nominal anual
(TNA) y del número (entero) de períodos de capitalización (del número de
veces en el año que los intereses pasan a formar parte del capital) según la
siguiente expresión: TIEA=(1 + TNA/m)
m-1, siendo m el número de periodos
total de un año (es decir, 12 si hablamos de períodos mensuales, 4 si es
trimestral, 2 si es semestral, etc.). Escribe una función que calcule el TIEA a
partir del TNA y el número de períodos.

"""
tna = float(input('Introduce el TNA: '))
m = int(input('Introduce el número de meses: '))

def tiea(tna, m):
    return 1 + ((tna / m) ** (m-1))

print("El TIEA será de:",tiea(tna, m))