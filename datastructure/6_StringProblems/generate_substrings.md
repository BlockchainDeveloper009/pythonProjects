# Assume we have a string s and an integer length

# 1. 'range(len(s) - length + 1)' creates a sequence of numbers (indices) starting from 0
#    up to the last index where a substring of 'length' can start without exceeding s's boundary.
indices = range(len(s) - length + 1)

# 2. For each index i in the above range:
for i in indices:
    # a. 's[i:i+length]' extracts a substring from string s,
    #    starting at index i and extending up to (but not including) i+length.
    substring = s[i:i+length]
    
    # b. This substring is the current substring of length 'length' starting at i.
    print(substring)

# 3. The curly braces '{}' make this a set comprehension, which:
#    - collects all generated substrings into a set
#    - automatically removes duplicate substrings
#    - results in an unordered collection of unique substrings

# To illustrate, manually collecting the substrings into a set:
substrings_set = set()
for i in indices:
    substrings_set.add(s[i:i+length])

print(substrings_set)
