# Write a recursive function called reverse which accepts a string and returns a new string in reverse.

# Examples

# reverse('python') # 'nohtyp'
# reverse('appmillers') # 'srellimppa'


def reverse(strng):
    length = len(strng)
    if length == 1:
        return strng
    return strng[-1] + reverse(strng[: length - 1])


print(reverse("appmillers"))
