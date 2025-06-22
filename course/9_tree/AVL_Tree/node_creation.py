class AVL_Node:
    def __init__(self, data=None):
        self.leftchild = None
        self.data = data
        self.rightchild = None
        self.height = 1  # To find whether this tree is balanced or not


new_AVL = AVL_Node(10)
