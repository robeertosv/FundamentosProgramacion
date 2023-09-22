hora = [15, 23, 18] #Horas, minutos, segundos

segundosActual = hora[0] * 3600 + hora[1] * 60 + hora[2]

segundosMediaNoche = 24 * 3600

segundosAMediaNoche = segundosMediaNoche - segundosActual

print(f"Llevamos {segundosActual} segundos de día. Quedan {segundosAMediaNoche} segundos para media noche")
