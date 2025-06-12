def count_word_frequency(words):
    x = {}
    for i in words:
        x[i] = x.get(i, 0) + 1
    print(x)


words = ["apple", "orange", "banana", "apple", "orange", "apple"]
count_word_frequency(words)


def merge_dicts(dict1, dict2):
    # result = {}
    # for i in dict1:
    #     result[i] = dict1[i]
    #     if i in dict2:
    #         result[i] += dict2[i]
    # for j in dict2:
    #     if j not in result:
    #         result[j] = dict2[j]
    result = dict1.copy()
    for key, value in dict2.items():
        result[key] = result.get(key, 0) + value
    print(result)


dict1 = {"a": 1, "b": 2, "c": 3, "e": 6}
dict2 = {"b": 3, "c": 4, "d": 5}
merge_dicts(dict1, dict2)


def max_value_key(my_dict):
    # result = ""
    # highest = 0
    # for key, value in my_dict.items():
    #     if value > highest:
    #         highest = value
    #         result = key
    # print(result)
    print(max(my_dict, key=my_dict.get))


my_dict = {"a": 5, "b": 9, "c": 2}
max_value_key(my_dict)


def reverse_dict(my_dict):
    # result = {}
    # for i in my_dict:
    #     result[my_dict[i]] = i
    # print(result)
    print({v: k for k, v in my_dict.items()})


my_dict = {"a": 1, "b": 2, "c": 3}
reverse_dict(my_dict)


def filter_dict(my_dict, condition):
    print({k: v for k, v in my_dict.items() if condition(k, v)})


my_dict = {"a": 1, "b": 2, "c": 3, "d": 4}
filtered_dict = filter_dict(my_dict, lambda k, v: v % 2 == 0)


def check_same_frequency(list1, list2):
    result1 = {}
    result2 = {}
    for i in range(len(list1)):
        result1[list1[i]] = result1.get(list1[i], 0) + 1
        result2[list2[i]] = result2.get(list2[i], 0) + 1
    print(True) if result1 == result2 else print(False)


list1 = [1, 2, 3, 3, 1]
list2 = [3, 1, 2, 1, 3]
check_same_frequency(list1, list2)
