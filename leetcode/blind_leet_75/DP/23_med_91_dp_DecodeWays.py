class Solution:
    def numDecodings(self, s: str) -> int:
        n = len(s)
        # dp[i] will store the number of ways to decode the substring s[0...i-1]
        # We use n+1 size for dp array to handle base cases easily.
        dp = [0] * (n + 1)

        # Base case: An empty string has one way to decode (no characters, so no decoding needed).
        dp[0] = 1

        # Iterate through the string from left to right
        for i in range(1, n + 1):
            # Check for single-digit decoding
            # If the current digit is not '0', it can be decoded as a single character.
            if s[i - 1] != '0':
                dp[i] += dp[i - 1]

            # Check for two-digit decoding
            # If we are at least at the second character (i >= 2)
            # and the two-digit number formed by s[i-2]s[i-1] is valid (between 10 and 26 inclusive).
            if i >= 2:
                two_digit_num = int(s[i - 2:i])
                if 10 <= two_digit_num <= 26:
                    dp[i] += dp[i - 2]

        # The result is stored in dp[n], representing the number of ways to decode the entire string s.
        return dp[n]

s = Solution()
s1 = "12"

s.numDecodings(s1)

"""
91. Decode Ways
Medium
Topics
premium lock iconCompanies

You have intercepted a secret message encoded as a string of numbers. The message is decoded via the following mapping:

"1" -> 'A'

"2" -> 'B'

...

"25" -> 'Y'

"26" -> 'Z'

However, while decoding the message, you realize that there are many different ways you can decode the message because some codes are contained in other codes ("2" and "5" vs "25").

For example, "11106" can be decoded into:

    "AAJF" with the grouping (1, 1, 10, 6)
    "KJF" with the grouping (11, 10, 6)
    The grouping (1, 11, 06) is invalid because "06" is not a valid code (only "6" is valid).

Note: there may be strings that are impossible to decode.

Given a string s containing only digits, return the number of ways to decode it. If the entire string cannot be decoded in any valid way, return 0.

The test cases are generated so that the answer fits in a 32-bit integer.



Example 1:

Input: s = "12"

Output: 2

Explanation:

"12" could be decoded as "AB" (1 2) or "L" (12).

Example 2:

Input: s = "226"

Output: 3

Explanation:

"226" could be decoded as "BZ" (2 26), "VF" (22 6), or "BBF" (2 2 6).

Example 3:

Input: s = "06"

Output: 0

Explanation:

"06" cannot be mapped to "F" because of the leading zero ("6" is different from "06"). In this case, the string is not a valid encoding, so return 0.



Constraints:

    1 <= s.length <= 100
    s contains only digits and may contain leading zero(s).


"""