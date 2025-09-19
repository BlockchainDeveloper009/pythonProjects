"""
49. Group Anagrams
Medium
Topics
premium lock iconCompanies

Given an array of strings strs, group the

together. You can return the answer in any order.



Example 1:

Input: strs = ["eat","tea","tan","ate","nat","bat"]

Output: [["bat"],["nat","tan"],["ate","eat","tea"]]

Explanation:

    There is no string in strs that can be rearranged to form "bat".
    The strings "nat" and "tan" are anagrams as they can be rearranged to form each other.
    The strings "ate", "eat", and "tea" are anagrams as they can be rearranged to form each other.

Example 2:

Input: strs = [""]

Output: [[""]]

Example 3:

Input: strs = ["a"]

Output: [["a"]]


"""

from collections import defaultdict
from typing import List


class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        # Create a dictionary where key = sorted string, value = list of anagrams
        anagrams = defaultdict(list)

        for s in strs:
            # Sort characters in the string to get the key representing anagram class
            sorted_str = ''.join(sorted(s))

            # Append original string to the list at this key
            anagrams[sorted_str].append(s)

        # Return all groups of anagrams (dictionary values)
        return list(anagrams.values())


# Example usage:
sol = Solution()
print(sol.groupAnagrams(["eat", "tea", "tan", "ate", "nat", "bat"]))
# Output: [['eat', 'tea', 'ate'], ['tan', 'nat'], ['bat']]
