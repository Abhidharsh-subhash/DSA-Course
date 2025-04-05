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
            self.head.prev = new_node
        self.length += 1

    def update_index_value(self, index, value):
        if index < 0 or index > self.length - 1:
            return None
        elif index == 0:
            self.head.value = value
        elif index == self.length - 1:
            self.tail.value = value
        if self.length // 2 < index:
            current = self.tail
            for _ in range((self.length - 1) - index):
                current = current.prev
            current.value = value
        else:
            current = self.head
            for _ in range(index):
                current = current.next
            current.value = value


cd = CDLinkedList()
cd.append(10)
cd.append(20)
cd.append(30)
cd.append(40)
print(cd)
cd.update_index_value(3, 35)
print(cd)
