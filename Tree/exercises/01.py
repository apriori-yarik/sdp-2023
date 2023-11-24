class Node:
    def __init__(self, value):
        self.val = value
        self.left = None
        self.right = None

leftRight = [0, 0]

# корен - ляво поддърво - дясно поддърво
def preorder(root):
    if root is not None:
        if root.left is not None:
            leftRight[0] += 1
        if root.right is not None:
            leftRight[1] += 1
        preorder(root.left)
        preorder(root.right)

node = Node(1)
node.left = Node(2)
node.right = Node(3)
node.left.left = Node(5)
node.right.left = Node(6)

preorder(node)
print(" ".join([str(x) for x in leftRight]))

