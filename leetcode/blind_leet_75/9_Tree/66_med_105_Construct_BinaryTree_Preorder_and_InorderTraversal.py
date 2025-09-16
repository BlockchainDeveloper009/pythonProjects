
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

def buildTree(preorder, inorder):
    if not preorder or not inorder:
        return None

    root_val = preorder[0]
    root = TreeNode(root_val)

    # Find root index in inorder
    root_index = inorder.index(root_val)

    # Build left subtree
    root.left = buildTree(preorder[1: 1 + root_index], inorder[:root_index])
    # Build right subtree
    root.right = buildTree(preorder[1 + root_index:], inorder[root_index + 1:])

    return root



preorder = [3,9,20,15,7]
inorder = [9,3,15,20,7]
root = buildTree(preorder, inorder)
# root now represents the tree matching the given traversals


"""
105. Construct Binary Tree from Preorder and Inorder Traversal
Medium
Topics
premium lock iconCompanies

Given two integer arrays preorder and inorder where preorder is the preorder traversal of a binary tree and inorder is the inorder traversal of the same tree, construct and return the binary tree.



Example 1:

Input: preorder = [3,9,20,15,7], inorder = [9,3,15,20,7]
Output: [3,9,20,null,null,15,7]

Example 2:

Input: preorder = [-1], inorder = [-1]
Output: [-1]



Constraints:

    1 <= preorder.length <= 3000
    inorder.length == preorder.length
    -3000 <= preorder[i], inorder[i] <= 3000
    preorder and inorder consist of unique values.
    Each value of inorder also appears in preorder.
    preorder is guaranteed to be the preorder traversal of the tree.
    inorder is guaranteed to be the inorder traversal of the tree.



"""

"""
To construct a binary tree from preorder and inorder traversals, the key insight is:

- The first element in **preorder** is the root.
- Using that root value, split the **inorder** list into left and right subtrees.
- Recursively build left and right subtrees with corresponding preorder and inorder slices.

***

## Approach

1. Root = first element in preorder.
2. Find root index in inorder to distinguish left/right subtrees.
3. Left subtree size = root index in inorder.
4. Recursively build left subtree from:
   - preorder[1 : 1 + left subtree size]
   - inorder[0 : root index]
5. Recursively build right subtree from:
   - preorder[1 + left subtree size :]
   - inorder[root index + 1 :]

***

## Python Code

```python
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

def buildTree(preorder, inorder):
    if not preorder or not inorder:
        return None

    root_val = preorder[0]
    root = TreeNode(root_val)

    # Find root index in inorder
    root_index = inorder.index(root_val)

    # Build left subtree
    root.left = buildTree(preorder[1: 1 + root_index], inorder[:root_index])
    # Build right subtree
    root.right = buildTree(preorder[1 + root_index:], inorder[root_index + 1:])

    return root
```

***

## Explanation

- Preorder tells the root first.
- Inorder tells nodes to the left and right.
- Recursively rebuild tree using slices.

***

## Example Usage

```python
preorder = [3,9,20,15,7]
inorder = [9,3,15,20,7]
root = buildTree(preorder, inorder)
# root now represents the tree matching the given traversals
```

***

## Complexity

- Time: $$O(n^2)$$ worst case due to `inorder.index` calls; can be optimized with hash map.
- Space: $$O(n)$$ recursion stack and tree nodes.

***

**Optimization:**  
Use a hashmap to store value-to-index mapping of inorder to reduce index lookup to $$O(1)$$, improving time to $$O(n)$$.

***

**Summary:**  
Reconstruct the tree by picking roots from preorder and splitting inorder accordingly, recursively building left and right subtrees to form the original tree.
"""