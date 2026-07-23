## DSA Binary Search Trees
A Binary Search Tree is a Binary Tree where every node's left child has a lower value, and every node's right child has a higher value.

A clear advantage with Binary Search Trees is that operations like search, delete, and insert are fast and done without having to shift values in memory.

If X is a node in a tree then the following must be true.
1. The X node's left child and all of its descendants (children, children's children, and so on) have lower values than X's value

2. The right child, and all its descendants have higher values than X's value.

3. Left and right subtrees must also be Binary Search Trees.