array = [1,2,8,5,8,5,786,54,78,87,45,24,8,54,5,84,5,45,4,15,6,4,8,6,4,8]

def selectionSort(arr:list)->list:
    for i in range(len(arr)):
        min_idx = i
        
        for j in range(i+1, len(arr)):
            if arr[min_idx] > arr[j]:
                min_idx = j
                
        arr[min_idx], arr[i] = arr[i], arr[min_idx]
    return arr

print(selectionSort(array))