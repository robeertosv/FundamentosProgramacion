def request():
    numbers = []
    for i in range(10):
        numbers.append(int(input('Dime un número: ')))
    return numbers

def restador():
    numeros = request()
    restas = []
    for i in range(len(numeros)):
        try:
            restas.append((numeros[i], numeros[i+1]))
        except IndexError:
            restas.append((numeros[i], numeros[-1]))
    print(restas)
    
    print(' = ')
    for i in range(len(restas)):
        print(restas[i][0] - restas[i][1])
restador()