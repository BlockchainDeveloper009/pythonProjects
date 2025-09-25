### 128. Longest Consecutive Sequence
```commandline

128. Longest Consecutive Sequence
Given an unsorted array of integers nums, return the length of the longest consecutive elements sequence.

You must write an algorithm that runs in O(n) time.

 

Example 1:

Input: nums = [100,4,200,1,3,2]
Output: 4
Explanation: The longest consecutive elements sequence is [1, 2, 3, 4]. Therefore its length is 4.

```

Med.
### 1. Two Sum | 

````commandline
Given an integer array nums, return all the triplets [nums[i], nums[j], nums[k]] such that i != j, i != k, and j != k, and nums[i] + nums[j] + nums[k] == 0.

Notice that the solution set must not contain duplicate triplets.

 

Example 1:

Input: nums = [-1,0,1,2,-1,-4]
Output: [[-1,-1,2],[-1,0,1]]
Explanation: 
nums[0] + nums[1] + nums[2] = (-1) + 0 + 1 = 0.
nums[1] + nums[2] + nums[4] = 0 + 1 + (-1) = 0.
nums[0] + nums[3] + nums[4] = (-1) + 2 + (-1) = 0.
The distinct triplets are [-1,0,1] and [-1,-1,2].
Notice that the order of the output and the order of the triplets does not matter.

````

Easy
### 3. Longest Substring Without Repeating Characters

```
| Input: nums = [100,4,200,1,3,2]
Output: 4
Explanation: The longest consecutive elements
sequence is [1, 2, 3, 4]. Therefore its length is 4.
```

### 4. Longest Palindrome Substring:
Med.
```
5. Longest Palindromic Substring
Example 1:

Input: s = "babad"
Output: "bab"
Explanation: "aba" is also a valid answer.

Example 2:

Input: s = "cbbd"
Output: "bb"

```


Med.
### 5. _133. Clone Graph
```commandline
Given a reference of a node in a connected undirected graph.

Return a deep copy (clone) of the graph.

Each node in the graph contains a value (int) and a list (List[Node]) of its neighbors.

class Node {
    public int val;
    public List<Node> neighbors;
}



Test case format:

For simplicity, each node's value is the same as the node's index (1-indexed). For example, the first node with val == 1, the second node with val == 2, and so on. The graph is represented in the test case using an adjacency list.

An adjacency list is a collection of unordered lists used to represent a finite graph. Each list describes the set of neighbors of a node in the graph.

The given node will always be the first node with val = 1. You must return the copy of the given node as a reference to the cloned graph.



Example 1:

Input: adjList = [[2,4],[1,3],[2,4],[1,3]]
Output: [[2,4],[1,3],[2,4],[1,3]]
Explanation: There are 4 nodes in the graph.
1st node (val = 1)'s neighbors are 2nd node (val = 2) and 4th node (val = 4).
2nd node (val = 2)'s neighbors are 1st node (val = 1) and 3rd node (val = 3).
3rd node (val = 3)'s neighbors are 2nd node (val = 2) and 4th node (val = 4).
4th node (val = 4)'s neighbors are 1st node (val = 1) and 3rd node (val = 3).

```

Med.
### 261. Graph Valid Tree
49.5%
```commandline

```
Med.
### 647. Palindromic Substrings
72.1%

```commandline

```

Med.
### 11. Container With Most Water
58.4%
```commandline
You are given an integer array height of length n. There are n vertical 
lines drawn such that the two endpoints of the ith line are (i, 0) and (i, height[i]).

Find two lines that together with the x-axis form a container, such that the container contains the most water.
```
Med.
### 139. Word Break
48.6%

Med.


### 40.__141. Linked List Cycle
53.2%
```commandline

Given head, the head of a linked list, determine if the linked list has a cycle in it.

There is a cycle in a linked list if there is some node in the list that can be reached again by continuously following the next pointer. Internally, pos is used to denote the index of the node that tail's next pointer is connected to. Note that pos is not passed as a parameter.

Return true if there is a cycle in the linked list. Otherwise, return false.



Example 1:

Input: head = [3,2,0,-4], pos = 1
Output: true
Explanation: There is a cycle in the linked list, where the tail connects to the 1st node (0-indexed).

```
Easy
268. Missing Number
70.8%

