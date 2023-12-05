arr = [5, 2, 9, 7, 5, 48, 54, 12, 48, 15, 4, 8, 1, 415, 1, 8, 41, 54]

function bubbleSort(arr) {
    for (let i = 0; i < arr.length - 1; i++) {
        for (let j = 0; j < arr.length - i - 1; j++) {
            if(arr[j+1] < arr[j]) {
                let buffer = arr[j+1]
                arr[j+1] = arr[j]
                arr[j] = buffer
            }
        }
    }

    return arr
}

console.log(bubbleSort(arr))