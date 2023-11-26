def nameCheck(name):
    if name == 'roberto':
        print("Eres Roberto, bienvenido")
    else:
        n = input('No eres roberto, dime tu nombre: ')
        nameCheck(n)

def PIN():
    auth = False
    pin = int(input("Introduce tu PIN: "))
    
    if pin == 1234:
        auth = True
    else:
        print('Pin Incorrecto')
        auth =  PIN()
        
    return auth