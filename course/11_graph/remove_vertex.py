class Graph:
    def __init__(self):
        self.adjancency_list = {}

    def add_vertex(self, vertex):
        if vertex not in self.adjancency_list.keys():
            self.adjancency_list[vertex] = []
            return

    def add_edge(self, vertex, edge):
        if vertex and edge in self.adjancency_list.keys():
            self.adjancency_list.get(vertex).append(edge)
            self.adjancency_list.get(edge).append(vertex)
            return

    def remove_vertex(self, vertex):
        if vertex in self.adjancency_list.keys():
            for edge in self.adjancency_list[vertex]:
                if vertex in edge:
                    self.adjancency_list[edge].remove(vertex)
            self.adjancency_list.pop(vertex)
        return

    def display(self):
        for vertex, edge in self.adjancency_list.items():
            print(f"{vertex}: {edge}")


graph = Graph()
graph.add_vertex("A")
graph.add_vertex("B")
graph.add_vertex("C")
graph.add_vertex("D")
graph.add_vertex("E")
graph.add_edge("A", "E")
graph.add_edge("C", "D")
graph.add_edge("D", "A")
graph.add_edge("B", "C")
graph.add_edge("C", "E")
graph.display()
graph.remove_vertex("A")
graph.display()
