from utils.metrics_time_helper import TimeHelper


# This script calculates the number of connected components in an undirected graph
# using a recursive depth-first search (DFS) approach.

class ConnectedRecur:
    """
    A class to find the number of connected components in a graph using recursion.
    """

    def connectedComponentCount(self, graph: dict) -> int:
        """
        Counts the total number of connected components in the graph.

        Args:
            graph: A dictionary representing the graph's adjacency list.

        Returns:
            The number of connected components.
        """
        visited = set()
        count = 0

        # Iterate through each node in the graph
        for node in graph:
            # If the node has not been visited, it's the start of a new component
            if node not in visited:
                # Explore the entire component starting from this node
                # The 'self' argument is handled implicitly by Python.
                self.explore(graph, node, visited)
                count += 1

        return count

    def explore(self, graph: dict, current: int, visited: set) -> None:
        """
        Recursively explores a single connected component using DFS.

        Args:
            graph: The graph's adjacency list.
            current: The current node being explored.
            visited: A set to keep track of visited nodes.
        """
        # Base case: if the node has already been visited, stop exploring
        if current in visited:
            return

        # Add the current node to the visited set
        visited.add(current)

        # Recursively explore all neighbors of the current node
        for neighbor in graph[current]:
            # The 'self' argument is handled implicitly by Python.
            self.explore(graph, neighbor, visited)


# --- Example Usage ---


t = TimeHelper()
recur = ConnectedRecur()
print(recur.connectedComponentCount(
    {
        0: [8, 1, 5],
        1: [0],
        5: [0, 8],
        8: [0, 5],
        2: [3, 4],
        3: [2, 4],
        4: [3, 2]
    }
)) # Output: 2

t.print_time_taken("Connected_Components_recur", t.start_time)
