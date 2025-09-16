
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

def kthSmallest(root: TreeNode, k: int) -> int:
    stack = []
    current = root
    count = 0

    # Iterative in-order traversal
    while current or stack:
        while current:
            stack.append(current)
            current = current.left
        current = stack.pop()
        count += 1
        if count == k:
            return current.val
        current = current.right



# Example 1: [3,1,4,null,2], k=1
root = TreeNode(3,
          TreeNode(1, right=TreeNode(2)),
          TreeNode(4))
print(kthSmallest(root, 1))  # Output: 1

# Example 2: [5,3,6,2,4,null,null,1], k=3
root2 = TreeNode(5,
           TreeNode(3, TreeNode(2, TreeNode(1)), TreeNode(4)),
           TreeNode(6))
print(kthSmallest(root2, 3))  # Output: 3


"""
230. Kth Smallest Element in a BST
Medium
Topics
premium lock iconCompanies
Hint

Given the root of a binary search tree, and an integer k, return the kth smallest value (1-indexed) of all the values of the nodes in the tree.



Example 1:

Input: root = [3,1,4,null,2], k = 1
Output: 1

Example 2:

Input: root = [5,3,6,2,4,null,null,1], k = 3
Output: 3



Constraints:

    The number of nodes in the tree is n.
    1 <= k <= n <= 104
    0 <= Node.val <= 104

"""

"""
To find the **kth smallest element in a binary search tree (BST)**, an in-order traversal (left-root-right) yields node values in ascending order.

***

## Approach: In-Order Traversal

- Traverse the tree in-order, counting visited nodes.
- Stop and return the value when the kth node is visited.

***

## Python Code

```python
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

def kthSmallest(root: TreeNode, k: int) -> int:
    stack = []
    current = root
    count = 0

    # Iterative in-order traversal
    while current or stack:
        while current:
            stack.append(current)
            current = current.left
        current = stack.pop()
        count += 1
        if count == k:
            return current.val
        current = current.right
```

***

## Explanation

- In-order traversal collects BST values in sorted order.
- Each pop from stack is the next smallest value.
- Count increments until kth node is found.

***

## Example Usage

```python
# Example 1: [3,1,4,null,2], k=1
root = TreeNode(3,
          TreeNode(1, right=TreeNode(2)),
          TreeNode(4))
print(kthSmallest(root, 1))  # Output: 1

# Example 2: [5,3,6,2,4,null,null,1], k=3
root2 = TreeNode(5,
           TreeNode(3, TreeNode(2, TreeNode(1)), TreeNode(4)),
           TreeNode(6))
print(kthSmallest(root2, 3))  # Output: 3
```

***

## Complexity

- Time: $$O(h + k)$$, $$h$$ is tree height, up to $$k$$ pops from stack.
- Space: $$O(h)$$, stack for traversal.

***

**Summary:**  
Efficiently search for the kth smallest by in-order traversal which processes nodes in sorted order, stopping after k nodes.
"""