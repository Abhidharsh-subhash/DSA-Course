# def greatest_common_divisor(num1, num2):
#     divisor = 1
#     for i in range(2, (min(num1, num2))):
#         if num1 % i == 0 and num2 % i == 0:
#             divisor = i
#     return divisor


# this is the implementation if Eucledian algorithm


def greatest_common_divisor(num1, num2):
    large = max(num1, num2)
    small = min(num1, num2)
    reminder = large % small
    if reminder == 0:
        return small
    return greatest_common_divisor(small, reminder)


print(greatest_common_divisor(48, 18))
