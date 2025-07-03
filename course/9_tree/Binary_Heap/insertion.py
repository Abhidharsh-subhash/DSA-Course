class BinaryHeap:
    def __init__(self, size):
        self.maxsize = size + 1
        self.customlist = self.maxsize * [None]
        self.heapsize = 0


def peek(rootnode):
    if not rootnode:
        return
    else:
        return rootnode.customlist[1]


def HeapSize(rootnode):
    if not rootnode:
        return
    else:
        return rootnode.heapsize


def levelordertraversal(rootnode):
    if not rootnode:
        return
    else:
        for i in range(1, rootnode.heapsize + 1):
            print(rootnode.customlist[i])


def heapifytree(rootnode, index, heaptype):
    parent = int(index / 2)
    if index <= 1:
        return
    if heaptype == "Max":
        if rootnode.customlist[index] > rootnode.customlist[parent]:
            rootnode.customlist[index], rootnode.customlist[parent] = (
                rootnode.customlist[parent],
                rootnode.customlist[index],
            )
        heapifytree(rootnode, parent, heaptype)
    elif heaptype == "Min":
        if rootnode.customlist[index] < rootnode.customlist[parent]:
            rootnode.customlist[index], rootnode.customlist[parent] = (
                rootnode.customlist[parent],
                rootnode.customlist[index],
            )
        heapifytree(rootnode, parent, heaptype)


def Insert(rootnode, nodevalue, heaptype):
    if rootnode.heapsize + 1 == rootnode.maxsize:
        return "Binary heap is full"
    else:
        rootnode.customlist[rootnode.heapsize + 1] = nodevalue
        rootnode.heapsize += 1
        heapifytree(rootnode, rootnode.heapsize, heaptype)
        return "Node inserted successfully"


NewHeap = BinaryHeap(5)
Insert(NewHeap, 4, "Min")
Insert(NewHeap, 5, "Min")
Insert(NewHeap, 2, "Min")
Insert(NewHeap, 1, "Min")
levelordertraversal(NewHeap)
