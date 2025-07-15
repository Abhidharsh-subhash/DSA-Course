def Partition(arr, pivot, end):
    start = pivot
    for i in range(pivot + 1, end):
        if arr[i] > arr[pivot]:
            start += 1
            arr[i], arr[start], arr[start], arr[i]
    arr[pivot], arr[start] = arr[start], arr[pivot]
    return start


def QuickSortHelper(arr, left, right):
    if left < right:
        pivot = Partition(arr, left, right)
        QuickSortHelper(arr, left, pivot - 1)
        QuickSortHelper(arr, pivot + 1, right)
    return arr


def QuickSort(arr):
    return QuickSortHelper(arr, 0, len(arr) - 1)


print(QuickSort([1, 8, 8, 3, 5, 6]))
