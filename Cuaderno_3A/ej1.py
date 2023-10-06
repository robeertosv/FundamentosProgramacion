"""
Escribe un código que pide al vendedor el importe de una compra: Si la compra es
superior a 100EUR se aplica un descuento del 5% si se paga al contado, pero si el
pago es con tarjeta sólo se aplica el 2%. Asegúrate de que el importe de la compra
es un número válido antes de proceder a los cálculos (pista: usa try para
comprobar que es posible convertir la entrada a un float).

"""

def handler(importe, metodo):
    final = None
    if(float(importe)):
        if(importe > 100 and metodo == "efectivo"):
            final = importe*0.95
        elif(importe > 100 and metodo == "tarjeta"):
            final = importe*0.98
        elif(importe < 100):
            final = importe
        else: 
            print("ERROR")
            
    return final

print(handler(120, "efectivo"))