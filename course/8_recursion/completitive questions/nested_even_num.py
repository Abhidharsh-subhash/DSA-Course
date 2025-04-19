# Write a recursive function called nestedEvenSum. Return the sum of all even numbers in an object which may contain nested objects.

# Examples

# obj1 = {
#   "outer": 2,
#   "obj": {
#     "inner": 2,
#     "otherObj": {
#       "superInner": 2,
#       "notANumber": True,
#       "alsoNotANumber": "yup"
#     }
#   }
# }

# obj2 = {
#   "a": 2,
#   "b": {"b": 2, "bb": {"b": 3, "bb": {"b": 2}}},
#   "c": {"c": {"c": 2}, "cc": 'ball', "ccc": 5},
#   "d": 1,
#   "e": {"e": {"e": 2}, "ee": 'car'}
# }

# nestedEvenSum(obj1) # 6
# nestedEvenSum(obj2) # 10


def nestedEvenSum(obj, sum=0):
    for key in obj:
        value = obj[key]
        if isinstance(value, dict):
            sum += nestedEvenSum(value)
        elif isinstance(value, int) and not isinstance(value, bool) and value % 2 == 0:
            sum += value
    return sum


obj1 = {
    "outer": 2,
    "obj": {
        "inner": 2,
        "otherObj": {"superInner": 2, "notANumber": True, "alsoNotANumber": "yup"},
    },
}

obj2 = {
    "a": 2,
    "b": {"b": 2, "bb": {"b": 3, "bb": {"b": 2}}},
    "c": {"c": {"c": 2}, "cc": "ball", "ccc": 5},
    "d": 1,
    "e": {"e": {"e": 2}, "ee": "car"},
}
print(nestedEvenSum(obj1))
