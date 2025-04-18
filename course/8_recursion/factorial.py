# setting up the recursion limit externally for this function
# import sys
# sys.setrecursionlimit(1000)


def factorial(n: int):
    if n <= 1:
        return 1
    else:
        return n * factorial(n - 1)


print(factorial('a'))
