from collections import deque

class Queue:
    def __init__(self):
        self.items = deque()

    def is_empty(self):

        return len(self.items) == 0

    def enqueue(self, item):

        self.items.append(item)

    def dequeue(self):

        if self.is_empty():
            raise IndexError("удаление из очереди из пустой очереди")
        return self.items.popleft()

    def peek(self):

        if self.is_empty():
            raise IndexError(" пустая очередь")
        return self.items[0]

    def size(self):

        return len(self.items)


queue = Queue()
queue.enqueue(1)
queue.enqueue(2)
queue.enqueue(3)

print(queue.peek())
print(queue.dequeue())
print(queue.size())
print(queue.is_empty())