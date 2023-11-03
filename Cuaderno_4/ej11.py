"""
Un texto contiene comandos en forma de frases separadas por puntos. En cada
frase, la primera palabra contiene el código de la operación y la última el
resultado. Ejemplo:
SUMAR 45 50 95. AND A B TRUE. MULT 10 20 200. Etc.
Cree una lista de parejas [código-resultado] utilizando como entrada un texto
con el formato indicado
"""


def codeRes(x:str):
    separated = []
    separated = x.split('. ')
    comandos = []
    for i in range(len(separated)):
        comandos.append(separated[i].split(' '))
    res = []
    for i in range(len(comandos)):
        res.append([comandos[i][0], comandos[i][-1]])
    
    res.pop()
    return res
    
x = "SUMAR 45 50 95. AND A B TRUE. MULT 10 20 200. RESTA 20 10 10. "
print(codeRes(x))