def reverse_num(num: int):
    result = 0
    while num:
        rem = num % 10
        result = result * 10 + rem
        num = num // 10
    return result


print(reverse_num(1234))
