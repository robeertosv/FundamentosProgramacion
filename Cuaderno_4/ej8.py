"""
Crear una función que compruebe si dos cadenas de caracteres son iguales, sin
comparar las cadenas completas y sin usar el operador in. 
"""

x = 'Roberto'
y = 'Roberto'

def comprobador(c1, c2):
    iguales = False
    seguirMirando = True
    
    if(len(c1) != len(c2)):
        iguales = False
    else:
        for i in range(len(c1)):
            if(c1[i] != c2[i] and seguirMirando == True):
                iguales = False
                seguirMirando = False
            else:
                iguales = True
    return iguales
    

print(comprobador(x,y))