class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

class Codec:
    def serialize(self, root):
        # Encodes a tree to a single string.
        vals = []

        def dfs(node):
            if node is None:
                vals.append('#')
                return
            vals.append(str(node.val))
            dfs(node.left)
            dfs(node.right)
        dfs(root)
        return ','.join(vals)

    def deserialize(self, data):
        # Decodes your encoded data to tree.
        vals = iter(data.split(','))

        def dfs():
            val = next(vals)
            if val == '#':
                return None
            node = TreeNode(int(val))
            node.left = dfs()
            node.right = dfs()
            return node

        return dfs()

root = TreeNode(1)
root.left = TreeNode(2)
root.right = TreeNode(3)
root.right.left = TreeNode(4)
root.right.right = TreeNode(5)

codec = Codec()
data = codec.serialize(root)
print(data)  # Output: "1,2,#,#,3,4,#,#,5,#,#"

new_root = codec.deserialize(data)
# new_root represents the original tree structure again

"""
297. Serialize and Deserialize Binary Tree
Hard
Topics
premium lock iconCompanies

Serialization is the process of converting a data structure or object into 
a sequence of bits so that 
it can be stored in a file 
or memory buffer, or transmitted 
across a network connection link to be 
reconstructed later in the same or another computer environment.

Design an algorithm to serialize and deserialize a binary tree. 
There is no restriction on how your 
serialization/deserialization algorithm should work. 
You just need to ensure that a binary tree can 
be serialized to a string and this string can be deserialized to the original tree structure.

Clarification: The input/output format is the same as how 
LeetCode serializes a binary tree. 
You do not necessarily need to follow this format, 
so please be creative and come up with 
different approaches yourself.



Example 1:

Input: root = [1,2,3,null,null,4,5]
Output: [1,2,3,null,null,4,5]

Example 2:

Input: root = []
Output: []



Constraints:

    The number of nodes in the tree is in the range [0, 104].
    -1000 <= Node.val <= 1000



"""

"""
The problem is to **serialize** (convert tree to string) and **deserialize** (rebuild tree from string) a binary tree.

***

## Approach: Preorder Traversal (DFS)

- Serialize: Use preorder traversal, append node values, using a placeholder (like `#` or `null`) for `None` nodes.
- Deserialize: Use the serialized list to rebuild the tree recursively.

This approach uniquely encodes the tree structure including nulls.

***

## Python Code

```python
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

class Codec:
    def serialize(self, root):
        #Encodes a tree to a single string.
        vals = []

        def dfs(node):
            if node is None:
                vals.append('#')
                return
            vals.append(str(node.val))
            dfs(node.left)
            dfs(node.right)

        dfs(root)
        return ','.join(vals)

    def deserialize(self, data):
        #Decodes your encoded data to tree.
        vals = iter(data.split(','))

        def dfs():
            val = next(vals)
            if val == '#':
                return None
            node = TreeNode(int(val))
            node.left = dfs()
            node.right = dfs()
            return node
        
        return dfs()
```

***

## Explanation

- **Serialize:**  
  Preorder traversal records node value or `#` for null. E.g., `[1,2,null,null,3,4,null,null,5,null,null]`
- **Deserialize:**  
  Use an iterator over the serialized values, reconstruct tree with preorder logic.

***

## Example Usage

```python
# Build tree manually [1,2,3,null,null,4,5]
root = TreeNode(1)
root.left = TreeNode(2)
root.right = TreeNode(3)
root.right.left = TreeNode(4)
root.right.right = TreeNode(5)

codec = Codec()
data = codec.serialize(root)
print(data)  # Output: "1,2,#,#,3,4,#,#,5,#,#"

new_root = codec.deserialize(data)
# new_root represents the original tree structure again
```

***

## Complexity

- Time: $$O(n)$$ to serialize and deserialize where $$n$$ is nodes.
- Space: $$O(n)$$ for recursion stack and output string.

***

**Summary:**  
Preorder DFS with null markers provides a clean way to serialize and deserialize any binary tree uniquely, preserving exact structure with linear time and space.
"""