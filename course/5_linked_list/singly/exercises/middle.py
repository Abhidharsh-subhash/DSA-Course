# Write a function to find and return the middle node of a singly linked list. If the list has an even number of nodes, return the second of the two middle nodes.


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

    # def middle(self):
    #     if self.head is None:
    #         return None
    #     elif self.length == 1:
    #         return self.head
    #     else:
    #         temp = self.head
    #         for _ in range(self.length // 2):
    #             temp = temp.next
    #         return temp.value
    def middle(self):
        slow = self.head
        fast = self.head
        while fast is not None and fast.next is not None:
            slow = slow.next
            fast = fast.next.next
        return slow.value


singly = LinkedList()
singly.append(1)
singly.append(2)
singly.append(3)
singly.append(4)
# singly.append(5)
print(singly)
print(singly.middle())
