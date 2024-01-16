class Node:
    def __init__(self, data):
        self.data = data
        self.next = None

class StackLinkedList:
    def __init__(self):
        self.top = None

    def is_empty(self):
        return self.top is None

    def push(self, item):
        new_node = Node(item)
        new_node.next = self.top
        self.top = new_node

    def pop(self):
        if not self.is_empty():
            popped = self.top.data
            self.top = self.top.next
            return popped
        else:
            return "Stack is empty"

    def peek(self):
        if not self.is_empty():
            return self.top.data
        else:
            return "Stack is empty"

    def size(self):
        count = 0
        current = self.top
        while current:
            count += 1
            current = current.next
        return count

stack = Stack()
stack.push('a')
stack.push('b')
stack.push('c')
print(stack.size())
