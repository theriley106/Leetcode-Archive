class Solution(object):

    def extract(self, root):
        if (root == None):
            return []
        return ((self.extract(root.left) + [root.val]) + self.extract(root.right))

    def findSecondMinimumValue(self, root):
        try:
            return sorted(set(self.extract(root)))[1]
        except:
            return (-1)