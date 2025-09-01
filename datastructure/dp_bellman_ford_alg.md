The Bellman-Ford algorithm finds the shortest paths from a single source vertex to all other vertices in a weighted, directed graph. Its key advantage over algorithms like Dijkstra's is that it can handle graphs with **negative edge weights**. It can also detect if the graph contains a **negative cycle**, which makes a shortest path undefined.

The algorithm works in two main phases:

1.  **Relaxation**: The algorithm repeatedly "relaxes" all edges in the graph. Relaxing an edge means checking if the path to its destination can be shortened by going through its source. This process is repeated $V-1$ times (where $V$ is the number of vertices) to ensure all possible paths are checked.
2.  **Negative Cycle Detection**: After the $V-1$ iterations, if we can still find an edge that can be relaxed, it means there is a **negative cycle** in the graph. This is because a negative cycle would continuously shorten the path length with each traversal, making a true "shortest" path impossible.

-----

### Bellman-Ford Algorithm Implementation in Python

This implementation uses a list of edges and their weights to represent the graph.

```python
# The main function that implements the Bellman-Ford algorithm.
def bellman_ford(edges, V, start_node):
    """
    Finds the shortest paths from a single source to all other vertices.

    Args:
        edges (list): A list of tuples representing the graph edges.
                      Each tuple is (source, destination, weight).
        V (int): The number of vertices in the graph.
        start_node: The starting vertex for the shortest path search.

    Returns:
        A list of shortest distances from the start node, or None if a negative cycle is found.
    """
    
    # Step 1: Initialize distances from the start node.
    # We use a list to store the minimum distance from the start node to each vertex.
    # Set the distance to all vertices to infinity, except for the start node.
    distances = [float('inf')] * V
    distances[start_node] = 0
    
    # Step 2: Relax all edges V-1 times.
    # A path in a graph with V vertices can have at most V-1 edges.
    # By repeating the relaxation process V-1 times, we guarantee that we find the
    # shortest path for all vertices, even with negative weights.
    for _ in range(V - 1):
        # Iterate over all edges in the graph.
        for u, v, w in edges:
            # The relaxation step.
            # If the distance to 'u' is not infinity and the path through 'u'
            # to 'v' is shorter than the current known distance to 'v',
            if distances[u] != float('inf') and distances[u] + w < distances[v]:
                # Update the distance to 'v'.
                distances[v] = distances[u] + w

    # Step 3: Check for negative cycles.
    # Run the relaxation process one more time. If any distance is updated,
    # it means a negative cycle exists, making the shortest path undefined.
    for u, v, w in edges:
        if distances[u] != float('inf') and distances[u] + w < distances[v]:
            print("Graph contains a negative weight cycle!")
            return None # Indicate a negative cycle was found.
            
    # Step 4: Print the results.
    print("Shortest distances from source", start_node, ":")
    for i in range(V):
        print(f"  Vertex {i}: {distances[i]}")
        
    return distances

# --- Example Usage ---
# Our graph has 5 vertices (0 to 4).
V = 5
# Define the edges as (source, destination, weight).
# This graph contains a negative cycle: 1 -> 2 -> 4 -> 1 with a total weight of -1.
example_edges = [
    (0, 1, -1),
    (0, 2, 4),
    (1, 2, 3),
    (1, 3, 2),
    (1, 4, 2),
    (3, 2, 5),
    (3, 1, 1),
    (4, 3, -3)
]

# Run the algorithm and check for a negative cycle.
bellman_ford(example_edges, V, 0)

# Another example without a negative cycle.
V2 = 5
example_edges_no_cycle = [
    (0, 1, 6),
    (0, 2, 7),
    (1, 2, 8),
    (1, 3, 5),
    (1, 4, -4),
    (2, 3, -3),
    (2, 4, 9),
    (3, 1, -2),
    (4, 0, 2),
    (4, 3, 7)
]
print("\n--- Running on a graph without a negative cycle ---")
bellman_ford(example_edges_no_cycle, V2, 0)
```2