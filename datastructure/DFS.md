**Depth-First Search (DFS)** is an algorithm for traversing or searching a tree or graph data structure. It's called "depth-first" because it explores as deeply as possible along each branch before it **backtracks** to explore a new one. . Think of it like navigating a maze: you pick a path and follow it until you hit a dead end, then you go back to the last intersection and try a new path.

The DFS algorithm typically uses a **stack** data structure, which is "Last-In, First-Out" (LIFO). This means the most recently added node is the first one to be processed, which is how the algorithm prioritizes going deeper. DFS can be implemented either recursively (which uses the call stack) or iteratively (using an explicit stack data structure).

Here's the basic logic for an iterative DFS:

* **Step 1: Initialization**
    * Create a **stack** and add your starting node to it.
    * Create a `visited` set to keep track of nodes you've already seen to avoid infinite loops in graphs with cycles.

* **Step 2: Traversal**
    * While the stack is **not empty**, do the following:
        * Remove the top node from the stack.
        * If this node has not been visited:
            * Mark it as visited.
            * Process the node (e.g., print it).
            * Add all of its unvisited neighbors to the stack.

This process continues until the stack is empty, meaning all reachable nodes have been visited.

***

### DFS vs. BFS

DFS and Breadth-First Search (BFS) are both graph traversal algorithms, but they differ in their approach and the data structure they use:

| Feature | DFS | BFS |
| :--- | :--- | :--- |
| **Traversal Order** | **Depth-First:** Explores as far as possible down one path. | **Breadth-First:** Explores all nodes at the current level before moving to the next. |
| **Data Structure** | **Stack** (LIFO) or recursion. | **Queue** (FIFO). |
| **Best For** | Finding a path, cycle detection, or topological sorting. | Finding the shortest path in an unweighted graph. |

The key difference is that DFS goes "deeper," while BFS goes "wider."

This video offers a simple visual walkthrough of the DFS algorithm and its implementation in Python.
[Learn Depth First Search in 7 minutes](https://www.youtube.com/watch?v=by93qH4ACxo)
http://googleusercontent.com/youtube_content/0