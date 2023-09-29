"""
La ley de los gases ideales indica que el volumen V (en litros) ocupado por n
moles de un gas a presión P (en atmósferas) y temperatura T (en grados
Kelvin), responde a la siguiente fórmula:
V = nRT/P
siendo R la constante universal de los gases cuyo valor es 0,082 atmósferas
litro/Kmol. Hagamos un subprograma que calcule el volumen de un gas a
partir de su presión y temperatura y probémoslo.

"""

presion = float(input("Introduce la presión: "))
temperatura = float(input("Introduce la temperatura: "))

def calc(p, t):
    return (0.082 * t) / p