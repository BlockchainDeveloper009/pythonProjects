
def longestConsecutive(nums):
    if not nums:
        return 0

    num_set = set(nums)
    longest_streak = 0

    for num in num_set:
        # Only check for starts of sequences
        if num - 1 not in num_set:
            current_num = num
            current_streak = 1

            while current_num + 1 in num_set:
                current_num += 1
                current_streak += 1

            longest_streak = max(longest_streak, current_streak)

    return longest_streak

print(longestConsecutive([100,4,200,1,3,2])) # Output: 4
print(longestConsecutive([0,3,7,2,5,8,4,6,0,1])) # Output: 9
print(longestConsecutive([1,0,1,2])) # Output: 3


"""
128. Longest Consecutive Sequence
Medium
Topics
premium lock iconCompanies

Given an unsorted array of integers nums, return the length of the longest consecutive elements sequence.

You must write an algorithm that runs in O(n) time.



Example 1:

Input: nums = [100,4,200,1,3,2]
Output: 4
Explanation: The longest consecutive elements sequence is [1, 2, 3, 4]. Therefore its length is 4.

Example 2:

Input: nums = [0,3,7,2,5,8,4,6,0,1]
Output: 9

Example 3:

Input: nums = [1,0,1,2]
Output: 3



Constraints:

    0 <= nums.length <= 105
    -109 <= nums[i] <= 109


"""


"""
The **Longest Consecutive Sequence** problem can be solved in **O(n)** time using a hash set to achieve constant time lookups, avoiding sorting.

***

## Approach (Hash Set)

1. Insert all numbers into a set for O(1) lookups.
2. Iterate through each number, check if it's the start of a sequence (number - 1 is not in the set).
3. For each sequence start, count the length by checking consecutive numbers (number + 1, +2, ...).
4. Track the maximum length found.

***

## Python Code

```python
def longestConsecutive(nums):
    if not nums:
        return 0

    num_set = set(nums)
    longest_streak = 0

    for num in num_set:
        # Only check for starts of sequences
        if num - 1 not in num_set:
            current_num = num
            current_streak = 1

            while current_num + 1 in num_set:
                current_num += 1
                current_streak += 1

            longest_streak = max(longest_streak, current_streak)

    return longest_streak
```

***

## Example

```python
print(longestConsecutive([100,4,200,1,3,2])) # Output: 4
print(longestConsecutive([0,3,7,2,5,8,4,6,0,1])) # Output: 9
print(longestConsecutive([1,0,1,2])) # Output: 3
```

***

## Explanation

- Using a set allows constant time membership check.
- Only start counting streaks if current number is the start (no `num-1` in set).
- Efficiently finds longest consecutive sequences without sorting.

***

## Complexity

- **Time:** $$O(n)$$, each number is processed once.
- **Space:** $$O(n)$$ for the set.

***

**Summary:**  
Longest consecutive sequence is efficiently found by hashing and scanning only possible sequence starts, achieving linear time complexity.[1][2][3]

[1](https://www.youtube.com/watch?v=tkNWKvxI3mU)
[2](https://neetcode.io/solutions/longest-repeating-character-replacement)
[3](https://www.geeksforgeeks.org/dsa/find-the-smallest-window-in-a-string-containing-all-characters-of-another-string/)
"""