

class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

def isSameTree(s: TreeNode, t: TreeNode) -> bool:
    if not s and not t:
        return True
    if not s or not t:
        return False
    if s.val != t.val:
        return False
    return isSameTree(s.left, t.left) and isSameTree(s.right, t.right)

def isSubtree(root: TreeNode, subRoot: TreeNode) -> bool:
    if not root:
        return False
    if isSameTree(root, subRoot):
        return True
    return isSubtree(root.left, subRoot) or isSubtree(root.right, subRoot)


# Root tree [3,4,5,1,2]
root = TreeNode(3)
root.left = TreeNode(4, TreeNode(1), TreeNode(2))
root.right = TreeNode(5)

# SubRoot tree [4,1,2]
subRoot = TreeNode(4, TreeNode(1), TreeNode(2))

print(isSubtree(root, subRoot))  # True

# Another example with false
root.right.right = TreeNode(0)  # Add a node that breaks subtree match

print(isSubtree(root, subRoot))  # False

"""
572. Subtree of Another Tree
Easy
Topics
premium lock iconCompanies
Hint

Given the roots of two binary trees root and subRoot, return true if there is a subtree of root with the same structure and node values of subRoot and false otherwise.

A subtree of a binary tree tree is a tree that consists of a node in tree and all of this node's descendants. The tree tree could also be considered as a subtree of itself.



Example 1:

Input: root = [3,4,5,1,2], subRoot = [4,1,2]
Output: true

Example 2:

Input: root = [3,4,5,1,2,null,null,null,null,0], subRoot = [4,1,2]
Output: false



Constraints:

    The number of nodes in the root tree is in the range [1, 2000].
    The number of nodes in the subRoot tree is in the range [1, 1000].
    -104 <= root.val <= 104
    -104 <= subRoot.val <= 104


"""

"""
The problem is to determine if `subRoot` is a subtree of `root` — meaning whether there exists a node in `root` such that the subtree rooted at that node is identical to `subRoot`.

***

## Approach

1. Traverse through all nodes of `root`.
2. For each node, check if the subtree rooted at that node is identical to `subRoot`.
3. Recursively compare nodes and their children to validate identical structure and values.
4. If found identical subtree, return True.

***

## Python Code

```python
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

def isSameTree(s: TreeNode, t: TreeNode) -> bool:
    if not s and not t:
        return True
    if not s or not t:
        return False
    if s.val != t.val:
        return False
    return isSameTree(s.left, t.left) and isSameTree(s.right, t.right)

def isSubtree(root: TreeNode, subRoot: TreeNode) -> bool:
    if not root:
        return False
    if isSameTree(root, subRoot):
        return True
    return isSubtree(root.left, subRoot) or isSubtree(root.right, subRoot)
```

***

## Explanation

- `isSameTree` checks if two trees are identical in structure and values.
- `isSubtree` recursively checks every node in `root` to find a match for `subRoot`.
- If any subtree matches `subRoot`, returns True.

***

## Example Usage

```python
# Root tree [3,4,5,1,2]
root = TreeNode(3)
root.left = TreeNode(4, TreeNode(1), TreeNode(2))
root.right = TreeNode(5)

# SubRoot tree [4,1,2]
subRoot = TreeNode(4, TreeNode(1), TreeNode(2))

print(isSubtree(root, subRoot))  # True

# Another example with false
root.right.right = TreeNode(0)  # Add a node that breaks subtree match

print(isSubtree(root, subRoot))  # False
```

***

## Complexity

- Time: $$O(m \times n)$$ worst case, $$m, n$$ number of nodes in root and subRoot.
- Space: $$O(m + n)$$ recursion stack space.

***

**Summary:**  
By recursively comparing subtrees at each node with the candidate subtree, this approach verifies presence of an exact matching subtree efficiently for reasonable input sizes.
"""