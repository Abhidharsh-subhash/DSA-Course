class Node:
    def __init__(self, value):
        self.value = value
        self.next = None


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

    def update_at_index(self, index, value):
        temp = self.head
        if index > self.length - 1 or index < 0:
            print("worng index")
            return
        elif index == 0:
            temp.value = value
        else:
            for _ in range(index):
                temp = temp.next
            temp.value = value
            print("updated")


singly = LinkedList()
singly.append(10)
singly.append(99)
singly.append(11)
singly.append(89)
singly.append(67)
print(singly)
print(singly.length)
singly.update_at_index(2, 12)
print(singly)
