def best_sum_tabulation(target_sum, numbers):
    # Table where each index i stores shortest combo to sum i, or None if impossible
    table = [None] * (target_sum + 1)
    table[0] = []

    for i in range(target_sum + 1):
        if table[i] is not None:
            for num in numbers:
                combo = table[i] + [num]
                next_sum = i + num
                if next_sum <= target_sum:
                    if table[next_sum] is None or len(combo) < len(table[next_sum]):
                        table[next_sum] = combo
    return table[target_sum]

# Example:
print(
    best_sum_tabulation(8, [2, 3, 5]))  # Output: [3, 5]
