# This is for generating and displaying binary search trees
# The next step will be user modification after the tree is generated

import tree


def generate_bst(connections):
    bst = tree.BST()
    for val in connections:
        bst.insert(val)
    return bst


def display_bst(node, level=0):
    if node is not None:
        display_bst(node.right, level + 1)
        print(" " * 4 * level + "->", node.val)
        display_bst(node.left, level + 1)


# Usage:
connections = [10, 5, 15, 2, 7, 12, 18]
bst = generate_bst(connections)
display_bst(bst)
