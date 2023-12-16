"""
Realiza un programa para gestionar los datos de stock de una tienda de
comestibles. La información a recoger será: nombre de producto, precio y
cantidad de stock. La tienda dispone de 10 productos distintos. El programa
debe ser capaz de:
a. Dar de alta un producto nuevo
b. Buscar un producto por su nombre, empleando búsqueda secuencial.
c. Ordenar los productos por el método de la burbuja según su precio

"""
productos = [
    {
        'nombre': 'pan',
        'precio': 0.45,
        'stock': 200
    },
    {
        'nombre': 'galletas',
        'precio': 1,
        'stock': 100
    },
    {
        'nombre': 'leche',
        'precio': 1.45,
        'stock': 250
    },
    {
        'nombre': 'harina',
        'precio': 0.75,
        'stock': 200
    },
    {
        'nombre': 'cocacola',
        'precio': 1.45,
        'stock': 300
    },
    {
        'nombre': 'mesas',
        'precio': 25,
        'stock': 5
    },
    {
        'nombre': 'bolis',
        'precio': 0.25,
        'stock': 100
    },
    {
        'nombre': 'ratones',
        'precio': 9.45,
        'stock': 20
    },
    {
        'nombre': 'cascos',
        'precio': 10.45,
        'stock': 26
    },
    {
        'nombre': 'telefono',
        'precio': 200,
        'stock': 10
    }
]

def nuevoProducto(productos, name, precio, cantidad):
    existe = False
    i = 0
    
    while not existe and i < len(productos):
        if productos[i]['nombre'] == name:
            existe = True
        i+=1
    
    if not existe:
        productos.append({'nombre': name, 'precio': precio, 'stock': cantidad})

def searchByName(productos, name):
    found = False
    i = 0
    
    while not found and i < len(productos):
        if productos[i]['nombre'] == name:
            print(f'Nombre: {name} \nPrecio: {productos[i]["precio"]}€ \nCantidad: {productos[i]["stock"]}')
            found = True
        i += 1

def sortByPrice(productos):
    n = len(productos) -1 
    
    for i in range(n):
        for j in range(n-i):
            if productos[j+1]['precio'] < productos[j]['precio']:
                productos[j+1], productos[j] = productos[j], productos[j+1]
    print(productos)
    
sortByPrice(productos)