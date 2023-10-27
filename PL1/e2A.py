import math
def cruz(n):
    for i in range(math.floor(n/2)):
        print(" " * math.floor(n/2)*3 + "*")
    
    print(" * " * n)
    
    for i in range(math.floor(n/2)):
        print(" " * math.floor(n/2)*3 + "*")
    
cruz(7)