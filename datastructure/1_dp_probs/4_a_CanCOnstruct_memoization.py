def canConstruct(target, wordBank, memo=None):
    # Initialize memoization dictionary on first call
    if memo is None:
        memo = {}

    # If we've already solved for this target, return stored answer instantly (avoids repeat work)
    if target in memo:
        return memo[target]

    # Base case: If the target string is empty, we've successfully constructed it
    if target == "":
        return True

    # Try every word in the wordBank
    for word in wordBank:
        # If the word matches the prefix of the target
        if target.startswith(word):
            # Remove the prefix (word) from the target to form the remainder
            suffix = target[len(word):]
            # Recursively check if the remainder can be constructed
            if canConstruct(suffix, wordBank, memo):
                memo[target] = True
                return True  # early exit as soon as we find a way to construct

    # If no prefix matches or no construction is possible, store and return False
    memo[target] = False
    return False

# Example usage:
print(canConstruct("abcdef", ["ab", "abc", "cd", "def", "abcd"]))  # Output: True
