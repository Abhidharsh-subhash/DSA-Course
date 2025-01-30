# 1) MISSING NUMBER


# Time complexity is O(n^2)
def missing_number(arr, n):
    for i in range(1, n + 1):
        if i not in arr:
            return i


# Time complexity is O(n)
def missing_number1(arr, n):
    total = n * (n + 1) // 2
    arr_sum = sum(arr)
    return total - arr_sum


# Time complexity is O(n) because the if i not in arr1 is having complexity of O(1) because we are looking up in the set
def missing_number2(arr, n):
    arr1 = set(arr)
    for i in range(1, n + 1):
        if i not in arr1:
            return i


array = [1, 2, 3, 4, 6, 7, 8, 9, 10]
print(missing_number(array, 10))
print(missing_number1(array, 10))
print(missing_number2(array, 10))


# 2) TWO SUM
def two_sum(arr, val):
    for i in range(len(arr)):
        for j in range(i + 1, len(arr)):
            if arr[i] + arr[j] == val:
                return [i, j]
    return "no such data found"


def two_sum_dict(arr, val):
    seen = {}
    for i, num in enumerate(arr):
        complement = val - num
        if complement in seen:
            return [seen[complement], i]
        seen[num] = i


print(two_sum([2, 6, 3, 9, 11], 22))
print(two_sum_dict([2, 6, 3, 9, 11], 5))


# 3) LINEAR SEARCH
def linear_search(arr, val):
    for i in arr:
        if i == val:
            return "Found"
    return "Not Found"


print(linear_search([2, 6, 3, 9, 11], 11))


# 4) MAX PRODUCT
# (O(n^2))
def max_product(arr):
    largest_product = 0
    for i in range(len(arr)):
        for j in range(i + 1, len(arr)):
            x = arr[i] * arr[j]
            if x > largest_product:
                largest_product = x
    return largest_product


# (O(n))
def max_product1(arr):
    max1 = max2 = 0
    for i in arr:
        if i > max1:
            max2 = max1
            max1 = i
        elif i > max2:
            max2 = i
    return max1 * max2


print(max_product([2, 6, 3, 9, 11]))
print(max_product1([2, 6, 3, 9, 11]))

# Middle Function
# Write a function called middle that takes a list and returns a new list that contains all but the first and last elements.

# myList = [1, 2, 3, 4]
# middle(myList)  # [2,3]


def middle(lst):
    # return lst[1 : len(lst) - 1]
    return lst[1:-1]


print(middle([1, 2, 3, 4]))

# Given 2D list calculate the sum of diagonal elements.

# Example

# myList2D= [[1,2,3],[4,5,6],[7,8,9]]

# diagonal_sum(myList2D) # 15


def diagonal_sum(matrix):
    sum = 0
    for i in range(len(matrix)):
        for j in range(len(matrix[i])):
            if i == j:
                sum += matrix[i][j]
    return sum


def diagonal_sum1(matrix):
    sum = 0
    for i in range(len(matrix)):
        sum += matrix[i][i]
    return sum


print(diagonal_sum([[1, 2, 3, 13], [4, 5, 6, 14], [7, 8, 9, 15], [10, 11, 12, 20]]))
print(diagonal_sum1([[1, 2, 3, 13], [4, 5, 6, 14], [7, 8, 9, 15], [10, 11, 12, 20]]))


# Given a list, write a function to get first, second best scores from the list.

# List may contain duplicates.

# Example

# myList = [84,85,86,87,85,90,85,83,23,45,84,1,2,0]
# first_second(myList) # 90 87


def first_second(my_list):
    first = second = 0
    for i in my_list:
        if i > first:
            second, first = first, i
        elif i > second and i != first:
            second = i
    return first, second


print(first_second([84, 85, 86, 87, 85, 90, 85, 83, 23, 45, 84, 1, 2, 0]))


# Write a function to remove the duplicate numbers on given integer array/list.

# Example

# remove_duplicates([1, 1, 2, 2, 3, 4, 5])
# Output : [1, 2, 3, 4, 5]


def remove_duplicates(arr):
    return list(set(arr))


def remove_duplicates1(arr):
    result = []
    seen = set()
    for i in arr:
        if i not in seen:
            result.append(i)
            seen.add(i)
    return result


print(remove_duplicates([1, 1, 2, 2, 3, 4, 5]))
