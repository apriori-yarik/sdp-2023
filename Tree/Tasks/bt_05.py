class Node:
    def __init__(self, value):
        self.val = value
        self.left = None
        self.right = None

def getHeight(node):
    if node is None:
        return 0
 
    else:
        left_height = getHeight(node.left)
        right_height = getHeight(node.right)
 
        if (left_height > right_height):
            return left_height + 1
        else:
            return right_height + 1

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

print(getHeight(node))
