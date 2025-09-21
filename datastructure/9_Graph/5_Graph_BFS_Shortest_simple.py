from collections import deque


def bfs_shortest_path(graph, start, end):
    # Queue for BFS, storing (node, path) tuples
    queue = deque([(start, [start])])

    # Set to keep track of visited nodes
    visited = {start}

    while queue:
        # Get the next node and its current path
        current_node, path = queue.popleft()

        # If we have reached the destination, return the path
        if current_node == end:
            return path

        # Explore neighbors
        for neighbor in graph.get(current_node, []):
            if neighbor not in visited:
                visited.add(neighbor)
                # Create a new path by extending the current one
                new_path = path + [neighbor]
                # Add the neighbor and its new path to the queue
                queue.append((neighbor, new_path))

    # If the end node is not reachable
    return None

graph = {
    'A': ['B', 'C'],
    'B': ['A', 'D', 'E'],
    'C': ['A', 'F'],
    'D': ['B'],
    'E': ['B', 'F'],
    'F': ['C', 'E']
}

start_node = 'A'
end_node = 'F'

shortest_path = bfs_shortest_path(graph, start_node, end_node)

if shortest_path:
    print(f"The shortest path from {start_node} to {end_node} is: {' -> '.join(shortest_path)}")
else:
    print(f"No path found from {start_node} to {end_node}")



"""
To find the shortest path between two nodes in an **unweighted graph**, you can use **Breadth-First Search (BFS)**. This is the simplest and most efficient solution for this specific problem because every edge is treated as having a weight of 1, and BFS naturally explores the graph layer by layer, guaranteeing that the first time it reaches the destination node, it will be via the shortest possible path.

-----

### How Breadth-First Search (BFS) Works

BFS systematically explores a graph by starting at the source node and visiting all its direct neighbors. Then, it visits all the neighbors of those neighbors, and so on. This process continues until the destination node is found. It uses a **queue** (First-In, First-Out data structure) to keep track of the nodes to visit.

Here's the step-by-step process:

1.  **Initialization:** Create a queue and add the starting node to it. Keep track of visited nodes to avoid infinite loops. Also, use a dictionary to store the `parent` or `predecessor` of each node, which will be used to reconstruct the path later.

2.  **Exploration:** While the queue is not empty:

      * Dequeue the next node to visit.
      * If this node is the destination, you have found the shortest path.
      * For each unvisited neighbor of the current node:
          * Mark the neighbor as visited.
          * Set the current node as the neighbor's parent.
          * Enqueue the neighbor.

3.  **Path Reconstruction:** Once the destination is reached, trace back from the destination to the start using the parent pointers to get the shortest path.

-----

### Python Solution with an Example

We'll implement a function `bfs_shortest_path` that finds the shortest path in an unweighted graph.

#### **Step 1: Representing the Graph**

A dictionary is a simple and effective way to represent the graph's **adjacency list**.

```python
graph = {
    'A': ['B', 'C'],
    'B': ['A', 'D', 'E'],
    'C': ['A', 'F'],
    'D': ['B'],
    'E': ['B', 'F'],
    'F': ['C', 'E']
}
```

#### **Step 2: Implementing the BFS Algorithm**

We'll use Python's `collections.deque` for an efficient queue implementation.

```python
from collections import deque

def bfs_shortest_path(graph, start, end):
    # Queue for BFS, storing (node, path) tuples
    queue = deque([(start, [start])])
    
    # Set to keep track of visited nodes
    visited = {start}

    while queue:
        # Get the next node and its current path
        current_node, path = queue.popleft()

        # If we have reached the destination, return the path
        if current_node == end:
            return path

        # Explore neighbors
        for neighbor in graph.get(current_node, []):
            if neighbor not in visited:
                visited.add(neighbor)
                # Create a new path by extending the current one
                new_path = path + [neighbor]
                # Add the neighbor and its new path to the queue
                queue.append((neighbor, new_path))
    
    # If the end node is not reachable
    return None
```

#### **Step 3: Running the Example**

Let's find the shortest path from 'A' to 'F'.

```python
start_node = 'A'
end_node = 'F'

shortest_path = bfs_shortest_path(graph, start_node, end_node)

if shortest_path:
    print(f"The shortest path from {start_node} to {end_node} is: {' -> '.join(shortest_path)}")
else:
    print(f"No path found from {start_node} to {end_node}")
```

**Expected Output:**

```
The shortest path from A to F is: A -> C -> F
```

BFS correctly finds the path of length 2 (`A -> C -> F`) rather than the longer one via `E` (`A -> B -> E -> F`, length 3).

-----

### Key Critical Steps in the Solution

1.  **Use a Queue:** The **First-In, First-Out (FIFO) nature of a queue** is fundamental to BFS. It ensures that we explore all nodes at a distance of *k* from the source before moving on to any nodes at a distance of *k+1*. This guarantees that the first time we discover the destination node, we have found a path with the minimum number of edges.

2.  **Keep Track of Visited Nodes:** The `visited` set is crucial for **preventing cycles** and redundant computations. Without it, the algorithm could get stuck in an infinite loop on a graph with cycles (e.g., A -\> B -\> A). It also ensures that each node is processed only once, making the algorithm more efficient.

3.  **Store the Path during Exploration:** Instead of just enqueuing the node, we enqueue a tuple of `(node, path)`. This is a straightforward way to **build the path incrementally**. At each step, we simply extend the current path with the new neighbor. This avoids the need for a separate `predecessors` dictionary and a second pass for path reconstruction, simplifying the code.
"""