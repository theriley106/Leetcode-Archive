class Solution(object):

    def is_leaf(self, root):
        return ((root.left == None) and (root.right == None))

    def lcaDeepestLeaves(self, root):
        self.left = []
        self.right = []
        self.maxLength = 0
        self.paths = []
        self.d = {}

        def traverse(root, depth=1, past=[]):
            if (root == None):
                return None
            self.d[root] = depth
            if self.is_leaf(root):
                if (depth > self.maxLength):
                    self.maxLength = depth
                    self.paths = (past + [root])
                    return None
                elif (depth == self.maxLength):
                    self.paths += (past + [root])
                    return None
                else:
                    return None
            traverse(root.left, (depth + 1), (past + [root]))
            traverse(root.right, (depth + 1), (past + [root]))
        traverse(root)
        mostRecent = None
        if (len(list(set(self.paths))) == len(self.paths)):
            print 'AYY'
            return self.paths[(-1)]
        else:
            db = {}
            for val in self.paths:
                if (val not in db):
                    db[val] = 0
                else:
                    db[val] += 1
                    mostRecent = val
        return sorted([k for (k, v) in db.iteritems() if (v == max(db.values()))], key=(lambda t: self.d[t]))[(-1)]
        return mostRecent
        print self.maxLength
        print self.paths