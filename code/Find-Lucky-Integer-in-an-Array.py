class Solution(object):

    def findLucky(self, arr):
        db = {}
        for val in arr:
            if (val not in db):
                db[val] = 0
            db[val] += 1
        a = []
        for (k, v) in db.iteritems():
            if (k == v):
                a.append(v)
        if (len(a) == 0):
            return (-1)
        return max(a)