class Solution(object):

    def get_height(self, root):
        if (root == None):
            return 0
        return (1 + max(self.get_height(root.left), self.get_height(root.right)))

    def maxDepth(self, root):
        return self.get_height(root)