class Solution(object):

    def findDuplicateSubtrees(self, rootz):
        self.db = {}
        self.vals = []
        self.db2 = {}

        def get(root, path=''):
            if (root == None):
                return [None]
            t = (([root.val] + get(root.left)) + get(root.right))
            if (str(t) not in self.db):
                self.db2[str(t)] = []
                self.db[str(t)] = 0
            self.db[str(t)] += 1
            self.db2[str(t)].append(root)
            return t
        get(rootz)
        for val in self.db:
            if (self.db[val] > 1):
                for v in set(self.db2[val]):
                    if (v not in self.vals):
                        self.vals.append(v)
        g = []
        h = []
        for x in self.vals:
            if (str(x) not in g):
                h.append(x)
                g.append(str(x))
        return h