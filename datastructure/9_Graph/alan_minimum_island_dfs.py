import time
from collections import deque


# The main function to find the minimum island size
def minimum_island_dfs(grid):
    # Use a set to keep track of visited nodes to avoid cycles and redundant work.
    visited = set()
    # Initialize minimum size to infinity so any valid island size will be smaller.
    min_size = float('inf')

    # Loop through every cell in the grid
    for r in range(len(grid)):
        for c in range(len(grid[0])):
            # For each cell, try to find an island
            size = explore_size_dfs(grid, r, c, visited)

            # If an island was found (size > 0), check if it's the new minimum.
            if size > 0 and size < min_size:
                min_size = size

    # If no islands were found, min_size will still be infinity. Return 0 in that case.
    return min_size if min_size != float('inf') else 0


# A helper function that finds the size of a single island using DFS
def explore_size_dfs(grid, r, c, visited):
    # Get the dimensions of the grid
    rows, cols = len(grid), len(grid[0])

    # Base Case 1: If the current position is out of bounds, it's not part of an island.
    if not (0 <= r < rows and 0 <= c < cols):
        return 0

    # Base Case 2: If the current cell is water ('W'), it's not part of an island.
    if grid[r][c] == 'W':
        return 0

    # Create a tuple to represent the current cell's coordinates for the 'visited' set
    pos = (r, c)
    # Base Case 3: If the current cell has already been visited, return 0 to stop exploring this path.
    if pos in visited:
        return 0

    # Mark the current cell as visited
    visited.add(pos)
    # Start the size count for this island with 1 (for the current cell)
    size = 1

    # Recursively call this function for all four neighbors (up, down, left, right)
    # The sum of sizes from all recursive calls gives the total island size.
    size += explore_size_dfs(grid, r + 1, c, visited)
    size += explore_size_dfs(grid, r - 1, c, visited)
    size += explore_size_dfs(grid, r, c + 1, visited)
    size += explore_size_dfs(grid, r, c - 1, visited)

    return size


# Example Usage
grid = [
    ['W', 'L', 'W', 'W', 'W'],
    ['W', 'L', 'W', 'W', 'W'],
    ['W', 'W', 'W', 'L', 'W'],
    ['W', 'W', 'L', 'L', 'W'],
    ['L', 'W', 'W', 'L', 'L']
]
print(f"Minimum island size (DFS): {minimum_island_dfs(grid)}")


# Measure the time for the DFS approach
print("Measuring performance of DFS approach...")
start_time_dfs = time.time()
result_dfs = minimum_island_dfs(grid)
end_time_dfs = time.time()
duration_dfs = end_time_dfs - start_time_dfs

print(f"DFS result: {result_dfs}")
print(f"DFS duration: {duration_dfs:.6f} seconds\n")

"""
Minimum island size (DFS): 1
Measuring performance of DFS approach...
DFS result: 1
DFS duration: 0.000141 seconds

"""

"""
Measuring performance of BFS approach...
BFS result: 1
BFS duration: 0.000221 seconds

"""