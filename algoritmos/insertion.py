arr = [2,8,7,3,51,58,63,35,68,1,3,8,16,3,8,14,54,13,384,185,31,138]

def insertionSort(arr:list)->list:
    for i in range(len(arr)):
        key = arr[i]
        j = i-1
        
        while j >= 0 and key < arr[j]:
            arr[j+1] = arr[j]
            j-=1
        
        arr[j+1] = key
    return arr

print(insertionSort(arr))