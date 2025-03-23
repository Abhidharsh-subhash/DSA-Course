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
        temp = self.head
        result = ""
        while temp is not None:
            result += str(temp.value)
            if temp.next is not None:
                result += "->"
            temp = temp.next
        return result

    def append(self, value):
        new_node = Node(value)
        if self.head is None:
            self.head = self.tail = new_node
        else:
            self.tail.next = self.tail = new_node

    def remove_duplicates(self):
        prev = None
        current = self.head
        seen = set()
        while current is not None:
            if current.value in seen:
                prev.next, current.next = current.next, None
                prev = prev
                current = prev.next
            else:
                seen.add(current.value)
                prev = current
                current = current.next


singly = LinkedList()
singly.append(1)
singly.append(2)
singly.append(3)
singly.append(3)
singly.append(3)
singly.append(4)
singly.append(4)
singly.append(4)
singly.append(4)
print(singly)
singly.remove_duplicates()
print(singly)
