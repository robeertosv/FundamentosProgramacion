def is_isosceles(a,b,c)->bool:
    isosceles = False
    
    if a==b or a==c or b==c:
        isosceles = True
    
    return isosceles

def is_golden_ratio(a,b):
    is_golden = False
    
    if((a/b) == ((a+b)/b)):
        is_golden = True
    
    return is_golden

def leg_base_isosceles(a,b,c):
    leg = 0
    base = 0
    
    if(a==c):
        leg = a
        base = b
    elif a==b:
        leg = a
        base = c
    elif b==c:
        leg = b
        base = a
    
    return leg, base

def is_golden_triangle(a,b,c):
    is_golden = False
    if(is_isosceles(a,b,c)):
        leg, base = leg_base_isosceles(a,b,c)
        if(is_golden_ratio(leg, base)):
            is_golden = True
    
    return is_golden