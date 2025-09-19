https://blog.algomaster.io/p/15-leetcode-patterns

https://github.com/dipjul/Grokking-the-Coding-Interview-Patterns-for-Coding-Questions

https://github.com/ashishps1/awesome-leetcode-resources/blob/main/patterns/python/top_k_elements.py



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

## BFS
- FIFO queu is used

##  DFS
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


## Bactracking problems | Sudoku | WordSearch | Permutations_Combinations
    - Combinations, permutations, etc.
    - Building up a partial solution
    - Want all possible solutions
    - Need to discard bad paths early

### from collections import deque
    - 