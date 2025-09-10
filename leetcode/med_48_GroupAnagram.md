Here is a clean, efficient Python solution to LeetCode 49: **Group Anagrams**, with step-by-step comments to help understanding:

```python
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
print(sol.groupAnagrams(["eat","tea","tan","ate","nat","bat"]))
# Output: [['eat', 'tea', 'ate'], ['tan', 'nat'], ['bat']]
```

***

### Explanation:
- Each group of anagrams can be uniquely identified by sorting its characters (so "eat", "tea", "ate" all become "aet").[1][2]
- We use a dictionary (`defaultdict` of lists) to collect words grouped by these sorted keys.
- Finally, we return all grouped anagram lists as the result.
- This approach runs in $$O(N \times M \log M)$$ time, where $$N$$ is number of strings, and $$M$$ max string length (sorting each string).

This solution is standard, clean, and accepted widely in interviews and competitive coding platforms.[2][1]

[1](https://stackoverflow.com/questions/76901786/here-is-my-python-solution-for-leetcode-49-what-is-the-time-complexity-and-why)
[2](https://algo.monster/liteproblems/49)
[3](https://stackoverflow.com/questions/70636150/group-anagrams-leetcode-question-python)
[4](https://dev.to/jabermudez11/group-anagrams-python-solution-1482)
[5](https://leetcode.com/problems/group-anagrams/)
[6](https://www.youtube.com/watch?v=eDmxPfVa81k)
[7](https://www.reddit.com/r/leetcode/comments/vxbnz4/how_do_you_guys_solve_group_anagrams_problems/)
[8](https://neetcode.io/solutions/group-anagrams)
[9](https://www.youtube.com/watch?v=vzdNOK2oB2E)