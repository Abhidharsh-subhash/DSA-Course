class Queue:
    def __init__(self):
        self.items = []

    def isEmpty(self):
        if self.items == []:
            return True
        return False

    def __str__(self):
        if self.isEmpty():
            return "Empty Queue"
        values = [str(i) for i in self.items]
        return ",".join(values)

    def enqueue(self, value):
        self.items.append(value)

    def dequeue(self):
        if self.isEmpty():
            return "Empty Queue"
        self.items.pop(0)

    def peek(self):
        if self.isEmpty():
            return "Empty Queue"
        return self.items[0]

    def delete(self):
        self.items = []


queue = Queue()
print(queue)
queue.enqueue(20)
queue.enqueue(22)
queue.enqueue(24)
queue.enqueue(26)
queue.enqueue(28)
queue.enqueue(29)
print(queue)
queue.dequeue()
print(queue)
print(queue.peek())
queue.delete()
print(queue)
