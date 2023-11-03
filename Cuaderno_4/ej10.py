"""
Escriba un programa que “codifique” una frase modificando todas las vocales
según el siguiente código: a por 4, e por 3, i por 1, o por 0 y u por el símbolo #.
Por ejemplo, la frase: “Un perro del hortelano”, deberá devolverse: “#n p3rr0 d3l
h0rt3l4n0”.
"""
x = 'Un perro del hortelano'
def encoder(frase:str)->str:
    arr = []
    #Pasar la frase a un array
    for i in range(len(x)):
        arr.append(frase[i])
        
    #Modificar el array según lo que pide el ejercicio
    for i in range(len(arr)):
        if(arr[i] == 'A' or arr[i] == 'a'):
            arr[i] = '4'
        elif(arr[i] == 'e' or arr[i] == 'E'):
            arr[i] = '3'
        elif(arr[i] == 'i' or arr[i] == 'I'):
            arr[i] = '1'
        elif(arr[i] == 'o' or arr[i] == 'O'):
            arr[i] = '0'
        elif(arr[i] == 'u' or arr[i] == 'U'):
            arr[i] = '#'
    
    #Pasar el array a string
    s = ''
    for i in range(len(arr)):
        s += arr[i]
            
    return s

print(encoder(x))
