"""
Given a string s containing just the characters '(', ')', '{', '}', '[' and ']', determine if the input string is valid.

An input string is valid if:

    Open brackets must be closed by the same type of brackets.
    Open brackets must be closed in the correct order.
    Every close bracket has a corresponding open bracket of the same type.

"""

class Solution:
    def isValid(self, s: str) -> bool:
        # Map each closing bracket to its corresponding opening bracket
        bracket_map = {')': '(',
                       '}': '{',
                       ']': '['}
        stack = []

        # Iterate over each character in the string
        for char in s:
            # If character is a closing bracket
            if char in bracket_map:
                # Pop the top element from the stack if available; else assign dummy value '#'
                top_element = stack.pop() if stack else '#'
                # Check if the popped opening bracket matches the current closing bracket
                if bracket_map[char] != top_element:
                    return False
                print(bracket_map[char])
            else:
                # If it's an opening bracket, push it onto the stack
                stack.append(char)

        # If stack is empty at the end, all brackets matched correctly
        return not stack


sol = Solution()
print(sol.isValid("()[]{}"))   # True
print(sol.isValid("([)]"))     # False
print(sol.isValid("{[]}"))     # True
