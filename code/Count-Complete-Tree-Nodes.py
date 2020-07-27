class Solution(object):

    def countNodes(self, root):

        def f(root):
            if (root == None):
                return 0
            return ((f(root.right) + f(root.left)) + 1)
        return f(root)