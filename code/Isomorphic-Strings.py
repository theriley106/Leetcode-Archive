class Solution(object):

    def isIsomorphic(self, s, t):
        db = {}
        db2 = {}
        t = list(t)
        s = list(s)
        for i in range(len(t)):
            if (t[i] not in db):
                db[t[i]] = s[i]
                db2[s[i]] = t[i]
            elif ((s[i] != db[t[i]]) or (t[i] != db2[s[i]])):
                return False
        for i in range(len(t)):
            if (t[i] not in db):
                db[t[i]] = s[i]
                db2[s[i]] = t[i]
            elif ((s[i] != db[t[i]]) or (t[i] != db2[s[i]])):
                return False
        return True