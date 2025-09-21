import heapq

def dijkstra(graph, start, end):
    # Dictionary to store the shortest distance to each node
    distances = {node: float('inf') for node in graph}
    distances[start] = 0

    # Dictionary to store the predecessor of each node to reconstruct the path
    predecessors = {node: None for node in graph}

    # Priority queue: stores tuples of (distance, node)
    pq = [(0, start)]

    while pq:
        # Get the node with the smallest distance
        current_distance, current_node = heapq.heappop(pq)

        # If we have already found a shorter path, skip
        if current_distance > distances[current_node]:
            continue

        # If we reached the end node, we can stop
        if current_node == end:
            break

        # Explore neighbors of the current node
        for neighbor, weight in graph[current_node].items():
            distance = current_distance + weight

            # If a shorter path is found, update the distance and predecessor
            if distance < distances[neighbor]:
                distances[neighbor] = distance
                predecessors[neighbor] = current_node
                heapq.heappush(pq, (distance, neighbor))

    # Reconstruct the shortest path from the end node back to the start
    path = []
    current_node = end
    while current_node is not None:
        path.append(current_node)
        current_node = predecessors[current_node]
    path.reverse()

    return distances[end], path

graph = {
    'A': {'B': 1, 'C': 4},
    'B': {'A': 1, 'C': 2, 'D': 5},
    'C': {'A': 4, 'B': 2, 'D': 1},
    'D': {'B': 5, 'C': 1, 'E': 3},
    'E': {'D': 3}
}

start_node = 'A'
end_node = 'D'

shortest_distance, shortest_path = dijkstra(graph, start_node, end_node)

print(f"The shortest distance from {start_node} to {end_node} is: {shortest_distance}")
print(f"The shortest path is: {' -> '.join(shortest_path)}")