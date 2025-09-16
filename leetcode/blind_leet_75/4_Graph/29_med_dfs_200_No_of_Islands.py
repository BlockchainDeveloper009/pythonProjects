
def numIslands(grid):
    if not grid:
        return 0

    rows, cols = len(grid), len(grid[0])
    count = 0

    def dfs(r, c):
        if r < 0 or c < 0 or r >= rows or c >= cols or grid[r][c] == '0':
            return
        grid[r][c] = '0'  # Mark visited by sinking island
        # Visit neighbors
        dfs(r + 1, c)
        dfs(r - 1, c)
        dfs(r, c + 1)
        dfs(r, c - 1)

    for i in range(rows):
        for j in range(cols):
            if grid[i][j] == '1':
                dfs(i, j)
                count += 1  # New island found
    return count

grid1 = [
  ["1","1","1","1","0"],
  ["1","1","0","1","0"],
  ["1","1","0","0","0"],
  ["0","0","0","0","0"]
]

grid2 = [
  ["1","1","0","0","0"],
  ["1","1","0","0","0"],
  ["0","0","1","0","0"],
  ["0","0","0","1","1"]
]

print(numIslands(grid1)) # Output: 1
print(numIslands(grid2)) # Output: 3


"""
200. Number of Islands
Medium
Topics
premium lock iconCompanies

Given an m x n 2D binary grid grid which represents a map of '1's (land) and '0's (water), return the number of islands.

An island is surrounded by water and is formed by connecting adjacent lands horizontally or vertically. You may assume all four edges of the grid are all surrounded by water.



Example 1:

Input: grid = [
  ["1","1","1","1","0"],
  ["1","1","0","1","0"],
  ["1","1","0","0","0"],
  ["0","0","0","0","0"]
]
Output: 1

Example 2:

Input: grid = [
  ["1","1","0","0","0"],
  ["1","1","0","0","0"],
  ["0","0","1","0","0"],
  ["0","0","0","1","1"]
]
Output: 3



Constraints:

    m == grid.length
    n == grid[i].length
    1 <= m, n <= 300
    grid[i][j] is '0' or '1'.


"""

"""
The **Number of Islands** problem is a classic graph traversal problem where you count connected components (islands) in a grid. Each island is a group of adjacent '1's connected horizontally or vertically.

***

## Approach: DFS / BFS

1. **Iterate over all cells in the grid**.
2. When you encounter a '1' (land), initiate a DFS/BFS to:
   - Mark all connected land cells in the current island as visited (or change to '0' to avoid revisiting).
3. Increase the island count for every DFS/BFS invocation.
4. Continue until all cells are visited.

***

## Python DFS Solution

```python
def numIslands(grid):
    if not grid:
        return 0

    rows, cols = len(grid), len(grid[0])
    count = 0

    def dfs(r, c):
        if r < 0 or c < 0 or r >= rows or c >= cols or grid[r][c] == '0':
            return
        grid[r][c] = '0'  # Mark visited by sinking island
        # Visit neighbors
        dfs(r + 1, c)
        dfs(r - 1, c)
        dfs(r, c + 1)
        dfs(r, c - 1)

    for i in range(rows):
        for j in range(cols):
            if grid[i][j] == '1':
                dfs(i, j)
                count += 1  # New island found
    return count
```

***

## Example

```python
grid1 = [
  ["1","1","1","1","0"],
  ["1","1","0","1","0"],
  ["1","1","0","0","0"],
  ["0","0","0","0","0"]
]

grid2 = [
  ["1","1","0","0","0"],
  ["1","1","0","0","0"],
  ["0","0","1","0","0"],
  ["0","0","0","1","1"]
]

print(numIslands(grid1)) # Output: 1
print(numIslands(grid2)) # Output: 3
```

***

## Explanation

- Start DFS on each '1' that is not yet visited.
- Mark all connected '1's recursively.
- Increment count for each DFS (each island).
- Count total islands after full traversal.

***

## Complexity

- **Time:** $$O(m \times n)$$ since every cell is visited once.
- **Space:** $$O(m \times n)$$ recursion stack worst-case.

***

**Summary:**  
Counting islands boils down to counting connected components in a 2D grid using DFS or BFS. This is a fundamental graph traversal problem often asked in interviews.[1][2][3]

[1](https://www.interviewcoder.co/leetcode-problems/minimum-window-substring)
[2](https://www.thealgorists.com/Algo/SlidingWindow)
[3](https://www.geeksforgeeks.org/dsa/find-the-smallest-window-in-a-string-containing-all-characters-of-another-string/)
"""