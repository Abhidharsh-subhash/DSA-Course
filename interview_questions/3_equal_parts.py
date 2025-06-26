def partition(number, count):
    result_dict = {}
    for i in range(count):
        result_dict[f"x{i+1}"] = 0
    reminder = number % count
    quotient = number // count
    result_dict = {key: quotient for key in result_dict}
    if reminder == 0:
        result = result_dict.values()
    else:
        j = 1
        while reminder > 0:
            result_dict[f"x{j}"] += 1
            reminder -= 1
        result = result_dict.values()
    return result


def partition1(number, count):
    quotient, remainder = divmod(number, count)
    result_dict = {
        f"x{i+1}": quotient + (1 if i < remainder else 0) for i in range(count)
    }
    return result_dict.values()


print(partition1(13, 3))
