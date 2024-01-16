class CircularQueue:
    def __init__(self, max_size):
        self.queue = [None] * max_size
        self.front = self.rear = -1
        self.max_size = max_size

    def is_empty(self):
        return self.front == self.rear == -1

    def is_full(self):
        return (self.rear + 1) % self.max_size == self.front

    def enqueue(self, item):
        if self.is_empty():
            self.front = self.rear = 0
        elif not self.is_full():
            self.rear = (self.rear + 1) % self.max_size
        else:
            return "Circular Queue is full"
        self.queue[self.rear] = item

    def dequeue(self):
        if not self.is_empty():
            removed = self.queue[self.front]
            if self.front == self.rear:
                self.front = self.rear = -1
            else:
                self.front = (self.front + 1) % self.max_size
            return removed
        else:
            return "Circular Queue is empty"

    def front(self):
        if not self.is_empty():
            return self.queue[self.front]
        else:
            return "Circular Queue is empty"

    def size(self):
        if self.is_empty():
            return 0
        elif self.front <= self.rear:
            return self.rear - self.front + 1
        else:
            return self.max_size - self.front + self.rear + 1

circular = CircularQueue()
circular.enqueue('abc')
circular.enqueue('qwe')
circular.enqueue('rty')
circular.dequeue()
print(circular.size())
