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
        current = self.head
        result = ""
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
            new_node.prev = new_node.next = new_node
            self.head = self.tail = new_node
        else:
            new_node.next = self.head
            new_node.prev = self.tail
            self.tail.next = new_node
            self.head.prev = new_node
            self.tail = new_node
        self.length += 1

    def reverse_traversal(self):
        current = self.tail
        while current:
            print(current.value, end=" ")
            if current.prev == self.tail:
                break
            current = current.prev
        print("\n")


cd = CDLinkedList()
cd.append(10)
cd.append(20)
cd.append(30)
cd.append(40)
print(cd)
cd.reverse_traversal()
