from base import LinkedList


def partition(ll, value):
    result_ll = LinkedList()
    current = ll.head
    while current:
        if current.value < value:
            result_ll.add_at_start(current.value)
        else:
            result_ll.add(current.value)
        current = current.next
    return result_ll


ll = LinkedList()
ll.add(10)
ll.add(20)
ll.add(30)
ll.add(40)
ll.add(50)
ll.add(60)
ll.add(70)
ll.add(80)
ll.add(90)
ll.add(100)
print(ll)
print(partition(ll, 50))
