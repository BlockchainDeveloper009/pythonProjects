import heapq

class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

    def __lt__(self, other):  # for heap comparisons
        return self.val < other.val

    # The __repr__ method provides a useful string for developers
    def __repr__(self):
        return f"ListNode(val={self.val}, next={self.next})"

def mergeKLists(lists):
    min_heap = []
    for node in lists:
        if node:
            heapq.heappush(min_heap, node)

    dummy = ListNode()
    current = dummy
    #print(vars(current))
    while min_heap:
        node = heapq.heappop(min_heap)
        current.next = node
        current = current.next
       # print(vars(current))
        if node.next:
            heapq.heappush(min_heap, node.next)

    return dummy.next


#Python Code Using Divide and Conquer
def mergeTwoLists(l1, l2):
    if not l1 or not l2:
        return l1 or l2
    if l1.val < l2.val:
        l1.next = mergeTwoLists(l1.next, l2)
        return l1
    else:
        l2.next = mergeTwoLists(l1, l2.next)
        return l2

def mergeKListsDivideConquer(lists):
    if not lists:
        return None
    interval = 1
    n = len(lists)
    while interval < n:
        for i in range(0, n - interval, interval * 2):
            lists[i] = mergeTwoLists(lists[i], lists[i + interval])
        interval *= 2
    return lists[0]


def build_list(arr):
    dummy = ListNode()
    curr = dummy
    for val in arr:
        curr.next = ListNode(val)
        curr = curr.next
    return dummy.next

def print_list(head):
    vals = []
    while head:
        vals.append(head.val)
        head = head.next
    print(vals)


#
# lists_arr = [[1,4,5],[1,3,4],[2,6]]
# lists = [build_list(arr) for arr in lists_arr]

lists_arr2 = [[1,3,5],[2,4,6],[7,9,8]]
lists = [build_list(arr) for arr in lists_arr2]

merged_heap = mergeKLists(lists)
print_list(merged_heap)  # Output: [1,1,2,3,4,4,5,6]

# # Rebuild lists for divide and conquer since previous consumed them
# lists = [build_list(arr) for arr in lists_arr]
#
# merged_divide = mergeKListsDivideConquer(lists)
# print_list(merged_divide)  # Output: [1,1,2,3,4,4,5,6]


"""
23. Merge k Sorted Lists
Hard
Topics
premium lock iconCompanies
You are given an array of k linked-lists lists, each linked-list is sorted in ascending order.
Merge all the linked-lists into one sorted linked-list and return it.

Example 1:

Input: lists = [[1,4,5],[1,3,4],[2,6]]
Output: [1,1,2,3,4,4,5,6]
Explanation: The linked-lists are:
[
  1->4->5,
  1->3->4,
  2->6
]
merging them into one sorted linked list:
1->1->2->3->4->4->5->6

Example 2:
Input: lists = []
Output: []

Example 3:
Input: lists = [[]]
Output: []

Constraints:
    k == lists.length
    0 <= k <= 104
    0 <= lists[i].length <= 500
    -104 <= lists[i][j] <= 104
    lists[i] is sorted in ascending order.
    The sum of lists[i].length will not exceed 104.


"""


"""
The problem of merging k sorted linked lists efficiently can be solved using a **min-heap (priority queue)** or by **divide and conquer** merging.

***

## Approach 1: Min-Heap

- Push the head of every non-empty list into a min-heap keyed by node value.
- Pop the smallest element from heap, add it to the merged list.
- Push the next node from the popped element’s list into the heap.
- Repeat until heap is empty.

***

## Approach 2: Divide and Conquer (Pairwise Merge)

- Recursively merge pairs of linked lists until only one remains.
- This is like merge sort on lists, efficiently reducing complexity.

***

## Python Code Using Min-Heap

```python
import heapq

class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

    def __lt__(self, other):  # for heap comparisons
        return self.val < other.val

def mergeKLists(lists):
    min_heap = []
    for node in lists:
        if node:
            heapq.heappush(min_heap, node)

    dummy = ListNode()
    current = dummy

    while min_heap:
        node = heapq.heappop(min_heap)
        current.next = node
        current = current.next
        if node.next:
            heapq.heappush(min_heap, node.next)

    return dummy.next
```

***

## Python Code Using Divide and Conquer

```python
def mergeTwoLists(l1, l2):
    if not l1 or not l2:
        return l1 or l2
    if l1.val < l2.val:
        l1.next = mergeTwoLists(l1.next, l2)
        return l1
    else:
        l2.next = mergeTwoLists(l1, l2.next)
        return l2

def mergeKListsDivideConquer(lists):
    if not lists:
        return None
    interval = 1
    n = len(lists)
    while interval < n:
        for i in range(0, n - interval, interval * 2):
            lists[i] = mergeTwoLists(lists[i], lists[i + interval])
        interval *= 2
    return lists[0]
```

***

## Helper Functions to Build and Print Lists

```python
def build_list(arr):
    dummy = ListNode()
    curr = dummy
    for val in arr:
        curr.next = ListNode(val)
        curr = curr.next
    return dummy.next

def print_list(head):
    vals = []
    while head:
        vals.append(head.val)
        head = head.next
    print(vals)
```

***

## Example Usage

```python
lists_arr = [[1,4,5],[1,3,4],[2,6]]
lists = [build_list(arr) for arr in lists_arr]

merged_heap = mergeKLists(lists)
print_list(merged_heap)  # Output: [1,1,2,3,4,4,5,6]

# Rebuild lists for divide and conquer since previous consumed them
lists = [build_list(arr) for arr in lists_arr]

merged_divide = mergeKListsDivideConquer(lists)
print_list(merged_divide)  # Output: [1,1,2,3,4,4,5,6]
```

***

## Complexity

| Method                | Time Complexity                 | Space Complexity   |
|-----------------------|--------------------------------|--------------------|
| Min-Heap              | $$O(N \log k)$$, $$N$$ total nodes  | $$O(k)$$           |
| Divide and Conquer    | $$O(N \log k)$$                 | $$O(1)$$ or recursion stack |

***

**Summary:**  
The min-heap method is elegant and straightforward, while divide and conquer reduces problem size logarithmically. Both yield efficient merging of k sorted lists in $$O(N \log k)$$ time, where $$N$$ is total nodes across all lists.[1][2][3]

[1](https://neetcode.io/problems/clone-graph)
[2](https://algo.monster/liteproblems/133)
[3](https://neetcode.io/problems/linked-list-cycle-detection?list=neetcode150)
"""