arr = [2,8,7,3,51,58,63,35,68,1,3,8,16,3,8,14,54,13,384,185,31,138]

def bubbleSort(arr:list)->list:
    n = len(arr) - 1
    
    for i in range(n):
        for j in range(n-i):
            if arr[j+1] < arr[j]:
                arr[j+1], arr[j] = arr[j], arr[j+1]
                
    return arr

print(bubbleSort(arr))