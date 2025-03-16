class Node:
    def __init__(self, value):
        self.value = value
        self.next = None


class LinkedList:
    def __init__(self):
        self.head = self.tail = None
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

    # def insert_at_index(self, value, target_index):
    #     new_node = Node(value)
    #     if self.head is None:
    #         print("LinkedList is null")
    #     elif target_index == 0:
    #         new_node.next, self.head = self.head, new_node
    #     else:
    #         temp = self.head
    #         index = 0
    #         while temp is not None:
    #             if index == target_index-1:
    #                 new_node.next, temp.next = temp.next, new_node
    #                 self.length += 1
    #                 return
    #             index += 1
    #             temp = temp.next
    #         print("Linkedlist is not of that length")

    def insert_at_index(self, value, target_index):
        new_node = Node(value)
        if target_index < 0 or target_index - 1 > self.length:
            print("No such index is available")
        elif target_index == 0:
            new_node.next, self.head = self.head, new_node
        else:
            temp = self.head
            for _ in range(target_index - 1):
                temp = temp.next
            new_node.next, temp.next = temp.next, new_node
        self.length += 1


singly = LinkedList()
singly.append(1)
singly.append(2)
singly.append(3)
singly.append(4)
singly.insert_at_index(10, 10)
print(singly)
print(singly.length)
