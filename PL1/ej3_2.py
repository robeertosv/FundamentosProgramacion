import random

def tiradasDado():
    ok = False
    contador = 0
    while not ok:
        x = random.randint(1,6)
        if(x == 6):
            ok = True
        else:
            contador += 1
    return contador
#print(tiradasDado())

def secuenciaDado():
    tirada1 = 0
    tirada2 = 0
    tirada3 = 0
    contador = 0
    ok = False
    while not ok:
        tirada1 = random.randint(1,6)
        tirada2 = random.randint(1,6)
        tirada3 = random.randint(1,6)
        
        if(tirada1 == 6 and tirada2 == 6 and tirada3==6):
            ok = True
        else:
            contador += 1
    return contador

print(secuenciaDado())
    