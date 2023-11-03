import math

def perfect_square(x:int)->int:
    """Devuelve la raíz cuadrada del argumento x. x tiene que ser mayor o igual que 0"""
    
    if(x > 0):
        s = int(math.sqrt(x))
        if(type(s) == int):
            return s
        else:
            return None
    else:
        return None

print(perfect_square(83))