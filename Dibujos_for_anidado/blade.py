"""Piensa este como una matriz, quiero poner una * en la diagonal (cnd i == j) o en la diagonal contraria (cnd i == n+1-j)"""
def blade(n:int):
    for i in range(1, n+1):
        for j in range(1, n+1):
            if (i == j or i == n+1-j):
                print('  *  ', end="")
            else:
                print('     ', end="")
        print()
        
blade(7)