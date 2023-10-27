import math

def ternas(n):
    for i in range(1,n):
        for j in range(1, n):
            if(math.sqrt(i**2 + j**2) % 1 == 0):
                print(i, j, int(math.sqrt(i**2 + j**2)))

#ternas(40)

def ternasSinRepeticion(n):
    for i in range(1,n):
        for j in range(1, n):
            if(math.sqrt(i**2 + j**2) % 1 == 0):
                if(i**2 < j**2):
                    print(i, j, int(math.sqrt(i**2 + j**2)))

ternasSinRepeticion(40)