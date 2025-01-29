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
def misssing_number1(arr, n):
    arr1 = set(arr)
    for i in range(1, n + 1):
        if i not in arr1:
            return i


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
print(two_sum_dict([2, 6, 3, 9, 11], 20))


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
