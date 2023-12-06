arr = [2,8,7,3,51,58,63,35,68,1,3,8,16,3,8,14,54,13,384,185,31,138]

def partition(arr:list, low:int, high:int):
    pivot = arr[high]
    i = low - 1
    
    for j in range(low, high):
        if arr[j] <= pivot:
            i+=1
            arr[j], arr[i] = arr[i], arr[j]
    arr[i+1], arr[high] = arr[high], arr[i+1]
    return i+1

def quickSort(arr:list, low:int, high:int):
    if low < high:
        pi = partition(arr, low, high)
        quickSort(arr, low, pi-1)
        quickSort(arr, pi+1, high)

s = len(arr) - 1
quickSort(arr, 0, s)
print(arr)