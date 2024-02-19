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
