class Edge:
    def __init__(self, weight, start_vertex, end_vertex):
        self.weight = weight
        self.start_vertex = start_vertex
        self.end_vertex = end_vertex


class Node:
    def __init__(self, name):
        self.name = name
        self.visited = False
        # previous node where we come to this node
        self.predecessor = None
        self.neighbours = []
        self.min_distance = float("inf")

    def __lt__(self, other_vertex):
        return self.min_distance < other_vertex.min_distance

    def addEdge(self, weight, desination_vertex):
        edge = Edge(weight, self, desination_vertex)
        self.neighbours.append(edge)
