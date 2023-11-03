from e1A import typeOfTriangle

import random

def generateAngles():
    ok = False
    while(not ok):
        a1 = 0
        a2 = 0
        a3= 0
        for i in range(3):
            a1 = random.randint(0, 180)
            a2 = random.randint(0, 180)
            a3 = random.randint(0, 180)
            
            print(f'{a1}, {a2}, {a3}')
            
        if(a1 + a2 + a3 == 180):
            ok = True
            return (a1, a2, a3)
        
typeOfTriangle(generateAngles())