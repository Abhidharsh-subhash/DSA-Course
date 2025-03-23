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
        self.length += 1

    # def reverse(self):
    #     llist = []
    #     temp = self.head
    #     while temp is not None:
    #         llist.append(temp.value)
    #         temp = temp.next
    #     new_temp = self.head
    #     for i in range(len(llist)-1, -1, -1):
    #         new_temp.value = llist[i]
    #         new_temp = new_temp.next
    def reverse(self):
        prev_node = None
        current_node = self.head
        while current_node is not None:
            next_node = current_node.next
            current_node.next = prev_node
            prev_node = current_node
            current_node = next_node
        self.tail, self.head = self.head, self.tail


singly = LinkedList()
singly.append(1)
singly.append(2)
singly.append(3)
singly.append(4)
print(singly)
singly.reverse()
print(singly)
