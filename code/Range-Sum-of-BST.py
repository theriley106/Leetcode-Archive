class Solution(object):

    def rangeSumBST(self, root, L, R):
        if (root == None):
            return 0
        if ((root.val >= L) and (root.val <= R)):
            tempVal = root.val
        else:
            tempVal = 0
        return ((tempVal + self.rangeSumBST(root.left, L, R)) + self.rangeSumBST(root.right, L, R))