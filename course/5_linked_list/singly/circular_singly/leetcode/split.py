# Split a Circular Linked List into Two Equal Halves
# Write a function to split the circular linked list into two equal halves. If the list has odd number of nodes, the extra node should go to the first list.
import math


class Node:
    def __init__(self, value):
        self.value = value
        self.next = None


class CSLinkedList:
    def __init__(self):
        self.head = None
        self.tail = None
        self.length = 0

    def __str__(self):
        result = ""
        current = self.head
        while current:
            result += str(current.value)
            if current.next == self.head:
                break
            result += " -> "
            current = current.next
        return result

    def append(self, value):
        new_node = Node(value)
        if self.head is None:
            self.head = self.tail = new_node.next = new_node
        else:
            self.tail.next, new_node.next, self.tail = new_node, self.head, new_node
        self.length += 1

    def split(self):
        if self.head is None:
            return None, None
        else:
            mid = (self.length + 1) // 2

            first_list = CSLinkedList()
            second_list = CSLinkedList()

            current = self.head
            for _ in range(mid):
                first_list.append(current.value)
                current = current.next
                first_list.length += 1

            while current:
                second_list.append(current.value)
                if current.next == self.head:
                    break
                current = current.next
                second_list.length += 1
            print(first_list)
            print(second_list)
            return first_list, second_list


CS = CSLinkedList()
CS.append(10)
CS.append(20)
CS.append(30)
CS.append(40)
CS.append(50)
CS.append(60)
CS.append(70)
print(CS)
print(CS.split())
