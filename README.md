# Implementation of tree data structure in Python

This repo is an implementation of different tree data structures and their methods in python. The goal is to better understand the data structure and practice it's implementation. The content is derivative of lessons on boot.dev because that is where I am learning.

<!--toc:start-->

- [Implementation of tree data structure in Python](#implementation-of-tree-data-structure-in-python)
  - [A general overiew of trees](#a-general-overiew-of-trees)
  - [Binary Search Tree](#binary-search-tree)
  <!--toc:end-->

## A general overiew of trees

A tree data structure consists of parents and child nodes. Our root node has no parents, and each child node only has one parent. A parent node can have multiple child nodes. In the general case, children can have the same value as other children or their parent. These rules are often altered so that we can optimize data storage and retrieval.

## Binary Search Tree

A binary search tree (BST) applies a few rules to our above definition of a tree to make it easier to search and insert data. First, a parent can _only_ have two children, often said to be a right and left child. Second, the left child must be smaller than it's parent, and the right child must be larger than its parent. Lastly, no two nodes can have the same value. These rules get us a tree that is on average fast to insert into and search through. Problems arise with a simple BST when data is added that is sorted. Adding 1,2,3,4,5,6 into a BST in that order would result in a tree where each new insertion creates a right child since each next value is larger than the parent. This results in an unbalanced tree. To resolve this we can add a few rules to the BST to get us a red black tree.

## Red Black Trees

A red black tree (RBT) is a binary search tree that will balance itself after deletions or insertions. It does this by storing a bit of extra information in each node - a color, red or black. The rules for a RBT are all the ones defined above for a BST plus the following:

1. Every node is red or black

2. The root is black

3. All nil children are black

4. If a node is red, both its children are black

5.
