import tree

test_BST = tree.BST()
assert test_BST.val is None
test_BST.val = 5
assert test_BST.val == 5
test_BST.insert(4)
test_BST.insert(8)
assert test_BST.right.val == 8
assert test_BST.left.val == 4
