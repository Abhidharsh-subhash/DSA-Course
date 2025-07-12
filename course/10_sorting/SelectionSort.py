def SelectionSort(array):
    for i in range(len(array)):
        min = i
        for j in range(i + 1, len(array)):
            if array[j] < array[min]:
                min = j
        if min != i:
            array[i], array[min] = array[min], array[i]
    return array


print(SelectionSort([1, 8, 8, 3, 5, 6]))
