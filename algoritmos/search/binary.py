#arr = [2,8,7,3,51,58,63,35,68,1,3,8,3,8,14,54,13,384,185,31,138,16]
arr = ['roberto', 'luis', 'paco']

# Se trata de ir partiendo el array en mitades, para ello tiene que estar ordenado
def binarySearch(arr:list, elem:int)->str:
    arr.sort() # El array tiene que estar ordenado, se puden usar los algoritmos quickSort, insertionSort, bubble... Pero este ya te lo da Python
    print(arr)
    found = False
    i = 0
    
    index = len(arr) // 2
    msg = ''
    
    while elem >= arr[0] and elem <= arr[-1] and not found and i < len(arr):
        if arr[index] == elem:
            found = True
            
        #Mirar lo que hay a la derecha
        elif arr[index] < elem:
            index += len(arr[index:len(arr)]) // 2
            i+=1
        #Mirar lo que hay a la izquierda
        else:
            index //= 2
            i+=1
    
    return f'{elem} encontrado en la posición {index}' if found == True else f'El número {elem} no está en la lista'

print(binarySearch(arr, 'paco'))