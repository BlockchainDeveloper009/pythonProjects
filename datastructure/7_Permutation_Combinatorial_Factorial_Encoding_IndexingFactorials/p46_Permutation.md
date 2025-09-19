
Here is a Python backtracking solution to generate all permutations of a distinct integer array `nums`, with detailed comments for clarity:

```python
from typing import List

class Solution:
    def permute(self, nums: List[int]) -> List[List[int]]:
        """
        Generate all permutations of the input list nums.

        Args:
            nums (List[int]): List of distinct integers.

        Returns:
            List[List[int]]: List of all possible permutations.
        """
        def backtrack(start=0):
            # If we've reached the end, capture the current permutation
            if start == len(nums):
                result.append(nums[:])  # append a copy of current nums
                return

            for i in range(start, len(nums)):
                # Swap the current index with the start to fix one number
                nums[start], nums[i] = nums[i], nums[start]

                # Recurse for the next position
                backtrack(start + 1)

                # Backtrack: revert the swap to restore original order
                nums[start], nums[i] = nums[i], nums[start]

        result = []
        backtrack()
        return result

# Example usage:
sol = Solution()
print(sol.permute([1, 2, 3]))
# Output:
# [[1, 2, 3], [1, 3, 2],
#  [2, 1, 3], [2, 3, 1],
#  [3, 2, 1], [3, 1, 2]]
```

***

### Explanation of the approach:

- We use a helper function `backtrack(start)` to recursively build permutations starting at index `start`.
- At each call, swap each number from `start` to end into the `start` position to fix it, then recurse for the next position.
- When `start` reaches the length of `nums`, the current permutation is complete and added to the results.
- After recursion, swap back to undo changes (backtracking) so the original list is restored for the next iteration.

This in-place backtracking avoids extra memory for building permutations and systematically generates all permutations.

***

Let me know if you want alternative solutions using `itertools`, or a detailed walkthrough of this code!

[1](https://www.geeksforgeeks.org/dsa/different-ways-to-generate-permutations-of-an-array/)
[2](https://www.geeksforgeeks.org/python/generate-all-the-permutation-of-a-list-in-python/)
[3](https://stackoverflow.com/questions/104420/how-do-i-generate-all-permutations-of-a-list)
[4](https://www.w3schools.com/python/numpy/numpy_random_permutation.asp)
[5](https://blog.seancoughlin.me/mastering-leetcode-generating-all-permutations-of-an-array)
[6](https://leetcode.com/problems/permutations/)
[7](https://www.reddit.com/r/programminghorror/comments/e3s0ir/generating_permutations_for_any_array_without/)
[8](https://takeuforward.org/data-structure/print-all-permutations-of-a-string-array/)

+++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++
The "Permutations" problem (generate all permutations of a list of distinct integers) **cannot efficiently be solved using greedy or dynamic programming** because:

- **Greedy algorithms** work by making a locally optimal choice at each step. Generating permutations requires exploring all possible arrangements, not just greedy choices, so greedy cannot produce all permutations.
- **Dynamic programming (DP)** is typically used on problems with optimal substructure and overlapping subproblems. In permutations, once you fix a number in a position, the choices for the next element are independent, and every unique arrangement must be enumerated, so DP does not efficiently enumerate permutations without essentially reproducing the entire recursive/backtracking structure (which is exponential/factorial time anyway).[1][2]

***

### Factorial-Index Approach

However, **factorial-indexing** (also called "factoradic notation" or "constructing the k-th permutation directly") can be used to find a specific permutation by its rank/index—for example, "what is the k-th permutation in lexicographic order"—but it doesn't enumerate all permutations at once. It's used for problems like LeetCode "Permutation Sequence," not for producing all permutations.[3]

***

### Summary Table

| Approach                | Can generate all permutations? | Efficient? | Description                                                                         |
|-------------------------|-------------------------------|------------|-------------------------------------------------------------------------------------|
| Backtracking/DFS        | Yes                           | Yes        | Standard recursive method, enumerates by swapping or picking unused, runs in O(n!)   |
| Greedy                  | No                            | n/a        | Can’t enumerate; only solves some combinatorial/optimization problems                |
| Dynamic Programming     | No                            | n/a        | Can't reduce enumeration to optimal overlapping subproblems                          |
| Factorial Index         | No (all), Yes (by index)      | O(n^2)     | Selects the k-th lexicographically, not all permutations                             |

***

### Practical Implementation

- **Use backtracking for all permutations.**
- **Use factorial-indexing for single-ranked permutation.**
- Greedy/DP are not suitable here.

***

Let me know if you want code for factorial index/k-th permutation or want a visual trace of the permutation generation!

[1](https://algo.monster/liteproblems/46)
[2](https://www.codeproject.com/Tips/891811/Calculating-Permutation-Using-Dynamic-Programming)
[3](https://www.jointaro.com/interviews/questions/permutation-sequence/?company=meta)
[4](https://web.stanford.edu/class/archive/cs/cs161/cs161.1138/programming/Week_7.pdf)
[5](https://algocademy.com/link/?problem=permutations-with-k-inversions&lang=cpp&solution=1)
[6](https://www.geeksforgeeks.org/dsa/permutation-coefficient/)
[7](https://www.geeksforgeeks.org/dsa/find-permutation-of-numbers-1-to-n-having-x-local-maxima-peaks-and-y-local-minima-valleys/)
[8](https://www.quickperm.org/pexercises.php)
[9](https://stackoverflow.com/questions/56766700/how-do-i-solve-this-dynamic-programming-problem)