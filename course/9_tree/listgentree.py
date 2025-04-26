class TreeNode:
    def __init__(self, data, children=[]):
        self.data = data
        self.children = children

    def __str__(self, level=0):
        ret = " " * level + str(self.data) + "\n"
        for chil in self.children:
            ret += chil.__str__(level + 1)
        return ret

    def addChild(self, childNode):
        self.children.append(childNode)


drinks = TreeNode("Drinks", [])
cold = TreeNode("Cold", [])
hot = TreeNode("Hot", [])
drinks.addChild(cold)
drinks.addChild(hot)
tea = TreeNode("tea", [])
coffee = TreeNode("coffee", [])
mojito = TreeNode("mojito", [])
cool_drinks = TreeNode("cool_drinks", [])
cold.addChild(mojito)
cold.addChild(cool_drinks)
hot.addChild(tea)
hot.addChild(coffee)
print(drinks)
