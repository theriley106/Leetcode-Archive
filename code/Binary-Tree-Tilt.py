class Solution(object):

    def get_all(self, root):
        if (root == None):
            return 0
        left = self.get_all(root.left)
        right = self.get_all(root.right)
        self.tilt += abs((left - right))
        return ((root.val + left) + right)

    def findTilt(self, root):
        self.tilt = 0
        self.get_all(root)
        return self.tilt