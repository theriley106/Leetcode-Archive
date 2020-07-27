class Solution(object):

    def groupStrings(self, strings):
        a = list('abcdefghijklmnopqrstuvwxyz')
        db = {}
        diffVals = []
        for val in strings:
            e = []
            r = a.index(val[0])
            for v in val:
                e.append(((r - a.index(v)) % 26))
            z = str(e)
            if (z not in db):
                db[z] = []
            db[z].append(val)
        return db.values()