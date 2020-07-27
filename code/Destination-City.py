class Solution(object):

    def destCity(self, paths):
        db = {}
        for t in paths:
            (val, dst) = t
            if (val not in db):
                db[val] = []
            if (dst not in db):
                db[dst] = []
            db[val].append(dst)
        for (k, v) in db.iteritems():
            if (len(v) == 0):
                return k