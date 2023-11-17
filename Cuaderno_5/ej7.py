gasto = []
productos = []
suma = []

for i in range(10):
    g = int(input("Cuanto has gastado en gasolina? "))
    p = int(input('Cuanto has gastado en productos? '))
    
    gasto.append(g)
    productos.append(p)
    suma.append(g+p)

print(gasto)
print(productos)
print(suma)