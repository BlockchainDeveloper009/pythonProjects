

def eraseOverlapIntervals(intervals):
    if not intervals:
        return 0

    intervals.sort(key=lambda x: x[1])  # Sort by end time
    count = 0
    last_end = float('-inf')

    for interval in intervals:
        if interval[0] >= last_end:
            last_end = interval[1]
        else:
            count += 1  # Overlapping interval, needs removal

    return count



print(eraseOverlapIntervals([[1,2],[2,3],[3,4],[1,3]]))  # Output: 1
print(eraseOverlapIntervals([[1,2],[1,2],[1,2]]))        # Output: 2
print(eraseOverlapIntervals([[1,2],[2,3]]))              # Output: 0



"""
435. Non-overlapping Intervals
Medium
Topics
premium lock iconCompanies

Given an array of intervals intervals where intervals[i] = [starti, endi], return the minimum number of intervals you need to remove to make the rest of the intervals non-overlapping.

Note that intervals which only touch at a point are non-overlapping. For example, [1, 2] and [2, 3] are non-overlapping.



Example 1:

Input: intervals = [[1,2],[2,3],[3,4],[1,3]]
Output: 1
Explanation: [1,3] can be removed and the rest of the intervals are non-overlapping.

Example 2:

Input: intervals = [[1,2],[1,2],[1,2]]
Output: 2
Explanation: You need to remove two [1,2] to make the rest of the intervals non-overlapping.

Example 3:

Input: intervals = [[1,2],[2,3]]
Output: 0
Explanation: You don't need to remove any of the intervals since they're already non-overlapping.



Constraints:

    1 <= intervals.length <= 105
    intervals[i].length == 2
    -5 * 104 <= starti < endi <= 5 * 104


"""

"""
The **Non-overlapping Intervals** problem is best solved using a greedy approach by sorting intervals based on their **end times** and selecting intervals to keep while minimizing removals.

***

## Approach

1. Sort the intervals by their **end time** to always pick the interval that finishes earliest.
2. Iterate through the sorted intervals, keeping track of the end time of the last added interval.
3. For each interval:
   - If its start time is greater or equal to the last added interval's end, add it (no overlap).
   - Otherwise, skip it (count as removal).
4. The number of removals is total intervals minus the number of added intervals.

***

## Python Solution

```python
def eraseOverlapIntervals(intervals):
    if not intervals:
        return 0
    
    intervals.sort(key=lambda x: x[1])  # Sort by end time
    count = 0
    last_end = float('-inf')

    for interval in intervals:
        if interval[0] >= last_end:
            last_end = interval[1]
        else:
            count += 1  # Overlapping interval, needs removal

    return count
```

***

## Example Test Cases

```python
print(eraseOverlapIntervals([[1,2],[2,3],[3,4],[1,3]]))  # Output: 1
print(eraseOverlapIntervals([[1,2],[1,2],[1,2]]))        # Output: 2
print(eraseOverlapIntervals([[1,2],[2,3]]))              # Output: 0
```

***

## Explanation

- Sorting by end time ensures you always pick the earliest finishing interval.
- Keep intervals that do not overlap with the previous chosen interval.
- Count others as to be removed to avoid overlaps.

***

## Complexity

- Time: $$O(n \log n)$$ due to sorting.
- Space: $$O(1)$$ or $$O(n)$$ depending on sorting implementation.

***

**Summary:**  
This greedy approach efficiently computes the minimum removals needed to create a non-overlapping set by always choosing intervals with minimum end times to maximize non-overlapping intervals.[1][2]

[1](https://neetcode.io/solutions/longest-repeating-character-replacement)
[2](https://www.interviewcoder.co/leetcode-problems/minimum-window-substring)
"""