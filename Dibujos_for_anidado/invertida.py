def piramide(n):
    for i in range(n):
        for j in range(i):
            print(' ', end="")
        
        for k in range(1,n-i+1):
            print("& ", end="")
        
        print()
        
piramide(10)