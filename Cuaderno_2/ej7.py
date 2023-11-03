"""
7. La temperatura expresada en grados centígrados TC, se puede convertir a
grados Fahrenheit (TF) mediante la siguiente fórmula: TF = 9*TC/5 + 32.
Igualmente, es sabido que −273,15 °C corresponden con el 0 Kelvin. Escribe
una función devuelva la temperatura en grados Farenheit y otra en Kelvin a
partir de la temperatura en grados centígrados. Escribe un programa para
probarlas que a partir de una temperatura en grados centígrados obtenga e
imprima por pantalla la temperatura en Kelvin y Farenheit.

"""

def TCaK(tc):
   return tc + 273.15

def TCaTF(tc):
    return (tc * 9 / 5 )+ 32

tc = float(input('Introduce los ºC: '))

print(f'{tc}ºC son {TCaK(tc)}K y {TCaTF(tc)}ºF')
