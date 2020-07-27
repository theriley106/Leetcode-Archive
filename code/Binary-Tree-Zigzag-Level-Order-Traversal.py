class Solution(object):

    def zigzagLevelOrder(self, root):
        g = {}

        def f(root, i=0):
            if (root == None):
                return []
            if (i not in g):
                g[i] = []
            g[i].append(root.val)
            return (f(root.left, (i + 1)) + f(root.right, (i + 1)))
        a = f(root)
        if (len(g.keys()) == 0):
            return []
        a = []
        for i in range((max(g.keys()) + 1)):
            if ((i % 2) == 0):
                a.append(g[i])
            else:
                a.append(g[i][::(-1)])
        return a