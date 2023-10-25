def cruz(n:int):
    
    """La idea es pintar los palos de arriba de la cruz (la mitad por eso //2), luego la fila llena de cruces, y luego la otra mitad"""
    for i in range(n//2):
        for j in range(n//2):
            print('   ', end="")
        print('*')
    
    for i in range(n):
        print('*  ', end="")
    print()
    for i in range(n//2):
        for j in range(n//2):
            print('   ', end="")
        print('*')

cruz(7)