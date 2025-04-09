# Write a function to remove duplicates from an unsorted linked list. Input 1 -> 2 -> 2 -> 3 -> 4 -> 4 -> 4 -> 5 Output 1 -> 2 -> 3 -> 4 -> 5
from base import LinkedList

test = LinkedList()
test.add(1)
test.add(2)
test.add(2)
test.add(3)
test.add(4)
test.add(4)
test.add(4)
test.add(5)
print(len(test))
print(test)


def remove_duplicates(ll):
    prev = None
    current = ll.head
    seen = set()
    while current:
        if current.value in seen:
            prev.next, current.next = current.next, None
            current = prev.next
        else:
            seen.add(current.value)
            prev = current
            current = current.next
    return ll


print(remove_duplicates(test))
