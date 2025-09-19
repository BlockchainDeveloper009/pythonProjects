import itertools

def all_combinations(arr):
    # Store all possible non-empty combinations
    result = []
    # Loop through all possible sizes
    for r in range(1, len(arr) + 1):
        # Get all combinations of size r
        for combo in itertools.combinations(arr, r):
            result.append(combo)
    return result

# Example usage:
arr = ['A', 'B', 'C']
combinations = all_combinations(arr)
for combo in combinations:
    print(combo)
