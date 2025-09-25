
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

def lowestCommonAncestor(root: TreeNode,
                         leftNode: TreeNode, rightNode: TreeNode) -> TreeNode:
    current = root
    while current:
        if leftNode.val < current.val and rightNode.val < current.val:
            current = current.left
        elif leftNode.val > current.val and rightNode.val > current.val:
            current = current.right
        else:
            return current
innermost = TreeNode(4, TreeNode(3), TreeNode(5))
root = TreeNode(6,
                #left
                TreeNode(2,
                         TreeNode(0),
                         innermost
     )
                           ),
           TreeNode(8, TreeNode(7), TreeNode(9)))
p = root.left           # Node 2
q = root.right          # Node 8
print(lowestCommonAncestor(root, p, q).val)  # Output: 6

p2 = root.left          # Node 2
q2 = root.left.right    # Node 4
print(lowestCommonAncestor(root, p2, q2).val) # Output: 2

"""
[235. Lowest Common Ancestor of a Binary Search Tree](https://leetcode.com/problems/lowest-common-ancestor-of-a-binary-search-tree/)
Medium
Topics
Companies
Given a binary search tree (BST), find the lowest common ancestor (LCA) node of two given nodes in the BST.
According to the [definition of LCA on Wikipedia](https://en.wikipedia.org/wiki/Lowest_common_ancestor): “The lowest common ancestor is defined between two nodes p and q as the lowest node in T that has both p and q as descendants (where we allow a node to be a descendant of itself).”
 
Example 1:
Input: root = [6,2,8,0,4,7,9,null,null,3,5], p = 2, q = 8
Output: 6
Explanation: The LCA of nodes 2 and 8 is 6.

Example 2:
Input: root = [6,2,8,0,4,7,9,null,null,3,5], p = 2, q = 4
Output: 2
Explanation: The LCA of nodes 2 and 4 is 2, since a node can be a descendant of itself according to the LCA definition.

Example 3:
Input: root = [2,1], p = 2, q = 1
Output: 2

 
Constraints:
The number of nodes in the tree is in the range [2, 105].
-109 <= Node.val <= 109
All Node.val are unique.
p != q
p and q will exist in the BST.
"""



"""
To find the **lowest common ancestor (LCA)** of two nodes in a BST, leverage the BST property: for any node, all left child values are less, all right child values are greater.

***

## Approach: BST Value Comparison

- Start from the root.
- If both `p` and `q` have values less than root, LCA is in the left subtree.
- If both have values greater than root, LCA is in the right subtree.
- Else, root is the split point and the LCA.

***

## Python Code

```python
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

def lowestCommonAncestor(root: TreeNode, p: TreeNode, q: TreeNode) -> TreeNode:
    current = root
    while current:
        if p.val < current.val and q.val < current.val:
            current = current.left
        elif p.val > current.val and q.val > current.val:
            current = current.right
        else:
            return current
```

***

## Explanation

- Traverse tree from root.
- If both targets less than current value, branch left.
- If both greater, branch right.
- Otherwise, current node is LCA (first split).

***

## Example Usage

```python
root = TreeNode(6,
           TreeNode(2, TreeNode(0), TreeNode(4, TreeNode(3), TreeNode(5))),
           TreeNode(8, TreeNode(7), TreeNode(9)))
p = root.left           # Node 2
q = root.right          # Node 8
print(lowestCommonAncestor(root, p, q).val)  # Output: 6

p2 = root.left          # Node 2
q2 = root.left.right    # Node 4
print(lowestCommonAncestor(root, p2, q2).val) # Output: 2
```

***

## Complexity

- Time: $$O(h)$$, $$h$$ is tree height (O(log n) for balanced BST).
- Space: $$O(1)$$, only a pointer.

***

**Summary:**  
By following BST splitting logic, LCA is the first node where paths to `p` and `q` diverge or either node matches root, giving a clean, fast solution.
"""