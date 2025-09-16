def longestPalindrome(s: str) -> str:
    if len(s) < 2:
        return s

    start, max_len = 0, 1

    def expandAroundCenter(left, right):
        while left >= 0 and right < len(s) and s[left] == s[right]:
            left -= 1
            right += 1
        return left + 1, right - 1

    for i in range(len(s)):
        # Odd length palindrome
        left1, right1 = expandAroundCenter(i, i)
        # Even length palindrome
        left2, right2 = expandAroundCenter(i, i + 1)

        # Check odd length palindrome length
        if right1 - left1 + 1 > max_len:
            start, max_len = left1, right1 - left1 + 1

        # Check even length palindrome length
        if right2 - left2 + 1 > max_len:
            start, max_len = left2, right2 - left2 + 1

    return s[start:start + max_len]



print(longestPalindrome("babad"))  # "bab" or "aba"
print(longestPalindrome("cbbd"))   # "bb"



"""
5. Longest Palindromic Substring
Medium
Topics
premium lock iconCompanies
Hint

Given a string s, return the longest

in s.



Example 1:

Input: s = "babad"
Output: "bab"
Explanation: "aba" is also a valid answer.

Example 2:

Input: s = "cbbd"
Output: "bb"



Constraints:

    1 <= s.length <= 1000
    s consist of only digits and English letters.

"""

"""
The problem **Longest Palindromic Substring** asks for the longest contiguous substring of `s` that is a palindrome.

***

## Approach: Expand Around Center

- A palindrome mirrors around its center.
- Each character (and each gap between characters) could be the center.
- For each center, expand outwards while characters on both sides are equal.
- Track the longest palindrome found.

***

## Python Code

```python
def longestPalindrome(s: str) -> str:
    if len(s) < 2:
        return s
    
    start, max_len = 0, 1
    
    def expandAroundCenter(left, right):
        while left >= 0 and right < len(s) and s[left] == s[right]:
            left -= 1
            right += 1
        return left + 1, right - 1
    
    for i in range(len(s)):
        # Odd length palindrome
        left1, right1 = expandAroundCenter(i, i)
        # Even length palindrome
        left2, right2 = expandAroundCenter(i, i + 1)
        
        # Check odd length palindrome length
        if right1 - left1 + 1 > max_len:
            start, max_len = left1, right1 - left1 + 1
        
        # Check even length palindrome length
        if right2 - left2 + 1 > max_len:
            start, max_len = left2, right2 - left2 + 1
            
    return s[start:start + max_len]
```

***

## Example Usage

```python
print(longestPalindrome("babad"))  # "bab" or "aba"
print(longestPalindrome("cbbd"))   # "bb"
```

***

## Explanation

- Treat each index and gap as palindrome centers.
- Expand around centers to find max palindrome.
- Track and update longest substring.

***

## Complexity

- Time: $$O(n^2)$$ worst case, $$n$$ is string length.
- Space: $$O(1)$$ extra space.

***

**Summary:**  
Expanding around centers provides an elegant O(n²) solution for longest palindromic substring by checking all possible palindrome centers efficiently.[1]

[1](https://leetcode.com/problems/valid-anagram/)
"""