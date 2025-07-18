class Graph:
    def __init__(self):
        self.adjacency_list = {}

    def add_vertex(self, vertex):
        if vertex not in self.adjacency_list.keys():
            self.adjacency_list[vertex] = []
        return

    def add_edge(self, vertex1, vertex2):
        if vertex1 and vertex2 in self.adjacency_list.keys():
            self.adjacency_list.get(vertex1).append(vertex2)
            self.adjacency_list.get(vertex2).append(vertex1)
        return

    def display(self):
        for vertex, edge in self.adjacency_list.items():
            print(f"{vertex}: {edge}")

    def dfs(self, vertex):
        visited = set()
        stack = [vertex]
        visited.add(vertex)
        while stack:
            current = stack.pop()
            print(current)
            for vertex in self.adjacency_list.get(current):
                if vertex not in visited:
                    visited.add(vertex)
                    stack.append(vertex)
        return


graph = Graph()
graph.add_vertex("A")
graph.add_vertex("B")
graph.add_vertex("C")
graph.add_vertex("D")
graph.add_vertex("E")
graph.add_edge("A", "B")
graph.add_edge("A", "C")
graph.add_edge("B", "E")
graph.add_edge("E", "D")
graph.add_edge("D", "C")
graph.display()
print("DFS")
graph.dfs("A")
