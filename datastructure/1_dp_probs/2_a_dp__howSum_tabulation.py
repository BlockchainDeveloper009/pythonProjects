def howSum_tabulation(target_sum, numbers):
    """
    Returns any combination (as a list) of elements that add up to exactly target_sum.
    Uses DP tabulation to build up possible sums from 0 to target_sum.
    Returns None if impossible. If multiple combinations, returns any one.

    Args:
        target_sum (int): Target sum to achieve.
        numbers (List[int]): List of positive integers (can be used unlimited times).

    Returns:
        Optional[List[int]]: List with elements that sum to target_sum, or None.
    """
    # Table where index i holds a list: how to sum to i (None if impossible)
    table = [None] * (target_sum + 1)
    table[0] = []  # Base case: sum 0 is achieved with empty list

    # Iterate from 0 up to target_sum, building up solutions
    for i in range(target_sum + 1):
        if table[i] is not None:  # If current sum is achievable
            for num in numbers:
                next_sum = i + num
                if next_sum <= target_sum:
                    # If not filled, set new way; if filled, can ignore (any result is fine)
                    if table[next_sum] is None:
                        table[next_sum] = table[i] + [num]

    return table[target_sum]

# 5 test cases: (target_sum, numbers, expected output)
# test_cases = [
#     (7, [2, 3], [3, 2, 2]),   # Any combination, possible answer
#     (7, [5, 3, 4, 7], [7]),   # Single element works
#     (7, [2, 4], None),        # No combination exists
#     (8, [2, 3, 5], [2, 2, 2, 2]),  # All 2's work (any: [3,5], [2,3,3], etc.)
#     (0, [1, 2, 3], []),       # Edge case: zero sum always possible without elements
# ]
test_cases = [
    (7, [2, 3], [3, 2, 2]),   # Any combination, possible answer
]
for i, (target, arr, expected) in enumerate(test_cases, 1):
    result = howSum_tabulation(target, arr)
    print(f"Test {i}: howSum_tabulation({target}, {arr}) = {result} (Expected: {expected})")
