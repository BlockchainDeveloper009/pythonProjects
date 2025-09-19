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
