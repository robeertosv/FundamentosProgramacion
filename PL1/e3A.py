def secuencia()->float:
    ok = False #flag de control del bucle
    len = 0 # Numero de números introducidos
    tot = 0 # Sumatorio de los números introducidos
    media = 0 # Media de los números (Se calcula al final)
    prev = 0 # Almacena el numero previo
    while(not ok):
        try: #Comprueba si es un número
            n = int(input("Introduce el número: ")) #Pregunta el número al usuario
            
            if(n > prev): # Si es mayor que el anterior lo añade al sumatiorio, incrementa la cantidad de numeros y lo establece como prev
                tot += n
                len += 1
                prev = n
            else:
                if(len <= 2): #Si los dos primeros están mal lo indica y rompe la ejecución
                    print("Secuencia no válida")
                    ok = True
                else:
                    media = tot / len #Calcula la media y rompe el bucle
                    ok = True
        except ValueError:
            print("No es un número válido") #Excepción que salta si el usuario no introduce un número
    
    return media #Devuelve la media

print(secuencia())