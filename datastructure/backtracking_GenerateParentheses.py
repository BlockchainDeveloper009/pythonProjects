def generate_parentheses(n):
    """
    Generate all combinations of well-formed parentheses for n pairs.

    Args:
        n (int): Number of pairs of parentheses

    Returns:
        List[str]: List of all valid parentheses combinations
    """
    result = []

    def backtrack(open_count, close_count, current_string):
        # If the current string is of length 2 * n, it's a valid combination
        if len(current_string) == 2 * n:
            result.append(current_string)
            return

        # If we can still add an opening parenthesis, add it and recurse
        if open_count < n:
            backtrack(open_count + 1, close_count, current_string + '(')

        # If we can add a closing parenthesis without invalidating, add it and recurse
        if close_count < open_count:
            backtrack(open_count, close_count + 1, current_string + ')')

    # Start the recursion with zero open and close counts and empty current string
    backtrack(0, 0, "")

    return result

# Example usage:
n = 3
print(generate_parentheses(n))
