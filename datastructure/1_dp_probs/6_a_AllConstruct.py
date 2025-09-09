def allConstruct(target, wordBank):
    # Create a table where each entry holds lists of ways to build the prefix target[:i]
    # table[i] will contain a list of lists: each sublist is a sequence of words forming target[:i]
    table = [[] for _ in range(len(target) + 1)]
    table = [[]]  # One way to construct the empty string: use an empty list of words

    # Iterate through all positions in the target string
    for i in range(len(target) + 1):
        # Only proceed if there are ways to construct the prefix of length i
        for word in wordBank:
            # If word matches the substring starting at position i
            if target[i:i+len(word)] == word:
                # Make new combinations by appending word to each existing way to build target[:i]
                newCombinations = [combination + [word] for combination in table[i]]
                # Add all these new combinations to the position after this word
                table[i + len(word)].extend(newCombinations)

    # table[len(target)] holds all possible ways to construct the full target string
    return table[len(target)]

# --- Edge Case Test Invocations ---
print("Edge case 1 (empty target):", allConstruct("", ["a", "b"]))                 # [[]]
print("Edge case 2 (no solution):", allConstruct("hello", ["cat", "dog"]))         # []
print("Edge case 3 (multiple ways):", allConstruct("purple", ["purp", "p", "ur", "le", "purpl"]))  # [['purp', 'le'], ['p', 'ur', 'p', 'le']]
print("Edge case 4 (overlap/branch):", allConstruct("abcdef", ["ab", "abc", "cd", "def", "abcd", "ef", "c"]))  # [['ab', 'cd', 'ef'], ['ab', 'c', 'def'], ['abc', 'def'], ['abcd', 'ef']]
print("Edge case 5 (long, but impossible):", allConstruct("eeeeeeeeeeeeeeeeeeef", ["e", "ee", "eee", "eeee", "eeeee", "eeeeee"]))  # []
