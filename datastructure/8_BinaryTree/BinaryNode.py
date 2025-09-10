# The Node Class defines the structure of a Node
class BinaryNode:
    # Initialize the attributes of Node
    def __init__(self, data):
        self.left = None # Left Child
        self.right = None # Right Child
        self.data = data # Node Data
    def addNode(self, newData):
        if newData < self.data:
            if self.left is None:

                self.left = BinaryNode(newData)

            else:
                # do the left / right check recursively
                self.addNode(newData)
        else:
            if self.right is None:
                # assign the new node
                self.right = BinaryNode(newData)
            else:
                # do the left / right check recursively
                self.addNode(newData)


    def inorder(node):
        if node:
            # Recursively call inorder on the left subtree until it reaches a leaf node
            BinaryNode.inorder(node.left)

            # Once we reach a leaf, we print the data
            print(node.data)

            # Now, since the left subtree and the root has been printed, call inorder on right subtree recursively until we reach a leaf node.
            BinaryNode.inorder(node.right)


root = BinaryNode(10) # Instantiating the Tree
# Tree Structure
#        10
#      /    \
#     None   None

root.left = BinaryNode(34) # Setting the left child of the root to 34
root.right = BinaryNode(89) # Setting the right child of the root to 89

# Tree Structure
#          10
#        /    \
#       34      89
#     /    \  /    \
#  None  None None None

if __name__ == "__main__":
    parentNode = BinaryNode(5)
    parentNode.addNode(2)
    parentNode.addNode(6)

    print(parentNode)

    parentNode.addNode(1)
    parentNode.addNode(3)

