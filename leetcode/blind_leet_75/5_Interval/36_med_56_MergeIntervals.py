def merge(intervals):
    if not intervals:
        return []

    intervals.sort(key=lambda x: x[0])  # Sort by start time
    merged = [intervals[0]]

    for current in intervals[1:]:
        last = merged[-1]
        if current[0] <= last[1]:
            # Overlap: merge intervals
            last[1] = max(last[1], current[1])
        else:
            merged.append(current)
    return merged


print(merge([[1,3],[2,6],[8,10],[15,18]]))   # Output: [[1,6],[8,10],[15,18]]
print(merge([[1,4],[4,5]]))                   # Output: [[1,5]]
print(merge([[4,7],[1,4]]))                   # Output: [[1,7]]


"""
56. Merge Intervals
Medium
Topics
premium lock iconCompanies

Given an array of intervals where intervals[i] = [starti, endi], merge all overlapping intervals, and return an array of the non-overlapping intervals that cover all the intervals in the input.



Example 1:

Input: intervals = [[1,3],[2,6],[8,10],[15,18]]
Output: [[1,6],[8,10],[15,18]]
Explanation: Since intervals [1,3] and [2,6] overlap, merge them into [1,6].

Example 2:

Input: intervals = [[1,4],[4,5]]
Output: [[1,5]]
Explanation: Intervals [1,4] and [4,5] are considered overlapping.

Example 3:

Input: intervals = [[4,7],[1,4]]
Output: [[1,7]]
Explanation: Intervals [1,4] and [4,7] are considered overlapping.



Constraints:

    1 <= intervals.length <= 104
    intervals[i].length == 2
    0 <= starti <= endi <= 104


"""


"""
The **Merge Intervals** problem asks to combine all overlapping intervals into merged intervals that cover the same ranges without overlaps.

***

## Approach

1. Sort intervals by their start time.
2. Initialize an output list with the first interval.
3. For each interval from the second onward:
   - If it overlaps with the last interval in output (its start is <= last interval's end), merge by updating the end to max of both.
   - Else, append the interval as is.

***

## Python Solution

```python
def merge(intervals):
    if not intervals:
        return []
    
    intervals.sort(key=lambda x: x[0])  # Sort by start time
    merged = [intervals[0]]

    for current in intervals[1:]:
        last = merged[-1]
        if current[0] <= last[1]:
            # Overlap: merge intervals
            last[1] = max(last[1], current[1])
        else:
            merged.append(current)
    return merged
```

***

## Example Test Cases

```python
print(merge([[1,3],[2,6],[8,10],[15,18]]))   # Output: [[1,6],[8,10],[15,18]]
print(merge([[1,4],[4,5]]))                   # Output: [[1,5]]
print(merge([[4,7],[1,4]]))                   # Output: [[1,7]]
```

***

## Explanation

- Sort intervals to process them in ascending order.
- Merge intervals when overlapping occurs (start <= last end).
- Otherwise, simply append a new interval.

***

## Complexity

- Time: $$O(n \log n)$$ due to sorting.
- Space: $$O(n)$$ for the output array (in-place if allowed).

***

**Summary:**  
This is a classic greedy algorithm problem solved by sorting first and merging intervals in linear scan. It’s efficient for large inputs and widely used in scheduling and interval problems.[1][2]

[1](https://www.interviewcoder.co/leetcode-problems/minimum-window-substring)
[2](https://neetcode.io/solutions/longest-repeating-character-replacement)

"""