class Node:
    def __init__(self, value):
        self.value = value
        self.next = None


class CSLinkedlist:
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
            else:
                result += "->"
                current = current.next
        return result

    def append(self, value):
        new_node = Node(value)
        if self.head is None:
            self.head = self.tail = new_node
            new_node.next = new_node
        else:
            self.tail.next, new_node.next = new_node, self.head
            self.tail = new_node
        self.length += 1

    def prepend(self, value):
        new_node = Node(value)
        if self.head is None:
            self.head = self.tail = new_node.next = new_node
        else:
            new_node.next, self.head, self.tail.next = self.head, new_node, new_node
        self.length += 1


CS = CSLinkedlist()
CS.append(10)
CS.append(20)
print(CS)
CS.prepend(30)
print(CS)
CS.append(40)
CS.append(50)
print(CS)
CS.prepend(100)
print(CS)
