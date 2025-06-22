class AVL_Node:
    def __init__(self, data=None):
        self.leftchild = None
        self.data = data
        self.rightchild = None
        self.height = 1


def InorderTraversal(RootNode):
    if not RootNode:
        return
    else:
        InorderTraversal(RootNode.leftchild)
        print(RootNode.data)
        InorderTraversal(RootNode.rightchild)
