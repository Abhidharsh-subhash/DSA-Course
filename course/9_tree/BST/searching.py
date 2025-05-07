class BSTNode:
    def __init__(self, data):
        self.leftchild = None
        self.data = data
        self.rightchild = None


def InsertNode(RootNode, NodeValue):
    if RootNode.data is None:
        RootNode.data = NodeValue
    elif NodeValue <= RootNode.data:
        if RootNode.leftchild is None:
            RootNode.leftchild = BSTNode(NodeValue)
        else:
            InsertNode(RootNode.leftchild, NodeValue)
    else:
        if RootNode.rightchild is None:
            RootNode.rightchild = BSTNode(NodeValue)
        else:
            InsertNode(RootNode.rightchild, NodeValue)
    return "Node inserted successfully"


class Node:
    def __init__(self, value):
        self.value = value
        self.next = None


class LinkedList:
    def __init__(self):
        self.head = None
        self.tail = None


class Queue:
    def __init__(self):
        self.queue = LinkedList()

    def enqueue(self, value):
        new_node = Node(value)
        if self.queue.head is None:
            self.queue.head = self.queue.tail = new_node
        else:
            self.queue.tail.next = self.queue.tail = new_node

    def isEmpty(self):
        if self.queue.head is None:
            return True
        return False

    def dequeue(self):
        if self.isEmpty():
            return
        elif self.queue.head == self.queue.tail:
            popped_node = self.queue.head
            self.queue.head = self.queue.tail = None
            return popped_node
        else:
            popped_node = self.queue.head
            self.queue.head = self.queue.head.next
            popped_node.next = None
            return popped_node


def LevelorderTraversal(RootNode):
    if RootNode.data is None:
        return "Empty BST"
    else:
        queue = Queue()
        queue.enqueue(RootNode)
        while not queue.isEmpty():
            root = queue.dequeue()
            print(root.value.data)
            if root.value.leftchild is not None:
                queue.enqueue(root.value.leftchild)
            if root.value.rightchild is not None:
                queue.enqueue(root.value.rightchild)


def Searching(RootNode, SearchValue):
    if RootNode.data is None:
        print("not found")
    elif RootNode.data == SearchValue:
        print("found")
    else:
        if SearchValue < RootNode.data:
            if RootNode.leftchild is not None:
                Searching(RootNode.leftchild, SearchValue)
            else:
                return print("not found")
        elif SearchValue > RootNode.data:
            if RootNode.rightchild is not None:
                Searching(RootNode.rightchild, SearchValue)
            else:
                return print("not found")


# Time Complexity of O(logN) and Space Complexity is also O(logN)


NewTree = BSTNode(None)
print(InsertNode(NewTree, 70))
print(InsertNode(NewTree, 50))
print(InsertNode(NewTree, 90))
print(InsertNode(NewTree, 30))
print(InsertNode(NewTree, 60))
print(InsertNode(NewTree, 80))
print(InsertNode(NewTree, 100))
print(InsertNode(NewTree, 20))
print(InsertNode(NewTree, 40))
LevelorderTraversal(NewTree)
Searching(NewTree, 40)
