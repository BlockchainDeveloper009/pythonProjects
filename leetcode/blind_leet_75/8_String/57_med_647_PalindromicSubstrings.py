
def countSubstrings(s: str) -> int:
    count = 0

    def expandAroundCenter(left, right):
        nonlocal count
        while left >= 0 and right < len(s) and s[left] == s[right]:
            count += 1
            left -= 1
            right += 1

    for i in range(len(s)):
        # Odd length palindromes centered at i
        expandAroundCenter(i, i)
        # Even length palindromes centered between i and i+1
        expandAroundCenter(i, i + 1)

    return count

print(countSubstrings("abc"))  # 3 ("a", "b", "c")
print(countSubstrings("aaa"))  # 6 ("a", "a", "a", "aa", "aa", "aaa")



"""
647. Palindromic Substrings
Medium
Topics
premium lock iconCompanies
Hint

Given a string s, return the number of palindromic substrings in it.

A string is a palindrome when it reads the same backward as forward.

A substring is a contiguous sequence of characters within the string.



Example 1:

Input: s = "abc"
Output: 3
Explanation: Three palindromic strings: "a", "b", "c".

Example 2:

Input: s = "aaa"
Output: 6
Explanation: Six palindromic strings: "a", "a", "a", "aa", "aa", "aaa".



Constraints:

    1 <= s.length <= 1000
    s consists of lowercase English letters.



"""

"""
The problem **Palindromic Substrings** asks to count all substrings of a string `s` that are palindromes.

***

## Approach: Expand Around Center

- Every palindrome substring can be centered around one character or the gap between two characters.
- For each possible center, expand outward while characters match.
- Count each palindrome found.

***

## Python Code

```python
def countSubstrings(s: str) -> int:
    count = 0

    def expandAroundCenter(left, right):
        nonlocal count
        while left >= 0 and right < len(s) and s[left] == s[right]:
            count += 1
            left -= 1
            right += 1

    for i in range(len(s)):
        # Odd length palindromes centered at i
        expandAroundCenter(i, i)
        # Even length palindromes centered between i and i+1
        expandAroundCenter(i, i + 1)

    return count
```

***

## Example Usage

```python
print(countSubstrings("abc"))  # 3 ("a", "b", "c")
print(countSubstrings("aaa"))  # 6 ("a", "a", "a", "aa", "aa", "aaa")
```

***

## Explanation

- For each index, expand outwards to find palindromes of both odd and even lengths.
- Accumulate total count while expanding.
- Returns total count of palindromic substrings.

***

## Complexity

- Time: $$O(n^2)$$, worst case expanding for each character.
- Space: $$O(1)$$, only counters and pointers used.

***

**Summary:**  
Expanding around centers for all single and pair positions provides an elegant $$O(n^2)$$ solution to count palindromic substrings by traversing possible centers and counting the expansion.[1]

[1](https://leetcode.com/problems/valid-anagram/)
"""