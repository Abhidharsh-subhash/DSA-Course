class Graph:
    def __init__(self, vertices):
        self.V = vertices
        self.graph = []
        self.nodes = []

    def add_edge(self, s, d, w):
        self.graph.append[s, d, w]

    def add_node(self, value):
        self.nodes.append(value)

    def print_solution(self, dist):
        print("Vertex distance from source")
        for key, value in dist.items():
            print(" " + key, ": ", value)

    def BellmanFord(self, src):
        dist = {i: float("inf") for i in self.nodes}
        dist[src] = 0
