from utils.metrics_time_helper import  TimeHelper
from lib import th

def subsets_with_target_sum_backtracking(nums, target):
    """
    Generate all unique subsets using backtracking method.
    :param nums: List of integers
    :return:
    """


    result = []

    def backtrack(start_index, current_subset, current_sum):

        if current_sum == target:
            result.append(current_subset[:])
            return

        if current_sum > target: # Pruning: no need to continue
            return

        for i in range(start_index, len(nums)):
            current_subset.append(nums[i])
            backtrack(i+1, current_subset, current_sum + nums [i])
            current_subset.pop()

    backtrack(0, [], 0)
    return result

# Test with [ 1, 2, 3]
#nums = [ 1, 2, 3, 6, -2]
nums = [ 6, -2]

t = TimeHelper()
subsets = subsets_with_target_sum_backtracking(nums, 4)
t.print_time_taken("subsets_BitManipulation",t.start_time)
print(f"All Subsets of [nums]:")

print(f"reulst arr : {subsets}")
print(f"\n Total number of subsets: {len(subsets)}")




"""
90. Subsets II
Medium
Topics
premium lock iconCompanies

Given an integer array nums that may contain duplicates, return all possible

(the power set).

The solution set must not contain duplicate subsets. Return the solution in any order.

 

Example 1:

Input: nums = [1,2,2]
Output: [[],[1],[1,2],[1,2,2],[2],[2,2]]

Example 2:

Input: nums = [0]
Output: [[],[0]]

 

Constraints:

    1 <= nums.length <= 10
    -10 <= nums[i] <= 10

"""