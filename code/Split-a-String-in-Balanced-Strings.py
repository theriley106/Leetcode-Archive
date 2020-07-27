class Solution(object):

    def balancedStringSplit(self, s):
        db = {'L': 0, 'R': 0}
        count = 0
        for val in s:
            db[val] += 1
            if (len(set(db.values())) == 1):
                db = {'L': 0, 'R': 0}
                count += 1
        return count