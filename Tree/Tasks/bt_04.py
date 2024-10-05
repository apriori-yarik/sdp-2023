from collections import deque

class Node:
    def __init__(self, value):
        self.val = value
        self.left = None
        self.right = None

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

d = dict()

q = deque()
q.append((node, 0))

while len(q) != 0:
    current = q[0]

    if current[0].left is not None:
        q.append((current[0].left, current[1] + 1))
    if current[0].right is not None:
        q.append((current[0].right, current[1] + 1))

    if current[1] not in d:
        d[current[1]] = []
    d[current[1]].append(current[0].val)
    q.popleft()

print(d)
