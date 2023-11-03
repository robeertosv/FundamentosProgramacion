"""
Escribe un programa modularizado que a partir de una hora en formato [hora,
minutos y segundos] y utilizando una función que calcule el número total de
segundos transcurridos desde la última medianoche, lo muestre
posteriormente por pantalla.

"""

hora = [16, 59, 32] # 16:59:32

def horasAsegundos():
    return hora[0] * 3600

def minutosAsegundos():
    return hora[1] * 60

def segundosDesdeMediaNoche():
    return horasAsegundos() + minutosAsegundos() + hora[2]


print("Los segundos que han pasado desde media noche son:", segundosDesdeMediaNoche())