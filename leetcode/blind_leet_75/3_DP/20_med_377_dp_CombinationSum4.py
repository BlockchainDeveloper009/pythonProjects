class Solution:
    def combinationSum4(self, nums: list[int], target: int) -> int:
        # dp[i] will store the number of combinations that sum up to i
        dp = [0] * (target + 1)

        # There is one way to make a sum of 0: by choosing no numbers.
        dp[0] = 1

        # Iterate through each possible sum from 1 to target
        for i in range(1, target + 1):
            # For each sum 'i', iterate through all numbers in 'nums'
            for num in nums:
                # If 'num' can be part of a combination for 'i'
                if i - num >= 0:
                    # Add the number of combinations for (i - num) to dp[i]
                    # This is because if we add 'num' to any combination that sums to (i - num),
                    # we get a new combination that sums to 'i'.
                    dp[i] += dp[i - num]

        # The final answer is the number of combinations that sum up to 'target'
        return dp[target]

s = Solution()
nums = [1,2,3]
target = 4
print(s.combinationSum4(nums, target))

"""
377. Combination Sum IV
Medium
Topics
premium lock iconCompanies

Given an array of distinct integers nums and a target integer target, return the number of possible combinations that add up to target.

The test cases are generated so that the answer can fit in a 32-bit integer.



Example 1:

Input: nums = [1,2,3], target = 4
Output: 7
Explanation:
The possible combination ways are:
(1, 1, 1, 1)
(1, 1, 2)
(1, 2, 1)
(1, 3)
(2, 1, 1)
(2, 2)
(3, 1)
Note that different sequences are counted as different combinations.

Example 2:

Input: nums = [9], target = 3
Output: 0



Constraints:

    1 <= nums.length <= 200
    1 <= nums[i] <= 1000
    All the elements of nums are unique.
    1 <= target <= 1000

 
"""