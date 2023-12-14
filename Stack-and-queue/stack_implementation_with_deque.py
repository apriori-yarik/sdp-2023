

from collections import deque

class Stack:
    def __init__(self):
        self.stack = deque()
    def push(self, el):
        self.stack.append(el)
    def pop(self):
        return self.stack.pop()
    def peek(self):
        last = self.pop()
        self.push(last)
        return last
    def isEmpty(self):
        return self.stack == deque() # []

st = Stack()
st.push(4)
st.push(5)
st.push(3)

print(st.isEmpty()) # False
st.pop()
print(st.peek()) # 5
