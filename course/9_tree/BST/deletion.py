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

    def __iter__(self):
        current = self.head
        if current:
            yield current.value
            current = current.next


class Queue:
    def __init__(self):
        self.queue = LinkedList()

    def IsEmpty(self):
        return True if self.queue.head is None else False

    def __str__(self):
        result = [str(x) for x in self.queue]
        return " ".join(result)

    def enqueue(self, value):
        new_node = Node(value)
        if self.IsEmpty():
            self.queue.head = self.queue.tail = new_node
        else:
            self.queue.tail.next = self.queue.tail = new_node

    def dequeue(self):
        if self.IsEmpty():
            return "Empty Queue"
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
        return "Empty list"
    else:
        queue = Queue()
        queue.enqueue(RootNode)
        while not queue.IsEmpty():
            root = queue.dequeue()
            print(root.value.data)
            if root.value.leftchild is not None:
                queue.enqueue(root.value.leftchild)
            if root.value.rightchild is not None:
                queue.enqueue(root.value.rightchild)


def Searching(RootNode, SearchNode):
    if RootNode.data is None:
        print("Empty BST")
    elif RootNode.data == SearchNode:
        print("Value Found")
    else:
        if SearchNode <= RootNode.data:
            if RootNode.leftchild is not None:
                Searching(RootNode.leftchild, SearchNode)
            else:
                print("Value not found")
        else:
            if RootNode.rightchild is not None:
                Searching(RootNode.rightchild, SearchNode)
            else:
                print("Value not found")


def Successor(RootNode):
    if RootNode.data is None:
        print("Empty Tree")
    else:
        # min = RootNode.data
        # if RootNode.leftchild is not None:
        #     return Successor(RootNode.leftchild)
        # else:
        #     return min
        current = RootNode
        while current.leftchild is not None:
            current = current.leftchild
        return current.data


def DeleteNode(RootNode, NodeValue):
    if RootNode is None:
        return RootNode
    if NodeValue < RootNode.data:
        RootNode.leftchild = DeleteNode(RootNode.leftchild, NodeValue)
    elif NodeValue > RootNode.data:
        RootNode.rightchild = DeleteNode(RootNode.rightchild, NodeValue)
    else:
        if RootNode.leftchild is None:
            temp = RootNode.rightchild
            RootNode = None
            return temp
        if RootNode.rigthchild is None:
            temp = RootNode.leftchild
            RootNode = None
            return temp
        temp = Successor(RootNode.rightchild)
        RootNode.data = temp.data
        RootNode.rightchild = DeleteNode(RootNode.rightchild, temp.data)
    return RootNode


NewTree = BSTNode(None)
Searching(NewTree, 88)
print(InsertNode(NewTree, 70))
print(InsertNode(NewTree, 50))
print(InsertNode(NewTree, 90))
print(InsertNode(NewTree, 30))
print(InsertNode(NewTree, 60))
print(InsertNode(NewTree, 80))
print(InsertNode(NewTree, 100))
print(InsertNode(NewTree, 20))
print(InsertNode(NewTree, 40))
print("traversing")
LevelorderTraversal(NewTree)
print("searching")
Searching(NewTree, 200)
# print(Successor(NewTree.rightchild))
DeleteNode(NewTree, 100)
print("traversing")
LevelorderTraversal(NewTree)
