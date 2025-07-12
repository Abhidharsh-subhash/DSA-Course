def InsertionSort(arr):
    for i in range(1, len(arr)):
        val = arr[i]
        j = i - 1
        while j >= 0 and arr[j] < val:
            arr[j + 1] = arr[j]
            j -= 1
        arr[j + 1] = val
    return arr


print(InsertionSort([1, 8, 8, 3, 5, 6]))
