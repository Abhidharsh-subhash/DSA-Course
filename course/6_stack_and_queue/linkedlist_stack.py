class Node:
    def __init__(self, value):
        self.value = value
        self.next = None


class LinkedList:
    def __init__(self):
        self.head = None
        self.tail = None

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
            new_node.next, self.head = self.head, new_node

    def remove(self):
        if self.head:
            self.head = self.head.next


# ll = LinkedList()
# ll.add(10)
# ll.add(20)
# ll.add(40)
# ll.add(50)
# for i in ll:
#     print(i)


class Stack:
    def __init__(self):
        self.linkedlist = LinkedList()

    def isEmpty(self):
        if self.linkedlist.head:
            return False
        return True

    def __str__(self):
        if self.isEmpty():
            return "Empty stack"
        result = [str(i) for i in self.linkedlist]
        return ",".join(result)

    def push(self, value):
        self.linkedlist.add(value)

    def pop(self):
        if not self.isEmpty():
            self.linkedlist.remove()
        return "Empty stack"

    def peek(self):
        if not self.isEmpty():
            return self.linkedlist.head.value
        return "Empty stack"

    def delete(self):
        self.linkedlist.head = None


stack = Stack()
print(stack.isEmpty())
stack.push(10)
stack.push(20)
stack.push(30)
stack.push(40)
stack.push(50)
stack.push(60)
print(stack)
stack.pop()
print(stack)
print(stack.peek())
print(stack.isEmpty())
stack.delete()
print(stack)
