# Calcular el valor absoluto
def abs(x:float)-> float :
    if(x >= 0):
        return x
    else:
        return -x

# Otra manera
def abs1(x:float) -> float:
    return x if x >= 0 else -x