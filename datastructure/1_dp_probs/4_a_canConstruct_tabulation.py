def canConstruct(target, wordBank):
    # Create a table to record whether substrings of 'target' can be constructed.
    # table[i] means: can we construct target[:i] from the wordBank?
    table = [False] * (len(target) + 1)
    table = True  # Empty string can always be constructed (using no words)

    # Iterate over every position in the target string
    for i in range(len(target) + 1):
        # Only proceed if current position can be constructed
        if table[i]:
            # Try placing each word from the word bank at current position
            for word in wordBank:
                # If the word fits the substring starting at i
                if target[i:i+len(word)] == word:
                    # Mark the position after placing the word as constructible
                    table[i + len(word)] = True

    # The answer for entire target is found at the last table position
    return table[len(target)]

# --- Example edge case calls below ---

# Edge Case 1: Empty target
#print(canConstruct("", ["cat", "dog"]))   # True

# Edge Case 2: Impossible construction
print(canConstruct("abcdef", ["ab", "abc", "cd", "ef"]))   # False

# Edge Case 3: Very long target, almost possible
print(canConstruct("eeeeeeeeeeeeeeeeeeef",
                   ["e", "ee", "eee", "eeee", "eeeee", "eeeeee"]))  # False

# Edge Case 4: Multiple branches to true
print(canConstruct("purple", ["purp", "p", "ur", "le", "purpl"]))  # True

# Edge Case 5: Lots of pieces, no solution
print(canConstruct("skateboard", ["bo", "rd", "ate", "t", "ska", "sk", "boar"]))  # False
