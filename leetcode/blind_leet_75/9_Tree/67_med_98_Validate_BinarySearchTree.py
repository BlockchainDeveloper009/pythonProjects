

class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

def isValidBST(root: TreeNode) -> bool:
    def helper(node, minVal, maxVal):
        if not node:
            return True
        # Node value must be strictly between minVal and maxVal
        if not (minVal < node.val < maxVal):
            return False
        return (helper(node.left, minVal, node.val) and
                helper(node.right, node.val, maxVal))
    return helper(root, float('-inf'), float('inf'))


root1 = TreeNode(2, TreeNode(1), TreeNode(3))
print(isValidBST(root1))  # True

root2 = TreeNode(5,
            TreeNode(1),
            TreeNode(4, TreeNode(3), TreeNode(6)))
print(isValidBST(root2))  # False


"""
98. Validate Binary Search Tree
Medium
Topics
premium lock iconCompanies

Given the root of a binary tree, determine if it is a valid binary search tree (BST).

A valid BST is defined as follows:

    The left

    of a node contains only nodes with keys strictly less than the node's key.
    The right subtree of a node contains only nodes with keys strictly greater than the node's key.
    Both the left and right subtrees must also be binary search trees.



Example 1:

Input: root = [2,1,3]
Output: true

Example 2:

Input: root = [5,1,4,null,null,3,6]
Output: false
Explanation: The root node's value is 5 but its right child's value is 4.



Constraints:

    The number of nodes in the tree is in the range [1, 104].
    -231 <= Node.val <= 231 - 1

"""
"""
To check if a binary tree is a **valid binary search tree (BST)**, ensure every node value is strictly greater than all values in the left subtree and strictly less than all values in the right subtree.

***

## Approach: Recursion with Min/Max Bounds

- Use DFS to traverse the tree.
- Pass down allowed value bounds:
  - Left children must be less than the parent value.
  - Right children must be greater than the parent value.
- For every node, check:
  - If its value is within the allowed ($$(\text{min}, \text{max})$$).
  - Recursively validate left and right subtrees with updated bounds.

***

## Python Code

```python
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

def isValidBST(root: TreeNode) -> bool:
    def helper(node, minVal, maxVal):
        if not node:
            return True
        # Node value must be strictly between minVal and maxVal
        if not (minVal < node.val < maxVal):
            return False
        return (helper(node.left, minVal, node.val) and
                helper(node.right, node.val, maxVal))
    return helper(root, float('-inf'), float('inf'))
```

***

## Explanation

- Initialize bounds to $$(-\infty, +\infty)$$.
- For left subtree, update upper bound to parent value.
- For right subtree, update lower bound to parent value.
- If any node violates the constraints, return False.

***

## Example Usage

```python
root1 = TreeNode(2, TreeNode(1), TreeNode(3))
print(isValidBST(root1))  # True

root2 = TreeNode(5,
            TreeNode(1),
            TreeNode(4, TreeNode(3), TreeNode(6)))
print(isValidBST(root2))  # False
```

***

## Complexity

- Time: $$O(n)$$ (visit every node once)
- Space: $$O(h)$$ for recursion stack ($$h$$ is tree height)

***

**Summary:**  
Enforcing strict value bounds during DFS guarantees each node satisfies BST properties throughout the tree.
"""