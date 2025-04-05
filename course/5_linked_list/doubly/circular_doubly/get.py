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
            new_node.next = self.head
            new_node.prev = self.tail
            self.tail.next = new_node
            self.head.prev = new_node
            self.tail = new_node
        self.length += 1

    def get_index_value(self, index):
        if index < 0 or index > self.length - 1:
            return None
        if (self.length // 2) < index:
            current = self.tail
            for _ in range((self.length - 1) - index):
                current = current.prev
            return current.value
        else:
            current = self.head
            for _ in range(index):
                current = current.next
            return current.value


cd = CDLinkedList()
cd.append(10)
cd.append(20)
cd.append(30)
cd.append(40)
cd.append(50)
cd.append(60)
cd.append(70)
cd.append(80)
cd.append(90)
cd.append(100)
cd.append(120)
cd.append(130)
cd.append(140)
print(cd)
print(cd.get_index_value(0))
