class Solution:
    def generateParenthesis(self, n: int) -> list[str]:
        """
        Generates all combinations of well-formed parentheses for n pairs.

        Args:
            n (int): Number of pairs of parentheses.

        Returns:
            list[str]: All possible valid combinations.
        """

        def backtrack(s='', left=0, right=0):
            """
            Helper function that uses backtracking to build up valid combinations.

            Args:
                s (str): Current string being built.
                left (int): Number of '(' used so far.
                right (int): Number of ')' used so far.
            """

            # Base case: If the string has 2*n characters, it's complete
            if len(s) == 2 * n:
                # Add current combination to result list
                result.append(s)
                return

            # Can we add another '('? Only if we haven't used them all yet
            if left < n:
                # Add '(' and recurse (increase left count)
                backtrack(s + '(', left + 1, right)

            # Can we add another ')'? Only if it wouldn't exceed the number of '(' parentheses
            if right < left:
                # Add ')' and recurse (increase right count)
                backtrack(s + ')', left, right + 1)

        # Result list to hold all valid combinations
        result = []
        # Initial call to the helper function with an empty string and zero counts
        backtrack()
        # Return the complete list
        return result

# Example usage:
sol = Solution()
print(sol.generateParenthesis(3))  # Output: ["((()))","(()())","(())()","()(())","()()()"]
print(sol.generateParenthesis(1))  # Output: ["()"]
