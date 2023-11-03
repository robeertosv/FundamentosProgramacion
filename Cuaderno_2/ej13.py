"""
Haz un subprograma que determine los días, horas, minutos y segundos que
hay en una cantidad de segundos introducida por el usuario (desprecia las
fracciones de segundo). Escribe un probador para el mismo.

"""

def calcular_tiempo(segundos):
    # Calcular los días
    dias = segundos // 86400  # 86400 segundos en un día

    # Calcular las horas restantes
    segundos_restantes = segundos % 86400
    horas = segundos_restantes // 3600  # 3600 segundos en una hora

    # Calcular los minutos restantes
    segundos_restantes %= 3600
    minutos = segundos_restantes // 60  # 60 segundos en un minuto

    # Calcular los segundos restantes
    segundos_restantes %= 60

    return dias, horas, minutos, segundos_restantes

def probar_calculo_tiempo():
    segundos = int(input("Ingrese la cantidad de segundos: "))
    dias, horas, minutos, segundos_restantes = calcular_tiempo(segundos)

    print(f"Días: {dias}")
    print(f"Horas: {horas}")
    print(f"Minutos: {minutos}")
    print(f"Segundos: {segundos_restantes}")

# Ejecutar el probador
probar_calculo_tiempo()