class BinaryHeap:
    def __init__(self, size):
        self.HeapSize = 0
        self.MaxSize = size + 1
        self.CustomList = self.MaxSize * [None]


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


# Time complexity : O(1)
# Space complexity : O(1)


Heap = BinaryHeap(10)
print(HeapSize(Heap))
