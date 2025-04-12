class Stack:
    def __init__(self):
        self.list = []

    def isEmpty(self):
        if self.list == []:
            return True
        return False

    def __str__(self):
        if self.isEmpty():
            return "Stack is empty"
        rev_list = [str(self.list[i]) for i in range(len(self.list) - 1, -1, -1)]
        return ",".join(rev_list)

    def push(self, value):
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


stack = Stack()
print(stack.isEmpty())
stack.push(11)
stack.push(16)
stack.push(15)
stack.push(10)
stack.push(13)
print(stack)
stack.pop()
print(stack)
stack.pop()
print(stack.peek())
stack.delete()
print(stack)
