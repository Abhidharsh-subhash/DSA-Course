class TrieNode:
    def __init__(self):
        self.children = {}
        self.endofstring = False


class Trie:
    def __init__(self):
        self.root = TrieNode()

    def Insert(self, word):
        current = self.root
        for i in word:
            ch = i
            node = current.children.get(ch)
            if node is None:
                node = TrieNode()
                current.children.update({ch: node})
            current = node
        current.endofstring = True
        return "word inserted successfully"

    def Search(self, word):
        current = self.root
        for i in word:
            node = current.children.get(i)
            if node is None:
                return False
            current = node
        return current.endofstring


def DeleteString(root, word, index):
    ch = word[index]
    current = root.children.get(ch)
    canthisnodebedeleted = False

    # case1
    if len(current.children) > 1:
        DeleteString(current, word, index + 1)
        return False

    # case2
    if index == len(word) - 1:
        if len(current.children) >= 1:
            current.endofstring = False
            return False
        else:
            current.children.pop(ch)
            return True

    # case3
    if current.endofstring is True:
        DeleteString(current, word, index + 1)
        return False

    # case4
    canthisnodebedeleted = DeleteString(current, word, index + 1)
    if canthisnodebedeleted is True:
        root.children.pop(ch)
        return True
    else:
        return False


NewTrie = Trie()
print(NewTrie.Insert("Apple"))
print(NewTrie.Insert("App"))
DeleteString(NewTrie.root, "Apple", 0)
print(NewTrie.Search("Apple"))
