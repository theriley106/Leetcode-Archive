class Solution(object):

    def smallestCommonElement(self, mat):
        db = {}
        for val in mat:
            for v in val:
                if (v not in db):
                    db[v] = 0
                db[v] += 1
        inAllRows = []
        for (k, v) in db.iteritems():
            if (v == len(mat)):
                inAllRows.append(k)
        if (len(inAllRows) == 0):
            return (-1)
        return sorted(inAllRows)[0]