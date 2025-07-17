class Graph:
    def __init__(self, gdict=None):
        self.gdict = {} if gdict is None else gdict

    def addvertex(self, vertex):
        if vertex not in self.gdict.keys():
            self.gdict[vertex] = []
            return "Vertex inserted successfully"
        else:
            return "Vertex already exist"

    def addedge(self, vertex, edge):
        self.gdict.get(vertex).append(edge)
        return "edge added successfully"

    def __str__(self):
        return str(self.gdict)

    def printgraph(self):
        for vertex, edge in self.gdict.items():
            print(f"{vertex} : {edge}")


# customdict = {
#     "a": ["b", "c"],
#     "b": ["a", "d", "e"],
#     "c": ["a", "e"],
#     "d": ["b", "e", "f"],
#     "e": ["d", "f"],
#     "f": ["d", "e"],
# }
# graph = Graph(customdict)
graph = Graph()
graph.addvertex("A")
graph.printgraph()
# graph.addedge("a", "f")
# print(graph)
