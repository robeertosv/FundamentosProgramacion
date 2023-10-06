import random

some = 0
Ntr = 10
nnsid = 6

for i in range(Ntr):
    some = some + random.randint(1, nnsid)
    
print(some/Ntr)