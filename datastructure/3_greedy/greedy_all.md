Greedy algorithms are a class of algorithms that make the locally optimal choice at each step with the hope of finding a globally optimal solution. Here is a list of some of the most well-known greedy algorithms across different fields.

### Graph and Tree Algorithms
* **Dijkstra's Algorithm:** Finds the shortest path between nodes in a graph with non-negative edge weights. It greedily selects the unvisited node with the smallest known distance from the source.
* **Prim's Algorithm:** Finds a Minimum Spanning Tree (MST) for a weighted, undirected graph. It greedily adds the cheapest edge that connects a vertex in the MST to a vertex outside the MST.
* **Kruskal's Algorithm:** Also finds an MST. It greedily adds the cheapest edge from the entire graph, as long as that edge doesn't form a cycle.
* **Boruvka's Algorithm:** A less common but also greedy algorithm for finding an MST. It works by growing multiple components at once.

***

### Scheduling and Optimization
* **Activity Selection Problem:** Selects the maximum number of non-overlapping activities from a set of activities, each with a start and finish time. The greedy strategy is to always pick the activity that finishes first.
* **Fractional Knapsack Problem:** A classic optimization problem where you must fill a knapsack with items to maximize its total value. The greedy approach is to always take as much as possible of the item with the highest value-to-weight ratio.
* **Huffman Coding:** A data compression algorithm that creates a prefix code. The greedy strategy is to repeatedly merge the two characters with the smallest frequencies.

***

### Other Algorithms
* **Change-Making Algorithm:** A simple greedy algorithm to make change using the fewest coins possible. It works by repeatedly taking the largest coin denomination that is less than or equal to the remaining amount. (Note: This only works for certain coin systems, like USD, and not all.)
* **Greedy Best-First Search:** A search algorithm that explores a graph by always picking the next node that appears closest to the goal, according to a heuristic function.