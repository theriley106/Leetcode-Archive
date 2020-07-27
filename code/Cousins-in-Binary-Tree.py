class Solution(object):

    def isCousins(self, root, x, y):
        g = {}

        def f(root, i=0, parentVal=None):
            if (root == None):
                return
            g[root.val] = (i, parentVal)
            f(root.left, (i + 1), parentVal=root.val)
            f(root.right, (i + 1), parentVal=root.val)
        f(root)
        return ((g[x][0] == g[y][0]) and (g[x][1] != g[y][1]))