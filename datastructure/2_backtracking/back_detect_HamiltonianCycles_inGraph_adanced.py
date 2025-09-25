def find_all_hamiltonian_cycles(graph):
    """
    Finds and prints all Hamiltonian Cycles in a graph.
    """
    num_vertices = len(graph)
    cycles_found = 0
    start_node = sorted(list(graph.keys()))[0]  # Consistent starting point

    # We use a list to pass the cycles_found count by reference
    counter = [0]

    solve_hamiltonian_cycle_util(graph, start_node, [start_node], set([start_node]), counter)

    if counter[0] == 0:
        print("No Hamiltonian Cycles found.")


def solve_hamiltonian_cycle_util(graph, current_node, path, visited, counter):
    num_vertices = len(graph)

    # Base Case: Path is a full path visiting all vertices
    if len(path) == num_vertices:
        # Check if the last node is connected back to the start node
        if path[0] in graph[current_node]:
            # A cycle is found!
            counter[0] += 1
            print(f"Cycle {counter[0]}: {path + [path[0]]}")
        return

    # Recursive Step: Explore all valid neighbors
    for neighbor in sorted(graph[current_node]):
        if neighbor not in visited:
            # Choose: Make a move
            path.append(neighbor)
            visited.add(neighbor)

            # Explore: Recurse with the new state
            solve_hamiltonian_cycle_util(graph, neighbor, path, visited, counter)

            # Unchoose (Backtrack): Undo the move
            path.pop()
            visited.remove(neighbor)


# Example 1: A graph with cycles
graph1 = {
    0: [1, 2],
    1: [0, 2],
    2: [0, 1]
}

print("Searching graph 1:")
find_all_hamiltonian_cycles(graph1)

# Example 2: A more complex graph with multiple cycles
graph2 = {
    0: [1, 3],
    1: [0, 2],
    2: [1, 3],
    3: [0, 2]
}

print("\nSearching graph 2:")
find_all_hamiltonian_cycles(graph2)

# Example 3: A graph with no cycles
graph3 = {
    0: [1, 2],
    1: [0, 3],
    2: [0, 3],
    3: [1, 2]
}

print("\nSearching graph 3:")
find_all_hamiltonian_cycles(graph3)