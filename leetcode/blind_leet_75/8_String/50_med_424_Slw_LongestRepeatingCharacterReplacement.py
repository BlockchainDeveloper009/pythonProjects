def characterReplacement(s: str, k: int) -> int:
    from collections import defaultdict
    count = defaultdict(int)
    left = 0
    max_freq = 0
    result = 0

    for right in range(len(s)):
        count[s[right]] += 1
        max_freq = max(max_freq, count[s[right]])

        # If need to change more than k chars, shrink window from left
        while (right - left + 1) - max_freq > k:
            count[s[left]] -= 1
            left += 1

        result = max(result, right - left + 1)
    return result


"""
424. Longest Repeating Character Replacement
Medium
Topics
premium lock iconCompanies

You are given a string s and an integer k. You can choose any character of the string and change it to any other uppercase English character. You can perform this operation at most k times.

Return the length of the longest substring containing the same letter you can get after performing the above operations.



Example 1:

Input: s = "ABAB", k = 2
Output: 4
Explanation: Replace the two 'A's with two 'B's or vice versa.

Example 2:

Input: s = "AABABBA", k = 1
Output: 4
Explanation: Replace the one 'A' in the middle with 'B' and form "AABBBBA".
The substring "BBBB" has the longest repeating letters, which is 4.
There may exists other ways to achieve this answer too.



Constraints:

    1 <= s.length <= 105
    s consists of only uppercase English letters.
    0 <= k <= s.length


"""
"""
The optimal solution for **Longest Repeating Character Replacement** uses the **sliding window** technique with a character count map and tracks the max frequency in the current window.  
This approach lets us efficiently "simulate" replacement operations and always calculate the longest possible substring with at most `k` replacements.[1][2][3][4]

***

## Sliding Window Approach

### Steps
1. **Pointers:**  
   - Keep two pointers, `left` and `right`, that define your current window in the string.
2. **Character Count:**  
   - Use a dictionary (or array since input is only A-Z) to track the frequency of each character in the window.
3. **Max Frequency:**  
   - Track the count of the most frequent character in the current window (`max_freq`).
4. **Window Check:**  
   - For each step, check the size of the window minus `max_freq`. If this exceeds `k`, shrink the window from the left.
   - This check reflects: *How many characters need changing to make the window all one letter?*
5. **Result:**  
   - The longest valid window seen during the scan is your answer.

### Python Example

```python
def characterReplacement(s: str, k: int) -> int:
    from collections import defaultdict
    count = defaultdict(int)
    left = 0
    max_freq = 0
    result = 0

    for right in range(len(s)):
        count[s[right]] += 1
        max_freq = max(max_freq, count[s[right]])

        # If need to change more than k chars, shrink window from left
        while (right - left + 1) - max_freq > k:
            count[s[left]] -= 1
            left += 1

        result = max(result, right - left + 1)
    return result
```


***

## Intuition & Why It Works

- The value `(right - left + 1) - max_freq` tells you how many changes you'd need to make the window all one character.[5][2]
- Shrink window when replacements needed > k.
- Maximizing window size gives the longest possible valid substring.
- **Time Complexity:** $$O(n)$$, each character is processed at most twice.

***

## DP Style

- This is a textbook **sliding window / two pointer + hash-map** approach which, while not tabular DP, shares key ideas like state updates and optimal substructure.
- Not a true DP problem, but the state (`left`, `right`, `count`, `max_freq`) embodies all information needed to incrementally solve and optimize the window.[4][6]

***

### Summary Table

| Problem                         | Approach                          | State Definition                                 | Output                |
|----------------------------------|-----------------------------------|--------------------------------------------------|-----------------------|
| Longest Repeating Character Replacement | Sliding Window + HashMap            | Window size, char frequencies, max allowed changes | Max substring length  |

***

**Summary:**  
This efficient solution uses a sliding window and character map to check window validity and maximize length, handling at most `k` changes.  
It is interview-standard and optimal for Leetcode 424 with time $$O(n)$$, space $$O(1)$$ for 26 letters.[3][6][1][2][4]

[1](https://algo.monster/liteproblems/424)
[2](https://codeanddebug.in/blog/longest-repeating-character-replacement/)
[3](https://www.designgurus.io/answers/detail/424-longest-repeating-character-replacement-char24)
[4](https://neetcode.io/solutions/longest-repeating-character-replacement)
[5](https://guides.codepath.com/compsci/Longest-Repeating-Character-Replacement)
[6](https://www.hellointerview.com/learn/code/sliding-window/longest-repeating-character-replacement)
[7](https://www.youtube.com/watch?v=gqXU1UyA8pk)
[8](https://www.reddit.com/r/leetcode/comments/1462egd/longest_repeating_character_replacement_leetcode/)
[9](https://www.youtube.com/watch?v=tkNWKvxI3mU)
[10](https://blog.stackademic.com/longest-substring-without-repeating-character-brute-force-better-and-best-approaches-with-tips-e1c2b7dae9a7)
[11](https://leetcode.com/problems/longest-repeating-character-replacement/)
[12](https://stackoverflow.com/questions/78723353/longest-repeating-substring-with-replacement)
[13](https://read.learnyard.com/dsa/longest-repeating-character-replacement/)
"""