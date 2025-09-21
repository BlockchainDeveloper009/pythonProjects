class Solution:
    def numIslands(self, grid: list[list[str]]) -> int:
        if not grid or not grid[0]:
            return 0

        rows, cols = len(grid), len(grid[0])
        num_islands = 0

        def sink_island_recursive(r, c):
            # Base cases for recursion
            if r < 0 or r >= rows or c < 0 or c >= cols or grid[r][c] == '0':
                return

            grid[r][c] = '0'  # Mark the current cell as visited/sunk

            # Recursively explore all four adjacent directions
            sink_island_recursive(r + 1, c)
            sink_island_recursive(r - 1, c)
            sink_island_recursive(r, c + 1)
            sink_island_recursive(r, c - 1)

        for r in range(rows):
            for c in range(cols):
                if grid[r][c] == '1':
                    num_islands += 1
                    sink_island_recursive(r, c)

        return num_islands


from collections import deque


class SolutionIterative:
    def numIslands(self, grid: list[list[str]]) -> int:
        if not grid or not grid[0]:
            return 0

        rows, cols = len(grid), len(grid[0])
        num_islands = 0

        def sink_island_iterative(r, c):
            q = deque([(r, c)])
            grid[r][c] = '0'  # Mark the starting cell as visited

            while q:
                row, col = q.popleft()

                # Check all four adjacent directions
                for dr, dc in [(1, 0), (-1, 0), (0, 1), (0, -1)]:
                    new_r, new_c = row + dr, col + dc

                    # Check for valid and unvisited neighbor
                    if 0 <= new_r < rows and 0 <= new_c < cols and grid[new_r][new_c] == '1':
                        grid[new_r][new_c] = '0'  # Mark as visited/sunk
                        q.append((new_r, new_c))

        for r in range(rows):
            for c in range(cols):
                if grid[r][c] == '1':
                    num_islands += 1
                    sink_island_iterative(r, c)

        return num_islands