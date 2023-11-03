"""
El Barn es una unidad de superficie muy utilizada en la física de partículas,
que equivale a 10-28 m². Para ilustrar su tamaño, ten en cuenta que un Barn
es, aproximadamente, el área de la sección transversal del núcleo de un
átomo de uranio. Programa dos funciones, una que permita convertir
unidades en m² a Barns, y su inversa.

"""

barn = 10 ** -28

def mAbarns(m):
    return m * barn

def barnsAm(b):
    return b / barn

b = float(input('Introduce el número de barns: '))
m  = float(input('Introduce el número de metros^2: '))

print(f"{b} barns son {barnsAm(b)} m^2 \n {m} m^2 son {mAbarns(m)} barns")