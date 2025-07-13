def MergeSort(arr):
    if len(arr) <= 1:
        return arr
    mid = len(arr) // 2
    left = arr[:mid]
    right = arr[mid:]
    left = MergeSort(left)
    right = MergeSort(right)
    return Merge(left, right)


def Merge(arr1, arr2):
    result = []
    i = j = 0
    l1 = len(arr1)
    l2 = len(arr2)
    while i < l1 and j < l2:
        if arr1[i] < arr2[j]:
            result.append(arr2[j])
            j += 1
        else:
            result.append(arr1[i])
            i += 1
    while j < l2:
        result.append(arr2[j])
        j += 1
    while i < l1:
        result.append(arr1[i])
        i += 1
    return result


print(MergeSort([1, 8, 8, 3, 5, 6]))
