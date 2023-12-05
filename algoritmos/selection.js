let array = [1, 2, 8, 5, 8, 5, 786, 54, 78, 87, 45, 24, 8, 54, 5, 84, 5, 45, 4, 15, 6, 4, 8, 6, 4, 8]

function selectionSort(arr) {
    for(let  i = 0 ; i < arr.length; i++) {
        let min = i

        for(let j = i+1; j < arr.length; j++) {
            if(arr[min] > arr[j]) {
                min = j
            }
        }

        let buffer = arr[min]

        arr[min] = arr[i]
        arr[i] = buffer

    }
    return arr
}

console.log(selectionSort(array))