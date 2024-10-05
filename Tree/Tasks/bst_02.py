class Node:
    def __init__(self, value):
        self.val = value
        self.left = None
        self.right = None

nodes_sorted = []

def inorder(root):
    if root is not None:
        inorder(root.left)
        nodes_sorted.append(root.val)
        inorder(root.right)

node = Node(10)
node.left = Node(5)
node.right = Node(12)
node.left.left = Node(3)
node.left.left.right = Node(4)
node.left.right = Node(7)
node.left.right.right = Node(9)
node.right.right = Node(15)
node.right.left = Node(11)
node.right.right.left = Node(14)
node.right.right.right = Node(18)

k = int(input())
inorder(node)
print(sum(nodes_sorted[:k]))
