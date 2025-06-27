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

    def IsEmpty(self):
        return True if self.linkedlist.head is None else False

    def Enqueue(self, NodeValue):
        NewNode = Node(NodeValue)
        if self.IsEmpty():
            self.linkedlist.head = self.linkedlist.tail = NewNode
        else:
            self.linkedlist.tail.next = self.linkedlist.tail = NewNode
        self.linkedlist.length += 1

    def Dequeue(self):
        if self.IsEmpty():
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
    return 0 if not RootNode else RootNode.height


def GetBalance(RootNode):
    return (
        0
        if not RootNode
        else GetHeight(RootNode.leftchild) - GetHeight(RootNode.rightchild)
    )


def LeftRotate(DisbalancedNode):
    NewRoot = DisbalancedNode.rightchild
    DisbalancedNode.rightchild = DisbalancedNode.rightchild.leftchild
    NewRoot.leftchild = DisbalancedNode
    DisbalancedNode.height = 1 + max(
        GetHeight(DisbalancedNode.leftchild), GetHeight(DisbalancedNode.rightchild)
    )
    NewRoot.height = 1 + max(
        GetHeight(NewRoot.leftchild), GetHeight(NewRoot.rightchild)
    )
    return NewRoot


def RightRotate(DisbalancedNode):
    NewRoot = DisbalancedNode.leftchild
    DisbalancedNode.leftchild = DisbalancedNode.leftchild.rightchild
    NewRoot.rightchild = DisbalancedNode
    DisbalancedNode.height = 1 + max(
        GetHeight(DisbalancedNode.leftchild), GetHeight(DisbalancedNode.rightchild)
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
    if balance < -1 and NodeValue > RootNode.rightchild.data:
        return LeftRotate(RootNode)
    if balance < -1 and NodeValue < RootNode.rightchild.data:
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


def Searching(RootNode, SearchNode):
    if not RootNode:
        print(False)
    elif RootNode.data == SearchNode:
        print(True)
    else:
        if SearchNode < RootNode.data:
            Searching(RootNode.leftchild, SearchNode)
        elif SearchNode > RootNode.data:
            Searching(RootNode.rightchild, SearchNode)


new_AVL = AVL_Node(5)
new_AVL = InsertNode(new_AVL, 10)
new_AVL = InsertNode(new_AVL, 20)
new_AVL = InsertNode(new_AVL, 30)
new_AVL = InsertNode(new_AVL, 40)
new_AVL = InsertNode(new_AVL, 50)
new_AVL = InsertNode(new_AVL, 60)
new_AVL = InsertNode(new_AVL, 70)
LevelorderTraversal(new_AVL)
print("searching")
Searching(new_AVL, 80)
