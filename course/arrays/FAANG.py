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

# Write a function to find all pairs of an integer array whose sum is equal to a given number. Do not consider commutative pairs.

# Example

# pair_sum([2, 4, 3, 5, 6, -2, 4, 7, 8, 9],7)
# Output : ['2+5', '4+3', '3+4', '-2+9']


# Note:

# 4+3 comes from second and third elements from the main list.

# 3+4 comes from third and seventh elements from the main list.


# Time complexity O(n)
def pair_sum(myList, sum):
    result = []
    seen = {}
    used = set()
    for i, num in enumerate(myList):
        complement = sum - num
        if complement in seen:
            add = (i, seen[complement])
            if add not in used:
                used.add(add)
                result.append(f"{num} + {complement}")
        seen[num] = i
    return result


print(pair_sum([2, 4, 3, 5, 6, -2, 4, 7, 8, 9], 7))


# Time complexity O(n^2)
def pair_sum1(myList, sum):
    result = []
    for i in range(len(myList)):
        for j in range(i + 1, len(myList)):
            if myList[i] + myList[j] == sum:
                result.append(f"{myList[i]}+{myList[j]}")
    return result


print(pair_sum1([2, 4, 3, 5, 6, -2, 4, 7, 8, 9], 7))


# Given an integer array nums, return true if any value appears at least twice in the array, and return false if every element is distinct.

# Example :

# Input: nums = [1,2,3,1]
# Output: true


def contains_duplicate(nums):
    seen = set()
    for i in nums:
        if i in seen:
            return True
        else:
            seen.add(i)
    return False


print(contains_duplicate([1, 2, 3, 1]))


def permutation(list1, list2):
    if len(list1) != len(list2):
        return False
    list1.sort()
    list2.sort()
    if list1 == list2:
        return True
    else:
        return False


list1 = [1, 2, 3, 4]
list2 = [1, 4, 2, 3]
print(permutation(list1, list2))

# You are given an n x n 2D matrix representing an image, rotate the image by 90 degrees (clockwise).

# You have to rotate the image in-place, which means you have to modify the input 2D matrix directly.

# DO NOT allocate another 2D matrix and do the rotation.

# Example:


# Input: matrix = [[1,2,3],[4,5,6],[7,8,9]]
# Output: [[7,4,1],[8,5,2],[9,6,3]]


def rotate(matrix):
    n = len(matrix)
    for i in range(n):
        for j in range(i, n):
            matrix[i][j], matrix[j][i] = matrix[j][i], matrix[i][j]
    for row in matrix:
        row.reverse()
    return matrix


matrix = [[1, 2, 3], [4, 5, 6], [7, 8, 9]]
print(rotate(matrix))
