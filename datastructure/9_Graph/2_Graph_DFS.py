
def dfs_recursive(graph, node, visited=None, result=None):
    if visited is None:
        visited = set()
    if result is None:
        result = []

    visited.add(node)          # Mark node as visited
    result.append(node)        # Process the node (record or print)

    for neighbor in graph.get(node, []):
        if neighbor not in visited:
            dfs_recursive(graph, neighbor, visited, result)  # Recursive call on unvisited neighbors

    return result

def dfs_hasPath_iterative(graph, node, dst)-> bool:
    stack = [node]
    result = []

    while stack:
        node = stack.pop()
        if node == dst:
            return True
        result.append(node)
        for neighbor in graph[node]:
            stack.append(neighbor)


    return False

# Example graph as adjacency list (dict)
graph = {
    'A': ['B', 'C'],
    'B': ['D', 'E'],
    'C': ['F'],
    'D': [],
    'E': [],
    'F': []
}

print("DFS Traversal Order:", dfs_recursive(graph, 'A'))
