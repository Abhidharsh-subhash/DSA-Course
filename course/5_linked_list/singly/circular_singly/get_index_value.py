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
            result += "->"
            current = current.next
        return result

    def append(self, value):
        new_node = Node(value)
        if self.head is None:
            self.head = self.tail = new_node.next = new_node
        else:
            self.tail.next, self.tail, new_node.next = new_node, new_node, self.head
        self.length += 1

    def get_index_value(self, index):
        if index >= self.length or index < 0:
            return "wrong index"
        current = self.head
        for _ in range(index):
            current = current.next
        return current.value


CS = CSLinkedlist()
CS.append(10)
CS.append(20)
CS.append(30)
CS.append(40)
CS.append(50)
CS.append(60)
CS.append(70)
print(CS)
print(CS.get_index_value(7))
