from collections import defaultdict


def groupAnagrams(strs):
    groups = defaultdict(list)

    for s in strs:
        key = ''.join(sorted(s))
        groups[key].append(s)

    return list(groups.values())

print(groupAnagrams(["eat","tea","tan","ate","nat","bat"]))
# Output: [["eat","tea","ate"], ["tan","nat"], ["bat"]]

print(groupAnagrams([""]))
# Output: [[""]]

print(groupAnagrams(["a"]))
# Output: [["a"]]


"""
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



Constraints:

    1 <= strs.length <= 104
    0 <= strs[i].length <= 100
    strs[i] consists of lowercase English letters.

"""

"""
The problem is **Group Anagrams**: group all strings that are anagrams of each other together.

***

## Approach

- Use a hashmap (dictionary) keyed by a **canonical form** of the string: the sorted characters of the string.
- For each string:
  - Sort its characters to get the key.
  - Append the original string to the list for that key.
- Return all grouped lists.

***

## Python Solution

```python
from collections import defaultdict

def groupAnagrams(strs):
    groups = defaultdict(list)
    
    for s in strs:
        key = ''.join(sorted(s))
        groups[key].append(s)
    
    return list(groups.values())
```

***

## Explanation

- Sorting characters of an anagram results in a unique key.
- All strings sharing the same sorted key are anagrams grouped together.

***

## Example Usage

```python
print(groupAnagrams(["eat","tea","tan","ate","nat","bat"]))
# Output: [["eat","tea","ate"], ["tan","nat"], ["bat"]]

print(groupAnagrams([""]))
# Output: [[""]]

print(groupAnagrams(["a"]))
# Output: [["a"]]
```

***

## Complexity

- Time: $$O(n k \log k)$$, where $$n$$ is the number of strings, $$k$$ is max string length (sorting each string).
- Space: $$O(n k)$$ to store grouped strings.

***

**Summary:**  
Grouping anagrams is straightforward using sorted string keys as hashmap keys, enabling efficient and clear grouping of anagram strings.[1][2]

[1](https://algo.monster/liteproblems/242)
[2](https://leetcode.com/problems/valid-anagram/)
"""