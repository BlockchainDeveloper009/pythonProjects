https://blog.algomaster.io/p/15-leetcode-patterns

https://github.com/dipjul/Grokking-the-Coding-Interview-Patterns-for-Coding-Questions

https://github.com/ashishps1/awesome-leetcode-resources/blob/main/patterns/python/top_k_elements.py

## Videos:
 - [freecodecamp___DSA and Algorithm pattersn for leetcode Interviews | dynamic | backtracking](https://www.youtube.com/watch?v=Z_c4byLrNBU&t=1397s)

- [Super_Dynamicc programming_feecodecamp]()
- [Super_Dynamicc programming_feecodecamp]()

## sliding_window_problems

- length of longest substring that doesnt repeat characters
  \\\ [hashset | right | left pointers]/////



## Dynamic Window

- Find the length of the longest 
substring with at most K unique characters.
- Whats the smallest subarray with a 
sum greater than a target
- Return the longest window where a certain 
rule is valid.

## Binary Search Alg 

5. Array of bool, find the first place where i turns into true
[F, F, F, T, T, T, T, T]
6. Find Minimum in Rotated Sorted Array
input = [ 10, 20, 30, 40, 50, 0, 20]. Find index
of the minimum element in this array
[30, 40, 50, 0, 20]

## BFS - FIFO queue | visited Set() is used - | Undirected | 
### when is it used?
    - Shortest path betwen nodes 
    
    

##  DFS - Stack is used
### when is it used?
    - Explore every possibility 
    - Want to visit all nodes
    - Care about structure, not distance
#### DFS - Trees - usage
    - Flattening trees
    - Building or checking structures
    - Searching for nodes based on custom logic
#### DFS - Graph - usage
    - Graph has cycles, so visited is required
    - Puzzles and state exploration
    - Graph coloring
    - Recursive traversal
    - Backtracking

### A graph consists of:

    Nodes (or vertices): The points in the graph.

    Edges: The connections between the nodes.

    Weights: A value assigned to each edge, often representing distance, time, or cost. A graph with weights is called a weighted graph. A graph without weights is an unweighted graph, where each edge can be considered to have a weight of 1.

### The most common algorithms for solving the shortest path problem are:

    Dijkstra's Algorithm: Used for graphs with non-negative edge weights.

    Bellman-Ford Algorithm: Used for graphs that may have negative edge weights.

    *A Search Algorithm:** A more efficient algorithm that uses heuristics to guide the search toward the goal node.

## Bactracking problems | Sudoku | WordSearch | Permutations_Combinations
    - Combinations, permutations, etc.
    - Building up a partial solution
    - Want all possible solutions
    - Need to discard bad paths early

### from collections import deque
    - 