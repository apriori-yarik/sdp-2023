class Node:
    def __init__(self, value):
        self.val = value
        self.left = None
        self.right = None

summ = [0]
def preorder(root):
    if root is not None:
        if root.left is None and root.right is None:
            summ[0] += root.val
        preorder(root.left)
        preorder(root.right)

root = Node(3)
root.left = Node(5)
root.right = Node(10)
root.left.left = Node(7)
root.left.right = Node(9)
root.left.left.left = Node(8)

preorder(root)
print(summ[0])