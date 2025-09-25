class UnionFind:
    """
    A basic Union-Find (Disjoint Set) data structure with path compression and union by size.
    Used to efficiently manage and merge disjoint sets.
    """
    def __init__(self, size):
        # parent[i] stores the parent of element i.
        # Initially, each element is its own parent.
        self.parent = list(range(size))
        # size[i] stores the size of the set rooted at i.
        self.size = [1] * size
        # count tracks the number of disjoint sets.
        self.count = size

    def find(self, i):
        """
        Finds the root of the set containing element i, with path compression.
        """
        if self.parent[i] == i:
            return i
        # Path compression: make every visited node point directly to the root.
        self.parent[i] = self.find(self.parent[i])
        return self.parent[i]

    def union(self, i, j):
        """
        Merges the sets containing elements i and j, using union by size.
        Returns True if a union occurred (i.e., they were in different sets),
        and False otherwise.
        """
        root_i = self.find(i)
        root_j = self.find(j)
        if root_i != root_j:
            # Union by size: attach the smaller tree to the root of the larger tree.
            if self.size[root_i] < self.size[root_j]:
                root_i, root_j = root_j, root_i
            self.parent[root_j] = root_i
            self.size[root_i] += self.size[root_j]
            self.count -= 1  # Decrement the number of sets.
            return True
        return False

def numIslands(grid):
    """
    Counts the number of islands in a 2D grid using the Union-Find data structure.

    Args:
        grid: A 2D list of strings representing the map ('1' for land, '0' for water).

    Returns:
        The total number of islands.
    """
    if not grid or not grid[0]:
        return 0

    rows, cols = len(grid), len(grid[0])
    # The number of total possible elements is rows * cols.
    # Initialize the Union-Find with this size.
    uf = UnionFind(rows * cols)
    # The initial count of islands is the number of '1's in the grid.
    initial_islands = 0

    for r in range(rows):
        for c in range(cols):
            if grid[r][c] == '1':
                initial_islands += 1
                # Convert 2D coordinates to a 1D index for the UnionFind data structure.
                index = r * cols + c

                # Check the right neighbor.
                if c + 1 < cols and grid[r][c + 1] == '1':
                    neighbor_index = r * cols + (c + 1)
                    uf.union(index, neighbor_index)

                # Check the down neighbor.
                if r + 1 < rows and grid[r + 1][c] == '1':
                    neighbor_index = (r + 1) * cols + c
                    uf.union(index, neighbor_index)

    # The final number of islands is the number of disjoint sets,
    # minus the cells that were water from the start.
    water_cells = sum(row.count('0') for row in grid)
    return uf.count - water_cells

# --- Example Usage ---
grid1 = [
  ["1","1","1","1","0"],
  ["1","1","0","1","0"],
  ["1","1","0","0","0"],
  ["0","0","0","0","0"]
]

print(f"The number of islands using Union-Find is: {numIslands(grid1)}")
