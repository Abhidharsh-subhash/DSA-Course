# Remove Duplicates
# Given the head of a sorted linked list, delete all duplicates such that each element appears only once. Return the linked list sorted as well.

# Example 1:

# Input: head = [1,1,2]
# Output: [1,2]
# Example 2:

# Input: head = [1,1,2,3,3]
# Output: [1,2,3]


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
            self.head = self.tail = new_node
        else:
            self.tail.next = self.tail = new_node

    def remove_duplicates(self):
        seen = set()
        current = self.head
        prev = None
        while current is not None:
            if current.value in seen:
                prev.next = current.next
                current = current.next
            else:
                seen.add(current.value)
                prev = current
                current = current.next


singly = LinkedList()
singly.append(1)
singly.append(2)
singly.append(1)
singly.append(3)
singly.append(1)
singly.append(4)
singly.append(1)
print(singly)
singly.remove_duplicates()
print(singly)
