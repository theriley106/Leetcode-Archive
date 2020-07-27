class Solution(object):

    def pruneTree(self, root):

        def f(root):
            if (root == None):
                return []
            a = f(root.left)
            b = f(root.right)
            if (1 not in a):
                root.left = None
            if (1 not in b):
                root.right = None
            return ((a + [root.val]) + b)
        f(root)
        return root