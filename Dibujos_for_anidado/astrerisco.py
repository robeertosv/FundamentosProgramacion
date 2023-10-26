def asterisco(n):
    mid = n//2 +1
    for fila in range(1, n+1):
        for columna in range(1, n+1):
            if(columna == mid or fila == mid or columna == n-fila+1 or columna == fila):
                
                print(' * ', end="")
            else:
                print('   ', end="")
        print()
asterisco(7)