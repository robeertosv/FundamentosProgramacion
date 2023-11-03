"""

Escribe un programa que lea dos caracteres y averigüe si se introdujeron en el
orden de su código ASCII o no. Se deberá además comprobar si el primero de ellos
es una cifra, y en caso afirmativo indicar si es impar y si es o no primo. Modulariza
la solución. En tu código no deben aparecer los valores de la tabla ASCII, porque
produciría un código muy difícil de mantener, puedes usar ord() y chr() o
simplemente saber que en la tabla ASCII todos los dígitos son consecutivos).

"""

def es_digito(caracter):
    return '0' <= caracter <= '9'

def es_primo(numero):
    if numero <= 1:
        return False
    if numero <= 3:
        return True
    if numero % 2 == 0 or numero % 3 == 0:
        return False
    i = 5
    while i * i <= numero:
        if numero % i == 0 or numero % (i + 2) == 0:
            return False
        i += 6
    return True

def main():
    caracter1 = input("Introduce el primer caracter: ")
    caracter2 = input("Introduce el segundo caracter: ")

    if len(caracter1) == 1 and len(caracter2) == 1:
        if caracter1 < caracter2:
            print(f"Los caracteres '{caracter1}' y '{caracter2}' están en orden ASCII.")
        else:
            print(f"Los caracteres '{caracter1}' y '{caracter2}' NO están en orden ASCII.")
        
        if es_digito(caracter1):
            numero = int(caracter1)
            if numero % 2 == 1:
                print(f"{caracter1} es un número impar.")
            if es_primo(numero):
                print(f"{caracter1} es un número primo.")
            else:
                print(f"{caracter1} no es un número primo.")
        else:
            print(f"{caracter1} no es un dígito.")
    else:
        print("Por favor, introduce un solo caracter para cada entrada.")

if __name__ == "__main__":
    main()
