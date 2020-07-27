class Solution(object):

    def largestUniqueNumber(self, A):
        db = {}
        for val in A:
            if (val not in db):
                db[val] = 0
            db[val] += 1
        vals = [i for (i, x) in db.iteritems() if (x == 1)]
        if (len(vals) == 0):
            return (-1)
        return max(vals)