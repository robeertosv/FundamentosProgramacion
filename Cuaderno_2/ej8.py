"""
Escribe una función que a partir de las coordenadas 3D de dos puntos en el
espacio en formato (x, y, z) calcule la distancia que hay entre dichos puntos.

Prueba tu función. 
    
"""

a = (1, 2, 4)
b = (4, 5, 6)


def calc_vector(a, b) -> list:
    v = [0, 0, 0]  # v es el vector que va de a a b (AB)

    # Usando las matemáticas se asignan los valores a las posiciones del vector
    for i in range(len(a)):
        v[i] = b[i] - a[i]
    
    return v
    
def calc_vector_module(vec:list) -> int:
    import math
    
    m = 0 # variable a la que se sumarán los cuadrados de los elementos del vector
    
    for i in range(len(vec)):
        m += vec[i] ** 2
    
    return math.sqrt(m) # Devuelve la raíz cuadrada de la suma de los cuadrados de los componentes del vector (El módulo)

print(calc_vector_module(calc_vector(a,b)))