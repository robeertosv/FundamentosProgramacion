"""
El salario base de un vendedor es de 2.000 euros mensuales. A este salario
se le suma un 3% de comisión sobre el total de las ventas que ha realizado,
pero al total obtenido hay que descontarle un 32% del IRPF. Escribe un
programa que, a partir del importe de las ventas que ha realizado el vendedor
durante el último mes y escriba el salario neto que cobrará ese mes.

"""

importeVentas = float(input("Introduce cuánto has vendido este mes: "))

salario = ( 2000 + (importeVentas + importeVentas * 0.03) ) * (1 - 0.32)

print("Este mes vas a cobrar:",salario,"euros")