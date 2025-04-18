import math


# Time complexity of binary search is O(logn)
def binary(array, find):
    start = 0
    end = len(array) - 1
    middle = math.floor((start + end) / 2)
    while array[middle] != find and start <= end:
        if array[middle] < find:
            start = middle + 1
        elif array[middle] > find:
            end = middle - 1
        middle = math.floor((start + end) / 2)
    return middle if array[middle] == find else -1


x = [1, 2, 3, 4, 5, 6, 7, 8]
print(binary(x, 20))
