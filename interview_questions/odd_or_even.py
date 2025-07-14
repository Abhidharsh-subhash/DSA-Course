def OddOrEven(num):
    result = ("even", "odd")
    return result[num % 2]


print(OddOrEven(11))
