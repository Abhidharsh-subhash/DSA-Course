def find_max(array, n):
    if n == 1:
        return array[0]
    return max(array[n - 1], find_max(array, n - 1))


x = [1, 2, 3, 4, 5, 6, 7, 90, 88, 89]
print(find_max(x, 9))
