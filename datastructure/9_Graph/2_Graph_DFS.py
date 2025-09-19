def dfs(graph, node, visited=None, result=None):
    if visited is None:
        visited = set()
    if result is None:
        result = []

    visited.add(node)          # Mark node as visited
    result.append(node)        # Process the node (record or print)

    for neighbor in graph.get(node, []):
        if neighbor not in visited:
            dfs(graph, neighbor, visited, result)  # Recursive call on unvisited neighbors

    return result

# Example graph as adjacency list (dict)
graph = {
    'A': ['B', 'C'],
    'B': ['D', 'E'],
    'C': ['F'],
    'D': [],
    'E': [],
    'F': []
}

print("DFS Traversal Order:", dfs(graph, 'A'))
