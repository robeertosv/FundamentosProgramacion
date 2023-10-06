"""

Obtén las raíces de una ecuación de segundo grado ax^2 bx c = 0 a partir de sus
coeficientes a, b y c. Recuerda que si el discriminante es cero la raíz es única (-
b/2xa) y que si el discriminante es negativo las raíces son imaginarias, en cuyo
caso deberá indicarse con un mensaje “raíces imaginarias”. 

"""

from math import sqrt
a = float(input("Introduce en exponente a: "))
b = float(input("Introduce en exponente b: "))
c = float(input("Introduce en exponente c: "))

def resolver(a,b,c):
    if(b**2 - 4*a*c < 0):
        print("Raíz imagnaria")
        return
    s1 = (-b + sqrt(b**2 - 4*a*c)) / (2*a)
    s2 = (-b - sqrt(b**2 - 4*a*c)) / (2*a)
    
    return s1,s2

print(resolver(a,b,c))