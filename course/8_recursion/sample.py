def RecursiveMethod(n):
    if n <= 0:
        print("n is less than 1")
    else:
        RecursiveMethod(n - 1)
        print(n)


RecursiveMethod(4)
