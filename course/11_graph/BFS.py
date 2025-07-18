class Node:
    def __init__(self, data):
        self.data = data
        self.next = None


class LinkedList:
    def __init__(self):
        self.head = None
        self.tail = None
        self.length = None

    def __iter__(self):
        current = self.head
        while current:
            yield current.data
            current = current.next


class Queue:
    def __init__(self):
        self.queue = LinkedList()

    def enqueue(self, value):
        node = Node(value)
        if self.queue.head is None:
            self.queue.head = self.queue.tail = node
        else:
            self.queue.tail.next = self.queue.tail = node
        return

    def dequeue(self):
        if self.queue.head is None:
            return
        elif self.queue.head == self.queue.tail:
            deletion_node = self.queue.head.value
            self.queue.head = self.queue.tail = None
            return deletion_node
        else:
            deletion_node = self.queue.head.value
            self.queue.head = self.queue.head.next
            return deletion_node


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

    def bfs(self, vertex):
        visited = set()
        visited.add(vertex)
        queue = [vertex]
        while queue:
            current = queue.pop(0)
            print(current)
            for edge in self.adjacency_list[current]:
                if edge not in visited:
                    visited.add(edge)
                    queue.append(edge)
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
print("BFS")
graph.bfs("A")
