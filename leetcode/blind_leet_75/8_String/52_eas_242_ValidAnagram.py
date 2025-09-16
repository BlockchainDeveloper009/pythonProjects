from collections import Counter


def isAnagram(s: str, t: str) -> bool:
    # Quick length check, if lengths differ they cannot be anagrams
    if len(s) != len(t):
        return False

    # Count frequencies of characters in s
    char_count = Counter(s)

    # Decrement frequency for characters in t
    for char in t:
        char_count[char] -= 1
        # If any count goes below zero, t has more occurrences than s
        if char_count[char] < 0:
            return False

    # All counts matched, so t is an anagram of s
    return True



print(isAnagram("anagram", "nagaram"))  # True
print(isAnagram("rat", "car"))          # False


"""
242. Valid Anagram
Easy
Topics
premium lock iconCompanies

Given two strings s and t, return true if t is an

of s, and false otherwise.



Example 1:

Input: s = "anagram", t = "nagaram"

Output: true

Example 2:

Input: s = "rat", t = "car"

Output: false



Constraints:

    1 <= s.length, t.length <= 5 * 104
    s and t consist of lowercase English letters.



Follow up: What if the inputs contain Unicode characters? How would you adapt your solution to such a case?
"""

"""
Here is an efficient Python solution to the **Valid Anagram** problem (LeetCode 242), which ensures that string `t` is a true anagram of string `s` by verifying equal character frequencies:

```python
from collections import Counter

def isAnagram(s: str, t: str) -> bool:
    # Quick length check, if lengths differ they cannot be anagrams
    if len(s) != len(t):
        return False
    
    # Count frequencies of characters in s
    char_count = Counter(s)
    
    # Decrement frequency for characters in t
    for char in t:
        char_count[char] -= 1
        # If any count goes below zero, t has more occurrences than s
        if char_count[char] < 0:
            return False
    
    # All counts matched, so t is an anagram of s
    return True
```

***

### Explanation

- If two strings are anagrams, they have the same characters with the same counts.
- The `Counter` hash map counts how many times each character appears in `s`.
- We decrement the count when scanning `t`.
- If any count ever goes negative, `t` contains a character more times than `s`.
- If all pass, the strings are anagrams.

***

### Examples

```python
print(isAnagram("anagram", "nagaram"))  # True
print(isAnagram("rat", "car"))          # False
```

***

### Unicode Characters Consideration

- For Unicode support, Python’s `Counter` works directly on Unicode characters, so the above solution adapts without any changes.

***

### Complexity

- Time: $$O(n)$$, where $$n$$ is the length of the string.
- Space: $$O(1)$$ assuming fixed character set, otherwise $$O(k)$$ for unique chars. Usually small constant for alphabets.

***

**Summary:**  
This solution correctly and efficiently checks if two strings are anagrams by using a single frequency counter and early exit upon mismatch. It works for ASCII and Unicode strings alike.[1][6][7]

[1](https://algo.monster/liteproblems/242)
[2](https://www.youtube.com/watch?v=_cCTcPQik6A)
[3](https://www.reddit.com/r/leetcode/comments/xgvk09/242_valid_anagram_why_isnt_my_solution_correct/)
[4](https://stackoverflow.com/questions/77540503/leetcode-242-valid-anagram-why-is-my-code-failing-this-test-case)
[5](https://www.youtube.com/watch?v=9UtInBqnCgA)
[6](https://leetcode.com/problems/valid-anagram/)
[7](https://neetcode.io/solutions/valid-anagram)
[8](https://walkccc.me/LeetCode/problems/242/)
[9](https://algomap.io/problems/valid-anagram)
"""