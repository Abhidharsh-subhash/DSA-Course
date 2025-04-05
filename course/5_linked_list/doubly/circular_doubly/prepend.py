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

    def __str__(self):
        result = ""
        current = self.head
        while current:
            result += str(current.value)
            if current.next == self.head:
                break
            result += "<->"
            current = current.next
        return result

    def append(self, value):
        new_node = Node(value)
        if self.head is None:
            self.head = self.tail = new_node
            new_node.next = new_node.prev = new_node
        else:
            self.tail.next = new_node
            new_node.prev = self.tail
            new_node.next = self.head
            self.head.prev = new_node
            self.tail = new_node

    def prepend(self, value):
        new_node = Node(value)
        if self.head is None:
            self.head = self.tail = new_node
            new_node.next = new_node.prev = new_node
        else:
            new_node.next = self.head
            new_node.prev = self.tail
            self.head.prev = self.tail.next = new_node
            self.head = new_node
        self.length += 1


cd = CDLinkedList()
cd.prepend(5)
cd.prepend(3)
cd.append(10)
cd.append(20)
cd.append(30)
cd.append(40)
cd.prepend(1)
print(cd)
