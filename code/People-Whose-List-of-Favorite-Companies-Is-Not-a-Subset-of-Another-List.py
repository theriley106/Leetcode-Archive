class Solution(object):

    def peopleIndexes(self, favoriteCompanies):
        db = {}
        counts = {}
        for (i, val) in enumerate(favoriteCompanies):
            favoriteCompanies[i] = set(val)
            for v in val:
                if (v not in counts):
                    counts[v] = 0
                counts[v] += 1
        print favoriteCompanies
        er = []
        for (i, val) in enumerate(favoriteCompanies):
            count = len(val)
            f = True
            for (e, v) in enumerate(favoriteCompanies):
                if (e != i):
                    f = (f and (len((val - v)) > 0))
            if (f == True):
                er.append(i)
        return er