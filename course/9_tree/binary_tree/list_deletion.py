class BinaryTree:
    def __init__(self, size):
        self.tree = [None] * size
        self.MaxSize = size
        self.LastUsedIndex = 0

    def __str__(self):
        if self.LastUsedIndex == 0:
            return "Empty Tree"
        result = ""
        for i in range(1, self.LastUsedIndex + 1):
            result += f" {self.tree[i]}"
        return result

    def insert(self, value):
        if self.LastUsedIndex + 1 == self.MaxSize:
            return "Tree is full"
        self.LastUsedIndex += 1
        self.tree[self.LastUsedIndex] = value

    def levelordertraversal(self):
        for i in range(1, self.LastUsedIndex + 1):
            print(self.tree[i])

    def delete_node(self, value):
        if self.LastUsedIndex == 0:
            return "Empty Tree"
        for i in range(1, self.LastUsedIndex + 1):
            if self.tree[i] == value:
                self.tree[i] = self.tree[self.LastUsedIndex]
                self.tree[self.LastUsedIndex] = None
                self.LastUsedIndex -= 1
                return "node deleted successfully"
        return "node deletion failed"


BT = BinaryTree(10)
BT.insert("n1")
BT.insert("n2")
BT.insert("n3")
BT.insert("n4")
print(BT)
print(BT.delete_node("n2"))
BT.levelordertraversal()
