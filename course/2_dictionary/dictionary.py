my_dict = dict()
print(my_dict)

eng_sp = dict(one="uno", two="duo", three="tres")
print(eng_sp)

num_wor = {"one": 1, "two": 2, "three": 3}
print(num_wor)

listtup = [("key1", "value1"), ("key2", "value2"), ("key3", "value3")]
list_tup = dict(listtup)
print(list_tup)


def traverse(dictionary):
    for i in dictionary:
        print(i, dictionary[i])


traverse(list_tup)


def searchdict(dictionary, value):
    for key in dictionary:
        if dictionary[key] == value:
            return key, value
    return "not found"


print(searchdict(list_tup, "value"))


# Deletion
dict_sam = {"one": 1, "two": 2, "three": 3}
# del dict_sam["two"]
# removed_element = dict_sam.pop("three", None)
# removed_element = dict_sam.popitem()
dict_sam.clear()
print(dict_sam)
