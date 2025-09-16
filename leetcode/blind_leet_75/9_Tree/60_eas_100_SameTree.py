
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

def isSameTree(p: TreeNode, q: TreeNode) -> bool:
    if not p and not q:
        return True
    if not p or not q:
        return False
    if p.val != q.val:
        return False

    return isSameTree(p.left, q.left) and isSameTree(p.right, q.right)



# Tree 1: [1,2,3]
p = TreeNode(1, TreeNode(2), TreeNode(3))
# Tree 2: [1,2,3]
q = TreeNode(1, TreeNode(2), TreeNode(3))
print(isSameTree(p, q))  # True

# Tree 3: [1,2]
r = TreeNode(1, TreeNode(2))
# Tree 4: [1,null,2]
s = TreeNode(1, None, TreeNode(2))
print(isSameTree(r, s))  # False


"""
100. Same Tree
Easy
Topics
premium lock iconCompanies

Given the roots of two binary trees p and q, write a function to check if they are the same or not.

Two binary trees are considered the same if they are structurally identical, and the nodes have the same value.



Example 1:

Input: p = [1,2,3], q = [1,2,3]
Output: true

Example 2:

Input: p = [1,2], q = [1,null,2]
Output: false

Example 3:

Input: p = [1,2,1], q = [1,1,2]
Output: false



Constraints:

    The number of nodes in both trees is in the range [0, 100].
    -104 <= Node.val <= 104


"""


""""
To determine if two binary trees `p` and `q` are the same, we check if they are structurally identical and all corresponding nodes have the same values.

***

## Approach: Recursive Comparison

- If both nodes are `None`, they are identical at that position.
- If one node is `None` and the other isn’t, trees differ.
- If values differ, trees differ.
- Recursively check the left and right subtrees for equality.

***

## Python Code

```python
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

def isSameTree(p: TreeNode, q: TreeNode) -> bool:
    if not p and not q:
        return True
    if not p or not q:
        return False
    if p.val != q.val:
        return False

    return isSameTree(p.left, q.left) and isSameTree(p.right, q.right)
```

***

## Explanation

- Base cases handle null vs non-null nodes.
- Recursive calls confirm the entire structure and values match.

***

## Example Usage

```python
# Tree 1: [1,2,3]
p = TreeNode(1, TreeNode(2), TreeNode(3))
# Tree 2: [1,2,3]
q = TreeNode(1, TreeNode(2), TreeNode(3))
print(isSameTree(p, q))  # True

# Tree 3: [1,2]
r = TreeNode(1, TreeNode(2))
# Tree 4: [1,null,2]
s = TreeNode(1, None, TreeNode(2))
print(isSameTree(r, s))  # False
```

***

## Complexity

- Time: $$O(n)$$, where $$n$$ is number of nodes in the smaller tree.
- Space: $$O(h)$$, recursion stack depth (tree height).

***

**Summary:**  
Recursive checking of structure and node values provides a simple solution to confirm if two binary trees are identical.Would you like a runnable Rust implementation of any of these solutions for your coding practice?
"""