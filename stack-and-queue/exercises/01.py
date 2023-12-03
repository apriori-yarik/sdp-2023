from collections import deque

word = input()
st = deque()

for i in word:
    st.append(i)

new_word = ""
while len(st) > 0:
    last = st[-1]
    new_word += last
    st.pop()

print(new_word == word)