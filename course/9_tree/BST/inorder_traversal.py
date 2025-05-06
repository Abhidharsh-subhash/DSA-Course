class BSTNode:
    def __init__(self, data):
        self.leftchild = None
        self.data = data
        self.rightchild = None

    def __str__(self):
        return str(self.data)


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


def InorderTraversal(RootNode):
    if not RootNode:
        return "Empty Tree"
    else:
        InorderTraversal(RootNode.leftchild)
        print(RootNode.data)
        InorderTraversal(RootNode.rightchild)


NewTree = BSTNode(None)
print(InorderTraversal(NewTree))
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
InorderTraversal(NewTree)
