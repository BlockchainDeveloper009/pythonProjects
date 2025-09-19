from collections import deque

"""
1. a que for the current layer of exploration
2. a loop to process each node
3. a branching step where nodes are added to queu
"""

def bfs(graph, start):
    visited = set()  # Set to track visited nodes
    queue = deque([start])  # Queue initialized with start node
    visited.add(start)
    order = []  # List to store BFS traversal order

    while queue:
        node = queue.popleft()  # Remove node from front of queue
        order.append(node)  # Process the node

        for neighbor in graph.get(node, []):
            if neighbor not in visited:
                visited.add(neighbor)  # Mark neighbor visited
                queue.append(neighbor)  # Enqueue neighbor

    return order


# Example graph as adjacency list
graph = {
    'A': ['B', 'C'],
    'B': ['D', 'E'],
    'C': ['F'],
    'D': [],
    'E': [],
    'F': []
}

print("BFS Traversal Order:", bfs(graph, 'A'))
"""
BFS Traversal Order: ['A', 'B', 'C', 'D', 'E', 'F']
"""