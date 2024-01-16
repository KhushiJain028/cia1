import heapq

class PriorityQueue:
    def __init__(self):
        self.heap = []

    def is_empty(self):
        return len(self.heap) == 0

    def enqueue(self, item, priority):
        heapq.heappush(self.heap, (priority, item))

    def dequeue(self):
        if not self.is_empty():
            return heapq.heappop(self.heap)[1]
        else:
            return "Priority Queue is empty"

priority = PriorityQueue()
priority.enqueue('abc')
priority.enqueue('def')
priority.enqueue('ghi')
priority.dequeue()
