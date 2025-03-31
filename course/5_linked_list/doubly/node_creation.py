class Node:
    def __init__(self, value):
        self.prev = None
        self.value = value
        self.next = None

    def __str__(self):
        return f"{self.prev} <- {self.value} -> {self.next}"


new_node = Node(6)
print(new_node)
