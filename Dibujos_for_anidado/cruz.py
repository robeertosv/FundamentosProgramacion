def cruz(n:int):
    for i in range(1, n+1):
        for j in range(1, n+1):
            if(i == n//2+1 or j == n//2+1):
                print(' * ', end="")
            else:
                print('   ', end="")
        print()

cruz(7)