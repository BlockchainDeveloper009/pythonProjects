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

    def wordBreak_1(self, s: str, wordDict: list[str]) -> bool:
        wordSet = set(wordDict)
        dp = [False] * (len(s) + 1)
        dp[0] = True  # Base case: empty string can always be segmented

        # dp[i] indicates if s[:i] can be segmented
        for i in range(1, len(s) + 1):
            for j in range(i):

                if j ==3:
                    print('debug here')
                # If s[j:i] is in wordSet and s[:j] can also be segmented
                if dp[j] and s[j:i] in wordSet:
                    dp[i] = True
                    break
        return dp[len(s)]

s = Solution()
s1 = "leetcode"
wDict1 = ["leet", "code"]
s.wordBreak_1(s1,wDict1)

# s2 = "applepenapple"
# wDict2 = ["apple", "pen"]
# s.workBreak_1(s2,wDict2)
#
#
#
# s3 = "catsandog"
# wDict3 = ["cats","dog","sand","and","cat"]
# s.workBreak_1(s3,wDict3)



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