class Solution(object):

    def maxScore(self, s):
        maxScore = 0
        db = {'1': 0, '0': 0}
        for val in s:
            db[val] += 1
        zeroCount = 0
        for val in s[:(-1)]:
            if (val == '0'):
                zeroCount += 1
            else:
                db[val] -= 1
            score = (db['1'] + zeroCount)
            if (score > maxScore):
                maxScore = score
        return maxScore