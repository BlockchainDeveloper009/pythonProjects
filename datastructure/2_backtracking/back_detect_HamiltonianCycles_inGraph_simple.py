def find_hamiltonian_cycle(graph):
    """
    Finds a Hamiltonian Cycle in a graph using backtracking.
    """
    num_vertices = len(graph)
    path = []
    visited = set()
    start_node = 0  # We can start from any node

    # A single node graph is not a cycle
    if num_vertices == 1:
        return False

    path.append(start_node)
    visited.add(start_node)

    if solve_hamiltonian_cycle(graph, path, visited, start_node, num_vertices):
        return True

    return False


def solve_hamiltonian_cycle(graph, path, visited, start_node, num_vertices):
    """
    Recursive helper function to find the cycle.
    """
    # Base case: Path is complete
    if len(path) == num_vertices:
        last_node = path[-1]

        # Check if the last node is connected back to the start node
        if start_node in graph[last_node]:
            print("Hamiltonian Cycle found:", path + [start_node])
            return True
        else:
            return False

    current_node = path[-1]

    # Recursive step: Iterate through neighbors of the current node
    for neighbor in graph[current_node]:
        if neighbor not in visited:
            path.append(neighbor)
            visited.add(neighbor)

            # Recurse with the new state
            if solve_hamiltonian_cycle(graph, path, visited, start_node, num_vertices):
                return True

            # Backtrack
            path.pop()
            visited.remove(neighbor)

    return False


# Example Usage:
graph1 = {
    0: [1, 2],
    1: [0, 2],
    2: [0, 1]
}

print(find_hamiltonian_cycle(graph1))  # Expected output: True

graph2 = {
    0: [1, 2],
    1: [0, 3],
    2: [0, 3],
    3: [1, 2]
}

print(find_hamiltonian_cycle(graph2))  # Expected output: False