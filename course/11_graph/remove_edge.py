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

    def remove_edge(self, vertex1, vertex2):
        if vertex1 and vertex2 in self.adjancency_list.keys():
            if vertex2 in self.adjancency_list.get(vertex1):
                self.adjancency_list.get(vertex1).remove(vertex2)
            if vertex1 in self.adjancency_list.get(vertex2):
                self.adjancency_list.get(vertex2).remove(vertex1)
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
graph.remove_edge("A", "D")
graph.display()
