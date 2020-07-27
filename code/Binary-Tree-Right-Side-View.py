class Solution(object):

    def rightSideView(self, root):
        self.db = {}

        def f(root, row=0):
            if (root == None):
                return
            if (row not in self.db):
                self.db[row] = []
            self.db[row].append(root.val)
            f(root.left, (row + 1))
            f(root.right, (row + 1))
        f(root)
        a = []
        for (key, val) in self.db.iteritems():
            a.append(val[(-1)])
        return a