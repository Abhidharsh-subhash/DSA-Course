class BSTNode:
    def __init__(self, data):
        self.leftchild = None
        self.data = data
        self.rightchild = None


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


def Postorder_Traversal(RootNode):
    if not RootNode:
        return
    else:
        Postorder_Traversal(RootNode.leftchild)
        Postorder_Traversal(RootNode.rightchild)
        print(RootNode.data)


NewTree = BSTNode(None)
print(Postorder_Traversal(NewTree))
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
Postorder_Traversal(NewTree)
