class Solution(object):

    def maxDepth(self, root):
        if (root == None):
            return 0
        if (len(root.children) == 0):
            return 1
        a = [self.maxDepth(r) for r in root.children]
        print a
        return (1 + max(a))