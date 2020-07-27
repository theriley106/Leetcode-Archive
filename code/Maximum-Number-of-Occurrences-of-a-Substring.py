class Solution(object):

    def maxFreq(self, s, maxLetters, minSize, maxSize):
        db = {}

        def slidingWindow(size):
            for i in range(0, ((len(s) - size) + 1)):
                x = s[i:(i + size)]
                if (len(set(list(x))) <= maxLetters):
                    if (x not in db):
                        db[x] = 0
                    db[x] += 1
        for i in range(minSize, (maxSize + 1)):
            slidingWindow(i)
        if (len(db) == 0):
            return 0
        return max(db.values())