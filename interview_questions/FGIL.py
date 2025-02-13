# Sum of digits of a number using recursion
def sum_of_digits(num: int):
    if num == 0:
        return 0
    else:
        return num % 10 + sum_of_digits(num // 10)


print(sum_of_digits(12345))


# Bubble sort
