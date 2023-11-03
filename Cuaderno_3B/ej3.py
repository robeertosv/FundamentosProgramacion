"""
Escribe un programa que, después de preguntar ¿Cuántos números se van a
introducir?, pida esos números (enteros o reales) y devuelva su media aritmética,
el mayor y el menor. El programa debe controlar que la cantidad de números es
mayor de 2 y en caso contrario ha de mostrar un mensaje de error. Como siempre,
valida las entradas.
"""

def media()->float:
    correct = False
    nums = None
    
    while not correct:
        try:
            cantidad = int(input("Cuantos números se van a introducir?? "))  
        except ValueError:
            print("No se ha introducido un número")
        else:
            break
        
    nums = []
    for i in range(cantidad):
        try:
            nums.append(int(input(f"Introduce el {i+1}º número: ")))
        except ValueError:
            print("Ese número no es válido")            
    
    sumatorio = 0
    for i in range(cantidad):
        sumatorio += nums[i]

    return sumatorio / cantidad
print(media())