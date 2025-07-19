class Graph:
    def __init__(self, gdict):
        self.customlist = {} if gdict is None else gdict

    def dfs(self, start, end):
        queue = []
        queue.append([start])
        while queue:
            path = queue.pop(0)
            node = path[-1]
            if node == end:
                return path
            for adjacent in self.customlist.get(node, []):
                new_path = list(path)
                new_path.append(adjacent)
                queue.append(new_path)


customdict = {
    "a": ["b", "c"],
    "b": ["d", "g"],
    "c": ["d", "e"],
    "d": ["f"],
    "e": ["f"],
    "g": ["f"],
}
graph = Graph(customdict)
print(graph.dfs("a", "e"))
