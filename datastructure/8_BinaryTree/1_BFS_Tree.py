from collections import deque

def bfs(graph, start):
    visited = set()             # To keep track of visited nodes
    queue = deque([start])      # Use deque for efficient pop from left
    order = []                  # Store the BFS traversal order

    while queue:
        node = queue.popleft()  # Remove the node from the front of the queue
        if node not in visited:
            visited.add(node)
            order.append(node)
            # Add all unvisited neighbors to the queue
            for neighbor in graph[node]:
                if neighbor not in visited:
                    queue.append(neighbor)
    return order

# Example usage:
graph = {
    'A': ['B', 'C'],
    'B': ['D', 'E'],
    'C': ['F'],
    'D': [],
    'E': ['F'],
    'F': []
}

print("BFS Traversal:", bfs(graph, 'A'))
