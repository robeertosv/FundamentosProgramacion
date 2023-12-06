arr = [2,8,7,3,51,58,63,35,68,1,3,8,3,8,14,54,13,384,185,31,138,16]

# Se puede usar cualquier algoritmo de búsqueda, cuanto más rápido mejor, pero me daba pereza hacerlo con quickSort
def selectionSort(arr:list)->list:
    for i in range(len(arr)):
        min_idx = i
        
        for j in range(i+1, len(arr)):
            if arr[min_idx] > arr[j]:
                min_idx = j
        
        arr[i], arr[min_idx] = arr[min_idx], arr[i]
    return arr

# Se trata de ir partiendo el array en mitades, para ello tiene que estar ordenado
def binarySearch(arr:list, elem:int)->str:
    arr = selectionSort(arr) # Ordenar el array
    
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

print(binarySearch(arr, 5))