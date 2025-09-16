from collections import Counter


def topKFrequent(nums, k):
    freq_map = Counter(nums)
    max_freq = max(freq_map.values())

    # Buckets: frequency -> list of numbers
    buckets = [[] for _ in range(max_freq + 1)]

    for num, freq in freq_map.items():
        buckets[freq].append(num)

    result = []
    for freq in range(max_freq, 0, -1):
        for num in buckets[freq]:
            result.append(num)
            if len(result) == k:
                return result


print(topKFrequent([1,1,1,2,2,3], 2))  # Output: [1, 2]
print(topKFrequent([1], 1))            # Output: [1]
print(topKFrequent([1,2,1,2,1,2,3,1,3,2], 2))  # Output: [1, 2]



"""
347. Top K Frequent Elements
Medium
Topics
premium lock iconCompanies

Given an integer array nums and an integer k, return the k most frequent elements. You may return the answer in any order.



Example 1:

Input: nums = [1,1,1,2,2,3], k = 2

Output: [1,2]

Example 2:

Input: nums = [1], k = 1

Output: [1]

Example 3:

Input: nums = [1,2,1,2,1,2,3,1,3,2], k = 2

Output: [1,2]



Constraints:

    1 <= nums.length <= 105
    -104 <= nums[i] <= 104
    k is in the range [1, the number of unique elements in the array].
    It is guaranteed that the answer is unique.



Follow up: Your algorithm's time complexity must be better than O(n log n), where n is the array's size.

"""

""""
To find the **top k frequent elements** in an array efficiently, use a frequency map and a heap or bucket sort for better than $$O(n \log n)$$ complexity.

***

## Approach 1: Heap (Priority Queue)

- Count frequencies of elements using a hash map.
- Use a min-heap of size k to keep the top k frequent.
- Push element and frequency; if size > k, pop smallest frequency.
- Extract all elements in the heap at the end.

### Complexity  
- Time: $$O(n \log k)$$  
- Space: $$O(n)$$

***

## Approach 2: Bucket Sort (Better for this problem)

- Count frequencies using hash map.
- Create buckets where index = frequency, value = list of elements.
- Frequencies range 1 to max frequency.
- Iterate buckets in reverse to collect k most frequent elements.

### Complexity  
- Time: $$O(n)$$  
- Space: $$O(n)$$

***

## Python Code: Bucket Sort

```python
from collections import Counter

def topKFrequent(nums, k):
    freq_map = Counter(nums)
    max_freq = max(freq_map.values())
    
    # Buckets: frequency -> list of numbers
    buckets = [[] for _ in range(max_freq + 1)]
    
    for num, freq in freq_map.items():
        buckets[freq].append(num)
    
    result = []
    for freq in range(max_freq, 0, -1):
        for num in buckets[freq]:
            result.append(num)
            if len(result) == k:
                return result
```

***

## Example Usage

```python
print(topKFrequent([1,1,1,2,2,3], 2))  # Output: [1, 2]
print(topKFrequent([1], 1))            # Output: [1]
print(topKFrequent([1,2,1,2,1,2,3,1,3,2], 2))  # Output: [1, 2]
```

***

## Explanation

- Counting frequencies allows grouping elements by their occurrence count.
- Bucket sorting frequencies helps efficiently extract top k elements.
- Avoids sorting the entire array or map entries, improving performance.

***

**Summary:**  
Bucket sort based on frequency offers a linear-time solution suitable for large input, surpassing naive sorting by frequency.
"""