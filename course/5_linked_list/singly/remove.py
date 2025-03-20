class Node:
    def __init__(self, value):
        self.value = value
        self.next = None


class LinkedList:
    def __init__(self):
        self.head = None
        self.tail = None
        self.length = 1

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
        self.length += 1

    def remove(self, index):
        if index >= self.length or index < 0:
            print("index out of range")
        elif index == 0:
            self.head = self.head.next
        else:
            pop_node = self.head
            previous_node = None
            for _ in range(index):
                previous_node = pop_node
                pop_node = pop_node.next
            previous_node.next = pop_node.next
            # To denote the garbage collector that this is unused
            pop_node.next = None


singly = LinkedList()
singly.append(10)
singly.append(99)
singly.append(11)
singly.append(89)
singly.append(67)
print(singly)
singly.remove(2)
print(singly)
