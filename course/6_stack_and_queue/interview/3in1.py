# Describe how you could use a single python list to implement three stacks

# Use a single python list to implement three stacks


class MultiStack:
    def __init__(self, stacksize):
        self.numberstacks = 3
        self.cusList = [0] * (stacksize * self.numberstacks)
        self.sizes = [0] * self.numberstacks
        self.stacksize = stacksize

    def isFull(self, stacknum):
        if self.sizes[stacknum] == self.stacksize:
            return True
        return False

    def isEmpty(self, stacknum):
        if self.sizes[stacknum] == 0:
            return True
        return False

    def indexOfTop(self, stacknum):
        if self.isEmpty(stacknum):
            return "Empty queue"
        offset = self.stacksize * stacknum
        return offset + self.sizes[stacknum] - 1

    def push(self, value, stacknum):
        if self.isFull(stacknum):
            return "Stack is full"
        self.sizes[stacknum] += 1
        self.cusList[self.indexOfTop(stacknum)] = value

    def pop(self, stacknum):
        if self.isEmpty(stacknum):
            return "Stack is empty"
        value = self.cusList[self.indexOfTop(stacknum)]
        self.cusList[self.indexOfTop(stacknum)] = 0
        self.sizes[stacknum] -= 1
        return value

    def peek(self, stacknum):
        if self.isEmpty(stacknum):
            return "Stack is empty"
        value = self.cusList[self.indexOfTop(stacknum)]
        return value


customStack = MultiStack(5)
print(customStack.isEmpty(2))
print(customStack.isFull(0))
customStack.push(1, 0)
customStack.push(2, 1)
customStack.push(10, 0)
print(customStack.peek(2))
