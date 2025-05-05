class BSTNode:
    def __init__(self, data):
        self.leftchild = None
        self.data = data
        self.rightchild = None


def InsertNode(rootNode, NodeValue):
    if rootNode.data is None:
        rootNode.data = NodeValue
    elif NodeValue <= rootNode.data:
        if rootNode.leftchild is None:
            rootNode.leftchild = BSTNode(NodeValue)
        else:
            InsertNode(rootNode.leftchild, NodeValue)
    else:
        if rootNode.rightchild is None:
            rootNode.rightchild = BSTNode(NodeValue)
        else:
            InsertNode(rootNode.rightchild, NodeValue)
    return "Node has been successfully inserted"


# Time Complexity is O(logN)
# Space Complexity is O(logN)  becase here when we are calling a method recursively we are going to push a log(n) number of elements to the stack memory.

newBST = BSTNode(None)
print(InsertNode(newBST, 30))
print(InsertNode(newBST, 10))
print(InsertNode(newBST, 40))
print(InsertNode(newBST, 35))
