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


def heapsize(rootnode):
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
    elif heaptype == "Min":
        if rootnode.customlist[parent] > rootnode.customlist[index]:
            rootnode.customlist[parent], rootnode.customlist[index] = (
                rootnode.customlist[index],
                rootnode.customlist[parent],
            )
        heapifytree(rootnode, parent, heaptype)
    elif heaptype == "Max":
        if rootnode.customlist[parent] < rootnode.customlist[index]:
            rootnode.customlist[parent], rootnode.customlist[index] = (
                rootnode.customlist[index],
                rootnode.customlist[parent],
            )
        heapifytree(rootnode, parent, heaptype)


def insert(rootnode, nodevalue, heaptype):
    if rootnode.heapsize + 1 == rootnode.maxsize:
        return "Binary heap is full"
    else:
        rootnode.customlist[rootnode.heapsize + 1] = nodevalue
        rootnode.heapsize += 1
        heapifytree(rootnode, rootnode.heapsize, heaptype)


def heapifytreeextract(rootnode, index, heaptype):
    leftchild_index = index * 2
    rightchild_index = (index * 2) + 1
    swapchild = 0
    if rootnode.heapsize < leftchild_index:
        return
    elif rootnode.heapsize == leftchild_index:
        if heaptype == "Min":
            if rootnode.customlist[index] > rootnode.customlist[leftchild_index]:
                rootnode.customlist[index], rootnode.customlist[leftchild_index] = (
                    rootnode.customlist[leftchild_index],
                    rootnode.customlist[index],
                )
            return
        else:
            if rootnode.customlist[index] < rootnode.customlist[leftchild_index]:
                rootnode.customlist[index], rootnode.customlist[leftchild_index] = (
                    rootnode.customlist[leftchild_index],
                    rootnode.customlist[index],
                )
            return
    else:
        if heaptype == "Min":
            if (
                rootnode.customlist[leftchild_index]
                > rootnode.customlist[rightchild_index]
            ):
                swapchild = rightchild_index
            else:
                swapchild = leftchild_index
            if rootnode.customlist[index] > rootnode.customlist[swapchild]:
                rootnode.customlist[index], rootnode.customlist[swapchild] = (
                    rootnode.customlist[swapchild],
                    rootnode.customlist[index],
                )
        else:
            if (
                rootnode.customlist[leftchild_index]
                < rootnode.customlist[rightchild_index]
            ):
                swapchild = rightchild_index
            else:
                swapchild = leftchild_index
            if rootnode.customlist[index] < rootnode.customlist[swapchild]:
                rootnode.customlist[index], rootnode.customlist[swapchild] = (
                    rootnode.customlist[swapchild],
                    rootnode.customlist[index],
                )
        heapifytreeextract(rootnode, swapchild, heaptype)


def extractNode(rootnode, heaptype):
    if rootnode.heapsize == 0:
        return
    else:
        extract_node = rootnode.customlist[1]
        rootnode.customlist[1] = rootnode.customlist[rootnode.heapsize]
        rootnode.customlist[rootnode.heapsize] = None
        rootnode.heapsize -= 1
        heapifytreeextract(rootnode, 1, heaptype)
        return extract_node


NewHeap = BinaryHeap(5)
insert(NewHeap, 4, "Min")
insert(NewHeap, 5, "Min")
insert(NewHeap, 2, "Min")
insert(NewHeap, 1, "Min")
levelordertraversal(NewHeap)
print("after extraction")
extractNode(NewHeap, "Min")
levelordertraversal(NewHeap)
