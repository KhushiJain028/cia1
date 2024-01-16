class Node:
    def __init__(self, data):
        self.data = data
        self.next = None

class QueueLinkedList:
    def __init__(self):
        self.front = self.rear = None

    def is_empty(self):
        return self.front is None

    def enqueue(self, item):
        new_node = Node(item)
        if self.is_empty():
            self.front = self.rear = new_node
        else:
            self.rear.next = new_node
            self.rear = new_node

    def dequeue(self):
        if not self.is_empty():
            popped = self.front.data
            self.front = self.front.next
            if self.front is None:
                self.rear = None
            return popped
        else:
            return "Queue is empty"

    def front(self):
        if not self.is_empty():
            return self.front.data
        else:
            return "Queue is empty"

    def size(self):
        count = 0
        current = self.front
        while current:
            count += 1
            current = current.next
        return count

queue = QueueLinkedList()
queue.enqueue('a')
queue.enqueue('b')
queue.enqueue('c')
queue.dequeue()
print(queue.size())
