"""
Realiza un programa que almacene 10 frases diferentes en una lista y nos
permita ordenar la misma de forma descendentemente utilizando como
criterio la longitud de la frase. Utiliza el método de inserción directa.
"""

frases = ['hola', 'adios', 'array', 'tupla', 'variable', 'raton', 'teclado', 'pez', 'calamar','indice']
d = []

for frase in frases:
    d.append((len(frase), frase))
    
for i in range(len(d)):
    key = d[i]
    j = i-1
    
    while j >= 0 and key > d[j]:
        d[j+1], d[j] = d[j], d[j+1]
        j-=1

result = []
for frase in d:
    result.append(frase[1])
    
print(result)