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
        return " ".join(result)

    def isEmpty(self):
        if self.linkedlist.length == 0:
            return True
        return False

    def enqueue(self, NodeValue):
        new_node = Node(NodeValue)
        if self.isEmpty():
            self.linkedlist.head = self.linkedlist.tail = new_node
        else:
            self.linkedlist.tail.next = self.linkedlist.tail = new_node
        self.linkedlist.length += 1

    def dequeue(self):
        if self.isEmpty():
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


def GetHeight(RootNode):
    if not RootNode:
        return 0
    else:
        return RootNode.height


def GetBalance(RootNode):
    if not RootNode:
        return 0
    else:
        return GetHeight(RootNode.leftchild) - GetHeight(RootNode.rightchild)


def RightRotate(DislabancedNode):
    NewRoot = DislabancedNode.leftchild
    DislabancedNode.leftchild = DislabancedNode.leftchild.rightchild
    NewRoot.rightchild = DislabancedNode
    DislabancedNode.height = 1 + max(
        GetHeight(DislabancedNode.leftchild), GetHeight(DislabancedNode.rightchild)
    )
    NewRoot.height = 1 + max(
        GetHeight(NewRoot.leftchild), GetHeight(NewRoot.rightchild)
    )
    return NewRoot


def LeftRotate(DislabancedNode):
    NewRoot = DislabancedNode.rightchild
    DislabancedNode.rightchild = DislabancedNode.rightchild.leftchild
    NewRoot.leftchild = DislabancedNode
    DislabancedNode.height = 1 + max(
        GetHeight(DislabancedNode.leftchild), GetHeight(DislabancedNode.rightchild)
    )
    NewRoot.height = 1 + max(
        GetHeight(NewRoot.leftchild), GetHeight(NewRoot.rightchild)
    )
    return NewRoot


def InsertNode(RootNode, NodeValue):
    if not RootNode:
        return AVL_Node(NodeValue)
    elif NodeValue < RootNode.data:
        RootNode.leftchild = InsertNode(RootNode.leftchild, NodeValue)
    else:
        RootNode.rightchild = InsertNode(RootNode.rightchild, NodeValue)
    RootNode.height = 1 + max(
        GetHeight(RootNode.leftchild), GetHeight(RootNode.rightchild)
    )
    balance = GetBalance(RootNode)
    if balance > 1 and NodeValue < RootNode.leftchild.data:
        return RightRotate(RootNode)
    if balance > 1 and NodeValue > RootNode.leftchild.data:
        RootNode.leftchild = LeftRotate(RootNode.leftchild)
        return RightRotate(RootNode)
    if balance < -1 and NodeValue < RootNode.rightchild.data:
        RootNode.rightchild = RightRotate(RootNode.rightchild)
        return LeftRotate(RootNode)
    if balance < -1 and NodeValue > RootNode.rightchild.data:
        return LeftRotate(RootNode)
    return RootNode


def LevelorderTraversal(RootNode):
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


New_AVL = AVL_Node(5)
New_AVL = InsertNode(New_AVL, 10)
New_AVL = InsertNode(New_AVL, 20)
New_AVL = InsertNode(New_AVL, 30)
New_AVL = InsertNode(New_AVL, 40)
New_AVL = InsertNode(New_AVL, 50)
New_AVL = InsertNode(New_AVL, 60)
New_AVL = InsertNode(New_AVL, 70)
LevelorderTraversal(New_AVL)
