class Node:
    def __init__(self, value):
        self.value = value
        self.next = None


class LinkedList:
    def __init__(self):
        self.head = self.tail = None

    def __iter__(self):
        current = self.head
        while current:
            yield current.value
            current = current.next

    def add(self, value):
        new_node = Node(value)
        if self.head is None:
            self.head = self.tail = new_node
        else:
            self.tail.next = self.tail = new_node

    def delete_first(self):
        if self.head == self.tail:
            self.head = self.tail = None
        else:
            self.head = self.head.next

    def isEmpty(self):
        if self.head:
            return False
        return True

    def first_element(self):
        return self.head.value


# ll = LinkedList()
# ll.add(10)
# ll.add(20)
# ll.add(30)
# ll.add(40)
# ll.add(50)
# ll.add(60)
# for i in ll:
#     print(i)


class Queue:
    def __init__(self):
        self.items = LinkedList()

    def isEmpty(self):
        return self.items.isEmpty()

    def __str__(self):
        if self.isEmpty():
            return "Queue is empty"
        result = []
        for i in self.items:
            result.append(str(i))
        return ",".join(result)

    def enqueue(self, value):
        self.items.add(value)
        return "Value inserted"

    def dequeue(self):
        if self.isEmpty():
            return "Queue is empty"
        self.items.delete_first()
        return "Value deleted"

    def peek(self):
        if self.isEmpty():
            return "Queue is empty"
        return self.items.first_element()

    def delete(self):
        self.items.head = self.items.tail = None
        return "Queue deleted"


queue = Queue()
print(queue.enqueue(10))
print(queue.enqueue(20))
print(queue.enqueue(30))
print(queue.enqueue(40))
print(queue.enqueue(50))
print(queue)
print(queue.dequeue())
print(queue.dequeue())
print(queue.dequeue())
print(queue)
print(queue.peek())
print(queue.delete())
print(queue)
