import array

# array of integers
my_array = array.array("i")
# print(my_array)
my_array1 = array.array("i", [1, 2, 3, 4, 5])
# print(my_array1)

my_array1.insert(2, 10)
# print(my_array1)

import numpy as np

np_array = np.array([], dtype=int)
# print(np_array)
np_array1 = np.array([1, 2, 3, 4], dtype=int)
# print(np_array1)


def traversal(array):
    for i in array:
        print(i, end=" ")


traversal(np_array1)


def accessElement(array, index):
    print("Invalid Index") if len(array) <= index else print(array[index])


accessElement(np_array1, 9)


def linear_search(array, element):
    for i in range(len(array)):
        if array[i] == element:
            return i + 1
    return -1


print(linear_search(np_array1, 3))

print(my_array1)
my_array1.remove(3)
print(my_array1)
