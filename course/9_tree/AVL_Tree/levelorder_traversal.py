# Queue implementation
class LL_Node:
    def __init__(self, data):
        self.data = data
        self.next = None


class Linked_List:
    def __init__(self):
        self.head = None
        self.tail = None
        self.length = 0

    def __iter__(self):
        start = self.head
        while start:
            yield start.data
            start = start.next


class Queue:
    def __init__(self):
        self.queue = Linked_List()

    def __str__(self):
        result = [str(x) for x in self.queue]
        return result

    def isEmpty(self):
        if self.queue.length == 0:
            return True
        return False

    def enqueue(self, data):
        new_node = LL_Node(data)
        if not self.queue.head:
            self.queue.head = self.queue.tail = new_node
        else:
            self.queue.tail.next = self.queue.tail = new_node
        self.queue.length += 1

    def dequeue(self):
        if not self.queue.head:
            return
        elif self.queue.head == self.queue.tail:
            popped_node = self.queue.head
            self.queue.head = self.queue.tail = None
            self.queue.length -= 1
            return popped_node
        else:
            popped_node = self.queue.head
            self.queue.head = self.queue.head.next
            self.queue.length -= 1
            return popped_node


class AVL_Node:
    def __init__(self, data=None):
        self.leftchild = None
        self.data = data
        self.rightchild = None
        self.height = 1


def Levelorder_Traversal(RootNode):
    if not RootNode:
        return
    else:
        tracking = Queue()
        Queue.enqueue(RootNode)
        while not tracking.isEmpty():
            root = tracking.dequeue()
            print(root.data.data)
            if root.data.leftchild is not None:
                tracking.enqueue(root.data.leftchild)
            if root.data.rightchild is not None:
                tracking.enqueue(root.data.rightchild)
