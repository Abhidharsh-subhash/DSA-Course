# Implement Queue class which implements a queue using two stacks.


# class Queue:
#     def __init__(self):
#         self.items = []

#     def __len__(self):
#         return len(self.items)

#     def __str__(self):
#         return str(self.items)

#     def push(self, item):
#         self.items.append(item)
#         return "element inserted successfully"

#     def pop(self, stack):
#         if len(self.items) == 0:
#             return "empty queue"
#         item = self.items.pop()
#         stack.push(item)
#         return "element popped successfully"


# queue1 = Queue()
# queue2 = Queue()
# queue1.push(10)
# queue1.push(11)
# queue1.push(12)
# queue1.push(13)
# queue1.push(14)
# print(queue1.pop(queue2))
# print(queue1.pop(queue2))
# print(queue1.pop(queue2))
# print(queue2.pop(queue1))
# print(f"queue1: {queue1}")
# print(f"queue2: {queue2}")


class Stack:
    def __init__(self):
        self.list = []

    def __len__(self):
        return len(self.list)

    def push(self, item):
        self.list.append(item)

    def pop(self):
        if len(self.list) == 0:
            return "emtpy Stack"
        return self.list.pop()


class QueueviaStack:
    def __init__(self):
        self.inStack = Stack()
        self.outStack = Stack()

    def enqueue(self, item):
        self.inStack.push(item)

    def dequeue(self):
        while len(self.inStack):
            self.outStack.push(self.inStack.pop())
        result = self.outStack.pop()
        while len(self.outStack):
            self.inStack.push(self.outStack.pop())
        return result


queue = QueueviaStack()
queue.enqueue(10)
queue.enqueue(11)
queue.enqueue(12)
queue.enqueue(13)
queue.enqueue(14)
print(queue.dequeue())
print(queue.dequeue())
