To efficiently solve "Merge k Sorted Lists", use a **min-heap (priority queue)** so you always link the smallest current node among all the lists, achieving optimal $$O(N \log k)$$ complexity. Here’s a complete Python solution with comments:

```python
from typing import List, Optional
import heapq

# Definition for singly-linked list node.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next
    def __lt__(self, other):
        # Heap requires nodes to be comparable
        return self.val < other.val

class Solution:
    def mergeKLists(self, lists: List[Optional[ListNode]]) -> Optional[ListNode]:
        # Initialize a priority queue (min-heap)
        min_heap = []

        # Push the head of each list onto the heap (ignore empty lists)
        for i, node in enumerate(lists):
            if node:
                heapq.heappush(min_heap, node)

        # Dummy node to simplify edge cases
        dummy = ListNode(0)
        current = dummy

        while min_heap:
            # Pop node with smallest value
            smallest = heapq.heappop(min_heap)
            current.next = smallest
            current = current.next

            # If there's a next node, push onto heap
            if smallest.next:
                heapq.heappush(min_heap, smallest.next)

        return dummy.next
```

### How it works
- Each node on the heap is the smallest currently available from each list.
- Always append the smallest node to result, then push its successor node onto heap.
- Continues until all nodes are merged.

### Why is heap optimal?
- At most $$k$$ nodes are in the heap.
- Each heap operation ($$\log k$$) is efficient, yielding overall $$O(N \log k)$$ performance where $$N$$ is the total number of list nodes.[1][2][3]

***

If you want to see helper functions for building and printing lists, let me know! This implementation is standard for interviews and leetcode.

[1](https://algo.monster/liteproblems/23)
[2](https://neetcode.io/problems/merge-k-sorted-linked-lists?list=neetcode150)
[3](https://favtutor.com/articles/generate-parentheses/)
[4](https://stackoverflow.com/questions/79241278/merge-k-sorted-lists-maximum-recursive-depth-reached)
[5](https://stackoverflow.com/questions/56028554/leetcode-problem-23-merge-k-sorted-lists)
[6](https://www.reddit.com/r/leetcode/comments/1ag7caw/merge_k_sorted_lists_python_solution_question/)
[7](https://leetcode.com/problems/merge-k-sorted-lists/)
[8](https://www.youtube.com/watch?v=q5a5OiGbT6Q)
[9](https://www.youtube.com/watch?v=RyrVWP76lVo)
[10](https://walkccc.me/LeetCode/problems/23/)