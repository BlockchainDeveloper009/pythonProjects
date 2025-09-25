
class Solution:
    def canJump(self, nums: list[int]) -> bool:
        # If the array has only one element, the last index is already reached.
        if len(nums) <= 1:
            return True

        # Initialize 'max_reach' to 0, representing the farthest index we can reach.
        max_reach = 0

        # Iterate through the array.
        for i in range(len(nums)):
            # If the current index 'i' is beyond 'max_reach', it means we cannot reach
            # the current index, and therefore cannot reach the end.
            if i > max_reach:
                return False

            # Update 'max_reach' to the maximum of its current value and the
            # farthest index reachable from the current position (i + nums[i]).
            max_reach = max(max_reach, i + nums[i])

            # If 'max_reach' has already reached or surpassed the last index,
            # it means we can reach the end.
            if max_reach >= len(nums) - 1:
                return True

        # If the loop finishes and we haven't returned True, it means we couldn't reach the end.
        return False

s = Solution()
nums = [2,3,1,1,4]

print(s.canJump(nums))

"""
You are given an integer array nums. You are initially positioned 
at the array's first index, and each element in the array represents 
your maximum jump length at that position.

Return true if you can reach the last index, or false otherwise.



Example 1:

Input: nums = [2,3,1,1,4]
Output: true
Explanation: Jump 1 step from index 0 to 1, then 3 steps to the last index.

Example 2:

Input: nums = [3,2,1,0,4]
Output: false
Explanation: You will always arrive at index 3 no matter what. Its maximum jump length is 0, which makes it impossible to reach the last index.



Constraints:

    1 <= nums.length <= 104
    0 <= nums[i] <= 105


"""