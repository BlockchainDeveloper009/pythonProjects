Below is beginner-friendly Python code for finding a Hamiltonian cycle in a graph using backtracking, with detailed step-by-step comments and print statements showing the state of key variables at each step. This is based on classic solutions and incorporates iterative value outputs for maximum clarity.[1][2]

```python
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
```

### How the Algorithm Works
- **Start at vertex 0** and initialize the path to hold -1s (unvisited), except the start.
- **Recursively try to add each vertex** at each position, checking if adding is "safe" (connected to previous, not yet in path).
- **Prints each iterative attempt and backtracking step** to help visualize the process.
- **Stops if all vertices are added and the last connects to the first**, otherwise keeps backtracking.
- Prints all major internal state for clear understanding of how the solution unfolds.[2][1]

This annotated code is a strong learning resource for understanding backtracking and Hamiltonian cycles in graph theory for beginners.

[1](https://www.geeksforgeeks.org/dsa/hamiltonian-cycle/)
[2](https://www.geeksforgeeks.org/dsa/hamiltonian-path-cycle-in-python/)
[3](https://www.youtube.com/watch?v=Axsbz0EMQBk)
[4](https://codecrucks.com/hamiltonian-cycle-using-backtracking/)
[5](https://stackoverflow.com/questions/62715637/writing-a-python-function-that-finds-a-hamiltonian-path-in-a-graph)
[6](https://python-forum.io/thread-23458.html)
[7](https://drchristianphsalas.com/2024/08/22/using-the-python-library-networkx-to-find-all-hamiltonian-cycles-in-a-graph/)
[8](https://stackoverflow.com/questions/47982604/hamiltonian-path-using-python)
[9](https://www.reddit.com/r/learnpython/comments/h7sbvr/fastest_way_to_find_a_hamiltonian_cycle/)