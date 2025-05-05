class BSTNode:
    def __init__(self, data):
        self.leftchild = None
        self.data = data
        self.rightchild = None

    def __str__(self):
        return str(self.data)


BST = BSTNode(1)
print(BST)
