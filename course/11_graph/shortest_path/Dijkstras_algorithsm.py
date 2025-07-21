import heapq


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


# Djikstra Algoright
class Djikstra:
    def __init__(self):
        self.heap = []

    def calculate(self, start):
        start.min_distance = 0
        heapq.heappush(self.heap, start)

        while self.heap:
            # pop element with the lowest distance
            actual_vertex = heapq.heappop(self.heap)

            # consider the neightbours
            for edge in actual_vertex.neighbours:
                start = edge.start_vertex
                target = edge.end_vertex
                new_distance = start.min_distance + edge.weight
                if new_distance < target.min_distance:
                    target.min_distance = new_distance
                    target.predecessor = start
                    # update the heap
                    heapq.heappush(self.heap, target)
            actual_vertex.visited = True
