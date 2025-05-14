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
        while queue:
            root = queue.dequeue()
            print(root.value.data)
            if RootNode.value.leftchild is not None:
                queue.enqueue(RootNode.value.leftchild)
            if RootNode.value.rightchild is not None:
                queue.enqueue(RootNode.value.rightchild)


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


new_AVL = AVL_Node(10)
