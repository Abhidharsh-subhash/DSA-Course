# Insert into a Sorted Circular Linked List
# Write a function to insert a new node into a sorted circular linked list


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
            self.tail.next, self.tail, new_node.next = new_node, new_node, self.head
        self.length += 1

    def insert_into_sorted(self, value):
        new_node = Node(value)
        if self.head is None:
            self.head = self.tail = new_node.next = new_node
        elif self.head.value > value:
            new_node.next, self.tail.next, self.head = self.head, new_node, new_node
        elif self.tail.value < value:
            self.tail.next, self.tail, new_node.next = new_node, new_node, self.head
        else:
            prev = self.head
            current = self.head.next
            while current:
                if prev.value < value and current.value > value:
                    new_node.next, prev.next = prev.next, new_node
                elif current.next == self.head:
                    break
                prev = current
                current = current.next
        self.length += 1


CS = CircularLinkedList()
CS.append(10)
CS.append(20)
CS.append(30)
CS.append(40)
CS.append(50)
CS.append(60)
CS.append(70)
print(CS)
CS.insert_into_sorted(22)
print(CS)
