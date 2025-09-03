The **Bellman-Ford algorithm** is a single-source shortest path algorithm that finds the shortest paths from a single starting vertex to all other vertices in a weighted graph.  Unlike Dijkstra's algorithm, Bellman-Ford can handle graphs with **negative edge weights**.

### How it Works

The algorithm's core idea is to repeatedly relax (or update) the shortest path estimates for all edges in the graph. It does this by performing a series of iterations.

1.  **Initialization**: The algorithm starts by assigning a distance of 0 to the starting vertex and a distance of infinity to all other vertices.
2.  **Relaxation**: It then iterates `V - 1` times, where `V` is the number of vertices. In each iteration, it goes through every edge in the graph. For an edge from vertex `u` to `v` with weight `w`, it checks if the current shortest distance to `v` can be improved by going through `u`.
    * If `distance[u] + w < distance[v]`, it updates `distance[v] = distance[u] + w`.
3.  **Negative Cycle Detection**: After `V - 1` iterations, all shortest paths should have been found. The algorithm performs one final check. It iterates through all the edges one last time. If it finds an edge `(u, v)` where `distance[u] + w < distance[v]`, it means the graph contains a **negative cycle**. A negative cycle is a path that starts and ends at the same vertex, where the sum of the edge weights is negative. In such a case, the shortest path is undefined because you can traverse the cycle infinitely to make the path length arbitrarily small.

### Bellman-Ford vs. Dijkstra's

| Feature | Bellman-Ford | Dijkstra's |
| :--- | :--- | :--- |
| **Edge Weights** | Handles **negative** weights. | Requires **non-negative** weights. |
| **Negative Cycles** | **Can detect** negative cycles. | Fails if a negative cycle exists. |
| **Time Complexity** | Slower: $O(V * E)$, where $V$ is the number of vertices and $E$ is the number of edges. | Faster: $O(E + V \log V)$ using a min-priority queue. |