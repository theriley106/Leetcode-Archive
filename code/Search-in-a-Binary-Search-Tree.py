class Solution(object):

    def searchBST(self, root, val):
        if (root == None):
            return None
        if (root.val == val):
            return root
        k = self.searchBST(root.left, val)
        if (k != None):
            return k
        r = self.searchBST(root.right, val)
        if (r != None):
            return r
        return None