"""Lo mismo que ej 2 pero con selection sort"""

frases = ['hola', 'adios', 'array', 'tupla', 'variable', 'raton', 'teclado', 'pez', 'calamar','indice']
d = []

for frase in frases:
    d.append((len(frase), frase))
    
for i in range(len(d)):
    min_idx = i
    for j in range(i+1, len(d)):
        if d[min_idx][0] < d[j][0]:
            min_idx = j
            
    d[i], d[min_idx] = d[min_idx], d[i]

result = []
for frase in d:
    result.append(frase[1])
print(result)