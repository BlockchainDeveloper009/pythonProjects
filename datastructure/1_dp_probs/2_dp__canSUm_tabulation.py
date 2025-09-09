def canSum_tabulation(target_sum, numbers):
    """
    Determines if it's possible to generate 'target_sum' using any combination (with repeats) of 'numbers'.
    Uses dynamic programming (tabulation/bottom-up) for efficiency.

    Args:
        target_sum (int): Desired sum.
        numbers (List[int]): List of positive integers (can repeat any number of times).

    Returns:
        bool: True if possible, False otherwise.
    """
    # Create a table where index i means: "Can we sum to value i?"
    table = [False] * (target_sum + 1)
    # It's always possible to sum to 0 (by choosing nothing)
    table[0] = True
    #(starting 0th position can return 0, so its  true)

    # Fill the table iteratively
    for i in range(target_sum + 1):
        if table[i]:  # If current sum is possible...
            for num in numbers:
                #add curr pos with numbers in the array
                #[0,1,2,3,4,5,6,7]
                # |_____|
                next_sum = i + num
                # If adding num doesn't exceed target, mark that sum as possible
                if next_sum <= target_sum:
                    table[next_sum] = True

    return table[target_sum]


# --- Five solid test cases ---
test_cases = [
    # (target_sum, numbers, expected)
    (7, [2, 3], True),  # 2+2+3 or 3+2+2
    (7, [5, 3, 4, 7], True),  # 7 is in the list, or 3+4
    (7, [2, 4], False),  # Cannot sum to 7 with these
    (8, [2, 3, 5], True),  # 3+5 or 2+2+2+2
    (300, [7, 14], False),  # Cannot reach 300 with only 7s and 14s
]

for i, (target, arr, expected) in enumerate(test_cases, 1):
    res = canSum_tabulation(target, arr)
    print(f"Test {i}: canSum_tabulation({target}, {arr}) = {res} (Expected: {expected})")
