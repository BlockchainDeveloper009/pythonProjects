class Solution:
    def coinChange(self, coins: list[int], amount: int) -> int:
        # dp[i] will store the minimum number of coins needed to make amount i
        # Initialize with amount + 1, representing an impossible state or infinity
        dp = [float('inf')] * (amount + 1)

        # Base case: 0 coins are needed to make an amount of 0
        dp[0] = 0

        # Iterate through each possible amount from 1 to 'amount'
        for i in range(1, amount + 1):
            # For each amount 'i', iterate through all available coin denominations
            for coin in coins:
                # If the current coin can be used to make up amount 'i'
                if i - coin >= 0:
                    # Update dp[i] with the minimum of its current value
                    # and 1 (for the current coin) + the minimum coins needed for the remaining amount (i - coin)
                    dp[i] = min(dp[i], 1 + dp[i - coin])

        # If dp[amount] is still float('inf'), it means the amount cannot be made up
        # by any combination of coins, so return -1. Otherwise, return dp[amount].
        return dp[amount] if dp[amount] != float('inf') else -1

s = Solution()
coins = [1,2,5]
amount = 11
s.coinChange(coins, amount)

"""
322. Coin Change
Medium
Topics
premium lock iconCompanies

You are given an integer array coins representing coins of different denominations and an integer amount representing a total amount of money.

Return the fewest number of coins that you need to make up that amount. If that amount of money cannot be made up by any combination of the coins, return -1.

You may assume that you have an infinite number of each kind of coin.



Example 1:

Input: coins = [1,2,5], amount = 11
Output: 3
Explanation: 11 = 5 + 5 + 1

Example 2:

Input: coins = [2], amount = 3
Output: -1

Example 3:

Input: coins = [1], amount = 0
Output: 0

"""