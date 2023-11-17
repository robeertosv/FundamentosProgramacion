import math
coords = [
    {
        "x": 5,
        "y": 5
    },
    {
        "x": 2,
        "y": 5
    }
]

def distance(coords):
    x = []
    y = []
    
    for i in coords:
        x.append(i['x'])
    for i in coords:
        y.append(i['y'])
    
    return math.sqrt((x[1] - x[0])**2 + (y[1] - y[0])**2)

print(distance(coords))