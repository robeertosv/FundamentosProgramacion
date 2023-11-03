import math
import random

def distance(x1, y1, x2, y2):
    distancia = math.sqrt((x2-x1)**2+(y2-y1)**2)
    return distancia

def equal(x1, y1, x2, y2):
    eq = False
    if distance(x1, y1, x2, y2) == 0:
        eq = True
    return eq


def which_is_closer(x,y,x2,y2,x3,y3):
    closer = 0
    
    if(distance(x,y,x2,y2) < distance(x,y,x3,y3)):
        closer = x2, y2
    else:
        closer = x3, y3

    return closer


def generate_point(n):
    x= random.randint(1,n)
    y = random.randint(1,n)
    
    return x,y

def generate_distinct_points(x,y,n):
    ok = False
    p1 = 0
    p2 = 0 
    while not ok:
        p1 = generate_point(n)
        p2 = generate_point(n)
        
        if((x,y) != p1 != p2):
            ok = True
    return p1, p2

def print_point_and_two_randoms(x,y,n):
    ((x1, y1), (x2,y2)) = generate_distinct_points(x,y,n)
    
    a, b = which_is_closer(x,y,x1,y1,x2,y2)
    c,d = (0, 0)
    
    if(a == x1 and b==y1):
        c,d = x2, y2
    else:
        c, d = x1,y1
    
    for i in range(1, n+1):
        for j in range(1,n+1):
            if(i==x and j==y):
                print(' 0 ', end="")
            elif (i == a and j == b):
                print(' C ', end="")
            elif (i == c and j == d):
                print(' @ ', end="")
            else:
                print(' . ', end="")
        print()

print_point_and_two_randoms(3,3,10)
