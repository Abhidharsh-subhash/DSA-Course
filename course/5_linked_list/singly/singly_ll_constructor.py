class Node:
    def __init__(self, value):
        self.value = value
        self.ref = None


# LinkedList with only one node
class Singly_ll:
    def __init__(self, value):
        new_node = Node(value)
        self.head = new_node
        self.tail = new_node
        self.length = 1


new_ll = Singly_ll(10)
print(new_ll.head.value)
print(new_ll.tail.value)

# Empty LinkedList
# class Singly_ll:
#     def __init__(self):
#         self.head = None
#         self.tail = None
#         self.length = 0


# new_ll = Singly_ll()
# print(new_ll.head)
# print(new_ll.head)


# Time and Space complexity for creating a linked list with 1 and 0 elements is O(1)
