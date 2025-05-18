# Common operations in both BST and AVL Tree


class AVL_Node:
    def __init__(self, data):
        self.leftchild = None
        self.data = data
        self.rightchild = None
        self.height = 1


def PreorderTraversal(RootNode):
    if not RootNode:
        return
    else:
        print(RootNode.data)
        PreorderTraversal(RootNode.leftchild)
        PreorderTraversal(RootNode.rightchild)


def InorderTraversal(RootNode):
    if not RootNode:
        return
    else:
        InorderTraversal(RootNode.leftchild)
        print(RootNode.data)
        InorderTraversal(RootNode.rigtchild)


def PostorderTraversal(RootNode):
    if not RootNode:
        return
    else:
        PostorderTraversal(RootNode.leftchild)
        PostorderTraversal(RootNode.rightchild)
        print(RootNode.data)


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

    def enqueue(self, NodeValue):
        new_node = Node(NodeValue)
        if self.IsEmpty():
            self.queue.head = self.queue.tail = new_node
        else:
            self.queue.tail.next = self.queue.tail = new_node

    def __str__(self):
        result = []
        for i in self.queue:
            result.append(i)
        return " ".join(result)

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
    if not RootNode:
        return
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


def searching(RootNode, SearchValue):
    if not RootNode:
        return "Value does not exist"
    elif RootNode.data == SearchValue:
        return "Value Found"
    else:
        if SearchValue < RootNode.data:
            if RootNode.leftchild is not None:
                return searching(RootNode.leftchild, SearchValue)
            else:
                return "Value does not exist"
        elif SearchValue > RootNode.data:
            if RootNode.rightchild is not None:
                return searching(RootNode.rightchild, SearchValue)
            else:
                return "Value does not exist"


def getHeight(RootNode):
    if not RootNode:
        return 0
    return RootNode.height


def rightRotate(disbalancedNode):
    newRoot = disbalancedNode.leftchild
    disbalancedNode.leftchild = disbalancedNode.leftchild.rightchild
    newRoot.rightchild = disbalancedNode
    # here we are adding 1 because we have getting the height of left and rightchild so 1 more to be incremented to get the proper height of it
    disbalancedNode.height = 1 + max(
        getHeight(disbalancedNode.leftchild), getHeight(disbalancedNode.rightchild)
    )
    # set newRoot height
    newRoot.height = 1 + max(
        getHeight(newRoot.leftchild), getHeight(newRoot.rightchild)
    )
    return newRoot


def leftRotate(disbalancedNode):
    newRoot = disbalancedNode.rightchild
    disbalancedNode.rightchild = disbalancedNode.rightchild.leftchild
    newRoot.leftchild = disbalancedNode
    disbalancedNode.height = 1 + max(
        getHeight(disbalancedNode.leftchild), getHeight(disbalancedNode.rightchild)
    )
    newRoot.height = 1 + max(
        getHeight(newRoot.leftchild), getHeight(newRoot.rightchild)
    )
    return newRoot


def getBalance(RootNode):
    if not RootNode:
        return 0
    return getHeight(RootNode.leftchild) - getHeight(RootNode.rightchild)


def insertNode(RootNode, nodeValue):
    if not RootNode:
        return AVL_Node(nodeValue)
    elif nodeValue < RootNode.data:
        RootNode.leftchild = insertNode(RootNode.leftchild, nodeValue)
    else:
        RootNode.rightchild = insertNode(RootNode.rightchild, nodeValue)
    RootNode.height = 1 + max(
        getHeight(RootNode.leftchild), getHeight(RootNode.rightchild)
    )
    balance = getBalance(RootNode)
    if balance > 1 and nodeValue < RootNode.leftchild.data:
        return rightRotate(RootNode)
    if balance > 1 and nodeValue > RootNode.leftchild.data:
        RootNode.leftchild = leftRotate(RootNode.leftchild)
        return rightRotate(RootNode)
    if balance < -1 and nodeValue > RootNode.rightchild.data:
        return leftRotate(RootNode)
    if balance < -1 and nodeValue < RootNode.rightchild.data:
        RootNode.rightchild = rightRotate(RootNode.rightchild)
        return leftRotate(RootNode)
    return RootNode


new_AVL = AVL_Node(5)
new_AVL = insertNode(new_AVL, 10)
new_AVL = insertNode(new_AVL, 15)
new_AVL = insertNode(new_AVL, 20)
LevelorderTraversal(new_AVL)
