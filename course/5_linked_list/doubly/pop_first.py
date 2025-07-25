class Node:
    def __init__(self, value):
        self.prev = None
        self.value = value
        self.next = None


class DLinkedList:
    def __init__(self):
        self.head = None
        self.tail = None
        self.length = 0

    def __str__(self):
        result = ""
        current = self.head
        while current:
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
            new_node.prev, self.tail.next, self.tail = self.tail, new_node, new_node
        self.length += 1

    def pop_first(self):
        if self.head is None:
            return None
        elif self.length == 1:
            self.head = None
            self.tail = None
        else:
            self.head, self.head.next.prev = self.head.next, None
            self.length -= 1


dll = DLinkedList()
dll.append(10)
dll.append(20)
dll.append(30)
dll.append(40)
dll.append(50)
dll.append(60)
print(dll)
dll.pop_first()
print(dll)
