# Stack Tutorial

## 1. Introduction

In this tutorial, we will explore the concept of stacks in computer science. Stacks are a fundamental data structure that follows the Last In, First Out (LIFO) principle.

## 2. Definition

A stack is a linear data structure that follows the LIFO principle. This means that the last element added to the stack is the first one to be removed.

## 3. Array-based stack

An array-based stack uses an array to store elements. It has a fixed size and can lead to stack overflow if the size is exceeded.

## 4. Linked list-based stack

A linked list-based stack uses a linked list to store elements. It allows for dynamic resizing and does not have a fixed size.

## 5. Dynamic stack

A dynamic stack can resize itself to accommodate more elements as needed. It is typically implemented using a linked list.

## 6. Fixed-size stack

A fixed-size stack has a predetermined size and cannot resize itself. It is typically implemented using an array.

## 7. Bounded stack

A bounded stack has a maximum capacity and cannot exceed this capacity. It is similar to a fixed-size stack but may allow for resizing within the bounds.

## 8. Thread-safe stack

A thread-safe stack is designed to be used in a multithreaded environment, ensuring that operations on the stack are atomic and do not lead to race conditions.

## 9. Example

Here is a simple example of how you might implement a stack in Python using a list:

```python
class Stack:
    def __init__(self):
        self.items = []

    def push(self, item):
        self.items.append(item)

    def pop(self):
        return self.items.pop()

    def is_empty(self):
        return len(self.items) == 0

    def peek(self):
        return self.items[-1] if not self.is_empty() else None

# Usage
stack = Stack()
stack.push(1)
stack.push(2)
print(stack.pop())  # Output: 2
print(stack.peek()) # Output: 1
