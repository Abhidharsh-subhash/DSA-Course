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
            current = current.next
            if current == self.head:
                break
            result += "->"
        return result

    def append(self, value):
        new_node = Node(value)
        if self.head is None:
            self.head = self.tail = new_node.next = new_node
        else:
            self.tail.next, new_node.next, self.tail = new_node, self.head, new_node
        self.length += 1

    def insert_at_index(self, value, index):
        if index <= self.length:
            new_node = Node(value)
            if index == 0:
                new_node.next, self.head, self.tail.next = self.head, new_node, new_node
            else:
                current = self.head
                for _ in range(index - 1):
                    current = current.next
                new_node.next, current.next = current.next, new_node
            self.length += 1
        else:
            print("wrong index")


CS = CSLinkedlist()
CS.append(10)
CS.append(20)
CS.append(30)
CS.append(40)
CS.append(50)
print(CS)
CS.insert_at_index(100, 0)
print(CS)
print(CS.length)
CS.insert_at_index(200, 5)
print(CS)
