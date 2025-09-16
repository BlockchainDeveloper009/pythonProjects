

class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

def maxDepth(root: TreeNode) -> int:
    if not root:
        return 0
    left_depth = maxDepth(root.left)
    right_depth = maxDepth(root.right)
    return 1 + max(left_depth, right_depth)


root = TreeNode(3)
root.left = TreeNode(9)
root.right = TreeNode(20, TreeNode(15), TreeNode(7))

print(maxDepth(root))  # Output: 3


"""

104. Maximum Depth of Binary Tree
Easy
Topics
premium lock iconCompanies

Given the root of a binary tree, return its maximum depth.

A binary tree's maximum depth is the number of nodes along the longest path from the root node down to the farthest leaf node.



Example 1:

Input: root = [3,9,20,null,null,15,7]
Output: 3

Example 2:

Input: root = [1,null,2]
Output: 2



Constraints:

    The number of nodes in the tree is in the range [0, 104].
    -100 <= Node.val <= 100


"""

"""
The problem is to find the **maximum depth** of a binary tree, which is the length of the longest path from root to a leaf node.

***

## Approach: Recursive Depth-First Search (DFS)

- If the node is null, depth is 0.
- Recursively compute max depth of left and right subtrees.
- Max depth at current node = 1 + max(left_depth, right_depth).

***

## Python Code

```python
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

def maxDepth(root: TreeNode) -> int:
    if not root:
        return 0
    left_depth = maxDepth(root.left)
    right_depth = maxDepth(root.right)
    return 1 + max(left_depth, right_depth)
```

***

## Explanation

- Base case returns 0 for null nodes.
- Recursively explore left and right subtrees.
- Depth is one more than the maximum depth of its children.

***

## Example Usage

```python
root = TreeNode(3)
root.left = TreeNode(9)
root.right = TreeNode(20, TreeNode(15), TreeNode(7))

print(maxDepth(root))  # Output: 3
```

***

## Complexity

- Time: $$O(n)$$, where $$n$$ is the number of nodes, each visited once.
- Space: $$O(h)$$, recursion stack depth, where $$h$$ is tree height.

***

**Summary:**  
Simple recursive DFS explores subtrees and calculates maximum depth by aggregating height from leaves to root in linear time.
"""