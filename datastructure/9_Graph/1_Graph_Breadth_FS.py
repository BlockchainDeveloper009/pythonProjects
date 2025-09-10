from collections import deque


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
