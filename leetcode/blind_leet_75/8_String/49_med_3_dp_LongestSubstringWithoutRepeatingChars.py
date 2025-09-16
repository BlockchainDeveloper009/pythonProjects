
def lengthOfLongestSubstring(s: str) -> int:
    char_set = set()
    left = 0
    max_length = 0

    for right in range(len(s)):
        while s[right] in char_set:
            char_set.remove(s[left])
            left += 1
        char_set.add(s[right])
        max_length = max(max_length, right - left + 1)
    return max_length

testcases = ["abcabcbb" ,"bbbbb", "pwwkew" ]
for test in testcases:
    print('----')
    print(test)
    print(":")
    print(lengthOfLongestSubstring(test))



"""
3. Longest Substring Without Repeating Characters
Attempted
Medium
Topics
premium lock iconCompanies
Hint

Given a string s, find the length of the longest

without duplicate characters.



Example 1:

Input: s = "abcabcbb"
Output: 3
Explanation: The answer is "abc", with the length of 3.

Example 2:

Input: s = "bbbbb"
Output: 1
Explanation: The answer is "b", with the length of 1.

Example 3:

Input: s = "pwwkew"
Output: 3
Explanation: The answer is "wke", with the length of 3.
Notice that the answer must be a substring, "pwke" is a subsequence and not a substring.



Constraints:

    0 <= s.length <= 5 * 104
    s consists of English letters, digits, symbols and spaces.

"""


"""
The optimal solution for **Longest Substring Without Repeating Characters** uses a **sliding window and two pointers** to efficiently find the maximum length of substrings without duplicates.[1][2][3]

***

## Algorithm Approach

1. **Sliding Window Concept**
   - Use two pointers (`left`, `right`) to maintain a window of unique characters in the string.
   - The window expands by moving the right pointer; if a duplicate is seen, move the left pointer forward until all characters in the window are unique.[3][1]

2. **Hash Set/Map for Efficient Lookup**
   - Use a set (or dictionary) to check for duplicates in constant time.
   - Add each new character with the right pointer; if a duplicate is found, remove characters from the left until the window is unique.[4][2]

3. **Track Maximum Length**
   - After each window adjustment, update the maximum length found.

***

## Python Implementation (Sliding Window + HashSet)

```python
def lengthOfLongestSubstring(s: str) -> int:
    char_set = set()
    left = 0
    max_length = 0

    for right in range(len(s)):
        while s[right] in char_set:
            char_set.remove(s[left])
            left += 1
        char_set.add(s[right])
        max_length = max(max_length, right - left + 1)
    return max_length
```


***

### Explanation

- **Expand the window**: For each character at position `right`, add it to the set.
- **Contract the window**: If a duplicate is encountered, move `left` forward, removing characters from the set, until the window only contains unique characters.
- **Update result**: After each expansion, update `max_length`.
- **Time Complexity**: $$ O(n) $$ since each character is added/removed from the set at most once.[2][3]

***

## Summary

- This is a classic **sliding window** problem, using 1D decision logic (track substring boundaries).
- The solution is optimal and elegant: single pass, $$ O(n) $$ time, $$ O(k) $$ space (where $$ k $$ is unique character count).
- Perfect for interviews and competitive coding.[5][1][3][2]

[1](https://interviewing.io/questions/longest-substring-without-repeating-characters)
[2](https://algo.monster/liteproblems/3)
[3](https://neetcode.io/solutions/longest-substring-without-repeating-characters)
[4](https://www.enjoyalgorithms.com/blog/longest-substring-without-repeating-characters/)
[5](https://www.geeksforgeeks.org/dsa/length-of-the-longest-substring-without-repeating-characters/)
[6](https://www.youtube.com/watch?v=FsIyn_oe3eo)
[7](https://stackoverflow.com/questions/67897109/understanding-this-solution-to-the-longest-substring-without-repetition-problem)
[8](https://stackoverflow.com/questions/69962846/sliding-window-findlongestsubstring-please-explain-this-piece-of-code-answer)
[9](https://www.youtube.com/watch?v=FCbOzdHKW18)
[10](https://www.interviewbit.com/blog/longest-substring-without-repeating-characters/)
[11](https://www.youtube.com/watch?v=wiGpQwVHdE0)
[12](https://stackoverflow.com/questions/74966660/find-the-longest-substring-without-repeating-characters-my-code-works-for-half)
[13](https://www.reddit.com/r/learnpython/comments/1dls8dn/medium_leetcode_question_longest_substring/)
[14](https://leetcode.com/problems/longest-substring-without-repeating-characters/)
"""