from typing import List
"""
Given an array nums of distinct integers, return all the possible . You can return the answer in any order.
Example 1:

Input: nums = [1,2,3]
Output: [[1,2,3],[1,3,2],[2,1,3],[2,3,1],[3,1,2],[3,2,1]]

Example 2:

Input: nums = [0,1]
Output: [[0,1],[1,0]]

Example 3:

Input: nums = [1]
Output: [[1]]

 

Constraints:

    1 <= nums.length <= 6
    -10 <= nums[i] <= 10
    All the integers of nums are unique.

"""
class Solution:
    def permute(self, nums: List[int]) -> List[List[int]]:
        """
        Generate all permutations of the input list nums.

        Args:
            nums (List[int]): List of distinct integers.

        Returns:
            List[List[int]]: List of all possible permutations.
        """
        def backtrack(start=0):
            # If we've reached the end, capture the current permutation
            if start == len(nums):
                result.append(nums[:])  # append a copy of current nums
                return

            for i in range(start, len(nums)):
                # Swap the current index with the start to fix one number
                nums[start], nums[i] = nums[i], nums[start]

                # Recurse for the next position
                backtrack(start + 1)

                # Backtrack: revert the swap to restore original order
                nums[start], nums[i] = nums[i], nums[start]

        result = []
        backtrack()
        return result

# Example usage:
sol = Solution()
print(sol.permute([1, 2, 3]))
# Output:
# [[1, 2, 3], [1, 3, 2],
#  [2, 1, 3], [2, 3, 1],
#  [3, 2, 1], [3, 1, 2]]
