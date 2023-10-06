"""
Escribe un subprograma que lea una hora en notación de 24 horas y la devuelva
en notación de 12 horas (ejemplo: las 18:30 serán las 6:30 PM). Pruébalo utilizando
valores introducidos por el usuario, pero no olvides validad las entradas para
asegurarte de que se trata de valores en el rango correcto.

"""
import math

def converter(horas:int, minutos:int)->str:
    if(type(horas) != 'int' or type(minutos) != 'int'):
        if(horas < 24 or horas > 0 or minutos < 59 or minutos > 0):
            if(horas < 12):
                return str(horas) + ":" + str(minutos) + "AM"
            else:
                return str(horas-12) + ":" + str(minutos) + "PM"
    else:
        return "ERROR"
    
    

print(converter(13, 34))
print(converter(11, 40))