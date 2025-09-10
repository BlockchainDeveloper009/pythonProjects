class Node:
    def __init__(self, val):
        self.val = val
        self.left = None
        self.right = None




def dfs_stack(root, start):
    stack = [ root ]
    while len(stack) > 0:
        curr = stack.pop()
        print(curr.val)

        if curr.right is not None:
            stack.append(curr.right)

        if curr.left is not None:
            stack.append(curr.left)


root = Node('A')
root.left = Node('B')
root.right = Node('C')
root.left.left = Node('D')

dfs_stack(root)
# Output: A B D C

"""


"""