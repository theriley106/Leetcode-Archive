class Solution(object):

    def numEquivDominoPairs(self, dominoes):
        db = {}
        count = 0
        for val in dominoes:
            x = tuple(sorted(val))
            if (x not in db):
                db[x] = 0
            else:
                count += db[x]
            db[x] += 1
        return count