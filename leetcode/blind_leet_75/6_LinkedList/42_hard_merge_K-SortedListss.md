The nodes are **individual objects linked together in lists**, not arrays, but the input argument `lists` is an array of linked list heads. The merging algorithm keeps the output sorted by always picking the smallest available value using a min-heap.[3][6]

***

### How the min-heap maintains sorted order (detailed step-by-step for your example):

**Input:**  
lists = $$List1: 1→4→5, List2: 1→3→4, List3: 2→6$$

**Initialization:**  
- Push head nodes’ values and references into the min-heap:  
  heap = $$(1,List1), (1,List2), (2,List3)$$
- The heap always sorts its contents by node value, so pop() gives the minimum.

**Steps for Output:**

1. Pop min (1,List1). Add 1 to result. Push List1.next (4,List1) to heap.  
   heap = $$(1,List2), (2,List3), (4,List1)$$
2. Pop min (1,List2). Add 1 to result. Push List2.next (3,List2).  
   heap = $$(2,List3), (4,List1), (3,List2)$$ ← heap resorts: $$(2,List3), (3,List2), (4,List1)$$
3. Pop min (2,List3). Add 2 to result. Push List3.next (6,List3).  
   heap = $$(3,List2), (4,List1), (6,List3)$$
4. Pop min (3,List2). Add 3 to result. Push List2.next (4,List2).  
   heap = $$(4,List1), (6,List3), (4,List2)$$
5. Pop min (4,List1). Add 4 to result. Push List1.next (5,List1).  
   heap = $$(4,List2), (6,List3), (5,List1)$$
6. Pop min (4,List2). Add 4 to result. List2.next is None, heap unchanged.  
   heap = $$(5,List1), (6,List3)$$
7. Pop min (5,List1). Add 5 to result. List1.next is None.  
   heap = $$(6,List3)$$
8. Pop min (6,List3). Add 6 to result. List3.next is None.  
   heap = $$$$ (empty, done)

**Result List:** $$1, 1, 2, 3, 4, 4, 5, 6$$

***

### Why this produces sorted output

- The heap always contains the smallest available nodes from all lists.
- Each pop operation guarantees the next node in result is the lowest remaining value, maintaining sorted order regardless of which original list it’s from.

***

### Visualization

At each step, the heap efficiently surfaces the smallest candidate, and the output is assembled in increasing order by always picking and advancing only from the smallest node’s own next pointer.[6][3]

***

Let me know if you want a printout of heap contents at each line or a visualization for a larger example!

[1](https://docs.vultr.com/problem-set/merge-k-sorted-lists)
[2](https://www.finalroundai.com/articles/merge-k-sorted-linked-lists)
[3](https://www.geeksforgeeks.org/dsa/merge-k-sorted-linked-lists-set-2-using-min-heap/)
[4](https://takeuforward.org/linked-list/merge-k-sorted-linked-lists)
[5](https://www.geeksforgeeks.org/dsa/merge-k-sorted-linked-lists/)
[6](https://algo.monster/liteproblems/23)
[7](https://leetcode.com/problems/merge-k-sorted-lists/)
[8](https://www.youtube.com/watch?v=q5a5OiGbT6Q)
[9](https://javascript360.org/docs/blind-75-must-do-leetcode/merge-k-sorted-lists/)




Here's a **line-by-line illustration** of the min-heap contents for your example input, with commentary after every heap operation:

**Input:**  
lists = [, , ][1][2][3][4][5][6]

**Initialization:**
- Populate the heap with the head of each list:
  - Heap = [1 → (from list 1), 1 → (from list 2), 2 → (from list 3)]
  - Visually: `[(1, List 1), (1, List 2), (2, List 3)]`

***
[[1,4,5],[1,3,4],[2,6]]
#### Step-by-step heap status and output

| Step | Action                      | Heap Contents                                 | Output              |
|------|-----------------------------|-----------------------------------------------|---------------------|
| 1    | Pop 1 (from list 1)         | [(1, List 2), (2, List 3)]                    | [9]                 |
|      | Push 4 (from list 1)        | [(1, List 2), (2, List 3), (4, List 1)]       |                     |
| 2    | Pop 1 (from list 2)         | [(2, List 3), (4, List 1)]                    | [1][1]              |
|      | Push 3 (from list 2)        | [(2, List 3), (4, List 1), (3, List 2)]       |                     |
| 3    | Pop 2 (from list 3)         | [(3, List 2), (4, List 1)]                    | [1][1][2]           |
|      | Push 6 (from list 3)        | [(3, List 2), (4, List 1), (6, List 3)]       |                     |
| 4    | Pop 3 (from list 2)         | [(4, List 1), (6, List 3)]                    | [1][1][2][3]        |
|      | Push 4 (from list 2)        | [(4, List 1), (6, List 3), (4, List 2)]       |                     |
| 5    | Pop 4 (from list 1)         | [(4, List 2), (6, List 3)]                    | [1][1][2][3][4]     |
|      | Push 5 (from list 1)        | [(4, List 2), (6, List 3), (5, List 1)]       |                     |
| 6    | Pop 4 (from list 2)         | [(5, List 1), (6, List 3)]                    | [1][1][2][3][4][4]  |
|      | (list 2 exhausted)          |                                               |                     |
| 7    | Pop 5 (from list 1)         | [(6, List 3)]                                 | [1][1][2][3][4][4][5]|
|      | (list 1 exhausted)          |                                               |                     |
| 8    | Pop 6 (from list 3)         | []                                            | [1][1][2][3][4][4][5][6]|

***

### Visualization summary

At every step:
- The heap contains the current smallest available heads from each remaining list.
- You always pop the smallest node and if it has a next, you push its next node.
- The heap is a **min-priority queue** representing "the next most promising candidate" from across all the lists.
- The result is assembled in strictly sorted order as each pop provides the next minimum.

You can easily add `print([n for n in min_heap])` after every heap modification in your Python implementation to see these values in practice.

Let me know if you want a code version with printouts at every step!

[1](https://www.geeksforgeeks.org/dsa/merge-k-sorted-linked-lists-set-2-using-min-heap/)
[2](https://www.finalroundai.com/articles/merge-k-sorted-arrays)
[3](https://heycoach.in/blog/heap-based-approach-for-merge-k-sorted-lists/)
[4](https://www.youtube.com/watch?v=ptYUCjfNhJY)
[5](https://www.designgurus.io/answers/detail/23-merge-k-sorted-lists-msh356)
[6](https://heycoach.in/blog/applications-of-merge-k-sorted-lists-in-merging-data-streams/)
[7](https://stackoverflow.com/questions/67358848/merging-k-sorted-lists-using-heapq-module-in-python3)
[8](https://algo.monster/liteproblems/23)
[9](https://en.wikipedia.org/wiki/Trie)