class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

def maxPathSum(root: TreeNode) -> int:
    max_sum = float('-inf')

    def dfs(node):
        nonlocal max_sum
        if not node:
            return 0

        left = max(dfs(node.left), 0)    # max path sum on left extending up
        right = max(dfs(node.right), 0)  # max path sum on right extending up

        # Path sum through the node (both children included)
        current_sum = node.val + left + right

        # Update global max
        max_sum = max(max_sum, current_sum)

        # Return max path sum extending upwards (one branch only)
        return node.val + max(left, right)

    dfs(root)
    return max_sum



root1 = TreeNode(1, TreeNode(2), TreeNode(3))
print(maxPathSum(root1))  # Output: 6

root2 = TreeNode(-10, TreeNode(9), TreeNode(20, TreeNode(15), TreeNode(7)))
print(maxPathSum(root2))  # Output: 42


"""
124. Binary Tree Maximum Path Sum
Hard
Topics
premium lock iconCompanies

A path in a binary tree is a sequence of nodes where each pair of adjacent nodes in the sequence has an edge connecting them. A node can only appear in the sequence at most once. Note that the path does not need to pass through the root.

The path sum of a path is the sum of the node's values in the path.

Given the root of a binary tree, return the maximum path sum of any non-empty path.



Example 1:

Input: root = [1,2,3]
Output: 6
Explanation: The optimal path is 2 -> 1 -> 3 with a path sum of 2 + 1 + 3 = 6.

Example 2:

Input: root = [-10,9,20,null,null,15,7]
Output: 42
Explanation: The optimal path is 15 -> 20 -> 7 with a path sum of 15 + 20 + 7 = 42.



Constraints:

    The number of nodes in the tree is in the range [1, 3 * 104].
    -1000 <= Node.val <= 1000



"""


"""
The problem is to find the **maximum path sum** in a binary tree where a path can start and end at any node, not necessarily passing through the root.

***

## Approach: Recursive DFS with Postorder Traversal

- For each node:
  - Recursively calculate the maximum path sum of the left and right subtree **that extends upward** (single path).
  - Ignore negative sums by taking max with zero.
  - Compute the maximum path sum passing through the current node as:
    left path sum + node value + right path sum.
  - Update a global max with this sum.
  - Return the max path sum **extending upwards** from current node, which is:
    node value + max(left path sum, right path sum).

***

## Python Code

```python
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

def maxPathSum(root: TreeNode) -> int:
    max_sum = float('-inf')

    def dfs(node):
        nonlocal max_sum
        if not node:
            return 0

        left = max(dfs(node.left), 0)    # max path sum on left extending up
        right = max(dfs(node.right), 0)  # max path sum on right extending up

        # Path sum through the node (both children included)
        current_sum = node.val + left + right

        # Update global max
        max_sum = max(max_sum, current_sum)

        # Return max path sum extending upwards (one branch only)
        return node.val + max(left, right)

    dfs(root)
    return max_sum
```

***

## Explanation

- Negative path sums are discarded because we can choose to not include that subtree.
- We keep track of the highest path sum seen so far via `max_sum`.
- Recursive calls compute max sums from bottom up.

***

## Example Usage

```python
root1 = TreeNode(1, TreeNode(2), TreeNode(3))
print(maxPathSum(root1))  # Output: 6

root2 = TreeNode(-10, TreeNode(9), TreeNode(20, TreeNode(15), TreeNode(7)))
print(maxPathSum(root2))  # Output: 42
```

***

## Complexity

- Time: $$O(n)$$, each node visited once.
- Space: $$O(h)$$, recursion stack.

***

**Summary:**  
Using DFS, compute max upward path sums while updating global max including paths crossing a node and both children, elegantly solving maximum path sum with linear time.
"""