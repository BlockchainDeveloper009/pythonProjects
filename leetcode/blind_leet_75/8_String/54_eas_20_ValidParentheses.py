
def isValid(s: str) -> bool:
    stack = []
    matching = {')': '(', ']': '[', '}': '{'}

    for char in s:
        if char in matching.values():
            stack.append(char)
        elif char in matching:
            if not stack or stack.pop() != matching[char]:
                return False
        else:
            # Invalid character (not in problem constraints)
            return False

    return len(stack) == 0

print(isValid("()"))        # True
print(isValid("()[]{}"))    # True
print(isValid("(]"))        # False
print(isValid("([])"))      # True
print(isValid("([)]"))      # False


"""
20. Valid Parentheses
Easy
Topics
premium lock iconCompanies
Hint

Given a string s containing just the characters '(', ')', '{', '}', '[' and ']', determine if the input string is valid.

An input string is valid if:

    Open brackets must be closed by the same type of brackets.
    Open brackets must be closed in the correct order.
    Every close bracket has a corresponding open bracket of the same type.



Example 1:

Input: s = "()"

Output: true

Example 2:

Input: s = "()[]{}"

Output: true

Example 3:

Input: s = "(]"

Output: false

Example 4:

Input: s = "([])"

Output: true

Example 5:

Input: s = "([)]"

Output: false



Constraints:

    1 <= s.length <= 104
    s consists of parentheses only '()[]{}'.



"""

"""
The **Valid Parentheses** problem is a classic stack-based problem. The goal is to ensure every opening bracket is properly closed in the correct order.

***

## Approach

- Use a stack to track opening brackets.
- For each character:
  - If it is an opening bracket `(`, `[`, `{`, push it onto the stack.
  - If it is a closing bracket `)`, `]`, `}`, check if the stack is not empty and if the top of the stack has the matching opening bracket.
    - If it matches, pop from the stack.
    - Otherwise, return False.
- At the end, if the stack is empty, the string is valid; otherwise, invalid.

***

## Python Code

```python
def isValid(s: str) -> bool:
    stack = []
    matching = {')': '(', ']': '[', '}': '{'}

    for char in s:
        if char in matching.values():
            stack.append(char)
        elif char in matching:
            if not stack or stack.pop() != matching[char]:
                return False
        else:
            # Invalid character (not in problem constraints)
            return False

    return len(stack) == 0
```

***

## Examples

```python
print(isValid("()"))        # True
print(isValid("()[]{}"))    # True
print(isValid("(]"))        # False
print(isValid("([])"))      # True
print(isValid("([)]"))      # False
```

***

## Explanation

- Stack holds only open brackets pending a matching close.
- If the closing bracket doesn't match the last open, return False early.
- Valid only if all opens are properly closed by the end.

***

## Complexity

- Time: $$O(n)$$, where $$n$$ is the length of the string.
- Space: $$O(n)$$ in the worst case for the stack.

***

**Summary:**  
Use a stack to track open brackets and ensure each closing bracket matches the most recent open bracket. Return True if stack empty at the end, meaning all balanced correctly.[1][2]

[1](https://algo.monster/liteproblems/242)
[2](https://leetcode.com/problems/valid-anagram/)
"""