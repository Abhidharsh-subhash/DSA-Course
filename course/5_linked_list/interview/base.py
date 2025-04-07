import random


class Node:
    def __init__(self, value=None):
        self.prev = None
        self.value = value
        self.next = None

    def __str__(self):
        return str(self.value)


class LinkedList:
    def __init__(self, value=None):
        self.head = None
        self.tail = None

    # custom iterator
    def __iter__(self):
        current = self.head
        while current:
            yield current.value
            current = current.next

    def __str__(self):
        result = [str(i) for i in self]
        return "->".join(result)

    # custom length function
    def __len__(self):
        current = self.head
        result = 0
        while current:
            result += 1
            current = current.next
        return result

    def add(self, value):
        new_node = Node(value)
        if self.head is None:
            self.head = self.tail = new_node
        else:
            self.tail.next = self.tail = new_node
        return self.tail

    # generate linkedlist with length n and with random numbers between min_value and max_value
    def generate(self, n, min_value, max_value):
        for _ in range(n):
            value = random.randint(min_value, max_value)
            self.add(value)
        return self


test = LinkedList()
test.generate(5, 19, 90)
print(len(test))
print(test)
