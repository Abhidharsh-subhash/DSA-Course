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
            self.head = new_node
            self.tail = new_node
        else:
            self.tail.next = self.tail = new_node
        self.length += 1

    def parlindrome_check(self):
        result = []
        current = self.head
        while current is not None:
            result.append(current.value)
            current = current.next
        return result == result[::-1]


# class ListNode(object):
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

# class Solution(object):
#     def isPalindrome(self, head):
#         slow = fast = head
#         while fast and fast.next:
#             slow = slow.next
#             fast = fast.next.next

#         prev = None
#         while slow:
#             nxt = slow.next
#             slow.next = prev
#             prev = slow
#             slow = nxt

#         while prev:
#             if head.val != prev.val:
#                 return False
#             head = head.next
#             prev = prev.next
#         return True


singly = LinkedList()
singly.append(1)
singly.append(2)
singly.append(2)
singly.append(1)
# singly.appensd(5)
print(singly)
print(singly.parlindrome_check())
