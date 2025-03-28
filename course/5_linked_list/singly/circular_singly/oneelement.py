class Node:
    def __init__(self, value):
        self.value = value
        self.next = None


class CSLinkedList:
    def __init__(self, value):
        new_node = Node(value)
        new_node.next = new_node
        self.head = self.tail = new_node
        self.length = 1


CS = CSLinkedList(10)
print(CS.head.value)
