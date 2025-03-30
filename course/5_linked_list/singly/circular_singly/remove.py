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
            self.tail.next, new_node.next, self.tail = new_node, self.head, new_node
        self.length += 1

    def remove(self, value):
        if self.head.value == value:
            popped_node = self.head
            self.tail.next = self.head = self.head.next
            popped_node.next = None
            return True
        else:
            prev = None
            current = self.head
            while current:
                if current.value == value:
                    prev.next = current.next
                    current.next = None
                    return True
                elif current.next == self.head:
                    break
                prev = current
                current = current.next
            return False

    def delete_by_value(self, value):
        if self.head is None:
            return False
        elif self.head.value == value:
            self.tail.next = self.head = self.head.next
            self.length -= 1
            return True
        else:
            prev = None
            current = self.head
            while current:
                if current.value == value:
                    prev.next = current.next
                    self.length -= 1
                    return True
                elif current.next == self.head:
                    break
                prev = current
                current = current.next
            return False


CS = CSLinkedlist()
CS.append(10)
CS.append(20)
CS.append(30)
CS.append(40)
CS.append(50)
CS.append(60)
CS.append(70)
print(CS)
# print(CS.remove(10))
# print(CS)
print(CS.remove(70))
print(CS)
