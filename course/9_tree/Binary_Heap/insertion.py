class BinaryHeap:
    def __init__(self, size):
        self.MaxSize = size + 1
        self.CustomList = self.MaxSize * [None]
        self.HeapSize = 0


def peek(RootNode):
    if not RootNode:
        return
    else:
        return RootNode.CustomList[1]


def HeapSize(RootNode):
    if not RootNode:
        return
    else:
        return RootNode.HeapSize


def LevelOrderTraversal(RootNode):
    if not RootNode:
        return
    else:
        for i in range(1, RootNode.HeapSize + 1):
            print(RootNode.CustomList[i])
