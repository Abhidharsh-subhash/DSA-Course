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
            self.head.prev = new_node
            self.tail.next = new_node
            self.tail = new_node
        self.length += 1

    def set_at_index(self, index, value):
        if index < 0 or index > self.length - 1:
            return None
        new_node = Node(value)
        if index == 0:
            new_node.next = self.head
            new_node.prev = self.tail
            self.head.prev = new_node
            self.tail.next = new_node
            self.head = new_node
            return
        elif index == self.length - 1:
            new_node.prev = self.tail
            new_node.next = self.head
            self.tail.next = new_node
            self.tail = new_node
            self.head.prev = new_node
            return
        if self.length // 2 < index:
            current = self.tail
            for _ in range((self.length - 1) - index):
                current = current.prev
        else:
            current = self.head
            for _ in range(index):
                current = current.next
        new_node.prev = current.prev
        new_node.next = current
        current.prev.next = new_node
        current.prev = new_node
        self.length += 1


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
cd.append(110)
cd.append(120)
cd.append(130)
cd.append(140)
cd.append(150)
print(cd)
cd.set_at_index(11, 115)
print(cd.length)
print(cd)
