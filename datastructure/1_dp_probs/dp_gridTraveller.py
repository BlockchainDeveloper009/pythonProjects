def grid_traveller_memoization(m, n, memo=None):
    """
    Calculate the number of ways to travel on a m x n grid from top-left to bottom-right.
    Moves allowed: right or down.

    Args:
        m (int): number of rows
        n (int): number of columns
        memo (dict): cache for storing intermediate results to avoid recomputation

    Returns:
        int: number of unique paths from (0,0) to (m-1, n-1)
    """
    # Initialize memo dictionary in first call
    if memo is None:
        memo = {}

    # Use a tuple key representing current grid size to store/retrieve memoized results
    key = (m, n)

    # Check if result is cached
    if key in memo:
        return memo[key]

    # Base cases:
    if m == 1 and n == 1:
        # Only one cell means one valid way (standing still)
        return 1
    if m == 0 or n == 0:
        # If any dimension is zero, no valid paths
        return 0

    # The number of ways to reach (m, n) is sum of:
    # ways to reach the cell above (m-1, n)
    # plus ways to reach the cell to the left (m, n-1)
    memo[key] = grid_traveller_memoization(m - 1, n, memo) + grid_traveller_memoization(m, n - 1, memo)

    return memo[key]


# Compute the number of ways for 4 rows x 3 columns grid
m, n = 4, 3
total_ways = grid_traveller_memoization(m, n)

print(f"Number of ways to travel a {m}x{n} grid: {total_ways}")


def grid_traveller_dp(m, n):
    """
    Calculate the number of ways to travel an m x n grid using DP tabulation.

    Args:
        m (int): number of rows
        n (int): number of columns

    Returns:
        int: number of unique paths from top-left to bottom-right
    """
    # Create a 2D table filled with 0s
    dp = [[0 for _ in range(n + 1)] for _ in range(m + 1)]

    # The starting point has exactly 1 way to be "reached"
    dp[1][1] = 1

    # Fill the dp table row-wise
    for i in range(1, m + 1):
        for j in range(1, n + 1):
            # If not starting cell, number of ways is sum of ways from top and left cells
            if not (i == 1 and j == 1):
                dp[i][j] = dp[i - 1][j] + dp[i][j - 1]

    return dp[m][n]


# 5 solid test cases: (rows, columns) and expected output
test_cases = [
    (1, 1, 1),  # Single cell (only 1 way)
    (2, 3, 3),  # Smaller grid
    (3, 3, 6),  # Square grid
    (4, 3, 10),  # The 4x3 grid from previous example
    (5, 5, 70)  # Larger square grid
]

for m, n, expected in test_cases:
    result = grid_traveller_dp(m, n)
    print(f"grid_traveller_dp({m}, {n}) = {result} (Expected: {expected})")

"""
grid_traveller_dp(1, 1) = 1 (Expected: 1)
grid_traveller_dp(2, 3) = 3 (Expected: 3)
grid_traveller_dp(3, 3) = 6 (Expected: 6)
grid_traveller_dp(4, 3) = 10 (Expected: 10)
grid_traveller_dp(5, 5) = 70 (Expected: 70)

"""