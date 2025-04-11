from base import LinkedList


def intersection(ll1, ll2):
    length1 = len(ll1)
    length2 = len(ll2)
    greater = length1 if length1 > length2 else length2
    if greater == length1:
        ll1 = ll1
        ll2 = ll2
        diff = length1 - length2
    else:
        ll1 = ll2
        ll2 = ll1
        diff = length2 - length1
    start = ll1.head
    for _ in range(diff):
        start = start.next
    ll1_current = start
    ll2_current = ll2.head
    while ll1_current and ll2_current:
        if ll1_current.value == ll2_current.value:
            return ll2_current.value
        ll2_current = ll2_current.next
        ll1_current = ll1_current.next
    return "no intersection found"


ll1 = LinkedList()
ll1.add(3)
ll1.add(1)
ll1.add(5)
ll1.add(9)
ll1.add(7)
ll1.add(2)
ll1.add(1)
ll2 = LinkedList()
ll2.add(2)
ll2.add(4)
ll2.add(6)
ll2.add(7)
ll2.add(2)
ll2.add(1)
print(ll1)
print(ll2)
print(intersection(ll1, ll2))
