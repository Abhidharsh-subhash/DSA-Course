class Node:
    def __init__(self, value):
        self.value = value
        self.next = None


class LinkedList:
    def __init__(self):
        self.head = None
        self.tail = None
        self.length = None

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

    def find_value(self, value):
        current = self.head
        while current is not None:
            if current.value == value:
                print("found")
                return
            current = current.next
        print("not found")


singly = LinkedList()
singly.append(0)
singly.append(10)
singly.append(20)
singly.append(30)
print(singly)
singly.find_value(1)
