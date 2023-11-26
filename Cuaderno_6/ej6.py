"""
Realizar una función recursiva que dado un número entero, cuente su número
de dígitos. 
"""
num = 12345

def counter(num:int)->int:
    num = str(num)
    count = 0
    if(len(num) != 0):
        count += 1
        count += counter(num.rstrip(num[-1]))
    return count

print(f"El número {num} está formado por {counter(num)} dígitos")