class AVL_Node:
    def __init__(self, data=None):
        self.leftchild = None
        self.data = data
        self.rightchild = None
        self.height = 1


def Searching(RootNode, SearchValue):
    if RootNode.data == SearchValue:
        return True
    elif SearchValue < RootNode:
        if RootNode.leftchild.data == SearchValue:
            return True
        else:
            Searching(RootNode.leftchild, SearchValue)
    elif SearchValue > RootNode:
        if RootNode.rightchild.data == SearchValue:
            return True
        else:
            Searching(RootNode.rightchild, SearchValue)
    return False
