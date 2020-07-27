class Solution(object):

    def depthSumInverse(self, nestedList):
        self.db = {}

        def test(val, index=0):
            if (val.isInteger() == True):
                if (index not in self.db):
                    self.db[index] = []
                self.db[index].append(val.getInteger())
            else:
                for v in val.getList():
                    test(v, (index + 1))
        for v in nestedList:
            test(v)
        count = 0
        if (len(self.db) == 0):
            return 0
        self.maxVal = max(self.db.keys())

        def calc_depth(key):
            return ((self.maxVal - key) + 1)
        for (k, v) in self.db.iteritems():
            for u in v:
                count += (calc_depth(k) * u)
        return count