class Solution(object):

    def groupAnagrams(self, strs):
        db = {}
        for val in strs:
            info = {}
            for s in val:
                if (s not in info):
                    info[s] = 0
                info[s] += 1
            h = {}
            for v in sorted(info.keys()):
                h[v] = info[v]
            g = str(h.items())
            if (g not in db):
                db[g] = []
            db[g].append(val)
        print db
        return db.values()