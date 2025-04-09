# Find the kth element from the last
from base import LinkedList

test = LinkedList()
test.add(1)
test.add(2)
test.add(3)
test.add(4)
test.add(5)
test.add(6)
test.add(7)
test.add(8)
print(test)


def find_kth_from_last(ll, k):
    index = len(ll) - k
    current = ll.head
    for i in range(index):
        current = current.next
    return current.value


print(find_kth_from_last(test, 2))
