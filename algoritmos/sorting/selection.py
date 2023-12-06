arr = [2,8,7,3,51,58,63,35,68,1,3,8,16,3,8,14,54,13,384,185,31,138]

def selectionSort(arr:list)->list:
    for i in range(len(arr)):
        min_idx = i
        
        for j in range(i+1, len(arr)):
            if arr[min_idx] > arr[j]:
                min_idx = j
        
        arr[min_idx], arr[i] = arr[i], arr[min_idx]
    return arr

print(selectionSort(arr))