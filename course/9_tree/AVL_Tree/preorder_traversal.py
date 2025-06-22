class AVL_Node:
    def __init__(self, data=None):
        self.leftchild = None
        self.data = data
        self.rightchild = None
        self.height = 1


def PreorderTraversal(RootNode):
    if not RootNode:
        return
    else:
        print(RootNode.data)
        PreorderTraversal(RootNode.leftchild)
        PreorderTraversal(RootNode.rightchild)
