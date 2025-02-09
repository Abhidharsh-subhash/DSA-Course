newTuple = ("a", "b", "c", "d")
print(newTuple)
print(newTuple[3])
print(newTuple[-2])

print("traversing")
for i in newTuple:
    print(i)

print("search")
print("c" in newTuple)
print(newTuple.index("c"))
# def search(tup, val):
#     for i in tup:
#         if i == val:
#             return "found"
#     return "not found"
# print(search(newTuple, "e"))

myTuple1 = ("e", "f", "g", "h")
print(newTuple + myTuple1)
print(myTuple1 * 2)
print(myTuple1.count("f"))
print(max(myTuple1))
print(min(myTuple1))
