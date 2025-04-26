class BinaryTree:
    def __init__(self, size):
        self.tree = [None] * size
        self.LastUsedIndex = 0
        self.MaxSize = size

    def __str__(self):
        if self.LastUsedIndex == 0:
            return "Emtpy Tree"
        else:
            result = []
            for i in self.tree:
                if i is not None:
                    result.append(str(i))
            return " ".join(result)


BT = BinaryTree(10)
print(BT)
