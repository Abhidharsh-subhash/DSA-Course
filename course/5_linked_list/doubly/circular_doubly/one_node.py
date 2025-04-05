class Node:
    def __init__(self, value):
        self.prev = None
        self.value = value
        self.next = None

    def __str__(self):
        return self.value


class CDLinkedList:
    def __init__(self, value):
        new_node = Node(value)
        new_node.prev = new_node
        new_node.next = new_node
        self.head = new_node
        self.tail = new_node
        self.length = 1


cd = CDLinkedList(10)
print(cd.head.value)