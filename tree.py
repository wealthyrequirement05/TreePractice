class BST:
    def __init__(self, val=None):
        self.val = val
        self.right = None
        self.left = None

    def insert(self, val):
        if self.val is None:
            self.val = val
        elif self.val == val:
            return
        elif val < self.val:
            if self.left is not None:
                self.left.insert(val)
                return
            self.left = BST(val)
            return

        elif val > self.val:
            if self.right is not None:
                self.right.insert(val)
                return
            self.right = BST(val)
            return

    def delete(self, val):
        if self.val is None:
            return None
        if val < self.val:
            if self.left is not None:
                self.left = self.left.delete(val)
            return self
        if val > self.val:
            if self.right is not None:
                self.right = self.right.delete(val)
            return self
        if val == self.val:
            if self.right is None:
                return self.left
            elif self.left is None:
                return self.right
            else:
                min_larger_node = self.right
                while min_larger_node.left:
                    min_larger_node = min_larger_node.left
                self.val = min_larger_node.val
                self.right = self.right.delete(min_larger_node.val)
            return self
