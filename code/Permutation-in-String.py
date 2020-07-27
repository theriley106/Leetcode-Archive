class Solution(object):

    def checkInclusion(self, s1, s2):
        db1 = {}
        for val in s1:
            if (val not in db1):
                db1[val] = 0
            db1[val] += 1

        def calc_v(listString):
            db = {}
            for v in listString:
                if (v not in db):
                    db[v] = 0
                db[v] += 1
            return db
        prevDB = None
        for i in range(0, ((len(s2) - len(s1)) + 1)):
            if (prevDB == None):
                prevDB = calc_v(s2[i:(i + len(s1))])
            else:
                prevDB[s2[(i - 1):(i + len(s1))][0]
                       ] = (prevDB[s2[(i - 1):(i + len(s1))][0]] - 1)
                if (s2[i:(i + len(s1))][(-1)] not in prevDB):
                    prevDB[s2[i:(i + len(s1))][(-1)]] = 0
                prevDB[s2[i:(i + len(s1))][(-1)]] += 1
                h = []
                for (k, v) in prevDB.iteritems():
                    if (v == 0):
                        h.append(k)
                for val in h:
                    del prevDB[val]
            if (prevDB == db1):
                return True
        return False
