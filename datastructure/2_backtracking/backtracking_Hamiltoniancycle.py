def is_safe(v, graph, path, pos):
    """
    Determines if vertex v can be added at position pos in the Hamiltonian Cycle path.
    Args:
        v: vertex to check
        graph: adjacency matrix
        path: current path being built
        pos: current position in the path
    Returns:
        True if safe, else False
    """
    # Vertex v must be adjacent to the previously added vertex in path
    if graph[path[pos - 1]][v] == 0:
        print(f"Vertex {v} is not adjacent to {path[pos-1]}. Not safe.")
        return False

    # Vertex v must not already be in the path (no repeats)
    if v in path:
        print(f"Vertex {v} already in path {path}. Not safe.")
        return False

    print(f"Vertex {v} is safe to add at position {pos}.")
    return True

def ham_cycle_util(graph, path, pos):
    """
    Utility recursive function to solve Hamiltonian Cycle problem
    Args:
        graph: adjacency matrix
        path: current path being built
        pos: current position in path
    Returns:
        True if cycle is found, else False
    """
    # Base case: If all vertices are included, check if last connects to first
    if pos == len(graph):
        if graph[path[pos - 1]][path] == 1:
            print(f"All vertices visited. {path} forms a cycle (returns to {path}).")
            return True
        else:
            print(f"All vertices visited but {path[-1]} doesn't connect back to {path}. No cycle.")
            return False

    # Try different vertices as candidates for next position
    for v in range(1, len(graph)):
        print(f"Trying vertex {v} at position {pos}. Current path: {path}")
        if is_safe(v, graph, path, pos):
            path[pos] = v
            print(f"Path after adding vertex {v}: {path}")

            if ham_cycle_util(graph, path, pos + 1):  # Recurse to add next vertex
                return True

            # If adding vertex v didn't work, remove it (backtrack) and try others
            print(f"Backtracking from vertex {v}, position {pos}. Current path before removal: {path}")
            path[pos] = -1

    # No vertices can be added, so return False
    return False

def ham_cycle(graph):
    """
    Main function to solve Hamiltonian Cycle problem using backtracking
    Args:
        graph: adjacency matrix
    Returns:
        The Hamiltonian cycle path or None if no cycle exists
    """
    path = [-1] * len(graph)    # Initialize path
    path = 0                 # Start cycle from vertex 0

    if not ham_cycle_util(graph, path, 1):
        print("Solution does NOT exist")
        return None

    print("Hamiltonian Cycle found!")
    print("Cycle:", end=" ")
    for vertex in path:
        print(vertex, end=" ")
    print(path)  # Complete the cycle

    return path + [path]

# Example graph: Adjacency matrix
graph = [
    [0, 1, 0, 1, 0],
    [1, 0, 1, 1, 1],
    [0, 1, 0, 0, 1],
    [1, 1, 0, 0, 1],
    [0, 1, 1, 1, 0]
]

ham_cycle(graph)
