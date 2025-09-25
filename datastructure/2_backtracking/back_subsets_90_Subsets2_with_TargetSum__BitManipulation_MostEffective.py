from utils.metrics_time_helper import TimeHelper

#most memory efficient and fastest
def generate_subsets_interative(nums):
    """
    Generate all unique subsets using backtracking method.
    :param nums: List of integers
    :return:
    """
    n = len(nums)
    result = []
    for i in range(2**n):
        subset = []
        for j in range(n):
            if i & (i << j):
                subset.append(nums[j])
        result.append(subset)

    return result





# Test with [ 1, 2, 3]
nums = [ 1, 2, 3]
t = TimeHelper()
subsets = generate_subsets_interative(nums)
t.print_time_taken("subsets_BitManipulation",t.start_time)

print(f"All Subsets of generate_subsets_interative [nums]:")
for i, subset in enumerate(subsets):
    print(f"{i+1}: {subset}")

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