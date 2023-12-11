arr = [2,8,7,3,51,58,63,35,68,1,3,8,16,3,8,14,54,13,384,185,31,138]

def bubbleSort(arr:list)->list:
    n = len(arr) - 1
    
    for i in range(n):
        for j in range(n-i):
            if arr[j+1] < arr[j]:
                arr[j+1], arr[j] = arr[j], arr[j+1]
    return arr

#print(bubbleSort(arr))

def insertionSort(arr:list)->list:
    for i in range(len(arr)):
        key = arr[i]
        j = i-1
        
        while j >= 0 and key < arr[j]:
            arr[j+1] = arr[j]
            j-=1
        
        arr[j+1] = key
    
    return arr

#print(insertionSort(arr))

def selectionSort(arr:list)->list:
    for i in range(len(arr)):
        min_idx = i
        
        for j in range(i+1, len(arr)):
            if arr[min_idx] > arr[j]:
                min_idx = j
        
        arr[i], arr[min_idx] = arr[min_idx], arr[i]
    return arr

#print(selectionSort(arr))

"""Quick Sort"""
def partition(arr:list, low:int, high:int)->int:
    pivot = arr[high]
    i = low - 1
    
    for j in range(low, high):
        if arr[j] <= pivot:
            i+=1
            arr[j], arr[i] = arr[i], arr[j]
    arr[i+1], arr[high] = arr[high], arr[i+1]
    return i+1

def quickSort(arr, low, high):
    if low < high:
        pi = partition(arr, low, high)
        quickSort(arr, low, pi-1)
        quickSort(arr, pi+1, high)

s = len(arr) - 1
#quickSort(arr, 0, s)
#print(arr)

def binarySearch(arr:list, n:int):
    arr.sort()
    
    found = False
    i = 0
    index = len(arr) // 2 
    
    while n >= arr[0] and n <= arr[-1] and not found and i < len(arr):
        if arr[index] == n:
            found = True
        elif arr[index] < n:
            index += len(arr[index:len(arr)]) // 2
            i += 1
        else:
            index //= 2
            i += 1
    
    return f"{n} está en la posición {index}" if found else "Not found"

#print(binarySearch(arr, 1))
#print(binarySearch(arr, 384))
#print(binarySearch(arr, 5))
    