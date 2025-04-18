# def fibanocci(n):
#     result = []
#     a, b = 0, 1
#     result.append(a)
#     while b < n:
#         result.append(b)
#         a, b = b, a + b
#     return result


# print(fibanocci(100))


# this method will give back the number in the position n in fibanocci series
def fibanocci(n):
    if n <= 1:
        return n
    else:
        return fibanocci(n - 1) + fibanocci(n - 2)


print(fibanocci(10))
