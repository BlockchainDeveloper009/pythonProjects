import math


class Solution:
    def getPermutation(self, n: int, k: int) -> str:
        """
        Returns the k-th permutation sequence (1-indexed) of numbers 1 to n.
        Uses the factorial system to select each digit optimally.
        """
        # Initialize a list with numbers 1..n
        numbers = list(range(1, n + 1))
        k -= 1  # Convert k to 0-based for easier math

        result = []

        # Build permutation one digit at a time
        for i in range(n, 0, -1):
            fact = math.factorial(i - 1)  # permutations for each digit at this position
            index = k // fact  # which number to pick for this position
            result.append(str(numbers[index]))
            numbers.pop(index)  # remove chosen number to avoid repeats
            k = k % fact  # update k for the next digit

        return ''.join(result)


# Test cases for verification
sol = Solution()
print(sol.getPermutation(3, 3))  # Output: "213"
print(sol.getPermutation(4, 9))  # Output: "2314"
print(sol.getPermutation(3, 1))  # Output: "123"
