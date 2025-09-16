def insert(intervals, newInterval):
    result = []
    i = 0
    n = len(intervals)

    # Add intervals ending before newInterval starts
    while i < n and intervals[i][1] < newInterval[0]:
        result.append(intervals[i])
        i += 1

    # Merge overlapping intervals with newInterval
    while i < n and intervals[i][0] <= newInterval[1]:
        newInterval[0] = min(intervals[i][0], newInterval[0])
        newInterval[1] = max(intervals[i][1], newInterval[1])
        i += 1

    # Add the merged interval
    result.append(newInterval)

    # Add remaining intervals
    while i < n:
        result.append(intervals[i])
        i += 1

    return result


print(insert([[1,3],[6,9]], [2,5]))               # Output: [[1,5],[6,9]]
print(insert([[1,2],[3,5],[6,7],[8,10],[12,16]], [4,8]))  # Output: [[1,2],[3,10],[12,16]]
print(insert([], [5,7]))                           # Output: [[5,7]]
print(insert([[1,5]], [2,3]))                      # Output: [[1,5]]
print(insert([[1,5]], [2,7]))                      # Output: [[1,7]]



"""
57. Insert Interval
Medium
Topics
premium lock iconCompanies
Hint

You are given an array of non-overlapping intervals intervals where intervals[i] = [starti, endi] represent the start and the end of the ith interval and intervals is sorted in ascending order by starti. You are also given an interval newInterval = [start, end] that represents the start and end of another interval.

Insert newInterval into intervals such that intervals is still sorted in ascending order by starti and intervals still does not have any overlapping intervals (merge overlapping intervals if necessary).

Return intervals after the insertion.

Note that you don't need to modify intervals in-place. You can make a new array and return it.



Example 1:

Input: intervals = [[1,3],[6,9]], newInterval = [2,5]
Output: [[1,5],[6,9]]

Example 2:

Input: intervals = [[1,2],[3,5],[6,7],[8,10],[12,16]], newInterval = [4,8]
Output: [[1,2],[3,10],[12,16]]
Explanation: Because the new interval [4,8] overlaps with [3,5],[6,7],[8,10].



Constraints:

    0 <= intervals.length <= 104
    intervals[i].length == 2
    0 <= starti <= endi <= 105
    intervals is sorted by starti in ascending order.
    newInterval.length == 2
    0 <= start <= end <= 105


"""


"""
The problem **Insert Interval** requires inserting a new interval into a sorted list of non-overlapping intervals and merging any overlapping intervals after the insertion.

***

## Approach

1. **Add all intervals that end before the new interval starts** directly to the result since they don't overlap.
2. **Merge all intervals that overlap with the new interval** by updating the new interval's start and end.
3. **Add the merged new interval** to the result.
4. **Add remaining intervals** after the new interval.

***

## Python Solution

```python
def insert(intervals, newInterval):
    result = []
    i = 0
    n = len(intervals)

    # Add intervals ending before newInterval starts
    while i < n and intervals[i][1] < newInterval[0]:
        result.append(intervals[i])
        i += 1

    # Merge overlapping intervals with newInterval
    while i < n and intervals[i][0] <= newInterval[1]:
        newInterval[0] = min(intervals[i][0], newInterval[0])
        newInterval[1] = max(intervals[i][1], newInterval[1])
        i += 1

    # Add the merged interval
    result.append(newInterval)

    # Add remaining intervals
    while i < n:
        result.append(intervals[i])
        i += 1

    return result
```

***

## Example Test Cases

```python
print(insert([[1,3],[6,9]], [2,5]))               # Output: [[1,5],[6,9]]
print(insert([[1,2],[3,5],[6,7],[8,10],[12,16]], [4,8]))  # Output: [[1,2],[3,10],[12,16]]
print(insert([], [5,7]))                           # Output: [[5,7]]
print(insert([[1,5]], [2,3]))                      # Output: [[1,5]]
print(insert([[1,5]], [2,7]))                      # Output: [[1,7]]
```

***

## Explanation

- First, append all intervals which don’t overlap and come before `newInterval`.
- Merge all overlapping intervals by expanding `newInterval`.
- Append the merged interval.
- Append any intervals that come after `newInterval`.

***

## Complexity

- Time: $$O(n)$$ where $$n$$ is the number of intervals.
- Space: $$O(n)$$ for the merged list.

This approach efficiently inserts and merges intervals while maintaining sorted order and non-overlapping conditions.
"""