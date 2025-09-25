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
139. Word Break

Given a string s and a dictionary of strings wordDict, return true if s can be segmented into a space-separated sequence of one or more dictionary words.

Note that the same word in the dictionary may be reused multiple times in the segmentation.
 

Example 1:

Input: s = "leetcode", wordDict = ["leet","code"]
Output: true
Explanation: Return true because "leetcode" can be segmented as "leet code".

Example 2:

Input: s = "applepenapple", wordDict = ["apple","pen"]
Output: true
Explanation: Return true because "applepenapple" can be segmented as "apple pen apple".
Note that you are allowed to reuse a dictionary word.

Example 3:

Input: s = "catsandog", wordDict = ["cats","dog","sand","and","cat"]
Output: false

 

Constraints:

    1 <= s.length <= 300
    1 <= wordDict.length <= 1000
    1 <= wordDict[i].length <= 20
    s and wordDict[i] consist of only lowercase English letters.
    All the strings of wordDict are unique.


"""