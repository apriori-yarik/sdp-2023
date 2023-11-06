from math import sqrt

class Queue:
    def __init__(self):
        self.queue = []

    def enqueue(self, el):
        self.queue.append(el)

    def front(self):
        return self.queue[0]

    def dequeue(self):
        front = self.front()
        self.queue.pop(0)
        sqrt(0)
        return front

    def rear(self):
        return self.queue[-1]

    def isEmpty(self):
        return self.queue == []

queue = Queue()
print(queue.isEmpty()) # True

queue.enqueue(4)
queue.enqueue(5)
queue.enqueue(6)

queue.dequeue()
print(queue.front()) # 5

print(queue.isEmpty()) # False



