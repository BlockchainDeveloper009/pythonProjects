# The "Longest Consecutive Sequence" problem asks you to find the length
# of the longest sequence of consecutive numbers in an unsorted array of integers.
# The algorithm should run in O(n) time.

def longestConsecutive(nums: list) -> int:
    """
    Finds the length of the longest consecutive sequence in a list of numbers.

    This solution uses a set for efficient lookups, achieving an O(n) time complexity.
    It works by checking each number to see if it's the start of a new sequence
    and then counting how long that sequence is.

    Args:
        nums: A list of integers.

    Returns:
        The length of the longest consecutive sequence.
    """
    if not nums:
        # If the input list is empty, there are no sequences.
        return 0

    # Convert the list to a set for O(1) average time complexity lookups.
    num_set = set(nums)
    longest_streak = 0

    # Iterate through each unique number in the set.
    for num in num_set:
        # Check if the current number is the start of a sequence.
        # A number is a "start" if the number immediately before it (num - 1)
        # is not in the set. This crucial check prevents redundant work and
        # ensures the overall O(n) time complexity.
        if (num - 1) not in num_set:
            current_num = num
            current_streak = 1

            # While the next number in the sequence exists, continue the streak.
            while (current_num + 1) in num_set:
                current_num += 1
                current_streak += 1

            # Update the longest streak found so far.
            longest_streak = max(longest_streak, current_streak)

    return longest_streak


# --- Test Cases ---

# Example 1: Standard case
print(f"Longest consecutive sequence length for [100, 4, 200, 1, 3, 2] is: {longestConsecutive([100, 4, 200, 1, 3, 2])}")  # Output: 4 (from sequence 1, 2, 3, 4)

# Example 2: Sequence with duplicates and out-of-order numbers
print(f"Longest consecutive sequence length for [0, 3, 7, 2, 5, 8, 4, 6, 0, 1] is: {longestConsecutive([0, 3, 7, 2, 5, 8, 4, 6, 0, 1])}") # Output: 9 (from sequence 0, 1, 2, 3, 4, 5, 6, 7, 8)

# Example 3: Sequence with duplicates and a short sequence
print(f"Longest consecutive sequence length for [1, 0, 1, 2] is: {longestConsecutive([1, 0, 1, 2])}") # Output: 3 (from sequence 0, 1, 2)


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