Easy
15. 3Sum
37.7%
```

Given an integer array nums, return all the triplets [nums[i], nums[j], nums[k]] such that i != j, i != k, and j != k, and nums[i] + nums[j] + nums[k] == 0.

Notice that the solution set must not contain duplicate triplets.



Example 1:

Input: nums = [-1,0,1,2,-1,-4]
Output: [[-1,-1,2],[-1,0,1]]
Explanation:
nums[0] + nums[1] + nums[2] = (-1) + 0 + 1 = 0.
nums[1] + nums[2] + nums[4] = 0 + 1 + (-1) = 0.
nums[0] + nums[3] + nums[4] = (-1) + 2 + (-1) = 0.
The distinct triplets are [-1,0,1] and [-1,-1,2].
Notice that the order of the output and the order of the triplets does not matter.

```
Med.
### 44.---143. Reorder List
63.4%
```commandline

You are given the head of a singly linked-list. The list can be represented as:

L0 → L1 → … → Ln - 1 → Ln

Reorder the list to be on the following form:

L0 → Ln → L1 → Ln - 1 → L2 → Ln - 2 → …

You may not modify the values in the list's nodes. Only nodes themselves may be changed.



Example 1:

Input: head = [1,2,3,4]
Output: [1,4,2,3]

```
Med.
269. Alien Dictionary
36.8%

Hard
271. Encode and Decode Strings
50.3%

Med.
19. Remove Nth Node From End of List
49.9%

```commandline
Given the head of a linked list, remove the nth node from the end of the list and return its head.



Example 1:

Input: head = [1,2,3,4,5], n = 2
Output: [1,2,3,5]

```

Med.
20. Valid Parentheses
42.9%

Easy
21. Merge Two Sorted Lists
67.3%
```commandline
You are given the heads of two sorted linked lists list1 and list2.

Merge the two lists into one sorted list. The list should be made by splicing together the nodes of the first two lists.

Return the head of the merged linked list.



Example 1:

Input: list1 = [1,2,4], list2 = [1,3,4]
Output: [1,1,2,3,4,4]

```
Easy
23. Merge k Sorted Lists
57.7%
```commandline
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

```
Hard
### 4. __ 152. Maximum Product Subarray
35.4%

Med.
```commandline
Given an integer array nums, return an array answer such that answer[i] is equal to the product of all the elements of nums except nums[i].

The product of any prefix or suffix of nums is guaranteed to fit in a 32-bit integer.

You must write an algorithm that runs in O(n) time and without using the division operation.

Example 1:
Input: nums = [1,2,3,4]
Output: [24,12,8,6]

Example 2:
Input: nums = [-1,1,0,-3,3]
Output: [0,0,9,0,0]
```
### 153. Find Minimum in Rotated Sorted Array
53.2%

Med.
### 33. Search in Rotated Sorted Array
43.4%

Med.
### 417. Pacific Atlantic Water Flow
58.1%

Med.
### 39. Combination Sum
75.4%

Med.
### 295. Find Median from Data Stream
53.7%

Hard
### 297. Serialize and Deserialize Binary Tree
59.6%

Hard
### 424. Longest Repeating Character Replacement
58.1%

### Med.
300. Longest Increasing Subsequence
58.4%

Med.
### 48. Rotate Image
78.6%

Med.
### 49. Group Anagrams
71.5%

Med.
### 435. Non-overlapping Intervals
56.1%

Med.
### 53. Maximum Subarray
52.5%

Med.
### 54. Spiral Matrix
55.0%

Med.
### 55. Jump Game
39.9%

Med.
### 56. Merge Intervals
50.0%

Med.
### 57. Insert Interval
44.0%

Med.

### 572. Subtree of Another Tree
50.6%

Easy
### 62. Unique Paths
66.1%

