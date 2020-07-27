class Solution(object):

    def arraysIntersection(self, arr1, arr2, arr3):
        db = {}
        g = []
        for val in arr1:
            g.append(val)
        for val in arr2:
            g.append(val)
        for val in arr3:
            g.append(val)
        for val in g:
            if (val not in db):
                db[val] = 0
            db[val] += 1
        a = []
        for (k, v) in db.iteritems():
            if (v == 3):
                a.append(k)
        return a