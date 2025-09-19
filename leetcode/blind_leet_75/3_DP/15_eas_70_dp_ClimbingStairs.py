"""
70. Climbing Stairs
Easy
Topics
premium lock iconCompanies
Hint

You are climbing a staircase. It takes n steps to reach the top.

Each time you can either climb 1 or 2 steps. In how many distinct ways can you climb to the top?



Example 1:

Input: n = 2
Output: 2
Explanation: There are two ways to climb to the top.
1. 1 step + 1 step
2. 2 steps

Example 2:

Input: n = 3
Output: 3
Explanation: There are three ways to climb to the top.
1. 1 step + 1 step + 1 step
2. 1 step + 2 steps
3. 2 steps + 1 step

"""


class Solution:
    def climbStairs(self, n: int) -> int:
        if n == 1:
            return 1

        # Initialize variables to represent the number of ways to reach the previous two steps
        # 'one' represents ways to reach step i-1
        # 'two' represents ways to reach step i-2
        one, two = 1, 1

        # Iterate from the 2nd step up to the nth step
        # The loop runs n-1 times because we've already handled n=1 and initialized for n=2
        for i in range(n - 1):
            # Calculate the number of ways to reach the current step (i+1)
            # This is the sum of ways to reach the previous two steps
            temp = one + two

            # Update 'one' to be the old 'two' (ways to reach i-1 becomes ways to reach i)
            one = two

            # Update 'two' to be the newly calculated 'temp' (ways to reach i becomes ways to reach i+1)
            two = temp

        return two
