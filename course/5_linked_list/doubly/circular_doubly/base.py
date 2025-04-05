class Node:
    def __init__(self, value):
        self.prev = None
        self.value = value
        self.next = None


class CDLinkedList:
    def __init__(self):
        self.head = None
        self.tail = None
        self.length = 0
