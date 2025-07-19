from collections import defaultdict


class Graph:
    def __init__(self, noofvertices):
        self.graph = defaultdict(list)
        self.noofvertices = noofvertices

    def addedge(self, vertex, edge):
        self.graph[vertex].append(edge)

    def topologicalsortutil(self, v, visited, stack):
        visited.append(v)

        for i in self.graph[v]:
            if i not in visited:
                self.topologicalsortutil(i, visited, stack)

        stack.insert(0, v)

    def topologicalsort(self):
        visited = []
        stack = []

        for i in list(self.graph):
            if i not in visited:
                self.topologicalsortutil(i, visited, stack)

        print(stack)


customgraph = Graph(8)
customgraph.addedge("A", "C")
customgraph.addedge("C", "E")
customgraph.addedge("E", "H")
customgraph.addedge("E", "F")
customgraph.addedge("F", "G")
customgraph.addedge("B", "D")
customgraph.addedge("B", "C")
customgraph.addedge("D", "F")

customgraph.topologicalsort()
