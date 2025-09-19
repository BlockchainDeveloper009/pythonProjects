# Define the DFS function using recursion
def dfs(graph, start, visited=None):
    if visited is None:
        visited = set()  # Create a set to keep track of visited nodes

    visited.add(start)  # Mark the start node as visited
    print(start, end=' ')  # Process the node by printing it

    # Recurse for all the neighbors that haven't been visited
    for neighbor in graph[start]:
        if neighbor not in visited:
            dfs(graph, neighbor, visited)

# Example graph represented as an adjacency list in a dictionary
graph = {
    'A': ['B', 'C'],
    'B': ['D', 'E'],
    'C': ['F'],
    'D': [],
    'E': ['F'],
    'F': []
}

# Call the dfs function starting from node 'A'
print("DFS traversal starting from node A:")
dfs(graph, 'A')

