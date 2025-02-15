# Update/Insert
myList = [1, 2, 3, 4, 5, 6, 7]
print(myList)
myList.insert(3, 100)
print(myList)
myList.append(200)
print(myList)
myList1 = [150, 250, 350]
myList.extend(myList1)
print(myList)


# Slicing and deleting
print("slicing")
mylist = ["a", "b", "c", "d", "e", "f", "g", "h"]
print(mylist[:2])
mylist[1:3] = ["x", "y"]
print(mylist)
print("deletion")
mylist.pop(2)
print(mylist)
del mylist[1:4]
print(mylist)
mylist.remove("g")
print(mylist)

# searching
x = [1, 2, 3, 4, 5, 6, 7, 8, 9, 0]
print("in method")
target = 33
if target in x:
    print("found")
else:
    print("not found")

print("linear search method")


def search(array, targ):
    for i, value in enumerate(array):
        if value == targ:
            return f"value {targ} found at index {i}"
    return "searching failed"


print(search(x, 10))

# List comprehension
new_list = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
double = [2 * i for i in new_list]
print(double)
odd = [i for i in new_list if i % 2 == 1 and i < 8]
print(odd)
replace = [i if i % 2 == 0 else 0 for i in new_list]
print(replace)


def div(x):
    return True if x % 1.5 == 0 else False


fun = [i for i in new_list if div(i)]
print(fun)
