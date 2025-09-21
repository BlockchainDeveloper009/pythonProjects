from collections import defaultdict

class Graph:
    def __init__(self, edges):
        """
        Initializes the graph with a list of edges.
        """
        self.graph = self._buildGraph(edges)

    def _buildGraph(self, edges):
        """
        Private method to build the graph from edges.
        """
        graph = defaultdict(list)
        for edge in edges:
            if len(edge) >= 2:
                for i in range(len(edge) - 1):
                    graph[edge[i]].append(edge[i + 1])
        return graph

    def get_graph(self):
        """
        Returns the built graph dictionary.
        """
        return self.graph

    def print_output(self):
        """
        Prints the graph in a readable format.
        """
        for key, value in self.graph.items():
            print(f"'{key}': {value}")
        print("#=========================")




testcase1 = [
    ['i', 'j', 'h'],
    ['k', 'i'],
    ['m', 'k'],
    ['k', 'l'],
    ['o', 'n']
]

# Create an instance of the Graph class
my_graph = Graph(testcase1)

# Get and print the graph data
print("Graph data (from get_graph method):")
print(my_graph.get_graph())
print("\n")

# Use the class's own print method
print("Graph output (from print_output method):")
my_graph.print_output()
#=========================

testcase2 = [
    ['i', 'j'],
    ['k', 'i'],
    ['m', 'k'],
    ['k', 'l'],
    ['o', 'n']
]


# Create an instance of the Graph class
my_graph = Graph(testcase2)

# Get and print the graph data
print("Graph data (from get_graph method):")
print(my_graph.get_graph())
print("\n")

# Use the class's own print method
print("Graph output (from print_output method):")
my_graph.print_output()