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
        print("word inserted successfully")

    def Search(self, word):
        current = self.root
        for i in word:
            node = current.children.get(i)
            if node is None:
                return False
            current = node
        return current.endofstring


NewTrie = Trie()
NewTrie.Insert("App")
NewTrie.Insert("Apple")
print(NewTrie.Search("Apple"))
