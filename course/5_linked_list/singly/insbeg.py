class Node:
    def __init__(self, value):
        self.value, self.next = value, None


class LinkedList:
    def __init__(self):
        self.head = self.tail = None
        self.length = 0

    def __str__(self):
        temp_node = self.head
        result = ""
        while temp_node is not None:
            result += str(temp_node.value)
            if temp_node.next is not None:
                result += "->"
            temp_node = temp_node.next
        return result

    def append(self, value):
        new_node = Node(value)
        if self.head is None:
            self.head = self.tail = new_node
        else:
            self.tail.next = self.tail = new_node
        self.length += 1

    def insert_first(self, value):
        new_node = Node(value)
        if self.head is not None:
            self.head, new_node.next = new_node, self.head
        else:
            self.head = self.tail = new_node
        self.length += 1


singly = LinkedList()
singly.append(10)
singly.append(20)
singly.append(30)
singly.append(40)
singly.append(50)
print(singly)
print(singly.length)
print("inserting at the beginning")
singly.insert_first(100)
print(singly)
singly.insert_first(1000)
print(singly)
print(singly.length)
