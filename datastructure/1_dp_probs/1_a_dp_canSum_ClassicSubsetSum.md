If you want to pick each item **only once** (no repeated use of the same number), your problem becomes the classic **Subset Sum Problem**.

Here’s a **dynamic programming tabulation** approach to solve Subset Sum (no repeats allowed) with detailed explanation:

```python
def subset_sum_tabulation(numbers, target_sum):
    """
    Returns True if any subset (without repetition) of 'numbers' sums to 'target_sum'.
    Uses DP tabulation (bottom-up).
    
    Args:
        numbers (List[int]): list of distinct positive integers.
        target_sum (int): target sum to achieve.
    
    Returns:
        bool: True if a subset sums to target_sum, else False.
    """
    n = len(numbers)
    # dp[i][j] means: using first i numbers, is sum j achievable?
    dp = [[False] * (target_sum + 1) for _ in range(n + 1)]

    # Base case: sum=0 is achievable with empty subset for any i
    for i in range(n + 1):
        dp[i][0] = True

    # Build dp table
    for i in range(1, n + 1):
        for j in range(1, target_sum + 1):
            if numbers[i - 1] > j:
                # Can't include numbers[i-1], inherit from previous row
                dp[i][j] = dp[i - 1][j]
            else:
                # Either exclude or include current number
                dp[i][j] = dp[i - 1][j] or dp[i - 1][j - numbers[i - 1]]

    return dp[n][target_sum]

# --- Test cases ---
test_cases = [
    ([2, 3], 7, False),  # Can't reach 7 without repeats
    ([5, 3, 4, 7], 7, True),  # 7 itself or 3+4
    ([2, 4], 7, False),  # Can't reach 7
    ([2, 3, 5], 8, True),  # 3+5 for example
    ([7, 14], 300, False)  # no subset to reach 300
]

for idx, (nums, target, expected) in enumerate(test_cases, 1):
    res = subset_sum_tabulation(nums, target)
    print(f"Test {idx}: subset_sum_tabulation({nums}, {target}) = {res} (Expected: {expected})")
```

***

### Explanation for structure:
- `dp` is a 2D boolean table; dimension: `(number_of_elements + 1) x (target_sum + 1)`.
- `dp[i][j]` is True means using the first `i` numbers, it's possible to get sum `j`.
- Base condition: `dp[i] = True` for all `i`, because sum zero can always be made by choosing no elements.
- For each element and each achievable sum, we decide to include or exclude the current element.
- **No repetition** is ensured because we only look "above" in the table (`dp[i-1][?]`), not the same i-th row or repeated usage of the ith element.

***

This approach runs in $$O(n \times target\_sum)$$ time and space, classic for subset sum without repetition.

If you want a solution that outputs the actual subset(s) or a space-optimized version, just ask!

[1](https://www.geeksforgeeks.org/dsa/subset-sum-problem-dp-25/)
[2](https://stackoverflow.com/questions/4355955/subset-sum-algorithm)
[3](https://people.csail.mit.edu/rrw/SODA_2021_Subset_Sum_logspace.pdf)
[4](https://en.wikipedia.org/wiki/Subset_sum_problem)
[5](https://www.reddit.com/r/optimization/comments/1ad6cpt/best_way_to_solve_multiple_subset_sum/)
[6](https://www.geeksforgeeks.org/dsa/subset-sum-problem/)
[7](https://www.reddit.com/r/algorithms/comments/eotipg/subset_sum_problem_with_large_numbers_and_dynamic/)