class Graph:
    def __init__(self):
        self.adjanceny_list = {}

    def add_vertex(self, edge):
        if edge not in self.adjanceny_list.keys():
            self.adjanceny_list[edge] = []
            return "Vertex added successfully"
        else:
            return "Vertex already exists"

    def add_edge(self, vertex, edge):
        if edge and vertex in self.adjanceny_list.keys():
            self.adjanceny_list.get(vertex).append(edge)
            self.adjanceny_list.get(edge).append(vertex)
            return "Edge added successfully"
        else:
            return "You are trying with some Invalid values"

    def display(self):
        for vertex, edge in self.adjanceny_list.items():
            print(f"{vertex} : {edge}")


graph = Graph()
print(graph.add_vertex("A"))
print(graph.add_vertex("B"))
print(graph.add_vertex("C"))
print(graph.add_vertex("D"))
print(graph.add_vertex("E"))
print(graph.add_edge("A", "E"))
print(graph.add_edge("C", "D"))
print(graph.add_edge("D", "A"))
print(graph.add_edge("B", "C"))
print(graph.add_edge("C", "E"))
graph.display()
