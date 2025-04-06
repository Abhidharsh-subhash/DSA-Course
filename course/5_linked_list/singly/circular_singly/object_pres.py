class Node:
    def __init__(self, value):
        self.value = value
        self.next = None


class CSLinkedlist:
    def __init__(self):
        self.head = None
        self.tail = None
        self.length = 0

    def append(self, value):
        new_node = Node(value)
        if self.head is None:
            self.head = new_node
            self.tail = new_node
            new_node.next = new_node
        else:
            new_node.next, self.tail.next = self.head, new_node
            self.tail = new_node
        self.length += 1

    def __str__(self):
        result = ""
        current = self.head
        while current.next:
            result += str(current.value)
            if current.next == self.head:
                break
            result += "->"
            current = current.next
        return result


CS = CSLinkedlist()
CS.append(10)
CS.append(20)
CS.append(30)
CS.append(40)
CS.append(50)
print(CS)
