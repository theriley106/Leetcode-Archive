class Solution(object):

    def __init__(self):
        self.values = []

    def isUnivalTree(self, root):
        if (root == None):
            return
        if (root.val not in self.values):
            self.values.append(root.val)
        self.isUnivalTree(root.left)
        self.isUnivalTree(root.right)
        return (len(self.values) == 1)