def countConstruct(target, wordBank):
    # Create a table for dynamic programming.
    # table[i] will record the number of ways to build target[:i]
    table =  0 * (len(target) + 1)
    table = 1  # There is 1 way to construct the empty string (using nothing)

    # Walk through each position in the target string
    for i in range(len(target) + 1):
        # Skip positions that cannot be reached
        if table[i] > 0:
            # Try adding each word from the wordBank at position i
            for word in wordBank:
                # If the word fits starting at position i
                if target[i:i+len(word)] == word:
                    # Add current ways to the spot after the word
                    table[i + len(word)] += table[i]
    # Final answer is number of ways to create the entire target
    return table[len(target)]

# Example Usage
print(countConstruct("purple", ["purp", "p", "ur", "le", "purpl"]))  # Output: 2
