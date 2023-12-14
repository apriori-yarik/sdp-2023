

from collections import deque

class Queue:
    def __init__(self):
        self.queue = deque()

    def enqueue(self, el):
        self.queue.append(el)

    def dequeue(self):
        return self.queue.popleft()

    def front(self):
        first = self.dequeue()
        self.queue.appendleft(first)
        return first

    def rear(self):
        last = self.queue.pop()
        self.queue.append(last)
        return last

    def isEmpty(self):
        return self.queue == deque()


queue = Queue()
print(queue.isEmpty()) # True

queue.enqueue(4)
queue.enqueue(5)
queue.enqueue(6)

queue.dequeue()
print(queue.front()) # 5

print(queue.isEmpty()) # False
