from collections import deque
class Node:
    """A single node in a binary tree."""

    def __init__(self, data):
        self.data = data
        self.left = None
        self.right = None


def level_order_traversal(root: Node) -> list[list[int]]:
    res = []
    queue = deque([root])
    while len(queue)>0:
        n = len(queue)
        new_level = []
        for _ in range(n):
            node = queue.popleft()
            new_level.append(node.val)
            for child in [node.left, node.right]:
                if child is not None:
                    queue.append(child)
        res.append(new_level)
    return res

def build_tree(nodes, f):
    return ""

def inorder_traversal(node):
    """
    In-order Traversal: Left -> Root -> Right.

    This traversal visits the left subtree, then the root node, and finally the right subtree.
    The output is a sorted list of node values for a Binary Search Tree (BST).
    """
    if node:
        inorder_traversal(node.left)
        print(node.data, end=" ")
        inorder_traversal(node.right)


def preorder_traversal(node):
    """
    Pre-order Traversal: Root -> Left -> Right.

    This traversal visits the root node first, then the left subtree, and finally the right subtree.
    It is useful for creating a copy of a tree.
    """
    if node:
        print(node.data, end=" ")
        preorder_traversal(node.left)
        preorder_traversal(node.right)


def postorder_traversal(node):
    """
    Post-order Traversal: Left -> Right -> Root.

    This traversal visits the left subtree and the right subtree before visiting the root node.
    It is useful for deleting a tree from the bottom up.
    """
    if node:
        postorder_traversal(node.left)
        postorder_traversal(node.right)
        print(node.data, end=" ")


# --- Example Usage ---

# Create a sample binary tree
# The tree structure:
#      1
#     / \
#    2   3
#   / \
#  4   5
root = Node(1)
root.left = Node(2)
root.right = Node(3)
root.left.left = Node(4)
root.left.right = Node(5)

print("In-order Traversal:", end=" ")
inorder_traversal(root)  # Expected output: 4 2 5 1 3
print()

print("Pre-order Traversal:", end=" ")
preorder_traversal(root)  # Expected output: 1 2 4 5 3
print()

print("Post-order Traversal:", end=" ")
postorder_traversal(root)  # Expected output: 4 5 2 3 1
print()