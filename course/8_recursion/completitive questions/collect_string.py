# collectStrings
# Write a function called collectStrings which accepts an object and returns an array of all the values in the object that have a typeof string.

# Examples

# obj = {
#   "stuff": 'foo',
#   "data": {
#     "val": {
#       "thing": {
#         "info": 'bar',
#         "moreInfo": {
#           "evenMoreInfo": {
#             "weMadeIt": 'baz'
#           }
#         }
#       }
#     }
#   }
# }

# collectStrings(obj) # ['foo', 'bar', 'baz']


def collectStrings(obj):
    result = []
    for key in obj:
        value = obj[key]
        if isinstance(value, dict):
            result += collectStrings(value)
        elif isinstance(value, str):
            result.append(value)
    return result


obj = {
    "stuff": "foo",
    "data": {
        "val": {
            "thing": {"info": "bar", "moreInfo": {"evenMoreInfo": {"weMadeIt": "baz"}}}
        }
    },
}

print(collectStrings(obj))
