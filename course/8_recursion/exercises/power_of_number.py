def power(base, exp):
    if exp <= 1:
        return base
    return base * power(base, exp - 1)


print(power(3, 4))
