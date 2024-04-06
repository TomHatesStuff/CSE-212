class Node:
    def __init__(self, data=None):
        self.data = data
        self.next = None

class Queue:
    def __init__(self):
        self.front = None
        self.rear = None

    def is_empty(self):
        return self.front is None

    def enqueue(self, data):
        new_node = Node(data)
        if self.is_empty():
            self.front = new_node
            self.rear = new_node
        else:
            self.rear.next = new_node
            self.rear = new_node

    def dequeue(self):
        if self.is_empty():
            raise IndexError("Queue is empty")
        data = self.front.data
        self.front = self.front.next
        if self.front is None:
            self.rear = None
        return data

    def peek(self):
        if self.is_empty():
            raise IndexError("Queue is empty")
        return self.front.data

    def __str__(self):
        if self.is_empty():
            return "Queue is empty"
        current = self.front
        result = ""
        while current:
            result += str(current.data) + " <- "
            current = current.next
        return result[:-4]  # Remove the last arrow

# Usage
queue = Queue()
queue.enqueue(1)
queue.enqueue(2)
queue.enqueue(3)
print("Queue:", queue)  # Output: Queue: 1 <- 2 <- 3
print("Dequeue:", queue.dequeue())  # Output: Dequeue: 1
print("Queue after dequeue:", queue)  # Output: Queue after dequeue: 2 <- 3
print("Peek:", queue.peek())  # Output: Peek: 2
