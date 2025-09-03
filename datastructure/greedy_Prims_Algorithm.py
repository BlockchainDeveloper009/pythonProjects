# Prim's Algorithm
# This implementation uses a priority queue (min-heap) to efficiently find the minimum-weight edge
# at each step. This approach is generally more efficient for sparse graphs.

import heapq


def prim(graph, start_vertex):
    """
    Finds the Minimum Spanning Tree (MST) of a weighted, undirected graph
    starting from a specified vertex.

    Args:
        graph (dict): The graph represented as an adjacency list.
                      Keys are vertices, and values are lists of tuples:
                      (neighbor, weight).
        start_vertex: The vertex to start the algorithm from.

    Returns:
        list: A list of edges (u, v) that form the MST. Returns an empty list
              if the graph is not connected.
    """
    # Check if the start_vertex exists in the graph
    if start_vertex not in graph:
        print(f"Error: Starting vertex '{start_vertex}' not in graph.")
        return []

    # 1. Initialize data structures
    # 'mst' will store the edges of our MST.
    mst = []

    # 'visited' keeps track of vertices already in the MST to prevent cycles.
    visited = set()

    # 'min_heap' is a priority queue that stores edges as tuples: (weight, u, v).
    # It ensures we always process the edge with the smallest weight.
    min_heap = []

    # 2. Start the algorithm
    # Add the starting vertex to the visited set.
    visited.add(start_vertex)

    # Push all edges from the start_vertex to the min-heap.
    for neighbor, weight in graph[start_vertex]:
        heapq.heappush(min_heap, (weight, start_vertex, neighbor))

    # 3. Main loop to build the MST
    # The loop continues as long as we have edges to explore and haven't
    # included all vertices (V-1 edges for a connected graph).
    while min_heap:
        # Get the edge with the minimum weight from the heap.
        weight, u, v = heapq.heappop(min_heap)

        # 4. Check if the edge forms a cycle
        # An edge (u, v) forms a cycle if v is already in the visited set.
        # We only want to add edges that connect a visited vertex (u) to an unvisited one (v).
        if v not in visited:
            # Add the edge to our MST.
            mst.append((u, v, weight))

            # Add the newly reached vertex (v) to the visited set.
            visited.add(v)

            # 5. Explore new edges
            # Now, push all edges from the newly added vertex (v) to the heap.
            # This ensures we consider all possible connections from the growing MST.
            if v in graph:
                for neighbor, edge_weight in graph[v]:
                    if neighbor not in visited:
                        heapq.heappush(min_heap, (edge_weight, v, neighbor))

    # 6. Return the result
    # If len(mst) is less than the total number of vertices minus 1, it means
    # the graph is not connected, and an MST spanning all vertices does not exist.
    if len(mst) == len(graph) - 1:
        return mst
    else:
        return []  # Return an empty list for a disconnected graph


# Example usage:
if __name__ == '__main__':
    # Define a graph using an adjacency list.
    graph = {
        'A': [('B', 2), ('D', 4)],
        'B': [('A', 2), ('C', 3), ('D', 1)],
        'C': [('B', 3), ('E', 5)],
        'D': [('A', 4), ('B', 1), ('E', 6)],
        'E': [('C', 5), ('D', 6)]
    }

    # Example 1: Find the MST of the connected graph
    mst_result = prim(graph, 'A')
    print("Minimum Spanning Tree Edges for a connected graph:")
    if mst_result:
        for u, v, w in mst_result:
            print(f"Edge: {u}-{v}, Weight: {w}")
    else:
        print("Graph is not connected.")

    # Example 2: Test with a disconnected graph
    disconnected_graph = {
        'A': [('B', 1)],
        'B': [('A', 1)],
        'C': [('D', 2)],
        'D': [('C', 2)]
    }

    mst_disconnected_result = prim(disconnected_graph, 'A')
    print("\nMinimum Spanning Tree Edges for a disconnected graph:")
    if mst_disconnected_result:
        for u, v, w in mst_disconnected_result:
            print(f"Edge: {u}-{v}, Weight: {w}")
    else:
        print("Graph is not connected.")