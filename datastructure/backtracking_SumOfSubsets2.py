def sum_of_subsets(nums, target):
    """
    Finds and prints all subsets of 'nums' that sum to 'target' using backtracking.

    Args:
        nums: List of integers.
        target: Integer, the target sum.
    """
    solutions = []  # Store all solutions found

    def backtrack(index, current_subset, current_sum):
        print(f"Index: {index}, Current Subset: {current_subset}, Current Sum: {current_sum}")
        # Base case: If current sum equals target, print the subset
        if current_sum == target:
            print(f"Subset found: {current_subset}")
            solutions.append(list(current_subset))   # Store a copy of the solution
            # Continue to search for other solutions (do not return yet)
            # as there might be more valid subsets including further numbers.
        # Base case: If we've gone through all numbers or sum > target, stop
        if index == len(nums) or current_sum > target:
            return

        # Choice 1: include nums[index] in the subset
        print(f"Trying to INCLUDE {nums[index]}")
        current_subset.append(nums[index])
        backtrack(index + 1, current_subset, current_sum + nums[index])
        current_subset.pop()  # Undo choice (backtrack)
        print(f"Backtracked, REMOVED {nums[index]}")

        # Choice 2: exclude nums[index] from the subset
        print(f"Trying to EXCLUDE {nums[index]}")
        backtrack(index + 1, current_subset, current_sum)

    # Start the backtracking from index 0, empty subset, sum 0
    backtrack(0, [], 0)
    print("\nAll subsets found:")
    for s in solutions:
        print(s)
    return solutions

# Example usage
nums = [3, 5, 6, 7]
target = 15
sum_of_subsets(nums, target)
