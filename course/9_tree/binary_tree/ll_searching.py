class Node:
    def __init__(self, data):
        self.data = data
        self.next = None

    def __str__(self):
        return str(self.data)


class LinkedList:
    def __init__(self):
        self.head = self.tail = None

    def __iter__(self):
        node = self.head
        while node:
            yield node
            node = node.next


class Queue:
    def __init__(self):
        self.queue = LinkedList()

    def __str__(self):
        values = [str(x) for x in self.queue]
        return " ".join(values)

    def isEmpty(self):
        if self.queue.head is None:
            return True
        return False

    def enqueue(self, value):
        new_node = Node(value)
        if self.isEmpty():
            self.queue.head = self.queue.tail = new_node
        else:
            self.queue.tail.next = self.queue.tail = new_node

    def dequeue(self):
        if self.isEmpty():
            return "Empty queue"
        elif self.queue.head == self.queue.tail:
            popped_node = self.queue.head
            self.queue.head = self.queue.tail = None
            return popped_node
        popped_node = self.queue.head
        self.queue.head = self.queue.head.next
        return popped_node


class TreeNode:
    def __init__(self, value):
        self.leftchild = None
        self.value = value
        self.rightchild = None


n1 = TreeNode("n1")
n2 = TreeNode("n2")
n3 = TreeNode("n3")
n4 = TreeNode("n4")
n5 = TreeNode("n5")
n6 = TreeNode("n6")
n7 = TreeNode("n7")
n8 = TreeNode("n8")
n9 = TreeNode("n9")
n10 = TreeNode("n10")
n1.leftchild = n2
n1.rightchild = n3
n2.leftchild = n4
n2.rightchild = n5
n4.leftchild = n9
n4.rightchild = n10
n3.leftchild = n6
n3.rightchild = n7


def search(rootnode, search):
    if not rootnode:
        return
    customqueue = Queue()
    customqueue.enqueue(rootnode)
    while not customqueue.isEmpty():
        root = customqueue.dequeue()
        if root.data.value == search:
            return True
        else:
            if root.data.leftchild is not None:
                customqueue.enqueue(root.data.leftchild)
            if root.data.rightchild is not None:
                customqueue.enqueue(root.data.rightchild)
    return False


print(search(n1, "n10"))
