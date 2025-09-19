
import heapq

class MedianFinder:
    def __init__(self):
        # Max-heap for smaller half (store negatives of numbers)
        self.small = []
        # Min-heap for larger half
        self.large = []

    def addNum(self, num: int) -> None:
        # Add to max heap (small)
        heapq.heappush(self.small, -num)

        # Move the largest of small to large
        if self.small and self.large and (-self.small[0]) > self.large[0]:
            val = -heapq.heappop(self.small)
            heapq.heappush(self.large, val)

        # Balance sizes: allow small to have one more element
        if len(self.small) > len(self.large) + 1:
            val = -heapq.heappop(self.small)
            heapq.heappush(self.large, val)
        elif len(self.large) > len(self.small):
            val = heapq.heappop(self.large)
            heapq.heappush(self.small, -val)

    def findMedian(self) -> float:
        if len(self.small) > len(self.large):
            return float(-self.small[0])
        else:
            return (-self.small[0] + self.large[0]) / 2.0


mf = MedianFinder()
mf.addNum(1)              # [1]
mf.addNum(2)              # [1, 2]
print(mf.findMedian())    # 1.5
mf.addNum(3)              # [1, 2, 3]
print(mf.findMedian())    # 2.0


"""
295. Find Median from Data Stream
Hard
Topics
premium lock iconCompanies

The median is the middle value in an ordered integer list. If the size of the list is even, there is no middle value, and the median is the mean of the two middle values.

    For example, for arr = [2,3,4], the median is 3.
    For example, for arr = [2,3], the median is (2 + 3) / 2 = 2.5.

Implement the MedianFinder class:

    MedianFinder() initializes the MedianFinder object.
    void addNum(int num) adds the integer num from the data stream to the data structure.
    double findMedian() returns the median of all elements so far. Answers within 10-5 of the actual answer will be accepted.



Example 1:

Input
["MedianFinder", "addNum", "addNum", "findMedian", "addNum", "findMedian"]
[[], [1], [2], [], [3], []]
Output
[null, null, null, 1.5, null, 2.0]

Explanation
MedianFinder medianFinder = new MedianFinder();
medianFinder.addNum(1);    // arr = [1]
medianFinder.addNum(2);    // arr = [1, 2]
medianFinder.findMedian(); // return 1.5 (i.e., (1 + 2) / 2)
medianFinder.addNum(3);    // arr[1, 2, 3]
medianFinder.findMedian(); // return 2.0



Constraints:

    -105 <= num <= 105
    There will be at least one element in the data structure before calling findMedian.
    At most 5 * 104 calls will be made to addNum and findMedian.



Follow up:

    If all integer numbers from the stream are in the range [0, 100], how would you optimize your solution?
    If 99% of all integer numbers from the stream are in the range [0, 100], how would you optimize your solution?


"""


"""
The problem is to design a data structure that efficiently supports adding numbers from a stream and finding the median at any time.

***

## Approach: Two Heaps

Maintain two heaps:
- **Max-heap:** stores the smaller half of numbers.
- **Min-heap:** stores the larger half.

Balance these heaps so that:
- Their sizes differ at most by 1.
- Max-heap root ≤ Min-heap root.

Median:
- If sizes equal, median = average of roots of both heaps.
- Otherwise, median = root of the larger heap.

***

## Python Code

```python
import heapq

class MedianFinder:
    def __init__(self):
        # Max-heap for smaller half (store negatives of numbers)
        self.small = []
        # Min-heap for larger half
        self.large = []

    def addNum(self, num: int) -> None:
        # Add to max heap (small)
        heapq.heappush(self.small, -num)

        # Move the largest of small to large
        if self.small and self.large and (-self.small[0]) > self.large[0]:
            val = -heapq.heappop(self.small)
            heapq.heappush(self.large, val)

        # Balance sizes: allow small to have one more element
        if len(self.small) > len(self.large) + 1:
            val = -heapq.heappop(self.small)
            heapq.heappush(self.large, val)
        elif len(self.large) > len(self.small):
            val = heapq.heappop(self.large)
            heapq.heappush(self.small, -val)

    def findMedian(self) -> float:
        if len(self.small) > len(self.large):
            return float(-self.small[0])
        else:
            return (-self.small[0] + self.large[0]) / 2.0
```

***

## Explanation

- Use negative values in `small` heap to simulate max-heap.
- Always move top element crossing the heap condition.
- Keeps two balanced heaps for median computation.

***

## Example Usage

```python
mf = MedianFinder()
mf.addNum(1)              # [1]
mf.addNum(2)              # [1, 2]
print(mf.findMedian())    # 1.5
mf.addNum(3)              # [1, 2, 3]
print(mf.findMedian())    # 2.0
```

***

## Complexity

- addNum: $$O(\log n)$$ due to heap push/pop.
- findMedian: $$O(1)$$.

***

## Follow-up Tips

- If numbers range only [0..100], use a frequency array for counting and prefix sums for median.
- If 99% numbers are in [0..100], combine frequency array for that range and separate structure for outliers.

***

**Summary:**  
Using two heaps to maintain balanced halves of the data stream, median can be found efficiently with logarithmic insert time and constant retrieval time.
"""