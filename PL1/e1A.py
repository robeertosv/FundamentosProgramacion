angulos = []
#for i in range(3):
 #   angulos.append(float(input(f'Dime el {i+1} ángulo')))


def typeOfTriangle(angulos):
    """Introducir un array de 3 posiciones"""
    if(90 in angulos):
        print("Es rectángulo")   
    elif(angulos[0] < 90 and angulos[1] < 90 and angulos[2] < 90):
        print("Es acutángulo")
    else:
        print("Es obtusangulo")