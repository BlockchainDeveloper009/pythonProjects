class Solution:
    def rob(self, nums: list[int]) -> int:
        if not nums:
            return 0
        if len(nums) == 1:
            return nums[0]

        # rob1 represents the maximum amount robbed up to the previous house (i-1)
        # rob2 represents the maximum amount robbed up to the house before the previous (i-2)
        rob1 = 0
        rob2 = 0

        # Iterate through each house
        for n in nums:
            # The maximum amount we can rob up to the current house (n)
            # is the maximum of:
            # 1. Robbing the current house: n + rob1 (cannot rob the immediate previous house)
            # 2. Not robbing the current house: rob2 (take the max from the previous house)
            temp = max(n + rob1, rob2)

            # Update rob1 and rob2 for the next iteration
            rob1 = rob2
            rob2 = temp

        return rob2


"""
https://medium.com/@pratham.kesarkar/leetcode-198-house-robber-cc3d13dcbaf7

198. House Robber
Medium
Topics
premium lock iconCompanies

You are a professional robber planning to rob houses along a street. Each house has a certain amount of money stashed, the only constraint stopping you from robbing each of them is that adjacent houses have security systems connected and it will automatically contact the police if two adjacent houses were broken into on the same night.

Given an integer array nums representing the amount of money of each house, return the maximum amount of money you can rob tonight without alerting the police.



Example 1:

Input: nums = [1,2,3,1]
Output: 4
Explanation: Rob house 1 (money = 1) and then rob house 3 (money = 3).
Total amount you can rob = 1 + 3 = 4.

Example 2:

Input: nums = [2,7,9,3,1]
Output: 12
Explanation: Rob house 1 (money = 2), rob house 3 (money = 9) and rob house 5 (money = 1).
Total amount you can rob = 2 + 9 + 1 = 12.



Constraints:

    1 <= nums.length <= 100
    0 <= nums[i] <= 400


"""