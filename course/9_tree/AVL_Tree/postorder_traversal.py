class AVL_Node:
    def __init__(self, data=None):
        self.leftchild = None
        self.data = data
        self.rightchild = None
        self.height = None


def PostorderTraversal(RootNode):
    if not RootNode:
        return
    else:
        PostorderTraversal(RootNode.leftchild)
        PostorderTraversal(RootNode.rightchild)
        print(RootNode.data)
