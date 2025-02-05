# What is the runtime of the below codes


# 1)
def foo(array):
    sum = 0
    product = 1
    for i in array:
        sum += i
    for i in array:
        product *= i
    print(f"Sum = {sum}, Product = {product}")


# Time complexity is O(n)
foo([1, 2, 3, 4, 5])


# 2)
def printPairs(array):
    for i in array:
        for j in array:
            print(f"{i}, {j}")


# Time complexity is O(n^2)
printPairs([1, 2, 3, 4, 5])


# 3)
def printUnorderedPairs(array):
    for i in range(0, len(array)):
        for j in range(i + 1, len(array)):
            print(f"{array[i]}, {array[j]}")


# Time complexity is O(n^2)
printUnorderedPairs([1, 2, 3, 4, 5])


# 4)
def printUnorderedPairs1(array1, array2):
    for i in range(len(array1)):
        for j in range(len(array2)):
            if array1[i] < array2[j]:
                print(f"{array1[i]}, {array2[j]}")


# Time complexity is O(len(array1)*len*(array2))
printUnorderedPairs1([1, 2, 3, 4, 5], [6, 7, 8, 9, 10])
