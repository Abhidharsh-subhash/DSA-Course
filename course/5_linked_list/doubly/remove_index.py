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
                result += " -> "
            current = current.next
        return result

    def append(self, value):
        new_node = Node(value)
        if self.head is None:
            self.head = self.tail = new_node
        else:
            self.tail.next, new_node.prev, self.tail = new_node, self.tail, new_node
        self.length += 1

    def remove_index_value(self, index):
        if self.head is None:
            return None
        elif index > self.length - 1:
            return None
        elif index == 0:
            popped_node = self.head
            popped_node.next.prev, self.head = None, popped_node.next
        elif index < self.length // 2:
            current = self.head
            for _ in range(index):
                current = current.next
            popped_node = current
            current.prev.next, current.next.prev = popped_node.next, popped_node.prev
            self.length -= 1
        else:
            current = self.tail
            for _ in range((self.length - 1) - index):
                current = current.prev
            popped_node = current
            current.prev.next, current.next.prev = popped_node.next, popped_node.prev
            self.length -= 1


dll = DLinkedList()
dll.append(10)
dll.append(20)
dll.append(30)
dll.append(40)
dll.append(50)
dll.append(60)
print(dll)
dll.remove_index_value(0)
print(dll)
dll.remove_index_value(3)
print(dll)
