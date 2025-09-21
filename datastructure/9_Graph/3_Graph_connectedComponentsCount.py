def connectedComponentCount(graph) -> int:
    visited = set()
    count = 0

    for node in graph:
        if node not in visited:  # Check if the node has been visited
            explore(graph, node, visited)
            count += 1

    return count

def explore(graph, current, visited) -> None: # It doesn't need to return a value
    if current in visited:
        return

    visited.add(current) # Correct way to add to a set

    for neighbor in graph[current]:
        explore(graph, neighbor, visited)


print(connectedComponentCount(
    {
        0: [8, 1, 5],
        1: [0],
        5: [0, 8],
        8: [0, 5],
        2: [3, 4],
        3: [2, 4],
        4: [3, 2]
    }
)) # Output: 2