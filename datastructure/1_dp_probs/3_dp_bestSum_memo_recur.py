def bestSum(targetSum, numbers, memo=None):
    # Initialize memo dictionary on first call
    if memo is None:
        memo = {}

    # If we've already solved this sum, return the stored answer to save time (DP memoization)
    if targetSum in memo:
        return memo[targetSum]

    # Base case: If targetSum is 0, the shortest way to reach 0 is to pick nothing.
    if targetSum == 0:
        return []

    # Base case: If targetSum is negative, it's not possible to reach this sum with positive numbers.
    if targetSum < 0:
        return None

    # Track the shortest combination found so far
    shortest_combination = None

    # Try each number in the list
    for num in numbers:
        # Find remainder after choosing num
        remainder = targetSum - num

        # Recursively try to solve the remainder
        remainder_combination = bestSum(remainder, numbers, memo)

        # If remainder_combination is a valid solution (not None)
        if remainder_combination is not None:
            # Create a new combination by adding current num to solution for remainder
            combination = remainder_combination + [num]

            # If it's the first valid combination, or shorter than the shortest so far, update it
            if (shortest_combination is None) or (len(combination) < len(shortest_combination)):
                shortest_combination = combination

    # Save the result to memo for future reference
    memo[targetSum] = shortest_combination
    return shortest_combination

# Example usage and output:
print(bestSum(8, [2, 3, 5]))  # Output: [3, 5] or [2, 2, 2, 2] (any shortest combination)



"""
bestSum(8, [2, 3, 5])
#Expected: [3, 5] or [2, 2, 2, 2] (any shortest combination)
Edge Cases

    No Solution Exists:
    bestSum(7, [2, 4])
    Expected: None (none of the combinations of add up to 7)

Target is Zero:
bestSum(0, [1, 2, 3])
Expected: [] (an empty list – 0 sum achieved by picking nothing)

Array Contains All Larger Than Target:
bestSum(3, [5, 6, 7])
Expected: None (no element is less than or equal to 3)

Array Contains Duplicates:
bestSum(8, [2, 2, 3])
Expected: [2, 2, 2, 2] or [3, 2, 3] (any shortest; checks duplicate handling)

Single Element Array:
bestSum(8, )

Expected: `` (solution is the element itself)

Empty Array:
bestSum(7, [])
Expected: None (no numbers to use)
Large Target Value Example

    bestSum(100, [1, 2, 5, 25])
    Expected: [25, 25, 25, 25] (4 elements is shortest)`
"""