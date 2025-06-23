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
            self.linkedlist.length += 1
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


def RightRotate(RootNode):
    pass


def LeftRotate(RootNode):
    pass


def InsertNode(RootNode, NodeValue):
    pass


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
