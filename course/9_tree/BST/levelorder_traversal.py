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

    def __str__(self):
        result = [str(x) for x in self.queue]
        return " ".join(result)

    def isEmpty(self):
        return True if self.queue.head is None else False

    def enqueue(self, new_value):
        new_node = Node(new_value)
        if self.queue.head is None:
            self.queue.head = self.queue.tail = new_node
        else:
            self.queue.tail.next = self.queue.tail = new_node

    def dequeue(self):
        if self.queue.head is None:
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


def Levelorder_Traversal(RootNode):
    if not RootNode:
        return
    else:
        pass


NewTree = BSTNode(None)
print(Levelorder_Traversal(NewTree))
print(InsertNode(NewTree, 70))
print(InsertNode(NewTree, 50))
print(InsertNode(NewTree, 90))
print(InsertNode(NewTree, 30))
print(InsertNode(NewTree, 60))
print(InsertNode(NewTree, 80))
print(InsertNode(NewTree, 100))
print(InsertNode(NewTree, 20))
print(InsertNode(NewTree, 40))
print("Traversal")
Levelorder_Traversal(NewTree)
