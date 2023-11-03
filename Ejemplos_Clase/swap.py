# Supongamos dos variables
a = 1
b = 2

# Los valores son evaluados, se guardan en memoria y tienen una etiqueta

# Cambiar los valores
def swap(z, s):
    aux = z
    z = s
    s = aux

    return z, s  # Devuelve un tuple con dos valores

a, b = swap(a, b)

# Aux no está definida fuera del scope de la funcion swap

# Otra manera de hacer esto sería
a, b = b, a