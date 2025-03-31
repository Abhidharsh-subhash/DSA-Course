class Node:
    def __init__(self, value):
        self.prev = None
        self.value = value
        self.next = None


class DLinkedList:
    def __init__(self):
        self.head = self.tail = None
        self.length = 0

    def __str__(self):
        result = ""
        current = self.head
        while current is not None:
            result += str(current.value)
            if current.next is not None:
                result += " <-> "
            current = current.next
        return result

    def append(self, value):
        new_node = Node(value)
        if self.head is None:
            self.head = self.tail = new_node
        else:
            self.tail.next, new_node.prev, self.tail = new_node, self.tail, new_node
        self.length += 1

    def prepend(self, value):
        new_node = Node(value)
        if self.head is None:
            self.head = self.tail = new_node
        else:
            new_node.next, self.head.prev, self.head = self.head, new_node, new_node
        self.length += 1


dll = DLinkedList()
dll.append(10)
dll.append(20)
dll.append(30)
dll.append(40)
dll.append(50)
dll.append(60)
print(dll)
dll.prepend(5)
dll.prepend(3)
print(dll)
