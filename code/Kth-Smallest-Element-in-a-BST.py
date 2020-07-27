class Solution(object):

    def extract(self, root):
        if (root == None):
            return []
        return ((self.extract(root.left) + [root.val]) + self.extract(root.right))

    def kthSmallest(self, root, k):
        return sorted(self.extract(root))[(k - 1)]