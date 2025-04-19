# def Decimal_to_Binary(n):
#     if n // 2 == 0:
#         return str(1)
#     return Decimal_to_Binary(n // 2) + str(n % 2)


def Decimal_to_Binary(n):
    if n == 0:
        return 0
    else:
        return n % 2 + 10 * Decimal_to_Binary(n // 2)


print(Decimal_to_Binary(10))
