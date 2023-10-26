def piramide(n):
    for i in range(1, n):
        for j in range(i, n):
            print(' ', end="")
            
        for k in range(i):
            print('* ', end="")
        print()            
        
piramide(10)