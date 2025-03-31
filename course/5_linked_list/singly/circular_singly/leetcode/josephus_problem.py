# Josephus Circle using Circular Linked List
# Solve the Josephus problem using a circular linked list. Implement a function that takes the number of people n and the step rate k and returns the position of the last person standing.

# Output: Last person left standing: 3


class Node:
    def __init__(self, value):
        self.value = value
        self.next = None


class CircularLinkedList:
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

    def josephus_circle(self, step):
        prev = None
        current = self.head
        count = 0
        while current:
            count += 1
            if self.length == 1:
                return f"Last person left standing: {current.value}"
            elif count == step:
                prev.next = current.next
                self.length -= 1
                count = 0
                prev = prev
            else:
                prev = current
            current = current.next


CS = CircularLinkedList()
CS.append(10)
CS.append(20)
CS.append(30)
CS.append(40)
CS.append(50)
CS.append(60)
CS.append(70)
print(CS)
print(CS.josephus_circle(3))
