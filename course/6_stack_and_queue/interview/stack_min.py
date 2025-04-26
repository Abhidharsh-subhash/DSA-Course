# How would you design a stack which, in addition to push and pop, has a function which returns the minimum element ? Push, Pop and min should operate in O(1)


class Node:
    def __init__(self, value, next=None):
        self.value = value
        self.next = next

    def __str__(self):
        string = str(self.value)
        return string


class stack:
    def __init__(self):
        self.top = None
        self.minNode = None

    def min(self):
        return self.minNode

    def push(self, item):
        if self.minNode and (self.minNode.value < item):
            self.minNode = Node(value=self.minNode.value, next=self.minNode)
        else:
            self.minNode = Node(value=item, next=self.minNode)
        self.top = Node(value=item, next=self.top)

    def pop(self):
        if not self.top:
            return None
        self.minNode = self.minNode.next
        item = self.top.value
        self.top = self.top.next
        return item


CustomStack = stack()
CustomStack.push(.5)
CustomStack.push(6)
CustomStack.push(1)
CustomStack.push(10)
CustomStack.push(0)
CustomStack.pop()
print(CustomStack.min())
