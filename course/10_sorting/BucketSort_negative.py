import math


def InsertionSort(arr, reverse=False):
    for i in range(1, len(arr)):
        val = arr[i]
        j = i - 1
        while j >= 0 and ((arr[j] < val) if reverse else (arr[j] > val)):
            arr[j + 1] = arr[j]
            j -= 1
        arr[j + 1] = val
    return arr


def BucketSort(customList):
    numberofBuckets = round(math.sqrt(len(customList)))
    minValue = min(customList)
    maxValue = max(customList)
    rangeVal = (maxValue - minValue) / numberofBuckets

    buckets = [[] for _ in range(numberofBuckets)]

    for j in customList:
        if j == maxValue:
            buckets[-1].append(j)
        else:
            index_b = math.floor((j - minValue) / rangeVal)
            buckets[index_b].append(j)

    sorted_array = []
    for i in range(numberofBuckets):
        buckets[i] = InsertionSort(buckets[i])
        sorted_array.extend(buckets[i])

    return sorted_array


print(BucketSort([1, 8, 8, 3, 5, 6, -2]))
