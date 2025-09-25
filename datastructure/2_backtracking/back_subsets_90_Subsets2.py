from lib import th, logger

def generate_subsets_backtracking(nums):
    """
    Generate all unique subsets using backtracking method.
    :param nums: List of integers
    :return:
    """

    result = []
    current_subset = []

    def backtrack(start_index):
        #Base case: add current subset to result
        result.append(current_subset[:]) # Make a copy o current subset

        #Try adding each remaining element
        for i in range(start_index, len(nums)):
            #choose: add current element to subset
            current_subset.append(nums[i])

            #Explore: recurse with next index
            backtrack(i+1)

            #unchoose: remove current element (backtrack
            current_subset.pop()


        backtrack(0)
        return result

# Test with [ 1, 2, 3]
nums = [ 1, 2, 3]
T = th()
subsets = generate_subsets_backtracking(nums)
T.print_time_taken("Subsets_2", T.start_time)
logger.info("logg warning")

print(f"All Subsets of [nums]:")
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