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
            new_node.next = new_node.prev = new_node
            self.head = self.tail = new_node
        else:
            new_node.prev = self.tail
            new_node.next = self.head
            self.tail.next = new_node
            self.tail = new_node

    def pop_first(self):
        if self.head is None:
            return None
        elif self.head == self.tail:
            self.head = None
            self.tail = None
        else:
            popped_node = self.head
            self.head.next.prev = self.tail
            self.tail.next = self.head = self.head.next
            popped_node.prev = popped_node.next = None
        self.length -= 1


cd = CDLinkedList()
cd.append(10)
cd.append(20)
cd.append(30)
cd.append(40)
cd.append(50)
print(cd)
cd.pop_first()
print(cd)
