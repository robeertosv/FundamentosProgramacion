import random

for i in range(21):
    for j in range(21):
        n = random.randint(0,1)
        if(n == 0):
            print(" ", end=" ")
        else:
            print("*", end=" ")
    print()