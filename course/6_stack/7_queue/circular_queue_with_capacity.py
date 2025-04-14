class CircularQueue:
    def __init__(self, size):
        self.items = size * [None]
        self.size = size
        self.start = -1
        self.end = -1

    def __str__(self):
        if self.isEmpty():
            return "Queue is empty"
        current = self.start
        result = []
        while current != self.end:
            result.append(str(self.items[current]))
            if current + 1 == self.size:
                current = 0
            else:
                current += 1
        result.append(str(self.items[current]))
        return ",".join(result)

    def isFull(self):
        if self.end + 1 == self.start:
            return True
        elif self.start == 0 and self.end + 1 == self.size:
            return True
        else:
            return False

    def isEmpty(self):
        if self.start == self.end:
            return True
        return False

    def enqueue(self, value):
        if self.isFull():
            return "Queue is full"
        else:
            if self.end + 1 == self.size:
                self.end = 0
            else:
                self.end += 1
                if self.start == -1:
                    self.start = 0
                self.items[self.end] = value
            return "Element inserted successfully"

    def dequeue(self):
        if self.isEmpty():
            return "Queue is empty"
        else:
            self.items[self.start] = None
            if self.start + 1 == self.size:
                self.start = 0
            else:
                self.start += 1
            return "Element deleted successfully"

    def peek(self):
        if self.isEmpty():
            return "Queue is empty"
        return self.items[self.start]

    def delete(self):
        self.items = self.size * [None]
        self.start = -1
        self.end = -1
        return "Queue is deleted"


cqueue = CircularQueue(10)
print(cqueue.isFull())
print(cqueue.isEmpty())
print(cqueue.enqueue(10))
print(cqueue.enqueue(20))
print(cqueue.enqueue(30))
print(cqueue.enqueue(40))
print(cqueue.enqueue(50))
print(cqueue.enqueue(60))
print(cqueue)
print(cqueue.dequeue())
print(cqueue.dequeue())
print(cqueue.dequeue())
print(cqueue.dequeue())
print(cqueue.enqueue(70))
print(cqueue.enqueue(80))
print(cqueue.enqueue(90))
print(cqueue.enqueue(100))
print(cqueue.dequeue())
print(cqueue.dequeue())
print(cqueue.dequeue())
print(cqueue)
print(cqueue.peek())
print(cqueue.delete())
print(cqueue)
