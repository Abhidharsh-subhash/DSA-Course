class BinaryHeap:
    def __init__(self, size):
        self.MaxSize = size + 1
        self.HeapSize = 0
        self.CustomList = self.MaxSize * [None]


def peek(RootNode):
    if not RootNode:
        return
    else:
        return RootNode.CustomList[1]


# Time complexity : O(1)
# Space complexity : O(1)
