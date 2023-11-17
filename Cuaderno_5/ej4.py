coords = [
    {
        "x": 5,
        "y": 5
    },
    {
        "x": 2,
        "y": 5
    },
    {
        "x": 3,
        "y": 0
    }
]

def suma(coords):
    x = []
    y = []
    
    for coord in coords:
        x.append(coord['x'])
        y.append(coord['y'])
    
    sumaX = 0
    sumaY = 0
    for c in x:
        sumaX += c
    for c in y:
        sumaY += c
    
    return (sumaX, sumaY)

def resta(coords):
    x = []
    y = []
    
    for coord in coords:
        x.append(coord['x'])
        y.append(coord['y'])
    
    sumaX = x[0]
    sumaY = y[0]
    
    for i in range(1, len(x)):
        sumaX -= x[i]
    
    for i in range(1, len(y)):
        sumaY -= y[i]
        
    
    return (sumaX, sumaY)

print(f"Suma de coordenadas: {suma(coords)}")
print(f"Resta de coordenadas: {resta(coords)}")