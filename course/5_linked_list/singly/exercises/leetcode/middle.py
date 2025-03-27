class Node:
    def __init__(self, value):
        self.value = value
        self.next = None


class LinkedList:
    def __init__(self):
        self.head = None
        self.tail = None
        self.length = 0

    def __str__(self):
        current = self.head
        result = ""
        while current is not None:
            result += str(current.value)
            if current.next is not None:
                result += "->"
            current = current.next
        return result

    def append(self, value):
        new_node = Node(value)
        if self.head is None:
            self.head = self.tail = new_node
        else:
            self.tail.next = self.tail = new_node
        self.length += 1

    def find_middle(self):
        slow = self.head
        fast = self.head
        while fast and fast.next:
            slow = slow.next
            fast = fast.next.next
        return slow.value


singly = LinkedList()
singly.append(1)
singly.append(2)
singly.append(3)
singly.append(4)
singly.append(5)
singly.append(6)
print(singly)
print(singly.find_middle())
