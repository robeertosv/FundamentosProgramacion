"""
Escribir una función que permita mostrar los caracteres de una cadena del final
al principio, pero nunca mostrando la letra “a”. Ejemplo: si la entrada es “barco
amarillo”, la función devolverá: “ollirm ocrb”. 
"""
def reverser(string):
    arr= []
    for i in range(len(string)):
        if(string[i] != 'a'):
            arr.append(string[i])
    
    arr = arr[::-1]
    result = ''
    
    for i in range(len(arr)):
        result += arr[i]
    
    return result

print(reverser('barco amarillo'))