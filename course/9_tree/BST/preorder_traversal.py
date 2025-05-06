class BSTNode:
    def __init__(self, data):
        self.leftchild = None
        self.data = data
        self.rightchild = None


def insert(RootNode, NodeValue):
    if RootNode.data is None:
        RootNode.data = NodeValue
    elif NodeValue <= RootNode.data:
        if RootNode.leftchild is None:
            RootNode.leftchild = BSTNode(NodeValue)
        else:
            insert(RootNode.leftchild, NodeValue)
    else:
        if RootNode.rightchild is None:
            RootNode.rightchild = BSTNode(NodeValue)
        else:
            insert(RootNode.rightchild, NodeValue)
    return "Node inserted successfully"


def PreorderTraversal(RootNode):
    if not RootNode:
        return "Empty Tree"
    else:
        print(RootNode.data)
        PreorderTraversal(RootNode.leftchild)
        PreorderTraversal(RootNode.rightchild)


NewTree = BSTNode(None)
print(PreorderTraversal(NewTree))
print(insert(NewTree, 70))
print(insert(NewTree, 50))
print(insert(NewTree, 90))
print(insert(NewTree, 30))
print(insert(NewTree, 60))
print(insert(NewTree, 80))
print(insert(NewTree, 100))
print(insert(NewTree, 20))
print(insert(NewTree, 40))
print("Traversal")
PreorderTraversal(NewTree)
