"""
Por consideraciones históricas, un programador suele interpretar que los
identificadores i, j, k, l, m, n corresponden a datos enteros, mientras que a,
b, c, x, y, z son identificadores que suelen asociarse con valores reales.
Escribe un programa que, a partir de 3 números reales que inicializarás,
calcule su media, suma total y producto total y muestre todos estos datos por
pantalla.

"""

a = 2.5
b = 5.25
c = 8.2


def media(a, b, c):
    return (a + b + c) / 2


def sumaTotal(a, b, c):
    return a + b + c


def productoTotal(a, b, c):
    return a * b * c


print(f'La media de {a}, {b} y {c} es: {media(a,b,c)}\nLa suma total de esos tres números es {sumaTotal(a,b,c)}\nEl producto total es {productoTotal(a,b,c)}')
