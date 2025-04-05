class Node:
    def __init__(self, value):
        self.value = value
        self.prev = None
        self.next = None


class CDLinkedList:
    def __init__(self):
        self.head = self.tail = None
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

    def remove_index_node(self, index):
        if index < 0 or index > self.length - 1:
            return None
        elif index == 0:
            self.head.next.prev = self.tail
            self.tail.next = self.head.next
            self.head = self.head.next
            return
        elif index == self.length - 1:
            self.tail.prev.next = self.head
            self.head.prev = self.tail.prev
            self.tail = self.tail.prev
            return
        else:
            if self.length // 2 < index:
                current = self.tail
                for _ in range((self.length - 1) - index):
                    current = current.prev
            else:
                current = self.head
                for _ in range(index):
                    current = current.next
            popped_node = current
            current.prev.next = current.next
            current.next.prev = current.prev
            popped_node.next = popped_node.prev = None


cd = CDLinkedList()
cd.append(10)
cd.append(20)
cd.append(30)
cd.append(40)
cd.append(50)
cd.append(60)
print(cd)
cd.remove_index_node(2)
print(cd)
