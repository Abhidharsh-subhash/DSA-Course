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

    def get_index_value(self, index):
        temp = self.head
        if index > self.length-1:
            print("worng index")
        elif index == 0:
            print(temp.value)
            return
        else:
            for _ in range(index):
                temp = temp.next
            print(temp.value)
            return


singly = LinkedList()
singly.append(10)
singly.append(99)
singly.append(00)
singly.append(22)
singly.append(78)
print(singly)
print(singly.length)
singly.get_index_value(5)
