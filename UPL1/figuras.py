import random

def dados():
    ok = False
    sumador  = 0
    
    while not ok:
        d1 = random.randint(1,6)
        d2 = random.randint(1,6)
        d3 = random.randint(1,6)
        sumador +=1
        print(d1, d2, d3)
        if(d1 == d2 == d3 == 6):
            print(sumador)
            ok = True
dados()