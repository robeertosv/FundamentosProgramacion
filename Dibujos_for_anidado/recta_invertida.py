def recta_invertida(n):
    for i in range(1, n):
        for i in range(n-i):
            print('* ', end="")
        print()
recta_invertida(10)