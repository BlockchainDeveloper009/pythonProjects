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

