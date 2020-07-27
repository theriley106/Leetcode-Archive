class Solution(object):

    def isValidBST(self, root):
        list_of_vals = self.inorder(root)
        for i in range(1, len(list_of_vals)):
            if (list_of_vals[(i - 1)] >= list_of_vals[i]):
                return False
        return True

    def inorder(self, root):
        if (root == None):
            return []
        return ((self.inorder(root.left) + [root.val]) + self.inorder(root.right))