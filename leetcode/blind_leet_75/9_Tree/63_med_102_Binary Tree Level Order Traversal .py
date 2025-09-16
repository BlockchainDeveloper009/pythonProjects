
from collections import deque

class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

def levelOrder(root: TreeNode):
    result = []
    if not root:
        return result

    queue = deque([root])
    while queue:
        level = []
        for _ in range(len(queue)):  # Only nodes on the current level
            node = queue.popleft()
            level.append(node.val)
            if node.left:
                queue.append(node.left)
            if node.right:
                queue.append(node.right)
        result.append(level)
    return result





# Example 1: [3,9,20,null,null,15,7]
root = TreeNode(3)
root.left = TreeNode(9)
root.right = TreeNode(20, TreeNode(15), TreeNode(7))
print(levelOrder(root))  # Output: [[3], [9, 20], [15, 7]]

# Example 2: [1]
print(levelOrder(TreeNode(1)))  # Output: [[1]]

# Example 3: []
print(levelOrder(None))  # Output: []




"""
102. Binary Tree Level Order Traversal
Medium
Topics
premium lock iconCompanies
Hint

Given the root of a binary tree, return the level order traversal of its nodes' values. (i.e., from left to right, level by level).



Example 1:

Input: root = [3,9,20,null,null,15,7]
Output: [[3],[9,20],[15,7]]

Example 2:

Input: root = [1]
Output: [[1]]

Example 3:

Input: root = []
Output: []



Constraints:

    The number of nodes in the tree is in the range [0, 2000].
    -1000 <= Node.val <= 1000



"""


"""
To perform a **level order traversal** (breadth-first search, BFS) on a binary tree and return each level as a sublist, use a queue to process nodes by level.

***

## Approach: BFS Using a Queue

- Use a queue to process nodes, enqueuing the children of each node.
- For each level, process all nodes currently in the queue (these represent the current level).
- Append their values to a list, and enqueue their left and right children.
- Repeat until the queue is empty.

***

## Python Code

```python
from collections import deque

class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

def levelOrder(root: TreeNode):
    result = []
    if not root:
        return result

    queue = deque([root])
    while queue:
        level = []
        for _ in range(len(queue)):  # Only nodes on the current level
            node = queue.popleft()
            level.append(node.val)
            if node.left:
                queue.append(node.left)
            if node.right:
                queue.append(node.right)
        result.append(level)
    return result
```

***

## Example Usage

```python
# Example 1: [3,9,20,null,null,15,7]
root = TreeNode(3)
root.left = TreeNode(9)
root.right = TreeNode(20, TreeNode(15), TreeNode(7))
print(levelOrder(root))  # Output: [[3], [9, 20], [15, 7]]

# Example 2: [1]
print(levelOrder(TreeNode(1)))  # Output: [[1]]

# Example 3: []
print(levelOrder(None))  # Output: []
```

***

## Explanation

- Each loop iteration processes all nodes at the current level and collects their children for the next level.
- Results in a list of lists, where each sublist is the values on one level.

***

## Complexity

- **Time:** $$O(n)$$, every node visited once.
- **Space:** $$O(n)$$, for the queue and return structure.

***

**Summary:**  
Breadth-first traversal by level using a queue yields each tree level as a sublist, cleanly and efficiently producing the required order.
"""