def isPalindrome(s: str) -> bool:
    left, right = 0, len(s) - 1

    while left < right:
        # Skip non-alphanumeric characters
        while left < right and not s[left].isalnum():
            left += 1
        while left < right and not s[right].isalnum():
            right -= 1

        # Compare characters ignoring case
        if s[left].lower() != s[right].lower():
            return False

        left += 1
        right -= 1

    return True



print(isPalindrome("A man, a plan, a canal: Panama"))  # True
print(isPalindrome("race a car"))                      # False
print(isPalindrome(" "))                                # True


"""
125. Valid Palindrome
Easy
Topics
premium lock iconCompanies

A phrase is a palindrome if, after converting all uppercase letters into lowercase letters and removing all non-alphanumeric characters, it reads the same forward and backward. Alphanumeric characters include letters and numbers.

Given a string s, return true if it is a palindrome, or false otherwise.



Example 1:

Input: s = "A man, a plan, a canal: Panama"
Output: true
Explanation: "amanaplanacanalpanama" is a palindrome.

Example 2:

Input: s = "race a car"
Output: false
Explanation: "raceacar" is not a palindrome.

Example 3:

Input: s = " "
Output: true
Explanation: s is an empty string "" after removing non-alphanumeric characters.
Since an empty string reads the same forward and backward, it is a palindrome.



Constraints:

    1 <= s.length <= 2 * 105
    s consists only of printable ASCII characters.


"""

"""
To check if a given string is a **valid palindrome** after converting to lowercase and removing all non-alphanumeric characters, a two-pointer approach is efficient.

***

## Approach

- Use two pointers: one starting at the beginning (`left`) and one at the end (`right`).
- Move both pointers toward the center:
  - Skip non-alphanumeric characters.
  - Compare characters in lowercase.
- If characters differ, return False.
- If pointers cross or meet, the string is a palindrome.

***

## Python Code

```python
def isPalindrome(s: str) -> bool:
    left, right = 0, len(s) - 1

    while left < right:
        # Skip non-alphanumeric characters
        while left < right and not s[left].isalnum():
            left += 1
        while left < right and not s[right].isalnum():
            right -= 1
        
        # Compare characters ignoring case
        if s[left].lower() != s[right].lower():
            return False
        
        left += 1
        right -= 1
    
    return True
```

***

## Example Usage

```python
print(isPalindrome("A man, a plan, a canal: Panama"))  # True
print(isPalindrome("race a car"))                      # False
print(isPalindrome(" "))                                # True
```

***

## Explanation

- Alphanumeric check filters out punctuation, spaces.
- Case-insensitive comparison ensures uniformity.
- Two pointers avoid extra space needed for string manipulation.

***

## Complexity

- Time: $$O(n)$$ where $$n$$ is string length.
- Space: $$O(1)$$ as no extra significant space is used.

***

**Summary:**  
Two-pointer technique efficiently validates palindrome by skipping unwanted characters and comparing only relevant characters, ensuring linear time and constant space complexity.[1]

[1](https://leetcode.com/problems/valid-anagram/)
"""