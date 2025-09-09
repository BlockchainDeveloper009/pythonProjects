def get_substrings(s, length):
    """
    Extract all unique substrings of given length from string s
    """

    # Step 1: Create an empty set to store unique substrings
    substrings = set()

    # Step 2: Calculate the number of possible substrings of given length
    # This is (length of s) - (length of substring) + 1
    max_start_index = len(s) - length + 1

    # Step 3: Loop over all valid starting indices for substrings
    for i in range(max_start_index):
        # Step 4: Use string slicing to get the substring starting at i of size 'length'
        substring = s[i:i+length]

        # Step 5: Add the substring to the set (automatically ensures uniqueness)
        substrings.add(substring)

    # Step 6: Return the set of unique substrings
    return substrings
