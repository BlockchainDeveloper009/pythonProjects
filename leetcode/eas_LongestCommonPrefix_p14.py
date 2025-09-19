from typing import List

class Solution:
    def longestCommonPrefix(self, strs: List[str]) -> str:
        if not strs:
            return ""

        # Iterate over the characters of the first string
        for i in range(len(strs[0])):
            # Get the character at position i in the first string
            char = strs[0][i]
            # Check the same position in all other strings
            for s in strs[1:]:
                # If the current index i is out of range for string or character doesn't match
                if i >= len(s) or s[i] != char:
                    # Return the prefix up to but not including i
                    return strs[0][:i]
        return strs[0]


sol = Solution()

print(sol.longestCommonPrefix(["inflo","flower","flow","flight"]))  # Output: "fl"
print(sol.longestCommonPrefix(["dog","racecar","car"]))     # Output: ""