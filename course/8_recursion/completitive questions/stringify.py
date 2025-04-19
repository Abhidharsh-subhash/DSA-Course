# stringifyNumbers
# Write a function called stringifyNumbers which takes in an object and finds all of the values which are numbers and converts them to strings. Recursion would be a great way to solve this!

# Examples

# obj = {
#   "num": 1,
#   "test": [],
#   "data": {
#     "val": 4,
#     "info": {
#       "isRight": True,
#       "random": 66
#     }
#   }
# }

# stringifyNumbers(obj)

# {'num': '1',
#  'test': [],
#  'data': {'val': '4',
#           'info': {'isRight': True, 'random': '66'}
#           }
# }


def stringifyNumbers(obj):
    for key in obj:
        value = obj[key]
        if isinstance(value, dict):
            stringifyNumbers(value)
        elif isinstance(value, int) and not isinstance(value, bool):
            obj[key] = str(value)
    return obj


obj = {
    "num": 1,
    "test": [],
    "data": {"val": 4, "info": {"isRight": True, "random": 66}},
}
print(stringifyNumbers(obj))
