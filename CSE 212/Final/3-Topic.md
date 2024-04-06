# Trees Tutorial

## 1. Introduction

In this tutorial, we will explore different types of trees, which are hierarchical data structures widely used in computer science.

## 2. Definition

A tree is a collection of nodes connected by edges. Each node has a parent node (except for the root) and zero or more child nodes. Trees, especially binary trees, can be thought of as a specialized form of linked list where each node has references to multiple nodes

## 3. Binary Tree

A binary tree is a tree in which each node has at most two children, referred to as the left child and the right child.


![Binary tree example](Final/allimages/new-binary-tree.png)


 ```python
class TreeNode:
    def __init__(self, key):
        self.key = key
        self.left = None
        self.right = None

# Usage
root = TreeNode(1)
root.left = TreeNode(2)
root.right = TreeNode(3)
```
## 4. Binary Search Tree (BST)

A binary search tree is a binary tree in which the left child of a node contains only nodes with keys less than the node's key, and the right child contains only nodes with keys greater than the node's key.

```python
class TreeNode:
    def __init__(self, key):
        self.key = key
        self.left = None
        self.right = None

class BinarySearchTree:
    def __init__(self):
        self.root = None

    def insert(self, key):
        self.root = self._insert(self.root, key)

    def _insert(self, node, key):
        if node is None:
            return TreeNode(key)
        if key < node.key:
            node.left = self._insert(node.left, key)
        elif key > node.key:
            node.right = self._insert(node.right, key)
        return node

# Usage
bst = BinarySearchTree()
bst.insert(2)
bst.insert(1)
bst.insert(3)

```
## 5. AVL Tree

An AVL tree is a self-balancing binary search tree where the heights of the two child subtrees of any node differ by at most one.

(usually need more complex examples)

## 6. Red-Black Tree

A red-black tree is another type of self-balancing binary search tree where each node has an extra bit for denoting the color (red or black) of the node.

(usually need more complex examples)

## 7. B-tree

A B-tree is a self-balancing tree data structure that maintains sorted data and allows searches, sequential access, insertions, and deletions in logarithmic time.
(usually need more complex examples)

## 8. Trie (Prefix Tree)

A trie, also known as a prefix tree, is a tree-like data structure that stores a dynamic set of strings, where each node represents a common prefix of a group of strings.

(usually need more complex examples)

## 9. Heap

A heap is a specialized tree-based data structure that satisfies the heap property. In a min-heap, the parent is smaller than or equal to its children; in a max-heap, the parent is larger than or equal to its children.
(usually need more complex examples)

## 10. Suffix Tree

A suffix tree is a compressed trie containing all the suffixes of the given text as their keys and positions in the text as their values.
(usually need more complex examples)

## 11. Segment Tree

A segment tree is a data structure used for storing information about intervals or segments. It allows querying which of the stored segments contain a given point.
(usually need more complex examples)

## 12. K-d Tree

A k-d tree, or k-dimensional tree, is a space-partitioning data structure for organizing points in a k-dimensional space.
(usually need more complex examples)

## 13. Problem to Solve

Write a program that uses a binary search tree to store and search for integers. The program should support the following operations: insert, search, and delete.

You can check the solution [here](Solution-3.py).

[Return to Main Page](0-Welcome.md)
