Prim's algorithm is a greedy algorithm used to find the **Minimum Spanning Tree (MST)** of a connected, undirected, and weighted graph. The MST is a subgraph that connects all the vertices together with the minimum possible total edge weight, without creating any cycles.

Think of it like building a network of roads to connect several towns. Each possible road has a cost (its weight), and your goal is to connect all the towns while spending the least amount of money. Prim's algorithm helps you by always choosing the cheapest new road that connects a town you've already connected to one you haven't yet.

The algorithm builds the MST **one vertex at a time** starting from a single, arbitrary vertex.

-----

### How Prim's Algorithm Works

The algorithm keeps track of two sets of vertices:

1.  **MST Set:** Vertices that are already part of your growing Minimum Spanning Tree.
2.  **Not-in-MST Set:** Vertices that are not yet connected.

Here are the step-by-step instructions:

1.  **Start with an empty MST.** Choose any starting vertex from the graph and add it to your MST Set.
2.  **Look at all edges** that connect a vertex in the MST Set to a vertex in the Not-in-MST Set.
3.  **Find the edge** with the **minimum weight** among all those edges.
4.  **Add this minimum-weight edge** and the new vertex it connects to the MST.
5.  **Repeat steps 2-4** until all vertices are in the MST Set.

A **priority queue** (like a min-heap) is the perfect data structure for this because it allows you to efficiently find the edge with the minimum weight in step 3.

-----

### Prim's Algorithm Implementation in Python

This implementation uses a `heapq` (Python's min-heap implementation for a priority queue) and a `set` to keep track of visited nodes.

```python
import heapq

# This function implements Prim's algorithm to find the Minimum Spanning Tree.
def prim(graph, start_node):
    """
    Finds the Minimum Spanning Tree of a graph using Prim's algorithm.

    Args:
        graph (dict): The graph represented as an adjacency list.
                      Example: {node: [(neighbor, weight), ...]}
        start_node: The node to start the algorithm from.
    """

    # A set to keep track of vertices already included in the MST.
    mst_set = set()
    
    # A priority queue (min-heap) to store edges with their weights.
    # The format is (weight, destination_node, source_node).
    # heapq.heappush automatically sorts by the first element (the weight).
    priority_queue = [(0, start_node, None)]
    
    # A dictionary to store the edges of the MST.
    # The format is {child_node: (parent_node, weight)}
    mst_edges = {}
    
    # The total weight of the MST.
    total_weight = 0

    # The main loop continues as long as there are nodes to consider.
    while priority_queue:
        # Get the edge with the minimum weight from the priority queue.
        weight, current_node, parent_node = heapq.heappop(priority_queue)

        # If the node has already been visited, skip it to avoid cycles.
        if current_node in mst_set:
            continue

        # Add the current node to our MST set.
        mst_set.add(current_node)
        
        # If it's not the start node, add the edge to our MST edges dictionary
        # and update the total weight.
        if parent_node is not None:
            mst_edges[current_node] = (parent_node, weight)
            total_weight += weight

        # Look at all neighbors of the current node.
        for neighbor, edge_weight in graph.get(current_node, []):
            # If a neighbor hasn't been visited yet,
            if neighbor not in mst_set:
                # Add it to the priority queue. This is how we find the next cheapest
                # edge that extends our MST to an unvisited node.
                heapq.heappush(priority_queue, (edge_weight, neighbor, current_node))

    # Print the resulting MST.
    print("Edges in the Minimum Spanning Tree:")
    for node, edge in mst_edges.items():
        print(f"  {edge[0]} -- {node} (Weight: {edge[1]})")
    print(f"\nTotal MST Weight: {total_weight}")

# --- Example Usage ---
# The graph is represented as an adjacency list with weights.
example_graph = {
    'A': [('B', 7), ('D', 5)],
    'B': [('A', 7), ('D', 9), ('C', 8), ('E', 7)],
    'C': [('B', 8), ('E', 5)],
    'D': [('A', 5), ('B', 9), ('E', 15), ('F', 6)],
    'E': [('B', 7), ('C', 5), ('D', 15), ('F', 8), ('G', 9)],
    'F': [('D', 6), ('E', 8), ('G', 11)],
    'G': [('E', 9), ('F', 11)]
}

# Run the algorithm starting from node 'A'.
prim(example_graph, 'A')
```

This video offers a visual explanation of Prim's algorithm that should help you follow the code and understand how the process unfolds.