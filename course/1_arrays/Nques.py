# Fibanocci series
def fibanocci(n):
    a, b = 0, 1
    for i in range(n):
        print(a, end=" ")
        a, b = b, a + b
    print("\n")


fibanocci(10)
