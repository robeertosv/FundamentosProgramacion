distancia = float(input("Cuantos km has hechado en el asfalto?\n"))
litrosFuel = float(input("Cuanto diesel has hechado?\n"))
precioFuel = float(input("A cuanto está el diesel?\n"))
costesVarios = float(input("En otros gastos, ¿cuánto te has fundido?\n"))

costeGasolina = litrosFuel * precioFuel
kilometroPorLitro = distancia / litrosFuel
costeTotalPorKM = (costeGasolina + costesVarios) / distancia

print(f"En gasolina has gastado {costeGasolina}€ \nEl consumo ha sido de {kilometroPorLitro} km/L \nEl coste total \
por kilómetro ha sido de {costeTotalPorKM} €/km")
