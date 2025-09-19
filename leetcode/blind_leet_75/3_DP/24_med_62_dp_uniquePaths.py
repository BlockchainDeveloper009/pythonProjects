

class Solution:
    def uniquePaths(self, m: int, n: int) -> int:
        # Create a 2D DP table initialized with 0s
        dp = [[0 for _ in range(n)] for _ in range(m)]

        # Base cases:
        # There's only one way to reach any cell in the first row (by moving right)
        for j in range(n):
            dp[0][j] = 1
        # There's only one way to reach any cell in the first column (by moving down)
        for i in range(m):
            dp[i][0] = 1

        # Fill the DP table
        # For any other cell (i, j), the number of unique paths to reach it
        # is the sum of unique paths to reach the cell above it (i-1, j)
        # and the cell to its left (i, j-1)
        for i in range(1, m):
            for j in range(1, n):
                dp[i][j] = dp[i - 1][j] + dp[i][j - 1]

        # The result is the number of unique paths to the bottom-right corner
        return dp[m - 1][n - 1]

s = Solution()
m = 3
n = 7
s.uniquePaths(m,n)


"""
62. Unique Paths
Medium
Topics
premium lock iconCompanies

There is a robot on an m x n grid. The robot is initially located at the top-left corner (i.e., grid[0][0]). The robot tries to move to the bottom-right corner (i.e., grid[m - 1][n - 1]). The robot can only move either down or right at any point in time.

Given the two integers m and n, return the number of possible unique paths that the robot can take to reach the bottom-right corner.

The test cases are generated so that the answer will be less than or equal to 2 * 109.



Example 1:

Input: m = 3, n = 7
Output: 28

Example 2:

Input: m = 3, n = 2
Output: 3
Explanation: From the top-left corner, there are a total of 3 ways to reach the bottom-right corner:
1. Right -> Down -> Down
2. Down -> Down -> Right
3. Down -> Right -> Down

"""