"""
Ya vimos que la validación de entradas es algo tan presente que no podemos
escapar de ello, así que si te parece vamos a escribir una función que solicite al
usuario introducir un entero y que no pare de pedírselo hasta que la información
introducida sea válida.

La idea es usar la construcción while combinada con la función de validación
programada en cuadernos anteriores, consiguiendo una función cuya cabecera
sería la siguiente:

def leer_entero_validado():
 "" None --> int
 OBJ: Solicita un entero al usuario, lo valida y lo retorna sólo
 cuando se ha asegurado de que es realmente un entero
 ""
"""

def leer_entero_validado():
    correcto = False
    num = None
    
    while not correcto:
        try:
            num = int(input("Introduce un número: "))
        except ValueError:
            print("No has metido un número válido, intentalo de nuevo")
        else:
            correcto = True
            
    return correcto

def is_int(x:int)->bool:
    try:
        int(x)
    except ValueError:
        return False
    else:
        return True