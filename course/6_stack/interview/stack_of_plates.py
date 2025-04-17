# Imagine a(literal) stack of plates. If the stack gets too high, it might topple. Therefore in real life, we would likely start a new stack, when the previous stack exceeds some
# threshold. Implement a SetOfStacks that mimics this. SetOfStack should be composed of several stacks and should create a new stack once the previos one exceeds capacity, SetOfStacks.push()
# and SetOfStack.pop() should identically behave to a single stack(that is pop() should return the same values as it would if there were just a single stack).

# Follow up:
#    Implment a function popAt(int index) which performs a pop operation on a specific sub - track


class PlatesStack:
    def __init__(self, limit):
        self.length = limit
        self.stacks = []

    def __str__(self):
        return str(self.stacks)

    def push(self, item):
        length = len(self.stacks)
        if length == 0:
            self.stacks.append([item])
        elif len(self.stacks[length - 1]) < self.length:
            self.stacks[length - 1].append(item)
        else:
            self.stacks.append([item])

    def pop(self):
        length = len(self.stacks)
        if length == 0:
            return "empty stack"
        else:
            self.stacks[length - 1].pop()
            if len(self.stacks[length-1]) == 0:
                self.stacks.pop()
            return "element popped out"


stack = PlatesStack(3)
stack.push(9)
stack.push(8)
stack.push(18)
stack.push(81)
stack.push(88)
stack.push(80)
stack.push(83)
print(stack.pop())
print(stack.pop())
print(stack.pop())
print(stack.pop())
print(stack.pop())
print(stack.pop())
print(stack.pop())
print(stack.pop())
print(stack)
