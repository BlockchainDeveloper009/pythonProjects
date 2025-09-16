class Solution:
    def lengthOfLIS(self, nums: list[int]) -> int:
        if not nums:
            return 0

        n = len(nums)
        dp = [1] * n  # Initialize all LIS lengths to 1 (each element is an LIS of length 1)

        for i in range(n):
            for j in range(i):
                if nums[i] > nums[j]:
                    dp[i] = max(dp[i], dp[j] + 1)

        return max(dp)

s = Solution()
nums = [10,9,2,5,3,7,101,18]

print(s.lengthOfLIS(nums))

"""
300. Longest Increasing Subsequence
Medium
Topics
premium lock iconCompanies

Given an integer array nums, return the length of the longest strictly increasing

.



Example 1:

Input: nums = [10,9,2,5,3,7,101,18]
Output: 4
Explanation: The longest increasing subsequence is [2,3,7,101], therefore the length is 4.

Example 2:

Input: nums = [0,1,0,3,2,3]
Output: 4

Example 3:

Input: nums = [7,7,7,7,7,7,7]
Output: 1



Constraints:

    1 <= nums.length <= 2500
    -104 <= nums[i] <= 104


"""