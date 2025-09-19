Here is an interview-approved Python implementation of **Breadth First Search (BFS)** for a binary search tree (BST), also known as **level-order traversal**.[2][3][4]

***

## Python BFS for Binary Search Tree

```python
from collections import deque

class TreeNode:
    def __init__(self, val):
        self.val = val
        self.left = None
        self.right = None

def bfs_tree(root):
    if not root:
        return []

    queue = deque([root])      # Start with the root node in the queue
    order = []                 # This will store the level-order traversal

    while queue:
        node = queue.popleft() # Remove the node at the front of the queue
        order.append(node.val) # Visit the node and record its value

        # Enqueue left and right children, if they exist
        if node.left:
            queue.append(node.left)
        if node.right:
            queue.append(node.right)
    return order

# Example usage:
#      5
#     / \
#    3   8
#   / \   \
#  2   4   9

root = TreeNode(5)
root.left = TreeNode(3)
root.right = TreeNode(8)
root.left.left = TreeNode(2)
root.left.right = TreeNode(4)
root.right.right = TreeNode(9)

print("BFS level-order:", bfs_tree(root))  # Output: [5, 3, 8, 2, 4, 9]
```

***

### Step-by-step Explanation

- **TreeNode class** defines the nodes of the binary tree, each with a value, and left/right children.[3][2]
- Begin with the root node in the queue.
- While the queue is not empty, repeat:
  - Remove and visit the front node (record its value).
  - Enqueue the left and right children of the node if they exist.
- Continue level by level, so each node at a given depth is visited before moving on to deeper nodes.
- Returns a list of node values in level-order (BFS) traversal.

***

This code is standard for interviews, handles all edge cases (empty tree, missing children), and highlights the reasoning behind BFS traversal in trees.[4][2][3]

[1](https://csanim.com/tutorials/breadth-first-search-python-visualization-and-code)
[2](https://dev.to/theramoliya/python-implement-breadth-first-search-bfs-for-graph-and-tree-traversal-566b)
[3](https://llego.dev/posts/breadth-first-search-traverse-binary-tree-python/)
[4](https://www.101computing.net/breadth-first-traversal-of-a-binary-tree/)
[5](https://www.youtube.com/watch?v=lyVRSBFVQQM)
[6](https://www.geeksforgeeks.org/dsa/level-order-tree-traversal/)
[7](https://stackoverflow.com/questions/36827377/implementing-dfs-and-bfs-for-binary-tree)
[8](https://www.geeksforgeeks.org/dsa/breadth-first-search-or-bfs-for-a-graph/)