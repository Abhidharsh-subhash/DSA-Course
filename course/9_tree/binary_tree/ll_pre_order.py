class TreeNode:
    def __init__(self, value):
        self.leftchild = None
        self.value = value
        self.rightchild = None


n1 = TreeNode("n1")
n2 = TreeNode("n2")
n3 = TreeNode("n3")
n4 = TreeNode("n4")
n5 = TreeNode("n5")
n6 = TreeNode("n6")
n7 = TreeNode("n7")
n8 = TreeNode("n8")
n9 = TreeNode("n9")
n10 = TreeNode("n10")
n1.leftchild = n2
n1.rightchild = n3
n2.leftchild = n4
n2.rightchild = n5
n4.leftchild = n9
n4.rightchild = n10
n3.leftchild = n6
n3.rightchild = n7


def preorder_traversal(rootnode):
    result = ""
    if not rootnode:
        return
    print(rootnode.value)
    preorder_traversal(rootnode.leftchild)
    preorder_traversal(rootnode.rightchild)
    return result


print(preorder_traversal(n1))
