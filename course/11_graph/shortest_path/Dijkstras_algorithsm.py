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

    def __str__(self):
        return self.name

    def __lt__(self, other_vertex):
        return self.min_distance < other_vertex.min_distance

    def addEdge(self, weight, desination_vertex):
        edge = Edge(weight, self, desination_vertex)
        self.neighbours.append(edge)


# Djikstra Algorithtm
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

    def get_shortest_path(self, vertex):
        print(f"the shortest distance to the vertex is {vertex.min_distance}")
        path = []
        actual_vertex = vertex
        while actual_vertex is not None:
            path.insert(0, actual_vertex.name)
            actual_vertex = actual_vertex.predecessor
        return path


# Step-1
nodeA = Node("A")
nodeB = Node("B")
nodeC = Node("C")
nodeD = Node("D")
nodeE = Node("E")
nodeF = Node("F")
nodeG = Node("G")
nodeH = Node("H")

# Step-2
nodeA.addEdge(6, nodeB)
nodeA.addEdge(10, nodeC)
nodeA.addEdge(9, nodeD)

nodeB.addEdge(16, nodeE)
nodeB.addEdge(13, nodeF)
nodeB.addEdge(5, nodeD)

nodeC.addEdge(6, nodeD)
nodeC.addEdge(21, nodeG)
nodeC.addEdge(5, nodeH)

nodeD.addEdge(8, nodeF)
nodeD.addEdge(7, nodeH)

nodeE.addEdge(10, nodeG)

nodeF.addEdge(4, nodeE)
nodeF.addEdge(12, nodeG)

nodeH.addEdge(2, nodeF)
nodeH.addEdge(14, nodeG)

algorithm = Djikstra()
algorithm.calculate(nodeA)
print(algorithm.get_shortest_path(nodeB))
