class Solution(object):

    def minDepth(self, root):

        def t(root, i=[]):
            if (root == None):
                return 0
            x = [root.left, root.right]
            if ((x[0] == None) and (x[1] == None)):
                return 1
            if (root.right == None):
                minVal = t(root.left)
            elif (root.left == None):
                minVal = t(root.right)
            else:
                minVal = min(t(root.right), t(root.left))
            return (1 + minVal)
        return t(root)