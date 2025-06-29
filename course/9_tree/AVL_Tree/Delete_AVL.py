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
            yield current.data
            current = current.next


class Queue:
    def __init__(self):
        self.linkedlist = LinkedList()

    def __str__(self):
        result = [str(x) for x in self.linkedlist]
        return " ".join(result)

    def IsEmpty(self):
        return True if self.linkedlist.head is None else False

    def Enqueue(self, data):
        New_Node = Node(data)
        if self.IsEmpty():
            self.linkedlist.head = self.linkedlist.tail = New_Node
        else:
            self.linkedlist.tail.next = self.linkedlist.tail = New_Node
        self.linkedlist.length += 1

    def Dequeue(self):
        if self.IsEmpty():
            return
        elif self.linkedlist.head == self.linkedlist.tail:
            popped_node = self.linkedlist.head
            self.linkedlist.head = self.linkedlist.tail = None
            return popped_node
        else:
            popped_node = self.linkedlist.head
            self.linkedlist.head = self.linkedlist.head.next
            return popped_node


class AVL_Node:
    def __init__(self, data):
        self.leftchild = None
        self.data = data
        self.rightchild = None
        self.height = 1


def GetHeight(RootNode):
    return 0 if not RootNode else RootNode.height


def GetBalance(RootNode):
    return (
        0
        if not RootNode
        else GetHeight(RootNode.leftchild) - GetHeight(RootNode.rightchild)
    )


def RightRotate(RootNode):
    NewRoot = RootNode.leftchild
    RootNode.leftchild = RootNode.leftchild.rightchild
    NewRoot.rightchild = RootNode
    RootNode.height = 1 + max(
        GetHeight(RootNode.leftchild), GetHeight(RootNode.rightchild)
    )
    NewRoot.height = 1 + max(
        GetHeight(RootNode.leftchild), GetHeight(RootNode.rightchild)
    )
    return NewRoot


def LeftRotate(RootNode):
    NewRoot = RootNode.rightchild
    RootNode.rightchild = RootNode.rightchild.leftchild
    NewRoot.leftchild = RootNode
    RootNode.height = 1 + max(
        GetHeight(RootNode.leftchild), GetHeight(RootNode.rightchild)
    )
    NewRoot.height = 1 + max(
        GetHeight(RootNode.leftchild), GetHeight(RootNode.rightchild)
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
        RootNode.rightchild = LeftRotate(RootNode.rightchild)
        return RightRotate(RootNode)
    if balance < -1 and NodeValue > RootNode.rightchild.data:
        return LeftRotate(RootNode)
    if balance < -1 and NodeValue < RootNode.rightchild.data:
        RootNode.rightchild = RightRotate(RootNode.rightchild)
        return LeftRotate(RootNode)
    return RootNode


def GetSuccessor(RootNode):
    if not RootNode or RootNode.leftchild is None:
        return RootNode
    else:
        GetSuccessor(RootNode.leftchild)


def DeleteNode(RootNode, NodeValue):
    if not RootNode:
        return
    elif NodeValue < RootNode.data:
        RootNode.leftchild = DeleteNode(RootNode.leftchild, NodeValue)
    elif NodeValue > RootNode.data:
        RootNode.rightchild = DeleteNode(RootNode.rightchild, NodeValue)
    else:
        if RootNode.leftchild is None:
            temp = RootNode.rightchild
            RootNode = None
            return temp
        elif RootNode.rightchild is None:
            temp = RootNode.leftchild
            RootNode = None
            return temp
        else:
            temp = GetSuccessor(RootNode.rightchild)
            RootNode.data = temp.data
            RootNode.rightchild = DeleteNode(RootNode.rightchild, NodeValue)
    RootNode.height = 1 + max(
        GetHeight(RootNode.leftchild), GetHeight(RootNode.rightchild)
    )
    balance = GetBalance(RootNode)
    if balance > 1 and GetBalance(RootNode.leftchild) >= 0:
        return RightRotate(RootNode)
    if balance > 1 and GetBalance(RootNode.leftchild) < 0:
        RootNode.leftchild = LeftRotate(RootNode.leftchild)
        return RightRotate(RootNode)
    if balance < -1 and GetBalance(RootNode.rightchild) <= 0:
        return LeftRotate(RootNode)
    if balance < -1 and GetBalance(RootNode.rightchild) > 0:
        RootNode.rightchild = RightRotate(RootNode.rightchild)
        return LeftRotate(RootNode)
    return RootNode


def LevelorderTraversal(RootNode):
    if not RootNode:
        return
    else:
        tracking = Queue()
        tracking.Enqueue(RootNode)
        while not tracking.IsEmpty():
            root = tracking.Dequeue()
            print(root.value.data)
            if root.value.leftchild is not None:
                tracking.Enqueue(root.value.leftchild)
            if root.value.rightchild is not None:
                tracking.Enqueue(root.value.rightchild)


New_AVL = AVL_Node(5)
New_AVL = InsertNode(New_AVL, 10)
New_AVL = InsertNode(New_AVL, 20)
New_AVL = InsertNode(New_AVL, 30)
New_AVL = InsertNode(New_AVL, 40)
New_AVL = InsertNode(New_AVL, 50)
New_AVL = InsertNode(New_AVL, 60)
New_AVL = InsertNode(New_AVL, 70)
print("Levelorder Traversal")
LevelorderTraversal(New_AVL)
New_AVL = DeleteNode(New_AVL, 60)
New_AVL = DeleteNode(New_AVL, 70)
print("after deletion")
LevelorderTraversal(New_AVL)
