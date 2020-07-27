class Solution(object):

    def lowestCommonAncestor(self, root, p, q):
        self.p = p
        self.q = q
        self.paths = TreeNode(float('inf'))
        self.pVals = []
        self.qVals = []
        h = {}

        def f(root, past=[], level=0):
            if (root == None):
                return
            h[root.val] = level
            if (root == self.p):
                self.pVals = (past + [root])
            elif (root == self.q):
                self.qVals = (past + [root])
            f(root.left, (past + [root]), (level - 1))
            f(root.right, (past + [root]), (level - 1))
        f(root)
        a = {}
        print [x.val for x in self.qVals]
        print [x.val for x in self.pVals]
        for v in set(self.pVals):
            if (v not in a):
                a[v] = 0
            a[v] += 1
        for v in set(self.qVals):
            if (v not in a):
                a[v] = 0
            a[v] += 1
        print a
        print [x.val for x in a]
        return sorted([x[0] for x in a.iteritems() if ((x[1] == 2) and (x[0].val in h))], key=(lambda k: h[k.val]))[0]
        return self.paths