class Node:
    def __init__(self, value):
        self.value = value
        self.next = None


class CircularLinkedList:
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
            current = current.next
            result += " -> "
        return result

    def append(self, value):
        new_node = Node(value)
        if self.head is None:
            self.head = self.tail = new_node.next = new_node
        else:
            self.tail.next, new_node.next, self.tail = new_node, self.head, new_node
        self.length += 1

    def is_sorted(self):
        if self.head is None:
            return None
        prev = self.head
        current = self.head.next
        while current:
            if current == self.head:
                break
            elif prev.value > current.value:
                return False
            prev = current
            current = current.next
        return True


CS = CircularLinkedList()
CS.append(10)
CS.append(20)
CS.append(30)
CS.append(40)
CS.append(50)
CS.append(60)
CS.append(70)
CS.append(66)
print(CS)
print(CS.is_sorted())
