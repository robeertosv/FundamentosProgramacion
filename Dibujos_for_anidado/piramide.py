def piramide(n):
    for i in range(n):
        for j in range(i, n*2-1):
            print(' ', end="")
            
        for k in range(i):
            print('* ', end="")
        print()            
        
piramide(10)