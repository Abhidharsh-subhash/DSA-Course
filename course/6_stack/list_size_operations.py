class Stack:
    def __init__(self, size):
        self.size = size
        self.list = []

    def isEmpty(self):
        if self.list == []:
            return True
        return False

    def __str__(self):
        if self.isEmpty():
            return "Stack is empty"
        result_list = [str(self.list[i]) for i in range(len(self.list) - 1, -1, -1)]
        return ",".join(result_list)

    def isFull(self):
        if len(self.list) == self.size:
            return True
        return False

    def push(self, value):
        if self.isFull():
            return "Stack is full"
        self.list.append(value)

    def pop(self):
        if self.isEmpty():
            return "Stack is empty"
        self.list.pop()

    def peek(self):
        if self.isEmpty():
            return "Stack is empty"
        return self.list[-1]

    def delete(self):
        self.list = []


stack = Stack(3)
stack.push(1)
stack.push(2)
stack.push(3)
print(stack.push(4))
print(stack)
stack.delete()
print(stack)
