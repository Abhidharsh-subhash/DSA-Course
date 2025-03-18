class Node:
    def __init__(self, value):
        self.value = value
        self.next = None
        self.length = 0


class LinkedList:
    def __init__(self):
        self.head = None
        self.tail = None
        self.length = 0

    def append(self, value):
        new_node = Node(value)
        if self.head is None:
            self.head = self.tail = new_node
        else:
            self.tail.next = self.tail = new_node
        self.length += 1

    def __str__(self):
        temp = self.head
        result = ""
        while temp is not None:
            result += str(temp.value)
            if temp.next is not None:
                result += "->"
            temp = temp.next
        return result

    def pop_first(self):
        if self.head is None:
            print("linkedlist is empty")
            return
        elif self.length == 1:
            self.head = self.tail = None
        else:
            self.head = self.head.next
        self.length -= 1


singly = LinkedList()
singly.append(10)
singly.append(99)
singly.append(11)
singly.append(89)
singly.append(67)
print(singly)
print(singly.length)
singly.pop_first()
print(singly)
print(singly.length)
