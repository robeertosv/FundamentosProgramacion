"""
El antiguo sistema anglosajón de unidades sigue en vigor en muchos lugares
y su uso es frecuente en algunos contextos. Programa una función que
determine el número de pintas que contiene una cierta cantidad de líquido
expresada en mililitros, sabiendo que 1 pinta (pt) = 473,176473 ml.

"""

PINTA = 473.176473 # 1 pinta en ml

ml = float(input("Introduce el número de mililítros: "))

def mlApintas(ml):
    return ml / PINTA

print(f'{ml} ml son {mlApintas(ml)} pintas')