Med.
### 190. Reverse Bits
64.4%

Easy
### 191. Number of 1 Bits
75.3%

Easy
### 322. Coin Change
47.2%

Med.
### 323. Number of Connected Components in an Undirected Graph
64.4%

Med.
### 70. Climbing Stairs
53.7%

Easy
### 198. House Robber
52.6%

Med.
### 200. Number of Islands
63.0%

Med.
### 73. Set Matrix Zeroes
61.5%

Med.
### 76. Minimum Window Substring
46.1%

Hard
### 206. Reverse Linked List
79.7%

Easy
### 79. Word Search
46.0%

Med.
### 207. Course Schedule
50.0%

Med.
### 208. Implement Trie (Prefix Tree)
68.5%

Med.
### 338. Counting Bits
80.1%

Easy
### 211. Design Add and Search Words Data Structure
47.5%

Med.
### 212. Word Search II
37.6%

Hard
### 213. House Robber II
44.1%

Med.
### 217. Contains Duplicate
63.6%

Easy
### 91. Decode Ways
37.0%

Med.
### 347. Top K Frequent Elements
64.8%

Med.
### 253. Meeting Rooms II
52.3%

Med.
### 98. Validate Binary Search Tree
34.8%

Med.
### 226. Invert Binary Tree
79.4%

Easy
```
Given the root of a binary tree, invert the tree, and return its root.
Example 1:
Input: root = [4,2,7,1,3,6,9]
Output: [4,7,2,9,6,3,1]

```
### 100. Same Tree
65.8%

Easy
### 1143. Longest Common Subsequence
58.5%

Med.
```
- Given two strings text1 and text2, return the length of their longest 
common subsequence. 
- If there is no common subsequence, return 0.
- A subsequence of a string is a new string generated from the original string 
with some characters (can be none) deleted without changing the relative order 
of the remaining characters.

For example, "ace" is a subsequence of "abcde".

A common subsequence of two strings is a subsequence that is common to both strings.

Example 1:

Input: text1 = "abcde", text2 = "ace" 
Output: 3  
Explanation: The longest common subsequence is "ace" and its length is 3.

Example 2:

Input: text1 = "abc", text2 = "abc"
```

### 102. Binary Tree Level Order Traversal
71.3%

Med.
```commandline
Given two integer arrays preorder and inorder where preorder is the preorder traversal of a binary tree and inorder is the 
inorder traversal of the same tree, construct and return the binary tree.
```
### 230. Kth Smallest Element in a BST
75.9%

Med.
````
Given the root of a binary search tree, and an integer k, return the kth smallest value (1-indexed) of all the values of the nodes in the tree.



Example 1:

Input: root = [3,1,4,null,2], k = 1
Output: 1

Example 2:

Input: root = [5,3,6,2,4,null,null,1], k = 3
Output: 3

````
### 104. Maximum Depth of Binary Tree
77.5%

Easy


### 105. Construct Binary Tree from Preorder and Inorder Traversal
67.6%

Med.
### 235. Lowest Common Ancestor of a Binary Search Tree
69.2%

````
Given a binary search tree (BST), find the lowest common ancestor (LCA) node of two given nodes in the BST.

According to the definition of LCA on Wikipedia: “The lowest common ancestor is defined between two nodes p and q as the lowest node in T that has both 
p and q as descendants (where we allow a node to be a descendant of itself).”
````
Med.
### 238. Product of Array Except Self
68.1%

Med.
### 242. Valid Anagram
67.2%
```commandline
Given two strings s and t, return true if t is an

of s, and false otherwise.

Example 1:
Input: s = "anagram", t = "nagaram"
Output: true
Example 2:
Input: s = "rat", t = "car"
Output: false

```
Easy
### 371. Sum of Two Integers
54.3%

Med.
### 252. Meeting Rooms
59.1%

Easy
### 121. Best Time to Buy and Sell Stock
55.8%

Easy
### 124. Binary Tree Maximum Path Sum
41.6%

Hard
### 125. Valid Palindrome