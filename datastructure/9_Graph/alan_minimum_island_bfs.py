import time
from collections import deque


# The main function to find the minimum island size using BFS
def minimum_island_bfs(grid):
    # Use a set to keep track of visited cells
    visited = set()
    # Initialize minimum size to infinity
    min_size = float('inf')

    # Loop through every cell in the grid
    for r in range(len(grid)):
        for c in range(len(grid[0])):
            # Find the size of the island starting from this cell
            size = explore_bfs(grid, r, c, visited)

            # If a valid island was found, update the minimum size
            if size > 0 and size < min_size:
                min_size = size

    # Return the minimum size found, or 0 if no islands exist
    return min_size if min_size != float('inf') else 0


# A helper function to find the size of a single island using BFS
def explore_bfs(grid, r, c, visited):
    rows, cols = len(grid), len(grid[0])

    # Check for invalid starting points (out of bounds or water)
    if not (0 <= r < rows and 0 <= c < cols) or grid[r][c] == 'W':
        return 0

    pos = (r, c)
    # Check if this cell has already been visited
    if pos in visited:
        return 0

    # Use a deque (double-ended queue) for efficient adding and removing from both ends.
    queue = deque([pos])
    # Add the starting cell to the visited set immediately
    visited.add(pos)
    # Start the island size count
    size = 0

    # Continue as long as there are cells in the queue to explore
    while queue:
        # Get the current cell from the front of the queue
        curr_r, curr_c = queue.popleft()
        # Increment the size for each cell we explore
        size += 1

        # Define the neighbors' coordinates (up, down, left, right)
        neighbors = [(curr_r + 1, curr_c), (curr_r - 1, curr_c), (curr_r, curr_c + 1), (curr_r, curr_c - 1)]

        # Check each neighbor
        for neighbor_r, neighbor_c in neighbors:
            neighbor_pos = (neighbor_r, neighbor_c)

            # Check if the neighbor is valid (within bounds, is land, and not visited)
            if (0 <= neighbor_r < rows and 0 <= neighbor_c < cols and
                    grid[neighbor_r][neighbor_c] == 'L' and
                    neighbor_pos not in visited):
                # If the neighbor is valid, add it to the visited set and the queue to be explored later
                visited.add(neighbor_pos)
                queue.append(neighbor_pos)

    return size


# Example Usage
grid = [
    ['W', 'L', 'W', 'W', 'W'],
    ['W', 'L', 'W', 'W', 'W'],
    ['W', 'W', 'W', 'L', 'W'],
    ['W', 'W', 'L', 'L', 'W'],
    ['L', 'W', 'W', 'L', 'L']
]
#print(f"Minimum island size (BFS): {minimum_island_bfs(grid)}")


# Measure the time for the BFS approach
print("Measuring performance of BFS approach...")
start_time_bfs = time.time()
result_bfs = minimum_island_bfs(grid)
end_time_bfs = time.time()
duration_bfs = end_time_bfs - start_time_bfs

print(f"BFS result: {result_bfs}")
print(f"BFS duration: {duration_bfs:.6f} seconds")


"""
Measuring performance of BFS approach...
BFS result: 1
BFS duration: 0.000221 seconds

"""