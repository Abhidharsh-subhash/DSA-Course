class Node:
    def __init__(self, value):
        self.value = value
        self.next = None


class LinkedList:
    def __init__(self):
        self.head = None
        self.tail = None
        self.length = 0

    def __iter__(self):
        current = self.head
        while current:
            yield current.value
            current = current.next


class Queue:
    def __init__(self):
        self.linkedlist = LinkedList()

    def __str__(self):
        result = [str(x) for x in self.linkedlist]
        return result

    def isEmpty(self):
        if self.linkedlist.head is None:
            return True
        return False

    def enqueue(self, data):
        new_node = Node(data)
        if self.linkedlist.head is None:
            self.linkedlist.head = self.linkedlist.tail = new_node
        else:
            self.linkedlist.tail.next = self.linkedlist.tail = new_node
        self.linkedlist.length += 1

    def dequeue(self):
        if self.linkedlist.head is None:
            return
        elif self.linkedlist.head == self.linkedlist.tail:
            popped_node = self.linkedlist.head
            self.linkedlist.head = self.linkedlist.tail = None
            self.linkedlist.length -= 1
            return popped_node
        else:
            popped_node = self.linkedlist.head
            self.linkedlist.head = self.linkedlist.head.next
            self.linkedlist.length -= 1
            return popped_node


class AVL_Node:
    def __init__(self, data):
        self.leftchild = None
        self.data = data
        self.rightchild = None
        self.height = 1


# Helper function to get the height of rootnode
def getHeight(RootNode):
    if not RootNode:
        return 0
    return RootNode.height


def rightRotate(DisbalancedNode):
    newRoot = DisbalancedNode.leftchild
    DisbalancedNode.leftchild = DisbalancedNode.leftchild.rightchild
    newRoot.rightchild = DisbalancedNode
    DisbalancedNode.height = 1 + max(
        getHeight(DisbalancedNode.leftchild), getHeight(DisbalancedNode.rightchild)
    )
    newRoot.height = 1 + max(
        getHeight(newRoot.leftchild), getHeight(newRoot.rightchild)
    )
    return newRoot


def leftRotate(DisbalancedNode):
    newRoot = DisbalancedNode.rightchild
    DisbalancedNode.rightchild = DisbalancedNode.rightchild.leftchild
    newRoot.leftchild = DisbalancedNode
    DisbalancedNode.height = 1 + max(
        getHeight(DisbalancedNode.leftchild), getHeight(DisbalancedNode.rightchild)
    )
    newRoot.height = 1 + max(
        getHeight(newRoot.leftchild), getHeight(newRoot.rightchild)
    )
    return newRoot


# Helper function to return the difference between the left and right child of a node
def getBalance(RootNode):
    if not RootNode:
        return 0
    return getHeight(RootNode.leftchild) - getHeight(RootNode.rightchild)


def insertNode(RootNode, NodeValue):
    if not RootNode:
        return AVL_Node(NodeValue)
    elif NodeValue < RootNode.data:
        RootNode.leftchild = insertNode(RootNode.leftchild, NodeValue)
    else:
        RootNode.rightchild = insertNode(RootNode.rightchild, NodeValue)
    RootNode.height = 1 + max(
        getHeight(RootNode.leftchild), getHeight(RootNode.rightchild)
    )
    balance = getBalance(RootNode)
    # LL
    if balance > 1 and NodeValue < RootNode.leftchild.data:
        return rightRotate(RootNode)
    # LR
    if balance > 1 and NodeValue > RootNode.leftchild.data:
        RootNode.leftchild = leftRotate(RootNode.leftchild)
        return rightRotate(RootNode)
    # RR
    if balance < -1 and NodeValue > RootNode.rightchild.data:
        return leftRotate(RootNode)
    # RL
    if balance < -1 and NodeValue < RootNode.rightchild.data:
        RootNode.rightchild = rightRotate(RootNode.rightchild)
        return leftRotate(RootNode)
    return RootNode


def LevelOrderTraversal(RootNode):
    if not RootNode:
        return
    else:
        tracking = Queue()
        tracking.enqueue(RootNode)
        while not tracking.isEmpty():
            root = tracking.dequeue()
            print(root.value.data)
            if root.value.leftchild is not None:
                tracking.enqueue(root.value.leftchild)
            if root.value.rightchild is not None:
                tracking.enqueue(root.value.rightchild)


new_AVL = AVL_Node(5)
new_AVL = insertNode(new_AVL, 10)
new_AVL = insertNode(new_AVL, 20)
new_AVL = insertNode(new_AVL, 30)
new_AVL = insertNode(new_AVL, 40)
new_AVL = insertNode(new_AVL, 50)
new_AVL = insertNode(new_AVL, 60)
new_AVL = insertNode(new_AVL, 70)
LevelOrderTraversal(new_AVL)
