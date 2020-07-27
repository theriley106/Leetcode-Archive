class Solution(object):

    def findRoot(self, tree):
        self.db = {}

        def check(tree):
            if (tree == None):
                return
            elif (type(tree) == list):
                for v in tree:
                    check(v)
            else:
                if (tree not in self.db):
                    self.db[tree] = 0
                self.db[tree] += 1
                if (self.db[tree] > 1):
                    return
                for v in tree.children:
                    check(v)
        check(tree)
        for (k, v) in self.db.iteritems():
            if (v == 1):
                return k