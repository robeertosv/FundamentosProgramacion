"""

Codifica un subprograma que reciba un número entero, y si es entre 1 y 12 escriba
un mensaje por pantalla indicando el mes a que dicho número corresponde. En
caso contrario deberá mostrar un mensaje de error. Valida las entradas.

"""

meses = ['Enero', 'Febrero', 'Marzo', 'Abril', 'Mayo', 'Junio', 'Julio', 'Agosto', 'Septiembre', 'Octubre', 'Noviembre', 'Diciembre']

def mes(n:int)->str:
    if(n > 12 or n < 0):
        return "Error"
    
    return meses[n-1]

n = int(input('Introduce el numero del mes: '))

print(mes(n))