array = [1,2,8,5,8,5,786,54,78,87,45,24,8,54,5,84,5,45,4,15,6,4,8,6,4,8]

def bubbleSort(arr:list)->list:
    n = len(arr)
    
    for i in range(n-1):
        for j in range(n-1-i):
            if arr[j] > arr[j+1]:
                arr[j+1], arr[j] = arr[j], arr[j+1]
    return arr

print(bubbleSort(array))