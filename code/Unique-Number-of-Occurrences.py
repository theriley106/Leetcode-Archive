class Solution(object):

    def uniqueOccurrences(self, arr):
        db = {}
        for val in arr:
            if (val not in db):
                db[val] = 0
            db[val] += 1
        return (len(db.values()) == len(set(db.values())))