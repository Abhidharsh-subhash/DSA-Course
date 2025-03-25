# Merge Two Sorted Linked List
# You are given the heads of two sorted linked lists list1 and list2.

# Merge the two lists in a one sorted list. The list should be made by splicing together the nodes of the first two lists.

# Return the head of the merged linked list.

# Example 1:
# Input: list1 = [1,2,4], list2 = [1,3,4]
# Output: [1,1,2,3,4,4]
# Example 2:
# Input: list1 = [], list2 = []
# Output: []
# Example 3:
# Input: list1 = [], list2 = [0]
# Output: [0]

# Constraints:

# The number of nodes in both lists is in the range [0, 50].

# -100 <= Node.val <= 100

# Both list1 and list2 are sorted in non-decreasing order.


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
            self.head = new_node
            self.tail = new_node
        else:
            self.tail.next = self.tail = new_node
        self.length += 1

    # def merge(self, ll):
    #     result = []
    #     my_current_node = self.head
    #     ll_current_node = ll.head
    #     for _ in range(self.length + 1):
    #         if my_current_node.value > ll_current_node.value:
    #             result.append(ll_current_node.value)
    #             ll_current_node = ll_current_node.next
    #         else:
    #             result.append(my_current_node.value)
    #             my_current_node = my_current_node.next
    #     while my_current_node or ll_current_node:
    #         if (
    #             ll_current_node is not None
    #             and my_current_node.value > ll_current_node.value
    #         ):
    #             result.append(ll_current_node.value)
    #             ll_current_node = ll_current_node.next
    #         else:
    #             if my_current_node is not None:
    #                 result.append(my_current_node.value)
    #                 my_current_node = my_current_node.next
    #     print(result)
    def merge(self, ll):
        dummy = Node(-1)
        current = dummy
        l1 = self.head
        l2 = ll.head
        while l1 and l2:
            if l1.value > l2.value:
                current.next = l2
                l2 = l2.next
            else:
                current.next = l1
                l1 = l1.next
            current = current.next
        current.next = l1 if l1 else l2
        temp = dummy.next
        result = ""
        while temp is not None:
            result += str(temp.value)
            if temp.next is not None:
                result += "->"
            temp = temp.next
        print(result)


singly1 = LinkedList()
singly1.append(1)
singly1.append(3)
singly1.append(5)
singly1.append(8)
singly1.append(9)
singly1.append(10)
singly1.append(11)
singly1.append(12)
singly2 = LinkedList()
singly2.append(2)
singly2.append(4)
singly2.append(7)
print(singly1)
print(singly2)
singly1.merge(singly2)
