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


def BucketSort(arr, descending=False):
    NumberOfBuckets = round(math.sqrt(len(arr)))
    MaxValue = max(arr)
    buckets = [[] for _ in range(NumberOfBuckets)]

    for i in arr:
        bucket_index = math.ceil(i * NumberOfBuckets / MaxValue)
        buckets[bucket_index - 1].append(i)

    for j in range(NumberOfBuckets):
        buckets[j] = InsertionSort(buckets[j], descending)

    x = 0
    buckets = reversed(buckets) if descending else buckets
    print(f"buckets: {list(buckets)}")
    for k in buckets:
        for m in k:
            arr[x] = m
            x += 1
    return arr


print(BucketSort([1, 8, 8, 3, 5, 6]))
print(BucketSort([1, 8, 8, 3, 5, 6], descending=True))
