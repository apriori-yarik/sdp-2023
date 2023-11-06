

class Stack:
    def __init__(self):
        self.stack = []
    def push(self, el):
        self.stack.append(el)
    def peek(self):
        return self.stack[len(self.stack) - 1]
    def pop(self):
        last = self.peek()
        self.stack.pop()
        return last
    def isEmpty(self):
        return self.stack == []

st = Stack()
st.push(4)
st.push(5)
st.push(3)

print(st.isEmpty()) # False
st.pop()
print(st.peek()) # 5












