class Graph:
    def __init__(self):

        self.adjacency_list = {}

    def add_vertex(self, vertex):

        if vertex not in self.adjacency_list:
            self.adjacency_list[vertex] = []

    def add_edge(self, vertex1, vertex2):

        if vertex1 in self.adjacency_list and vertex2 in self.adjacency_list:
            self.adjacency_list[vertex1].append(vertex2)
            self.adjacency_list[vertex2].append(vertex1)

    def remove_edge(self, vertex1, vertex2):

        if vertex1 in self.adjacency_list and vertex2 in self.adjacency_list:
            if vertex2 in self.adjacency_list[vertex1]:
                self.adjacency_list[vertex1].remove(vertex2)
            if vertex1 in self.adjacency_list[vertex2]:
                self.adjacency_list[vertex2].remove(vertex1)

    def remove_vertex(self, vertex):

        if vertex in self.adjacency_list:
            for adjacent in self.adjacency_list[vertex]:
                self.adjacency_list[adjacent].remove(vertex)
            del self.adjacency_list[vertex]

    def __str__(self):

        return str(self.adjacency_list)


graph = Graph()
graph.add_vertex("A")
graph.add_vertex("B")
graph.add_vertex("C")
graph.add_edge("A", "B")
graph.add_edge("A", "C")
graph.add_edge("B", "C")

print("Граф:")
print(graph)

graph.remove_edge("A", "B")
print("\nГраф после удаления ребра A-B:")
print(graph)

graph.remove_vertex("C")
print("\nГраф после удаления вершины C:")
print(graph)