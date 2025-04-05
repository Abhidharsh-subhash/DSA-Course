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
            self.tail = self.head = new_node
        else:
            new_node.prev = self.tail
            new_node.next = self.head
            self.tail.next = new_node
            self.tail = new_node
        self.length += 1

    def pop(self):
        if self.head is None:
            return None
        elif self.length == 1:
            self.head = None
            self.tail = None
        else:
            popped_node = self.tail
            self.tail.prev.next = self.head
            self.head.prev = self.tail.prev
            self.tail = self.tail.prev
            popped_node.next = popped_node.prev = None


cd = CDLinkedList()
cd.append(10)
cd.append(20)
cd.append(30)
cd.append(40)
cd.append(50)
print(cd)
cd.pop()
cd.pop()
print(cd)
