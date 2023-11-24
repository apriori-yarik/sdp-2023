class Node:
    def __init__(self, value, left = None, right = None):
        self.left = left
        self.right = right
        self.val = value

# Inorder traversal
# left subtree - root - right subtree
def inorder(root):
    if root is not None:
        inorder(root.left)
        print(root.val, end=" ")
        inorder(root.right)

# Preorder traversal
# root - left subtree - right subtree
def preorder(root):
    if root is not None:
        print(root.val, end=" ")
        preorder(root.left)
        preorder(root.right)

# Postorder traversal
# left subtree - right subtree - root
def postorder(root):
    if root is not None:
        postorder(root.left)
        postorder(root.right)
        print(root.val, end=" ")

root = Node(1)
root.left = Node(2)
root.right = Node(3)
root.left.left = Node(4)
root.left.right = Node(5)

inorder(root)
print()
preorder(root)
print()
postorder(root)


    