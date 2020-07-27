class Solution(object):

    def highFive(self, items):
        db = {}
        for val in items:
            if (val[0] not in db):
                db[val[0]] = []
            db[val[0]].append(val[1])
        for (k, v) in db.iteritems():
            db[k] = sorted(v)[(-5):]
        a = []
        for (k, v) in db.iteritems():
            a.append([k, (sum(v) / 5)])
        return a