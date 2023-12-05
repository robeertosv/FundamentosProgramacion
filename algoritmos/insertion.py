array = [1,2,8,5,8,5,786,54,78,87,45,24,8,54,5,84,5,45,4,15,6,4,8,6,4,8]

def insertionSort(arr:list)->list:
    for i in range(len(arr)):
        key = arr[i]
        j = i-1
        
        while j >= 0 and key < arr[j]:
            arr[j+1] = arr[j]
            j-=1
        
        arr[j+1] = key
    return arr

print(insertionSort(array))