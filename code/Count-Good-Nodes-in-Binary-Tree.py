class Solution(object):

    def goodNodes(self, root):
        self.count = 0

        def check(root, maxVal=float('-inf')):
            if (root == None):
                return
            if (maxVal <= root.val):
                self.count += 1
            check(root.left, max(maxVal, root.val))
            check(root.right, max(maxVal, root.val))
        check(root)
        return self.count