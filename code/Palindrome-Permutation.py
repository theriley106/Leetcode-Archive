class Solution(object):

    def canPermutePalindrome(self, s):
        db = {}
        for val in s:
            if (val not in db):
                db[val] = 0
            db[val] += 1
        maxOddVal = 0
        for (k, v) in db.iteritems():
            if ((v % 2) == 0):
                pass
            else:
                maxOddVal += 1
        return (maxOddVal < 2)