Here is a clean Python solution to generate all well-formed parentheses for `n` pairs, using backtracking:

```python
class Solution:
    def generateParenthesis(self, n: int) -> list[str]:
        def backtrack(s='', left=0, right=0):
            # Base case: when the constructed string's length is 2*n
            if len(s) == 2 * n:
                result.append(s)
                return
            # If we still have a left parenthesis we can add, do so
            if left < n:
                backtrack(s + '(', left + 1, right)
            # If we have more left used than right, we can add a right parenthesis
            if right < left:
                backtrack(s + ')', left, right + 1)

        result = []
        backtrack()
        return result

# Example usage:
sol = Solution()
print(sol.generateParenthesis(3))  # Output: ["((()))","(()())","(())()","()(())","()()()"]
print(sol.generateParenthesis(1))  # Output: ["()"]
```

***

### How This Works

- Uses recursion to build the string step by step.
- When string length reaches `2 * n` (meaning n left and n right parentheses), a valid combination is found.
- Only adds a left parenthesis if there are any left to add.
- Only adds a right parenthesis if it won’t exceed the number of left parentheses, keeping the string well-formed.
- Collects all valid combinations in `result`.

***

### Key Ideas

- Ensures no invalid parentheses are generated (pruning early).
- Efficiently builds only valid solutions using the rules of well-formed parentheses.
- Backtracking allows for exploring all possibilities and undoing choices.

Let me know if you want step-by-step recursion tracing or a non-recursive solution!

[1](https://www.tutorialspoint.com/generate-parentheses-in-python)
[2](https://algo.monster/liteproblems/22)
[3](https://www.geeksforgeeks.org/dsa/print-all-combinations-of-balanced-parentheses/)
[4](https://interviewing.io/questions/generate-parentheses)
[5](https://algocademy.com/link/?problem=generate-parentheses&lang=py&solution=1)
[6](https://llego.dev/posts/generating-valid-parentheses-combinations-python/)
[7](https://www.youtube.com/watch?v=oC4saZRNwfI)
[8](https://leetcode.com/problems/generate-parentheses/)
[9](https://stackoverflow.com/questions/75736866/python-solving-generate-parentheses-with-backtracking-confused-about-stac)