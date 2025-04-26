class BinaryTree:
    def __init__(self, size):
        self.tree = [None] * size
        self.MaxSize = size
        self.LastUsedIndex = 0

    def __str__(self):
        if self.LastUsedIndex == 0:
            return "Empty Tree"
        result = ""
        for i in range(1, self.LastUsedIndex):
            if self.tree[i] is not None:
                result += f" {self.tree[i]}"
        return result

    def insert(self, value):
        if self.LastUsedIndex + 1 == self.MaxSize:
            return "Tree is full"
        self.LastUsedIndex += 1
        self.tree[self.LastUsedIndex] = value

    def preordertraversal(self, index):
        if index > self.LastUsedIndex:
            return
        print(self.tree[index])
        self.preordertraversal(index * 2)
        self.preordertraversal((index * 2) + 1)


BT = BinaryTree(10)
BT.insert("n1")
BT.insert("n2")
BT.insert("n3")
BT.insert("n4")
print(BT)
BT.preordertraversal(1)
