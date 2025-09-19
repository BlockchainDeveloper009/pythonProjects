from collections import Counter

def minWindow(s: str, t: str) -> str:
    if not s or not t:
        return ""
    need = Counter(t)
    have = {}
    left = 0
    required = len(need)
    formed = 0
    min_len = float("inf")
    ans = (0, 0)
    for right, char in enumerate(s):
        have[char] = have.get(char, 0) + 1
        if char in need and have[char] == need[char]:
            formed += 1
        while formed == required:
            if right - left + 1 < min_len:
                min_len = right - left + 1
                ans = (left, right + 1)
            have[s[left]] -= 1
            if s[left] in need and have[s[left]] < need[s[left]]:
                formed -= 1
            left += 1
    return s[ans:ans] if min_len != float("inf") else ""



"""
76. Minimum Window Substring
Hard
Topics
premium lock iconCompanies
Hint

Given two strings s and t of lengths m and n respectively, return the minimum window

of s such that every character in t (including duplicates) is included in the window. If there is no such substring, return the empty string "".

The testcases will be generated such that the answer is unique.



Example 1:

Input: s = "ADOBECODEBANC", t = "ABC"
Output: "BANC"
Explanation: The minimum window substring "BANC" includes 'A', 'B', and 'C' from string t.

Example 2:

Input: s = "a", t = "a"
Output: "a"
Explanation: The entire string s is the minimum window.

Example 3:

Input: s = "a", t = "aa"
Output: ""
Explanation: Both 'a's from t must be included in the window.
Since the largest window of s only has one 'a', return empty string.



Constraints:

    m == s.length
    n == t.length
    1 <= m, n <= 105
    s and t consist of uppercase and lowercase English letters.



Follow up: Could you find an algorithm that runs in O(m + n) time?
"""


"""
The optimal solution for **Minimum Window Substring** uses a **sliding window + hash maps** approach to efficiently find the smallest substring in `s` that contains every character (including duplicates) from `t`.  
This method achieves the required $$O(m + n)$$ time by scanning `s` using two pointers and counting needed characters.[1][2][3][4]

***

## Sliding Window Solution Steps

1. **Frequency Maps**  
   - Build a hashmap or array, `need`, to store the count of each character required from `t`.
   - Use a second map, `window`, to track counts of characters in the current window of `s`.[3][1]

2. **Expand Window**  
   - Move `right` pointer across `s`, adding characters to `window` and adjusting `formed` (the number of needed characters satisfied).

3. **Contract Window**  
   - When the current window contains all needed characters (i.e., `formed == required` where `required` is the number of unique chars in `t`), move `left` forward to make it as small as possible while preserving validity.
   - Update the minimum window indices if a smaller valid window is found.

4. **Return Result**  
   - Return the substring from updated minimum window indices. If no valid window was found, return `""`.

***

## Python Example

```python
from collections import Counter

def minWindow(s: str, t: str) -> str:
    if not s or not t:
        return ""
    need = Counter(t)
    have = {}
    left = 0
    required = len(need)
    formed = 0
    min_len = float("inf")
    ans = (0, 0)
    for right, char in enumerate(s):
        have[char] = have.get(char, 0) + 1
        if char in need and have[char] == need[char]:
            formed += 1
        while formed == required:
            if right - left + 1 < min_len:
                min_len = right - left + 1
                ans = (left, right + 1)
            have[s[left]] -= 1
            if s[left] in need and have[s[left]] < need[s[left]]:
                formed -= 1
            left += 1
    return s[ans:ans] if min_len != float("inf") else ""
```


***

## Intuition

- **Expand window** until all characters from `t` (with correct counts) are present in the current window.
- **Contract window** from left to minimize size while maintaining the condition.
- Store and update the minimum length/indices whenever a valid window is found.
- Each character is processed at most twice (enter/leave), so runtime is linear.

***

### Summary Table

| Problem                   | Approach                 | State Definition            | Output            |
|---------------------------|--------------------------|-----------------------------|-------------------|
| Minimum Window Substring  | Sliding Window + HashMap | Window boundaries, char freq| Shortest substring|

***

**Summary:**  
- Use two hash maps and two pointers for efficient window size management.
- Check character counts to maintain window validity.
- Exact substring indices are tracked for the minimum window.
- Time: O(m + n) where m, n are lengths of `s` and `t`; space: O(u) for unique chars.[4][5][1][2][3]

[1](https://algo.monster/liteproblems/76)
[2](https://leetcode-in-java.github.io/src/main/java/g0001_0100/s0076_minimum_window_substring/)
[3](https://interviewing.io/questions/minimum-window-substring)
[4](https://neetcode.io/problems/minimum-window-with-characters)
[5](https://takeuforward.org/data-structure/minimum-window-substring)
[6](https://www.devpath.com/courses/grokking-coding-interview-in-go/solution-minimum-window-substring)
[7](https://www.youtube.com/watch?v=jSto0O4AJbM)
[8](https://leetcode.com/problems/minimum-window-substring/)
[9](https://www.interviewcoder.co/leetcode-problems/minimum-window-substring)
[10](https://www.thealgorists.com/Algo/SlidingWindow)
[11](https://www.geeksforgeeks.org/dsa/find-the-smallest-window-in-a-string-containing-all-characters-of-another-string/)
[12](https://www.designgurus.io/answers/detail/76-minimum-window-substring-wind35674)
[13](https://leetcode.com/discuss/interview-question/3722472/mastering-sliding-window-technique-a-comprehensive-guide)
"""