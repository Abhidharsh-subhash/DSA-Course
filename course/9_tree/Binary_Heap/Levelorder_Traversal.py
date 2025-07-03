class BinaryHeap:
    def __init__(self, size):
        self.MaxSize = size + 1
        self.CustomList = self.MaxSize * [None]
        self.HeapSize = 0


Heap = BinaryHeap(10)


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


def LevelorderTraversal(RootNode):
    if not RootNode:
        return
    else:
        for i in range(1, RootNode.HeapSize + 1):
            print(RootNode.CustomList[i])


def HeapifyTreeInsert(RootNode, Index, HeapType):
    parent = int(Index / 2)
    if Index <= 1:
        return
    if HeapType == "Min":
        if RootNode.CustomList[Index] < RootNode.CustomList[parent]:
            RootNode.CustomList[Index], RootNode.CustomList[parent] = (
                RootNode.CustomList[parent],
                RootNode.CustomList[Index],
            )
        HeapifyTreeInsert(RootNode, parent, HeapType)
    elif HeapType == "Max":
        if RootNode.CustomList[Index] > RootNode.CustomList[parent]:
            RootNode.CustomList[Index], RootNode.CustomList[parent] = (
                RootNode.CustomList[parent],
                RootNode.CustomList[Index],
            )
        HeapifyTreeInsert(RootNode, parent, HeapType)


def InsertNode(RootNode, NodeValue, HeapType):
    if RootNode.HeapSize + 1 == RootNode.MaxSize:
        return "The Binary Heap is full"
    RootNode.CustomList[RootNode.HeapSize + 1] = NodeValue
    RootNode.HeapSize += 1
    HeapifyTreeInsert(RootNode, RootNode.HeapSize, HeapType)
    return "Node inserted successfully"


NewHeap = BinaryHeap(5)
InsertNode(NewHeap, 4, "Max")
InsertNode(NewHeap, 5, "Max")
InsertNode(NewHeap, 2, "Max")
InsertNode(NewHeap, 1, "Max")
LevelorderTraversal(NewHeap)
