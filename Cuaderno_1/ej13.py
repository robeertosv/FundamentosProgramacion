"""
13.Se desea conocer el importe en Libras Esterlinas (GBP) al cambio de una
cantidad en Euros (EUR). Escribe un programa que, a partir de una cierta
cantidad en euros y del tipo de cambio del día, muestre el equivalente en
libras teniendo en cuenta que la casa de cambio retiene una comisión del 2%
sobre el total de la operación.

"""

euros = float(input("Introduce la cantidad de EUR: "))

EURaGBP = 0.87 # A 23 de septiembre de 2023

def cambio(eur):
    return euros * EURaGBP * (1-0.02)

print(f"Para {euros}EUR vas a recibir {cambio(euros)}")