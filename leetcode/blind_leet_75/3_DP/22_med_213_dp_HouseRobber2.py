
class Solution:
    def rob(self, nums: list[int]) -> int:
        n = len(nums)

        if n == 0:
            return 0
        if n == 1:
            return nums[0]

        # Helper function for the original House Robber problem (linear arrangement)
        def rob_linear(arr: list[int]) -> int:
            if not arr:
                return 0
            if len(arr) == 1:
                return arr[0]

            dp = [0] * len(arr)
            dp[0] = arr[0]
            dp[1] = max(arr[0], arr[1])

            for i in range(2, len(arr)):
                dp[i] = max(dp[i-1], arr[i] + dp[i-2])
            return dp[-1]

        # Scenario 1: Exclude the last house
        max_without_last = rob_linear(nums[:-1])

        # Scenario 2: Exclude the first house
        max_without_first = rob_linear(nums[1:])

        return max(max_without_last, max_without_first)

nums = [
[2,3,2],
[1,2,3,1],
[1,2,3]
]

s = Solution()
print(s.rob([1,2,3,1]))
# for arr in nums:
#     print(arr)
#     print(s.rob(arr))

"""
213. House Robber II
Medium
Topics
premium lock iconCompanies
Hint

You are a professional robber planning to rob houses along a street. Each house has a certain amount of money stashed.
 All houses at this place are arranged in a circle. That means the first house is the neighbor of the last one. 
 Meanwhile, adjacent houses have a security system connected, and it will automatically contact the police 
 if two adjacent houses were broken into on the same night.

Given an integer array nums representing the amount of money of each house, return the maximum amount of 
money you can rob tonight without alerting the police.



Example 1:

Input: nums = [2,3,2]
Output: 3
Explanation: You cannot rob house 1 (money = 2) and then rob house 3 (money = 2), because they are adjacent houses.

Example 2:

Input: nums = [1,2,3,1]
Output: 4
Explanation: Rob house 1 (money = 1) and then rob house 3 (money = 3).
Total amount you can rob = 1 + 3 = 4.

Example 3:

Input: nums = [1,2,3]
Output: 3



Constraints:

    1 <= nums.length <= 100
    0 <= nums[i] <= 1000



"""