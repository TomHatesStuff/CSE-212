# Linked List Tutorial

## 1. Introduction

In this tutorial, we will explore different types of linked lists, a fundamental data structure in computer science.

## 2. Definition

A linked list is a linear data structure where elements are not stored at contiguous memory locations. Instead, each element (node) points to the next element in the list.

## 3. Singly Linked List

A singly linked list is a type of linked list where each node only has a reference to the next node in the sequence.

## 4. Doubly Linked List

A doubly linked list is a type of linked list where each node has references to both the next and previous nodes in the sequence.
```python
class Node:
    def __init__(self, data=None):
        self.data = data
        self.prev = None
        self.next = None

# Create nodes
node1 = Node(1)
node2 = Node(2)
node3 = Node(3)

# Link nodes
node1.next = node2
node2.prev = node1
node2.next = node3
node3.prev = node2

# Traversal
current_node = node1
while current_node:
    print(current_node.data, end=" <-> ")
    current_node = current_node.next
print("None")
```
## 5. Circular Linked List

A circular linked list is a type of linked list where the last node points back to the first node, forming a circle.
```python
class Node:
    def __init__(self, data=None):
        self.data = data
        self.next = None

# Create nodes
node1 = Node(1)
node2 = Node(2)
node3 = Node(3)

# Link nodes
node1.next = node2
node2.next = node3
node3.next = node1  # Circular reference

# Traversal
current_node = node1
while current_node:
    print(current_node.data, end=" -> ")
    current_node = current_node.next
    if current_node == node1:
        break
print("...")
```
## 6. Sorted Linked List

A sorted linked list is a type of linked list where nodes are inserted in a sorted order based on their values.

## 7. Sparse Linked List

A sparse linked list is a type of linked list optimized for representing sparse data structures, where most elements are empty.

## 8. Memory-Efficient Linked List

A memory-efficient linked list is a type of linked list that reduces memory overhead by using special techniques, such as node reordering or compression.

## 9. Circular Doubly Linked List

A circular doubly linked list is a combination of a circular linked list and a doubly linked list, where each node has references to both the next and previous nodes, and the last node points back to the first node.

## 10. Example

Here is a simple example of how you might implement a singly linked list in Python:

```python
class Node:
    def __init__(self, data=None):
        self.data = data
        self.next = None

class SinglyLinkedList:
    def __init__(self):
        self.head = None

    def append(self, data):
        new_node = Node(data)
        if not self.head:
            self.head = new_node
            return
        last_node = self.head
        while last_node.next:
            last_node = last_node.next
        last_node.next = new_node

    def print_list(self):
        current_node = self.head
        while current_node:
            print(current_node.data, end=" -> ")
            current_node = current_node.next
        print("None")

# Usage
linked_list = SinglyLinkedList()
linked_list.append(1)
linked_list.append(2)
linked_list.append(3)
linked_list.print_list()  # Output: 1 -> 2 -> 3 -> None
```
## 11. Problem to Solve

Write a program that uses a linked list to implement a queue data structure. The queue should support the following operations: enqueue, dequeue, and peek.

### Solution

You can check the solution [here](solution-2.py).

[Return to Main Page](0-Welcome.md)
