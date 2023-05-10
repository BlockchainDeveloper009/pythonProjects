class Graph:
    def __init__(self):
        self.graph_dict = {}

    def add_node(self, node):
        if node not in self.graph_dict:
            self.graph_dict[node] = []

    def add_edge(self, node1, node2):
        self.add_node(node1)
        self.add_node(node2)
        self.graph_dict[node1].append(node2)
        self.graph_dict[node2].append(node1)

    def __str__(self):
        return str(self.graph_dict)

# Example usage
graph = Graph()

graph.add_node('A')
graph.add_node('B')
graph.add_node('C')

graph.add_edge('A', 'B')
graph.add_edge('B', 'C')
graph.add_edge('A', 'C')

print(graph)  # Output: {'A': ['B', 'C'], 'B': ['A', 'C'], 'C': ['B', 'A']}
