def pacificAtlantic(heights):
    if not heights or not heights[0]:
        return []

    ROWS, COLS = len(heights), len(heights[0])

    pacific_reachable = set()
    atlantic_reachable = set()

    def dfs(r, c, visited, prev_height):
        # Boundary and height check
        if ((r, c) in visited or
                r < 0 or c < 0 or
                r >= ROWS or c >= COLS or
                heights[r][c] < prev_height):
            return
        visited.add((r, c))
        # Explore neighbors
        for dr, dc in [(1, 0), (-1, 0), (0, 1), (0, -1)]:
            dfs(r + dr, c + dc, visited, heights[r][c])

    # Pacific ocean borders: top row and left col
    for c in range(COLS):
        dfs(0, c, pacific_reachable, heights[0][c])
    for r in range(ROWS):
        dfs(r, 0, pacific_reachable, heights[r][0])

    # Atlantic ocean borders: bottom row and right col
    for c in range(COLS):
        dfs(ROWS - 1, c, atlantic_reachable, heights[ROWS - 1][c])
    for r in range(ROWS):
        dfs(r, COLS - 1, atlantic_reachable, heights[r][COLS - 1])

    # Cells that can flow to both oceans
    return list(pacific_reachable & atlantic_reachable)

heights = [
    [1,2,2,3,5],
    [3,2,3,4,4],
    [2,4,5,3,1],
    [6,7,1,4,5],
    [5,1,1,2,4]
]

result = pacificAtlantic(heights)
print(sorted(result))

"""
417. Pacific Atlantic Water Flow
Medium
Topics
premium lock iconCompanies

There is an m x n rectangular island that borders both the Pacific Ocean and Atlantic Ocean. The Pacific Ocean touches the island's left and top edges, and the Atlantic Ocean touches the island's right and bottom edges.

The island is partitioned into a grid of square cells. You are given an m x n integer matrix heights where heights[r][c] represents the height above sea level of the cell at coordinate (r, c).

The island receives a lot of rain, and the rain water can flow to neighboring cells directly north, south, east, and west if the neighboring cell's height is less than or equal to the current cell's height. Water can flow from any cell adjacent to an ocean into the ocean.

Return a 2D list of grid coordinates result where result[i] = [ri, ci] denotes that rain water can flow from cell (ri, ci) to both the Pacific and Atlantic oceans.



Example 1:

Input: heights = [[1,2,2,3,5],[3,2,3,4,4],[2,4,5,3,1],[6,7,1,4,5],[5,1,1,2,4]]
Output: [[0,4],[1,3],[1,4],[2,2],[3,0],[3,1],[4,0]]
Explanation: The following cells can flow to the Pacific and Atlantic oceans, as shown below:
[0,4]: [0,4] -> Pacific Ocean
       [0,4] -> Atlantic Ocean
[1,3]: [1,3] -> [0,3] -> Pacific Ocean
       [1,3] -> [1,4] -> Atlantic Ocean
[1,4]: [1,4] -> [1,3] -> [0,3] -> Pacific Ocean
       [1,4] -> Atlantic Ocean
[2,2]: [2,2] -> [1,2] -> [0,2] -> Pacific Ocean
       [2,2] -> [2,3] -> [2,4] -> Atlantic Ocean
[3,0]: [3,0] -> Pacific Ocean
       [3,0] -> [4,0] -> Atlantic Ocean
[3,1]: [3,1] -> [3,0] -> Pacific Ocean
       [3,1] -> [4,1] -> Atlantic Ocean
[4,0]: [4,0] -> Pacific Ocean
       [4,0] -> Atlantic Ocean
Note that there are other possible paths for these cells to flow to the Pacific and Atlantic oceans.

Example 2:

Input: heights = [[1]]
Output: [[0,0]]
Explanation: The water can flow from the only cell to the Pacific and Atlantic oceans.



Constraints:

    m == heights.length
    n == heights[r].length
    1 <= m, n <= 200
    0 <= heights[r][c] <= 105


"""


"""
The **Pacific Atlantic Water Flow** problem can be solved similarly using **graph traversal** (DFS or BFS). The idea is to work backwards: start from cells adjacent to each ocean and find which cells can flow into them using water flow rules.

***

## Approach (DFS + Sets)

1. **Start DFS from all Pacific-bordering cells** (top row + left column).
2. **Start DFS from all Atlantic-bordering cells** (bottom row + right column).
3. Each DFS explores neighbors only if their height is >= current (water flows "downhill" or stays level).
4. Keep track of the cells reachable from Pacific and Atlantic separately.
5. Intersection of these two sets gives cells that flow to both oceans.

***

## Python Code

```python
def pacificAtlantic(heights):
    if not heights or not heights[0]:
        return []
    
    ROWS, COLS = len(heights), len(heights[0])
    
    pacific_reachable = set()
    atlantic_reachable = set()
    
    def dfs(r, c, visited, prev_height):
        # Boundary and height check
        if ((r, c) in visited or 
            r < 0 or c < 0 or 
            r >= ROWS or c >= COLS or 
            heights[r][c] < prev_height):
            return
        visited.add((r, c))
        # Explore neighbors
        for dr, dc in [(1,0), (-1,0), (0,1), (0,-1)]:
            dfs(r + dr, c + dc, visited, heights[r][c])
    
    # Pacific ocean borders: top row and left col
    for c in range(COLS):
        dfs(0, c, pacific_reachable, heights[0][c])
    for r in range(ROWS):
        dfs(r, 0, pacific_reachable, heights[r][0])
    
    # Atlantic ocean borders: bottom row and right col
    for c in range(COLS):
        dfs(ROWS-1, c, atlantic_reachable, heights[ROWS-1][c])
    for r in range(ROWS):
        dfs(r, COLS-1, atlantic_reachable, heights[r][COLS-1])
    
    # Cells that can flow to both oceans
    return list(pacific_reachable & atlantic_reachable)
```

***

## Example Test Case

```python
heights = [
    [1,2,2,3,5],
    [3,2,3,4,4],
    [2,4,5,3,1],
    [6,7,1,4,5],
    [5,1,1,2,4]
]

result = pacificAtlantic(heights)
print(sorted(result))
```

***

## Explanation

- DFS from ocean edges marks all cells flowing *to* that ocean (by following height constraints).
- The intersection of those cells reachable from both oceans is the answer.
- Uses two sets to efficiently track and intersect results.

***

## Complexity
- Time: About $$O(m \times n)$$ since each cell is processed a limited number of times.
- Space: $$O(m \times n)$$ for tracking visited cells.

***

This approach is very intuitive, easy to implement, and meets the requirement for $$O(m+n)$$ traversal approximately by doing DFS from boundaries.[1][2][3]

[1](https://algo.monster/liteproblems/76)
[2](https://interviewing.io/questions/minimum-window-substring)
[3](https://takeuforward.org/data-structure/minimum-window-substring)
"""