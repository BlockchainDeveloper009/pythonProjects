class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


def invertTree(root: TreeNode) -> TreeNode:
    if not root:
        return None

    root.left, root.right = root.right, root.left  # Swap children

    invertTree(root.left)
    invertTree(root.right)

    return root



"""

226. Invert Binary Tree
Easy
Topics
premium lock iconCompanies

Given the root of a binary tree, invert the tree, and return its root.



Example 1:

Input: root = [4,2,7,1,3,6,9]
Output: [4,7,2,9,6,3,1]

Example 2:

Input: root = [2,1,3]
Output: [2,3,1]

Example 3:

Input: root = []
Output: []



Constraints:

    The number of nodes in the tree is in the range [0, 100].
    -100 <= Node.val <= 100


"""

"""
The problem is to **invert a binary tree**, meaning swap every left subtree with its corresponding right subtree, recursively.

***

## Approach: Recursive Tree Traversal

- For each node:
  - Swap the left and right child nodes.
  - Recursively invert left and right subtrees.

***

## Python Code

```python
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

def invertTree(root: TreeNode) -> TreeNode:
    if not root:
        return None
    
    root.left, root.right = root.right, root.left  # Swap children
    
    invertTree(root.left)
    invertTree(root.right)
    
    return root
```

***

## Explanation

- Recursive calls invert each subtree.
- Swapping happens at each node.
- Base case is null node, which returns immediately.

***

## Example Usage

```python
root = TreeNode(4,
        TreeNode(2, TreeNode(1), TreeNode(3)),
        TreeNode(7, TreeNode(6), TreeNode(9))
)
inverted = invertTree(root)
# The inverted tree root structure is now:
# 4
# ├─7
# │  ├─9
# │  └─6
# └─2
#    ├─3
#    └─1
```

***

## Complexity

- Time: $$O(n)$$, visiting every node once.
- Space: $$O(h)$$ recursion stack where $$h$$ is tree height.

***

**Summary:**  
Inverting a binary tree is naturally done with recursive traversal, swapping left and right subtrees at each node in linear time.
"""