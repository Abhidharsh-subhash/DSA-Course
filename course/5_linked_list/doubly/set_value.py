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
            self.tail.next, new_node.prev, self.tail = new_node, self.tail, new_node
        self.length += 1

    def set(self, index, value):
        new_node = Node(value)
        if index > self.length - 1 or index < 0:
            return None
        if index == 0:
            new_node.next, self.head.prev, self.head = self.head, new_node, new_node
        elif index < self.length // 2:
            current = self.head
            for _ in range(index):
                current = current.next
            new_node.prev, new_node.next, current.prev.next = (
                current.prev,
                current,
                new_node,
            )
        else:
            current = self.tail
            for _ in range((self.length - 1) - index):
                current = current.prev
            new_node.prev, new_node.next, current.prev.next = (
                current.prev,
                current,
                new_node,
            )


dll = DLinkedList()
dll.append(10)
dll.append(20)
dll.append(30)
dll.append(40)
dll.append(50)
dll.append(60)
print(dll)
dll.set(3, 35)
dll.set(0, 5)
dll.set(5, 55)
print(dll)
