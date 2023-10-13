"""
Una mejora útil, al anterior ejercicio, es programar una función entero_pedido
(min, max, msj) que pedirá un entero pero limitará su rango, es decir, el entero
deberá estar comprendido entre un máximo y un mínimo. Además, la función
recibirá un mensaje que será el que empleará para interactuar con el usuario.
Como ayuda, te ponemos aquí cómo sería el probador:

#Probador
min = 1
max = 12
print(entero_pedido(min, max, f'mes entre {min} y {max}: '))

"""


def entero_pedido(min:int, max:int, msg:str)->None:
    num = None
    correct = False

    while not correct:
        try:
            num = int(input('Introduce un número: '))
        except ValueError:
            print("No es un número válido, introduce otro: ")

        if num >= min and num <= max:
            print(msg)
            return
        else:
            print("Número fuera de rango")


entero_pedido(0, 10, f'El numero está ok')
