def linear(array, find):
    for i, value in enumerate(array):
        if value == find:
            return i
    return -1


array = [1, 5, 7, 11, 45, 90]
print(linear(array, 99))
