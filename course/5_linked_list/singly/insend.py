class Node:
    def __init__(self, value):
        self.value = value
        self.next = None


class LinkedList:
    def __init__(self):
        self.head = None
        self.tail = None
        self.length = 0

    def append(self, value):
        new_node = Node(value)
        if self.head is None:
            self.head = new_node
            self.tail = new_node
        else:
            self.tail.next = new_node
            self.tail = new_node
        self.length += 1


singly = LinkedList()
singly.append(10)
singly.append(11)
singly.append(12)
print(singly.length)


# The time and space complexity for inserting an element to the end of the linkedlist is O(1)
