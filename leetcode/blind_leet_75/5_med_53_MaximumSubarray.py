class Solution:
    def maxSubArray(self, nums: list[int]) -> int:
        if not nums:
            return 0

        current_max = nums[0]
        global_max = nums[0]

        for i in range(1, len(nums)):
            # Decide whether to extend the current subarray or start a new one
            current_max = max(nums[i], current_max + nums[i])
            # Update the overall maximum sum found so far
            global_max = max(global_max, current_max)

        return global_max


"""
xample 1:

Input: nums = [-2,1,-3,4,-1,2,1,-5,4]
Output: 6
Explanation: The subarray [4,-1,2,1] has the largest sum 6.

Example 2:

Input: nums = [1]
Output: 1
Explanation: The subarray [1] has the largest sum 1.

Example 3:

Input: nums = [5,4,-1,7,8]
Output: 23
Explanation: The subarray [5,4,-1,7,8] has the largest sum 23.

 

Constraints:

    1 <= nums.length <= 105
    -104 <= nums[i] <= 104

"""