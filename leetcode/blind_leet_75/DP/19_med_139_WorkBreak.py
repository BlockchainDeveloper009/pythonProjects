class Solution:
    def wordBreak(self, s: str, wordDict: list[str]) -> bool:
        n = len(s)
        # Convert wordDict to a set for O(1) average time complexity lookups
        word_set = set(wordDict)

        # dp[i] will be True if s[0:i] can be segmented
        dp = [False] * (n + 1)
        dp[0] = True  # Empty string can always be segmented

        for i in range(1, n + 1):
            for j in range(i):
                # If s[0:j] is segmentable (dp[j] is True)
                # AND s[j:i] is a word in the dictionary
                if dp[j] and s[j:i] in word_set:
                    dp[i] = True
                    break  # Found a way to segment s[0:i], move to next i

        return dp[n]


"""
1143. Longest Common Subsequence
Medium
Topics
premium lock iconCompanies
Hint

Given two strings text1 and text2, return the length of their longest common subsequence. If there is no common subsequence, return 0.

A subsequence of a string is a new string generated from the original string with some characters (can be none) deleted without changing the relative order of the remaining characters.

    For example, "ace" is a subsequence of "abcde".

A common subsequence of two strings is a subsequence that is common to both strings.



Example 1:

Input: text1 = "abcde", text2 = "ace"
Output: 3
Explanation: The longest common subsequence is "ace" and its length is 3.

Example 2:

Input: text1 = "abc", text2 = "abc"
Output: 3
Explanation: The longest common subsequence is "abc" and its length is 3.

Example 3:

Input: text1 = "abc", text2 = "def"
Output: 0
Explanation: There is no such common subsequence, so the result is 0.

"""