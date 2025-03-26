# Given the head of a linked list and an integer val, remove all the nodes of the linked list that has Node.val == val, and return the new head.

# Example 1:

# Input: head = [1,2,6,3,4,5,6], val = 6
# Output: [1,2,3,4,5]
# Example 2:

# Input: head = [], val = 1
# Output: []
# Example 3:

# Input: head = [7,7,7,7], val = 7
# Output: []


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
            self.head = new_node
            self.tail = new_node
        else:
            self.tail.next = self.tail = new_node
        self.length += 1

    def delete_element(self, value):
        current = self.head
        prev = None
        while current is not None:
            if current.value == value:
                prev.next = current.next
                current = current.next
            else:
                prev = current
                current = current.next


singly = LinkedList()
singly.append(1)
singly.append(2)
singly.append(3)
singly.append(2)
singly.append(9)
singly.append(2)
singly.append(2)
print(singly)
singly.delete_element(2)
print(singly)
