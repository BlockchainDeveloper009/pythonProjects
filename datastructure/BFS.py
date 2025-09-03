from collections import deque

# This is our graph, represented as an adjacency list.
# A: [B, C] means that from node 'A', you can go to nodes 'B' and 'C'.
graph = {
    'A': ['B', 'C'],
    'B': ['D', 'E'],
    'C': ['F'],
    'D': [],
    'E': ['F'],
    'F': []
}
"""
     A
    / \
  B     C
  / \    \
  D  E -- F
"""

def bfs(graph, start_node):
    """
    Performs a Breadth-First Search on a graph.

    Args:
        graph (dict): The graph represented as an adjacency list.
        start_node: The node to start the traversal from.
    """
    # Create a queue and a set to keep track of visited nodes.
    # We use a deque for an efficient queue (fast appends and pops).
    visited = set()
    queue = deque([start_node])

    # Add the starting node to the visited set.
    visited.add(start_node)

    # The main loop continues as long as there are nodes to visit.
    while queue:
        # Get the first node from the queue and remove it.
        # This is the "breadth-first" part; we process the oldest node first.
        current_node = queue.popleft()
        print(current_node, end=' ') # Print the node we are currently visiting.

        # Look at all neighbors of the current node.
        for neighbor in graph[current_node]:
            # If the neighbor hasn't been visited yet,
            if neighbor not in visited:
                # Mark it as visited to prevent cycles and re-visiting.
                visited.add(neighbor)
                # Add the neighbor to the back of the queue to be processed later.
                queue.append(neighbor)

# --- Driver Code to test the BFS function ---
print("Following is the Breadth-First Search traversal:")
bfs(graph, 'A')
# Expected output: A B C D E F

# Example graph represented as an adjacency list in a dictionary
graph2 = {
    'A': ['B', 'C'],
    'B': ['A', 'D', 'E'],
    'C': ['A', 'F'],
    'D': ['B'],
    'E': ['B', 'F'],
    'F': ['C', 'E']
}
bfs(graph2, 'A')