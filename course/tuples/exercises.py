# 1) Write a function that calculates the sum and product of all elements in a tuple of numbers.
def sum_product(input_tuple):
    total = 0
    product = 1
    for i in input_tuple:
        total += i
        product *= i
    return total, product


input_tuple = (1, 2, 3, 4)
print(sum_product(input_tuple))


# 2)Create a function that takes two tuples and returns a tuple containing the element-wise sum of the input tuples.
def tuple_elementwise_sum(tuple1, tuple2):
    # result = []
    # for i in range(len(tuple1)):
    #     result.append(tuple1[i] + tuple2[i])
    # return tuple(result)
    # return tuple(map(sum, zip(tuple1, tuple2)))
    result = tuple(a + b for a, b in zip(tuple1, tuple2))
    return result


tuple1 = (1, 2, 3)
tuple2 = (4, 5, 6)
print(tuple_elementwise_sum(tuple1, tuple2))


# 3) Write a function that takes a tuple and a value, and returns a new tuple with the value inserted at the beginning of the original tuple.
def insert_value_front(input_tuple, value_to_insert):
    result = (value_to_insert,) + input_tuple
    return result


input_tuple = (2, 3, 4)
value_to_insert = 1
print(insert_value_front(input_tuple, value_to_insert))


# 4)Write a function that takes a tuple of strings and concatenates them, separating each string with a space.
def concatenate_strings(input_tuple):
    # result = ""
    # for i in range(len(input_tuple)):
    #     if i == 0:
    #         result += input_tuple[i]
    #     else:
    #         result += f" {input_tuple[i]}"
    # return result
    return " ".join(input_tuple)


input_tuple = ("Hello", "World", "from", "Python")
print(concatenate_strings(input_tuple))


# 5)Create a function that takes a tuple of tuples and returns a tuple containing the diagonal elements of the input.
def get_diagonal(input_tuple):
    # result = []
    # for i in range(len(input_tuple)):
    #     for j in range(len(input_tuple[i])):
    #         if i == j:
    #             result.append(input_tuple[i][j])
    # return tuple(result)
    return tuple(input_tuple[i][i] for i in range(len(input_tuple)))


input_tuple = ((1, 2, 3), (4, 5, 6), (7, 8, 9))
output_tuple = get_diagonal(input_tuple)
print(output_tuple)


# 6)Write a function that takes two tuples and returns a tuple containing the common elements of the input tuples.
def common_elements(tuple1, tuple2):
    # result = []
    # for i in tuple1:
    #     if i in tuple2:
    #         result.append(i)
    # return tuple(result)
    # return tuple(i for i in tuple1 if i in tuple2)
    return tuple(set(tuple1) & set(tuple2))


tuple1 = (1, 2, 3, 4, 5)
tuple2 = (4, 5, 6, 7, 8)
output_tuple = common_elements(tuple1, tuple2)
print(output_tuple)
