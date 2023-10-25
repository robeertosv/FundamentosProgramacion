def cruz(n:int):
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