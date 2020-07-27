class Solution(object):

    def averageOfLevels(self, root):
        g = {}

        def f(root, i=0):
            if (root == None):
                return
            if (i not in g):
                g[i] = []
            g[i].append(root.val)
            f(root.left, (i + 1))
            f(root.right, (i + 1))
        f(root)
        a = []
        if (len(g.keys()) == 0):
            return a
        for i in range((max(g.keys()) + 1)):
            a.append((float(sum(g[i])) / float(len(g[i]))))
        return a