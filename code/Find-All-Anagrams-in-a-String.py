class Solution(object):

    def findAnagrams(self, s, p):
        db = {}
        for val in p:
            if (val not in db):
                db[val] = 0
            db[val] += 1

        def is_same(db1, db2):
            if (set(db1.keys()) != set(db2.keys())):
                return False
            for (k, v) in db1.iteritems():
                if (db1[k] != db2[k]):
                    return False
            return True
        tempDB = {}
        for i in range(len(s)):
            if (s[i] not in db):
                db[s[i]] = 0
            tempDB[s[i]] = 0
        if (len(s) < len(p)):
            return []
        for i in range(len(p)):
            if (s[i] not in tempDB):
                tempDB[s[i]] = 0
            tempDB[s[i]] += 1
        toReturn = []
        if is_same(tempDB, db):
            toReturn.append(0)
        for i in range(1, ((len(s) - len(p)) + 1)):
            tempDB[s[(i - 1)]] = (tempDB[s[(i - 1)]] - 1)
            tempDB[s[((i + len(p)) - 1)]] += 1
            if is_same(tempDB, db):
                toReturn.append(i)
        return toReturn