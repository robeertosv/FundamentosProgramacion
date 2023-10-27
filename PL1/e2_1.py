def clasificadorDePuntos():
    Xcoord = float(input("Dime la componente X: "))
    Ycoord = float(input("Dime la componente Y: "))
    
    if (Xcoord > 0):
        #Puede estar en el I o IV
        if(Ycoord > 0):
            print("Punto en el cuadrante I")
        else:
            print("Punto en el cuadrante IV")
    else:
        #Puede estar en el II o III
        if(Ycoord > 0 ):
            print("Punto en el cuadrante II")
        else:
            print("Punto en el cuadrante III")

#clasificadorDePuntos()

import random
import math 
def circulo():
    radio = 1
    x0 = 0
    y0 = 0
    x = 0
    y = 0
    ok = False
    
    while(not ok):
        x = random.randint(-1, 1)
        y = random.randint(-1, 1)
        
        vectorX = x - x0
        vectorY = y - y0
        
        module = math.sqrt((vectorX**2 + vectorY**2))
        
        if(module <= radio):
            ok = True
    return x,y

print(circulo())