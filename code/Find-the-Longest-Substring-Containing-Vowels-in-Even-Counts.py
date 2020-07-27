class Solution(object):

    def findTheLongestSubstring(self, s):
        vowels = 'aeiou'

        def slidingWindow(windowSize):
            db = {}
            largest = []
            prev = None
            for i in range(((len(s) - windowSize) + 1)):
                windowVals = s[i:(i + windowSize)]
                if (prev != None):
                    db[prev] = (db[prev] - 1)
                    if (db[prev] == 0):
                        del db[prev]
                    if (windowVals[(-1)] not in db):
                        db[windowVals[(-1)]] = 0
                    db[windowVals[(-1)]] += 1
                else:
                    for val in windowVals:
                        if (val not in db):
                            db[val] = 0
                        db[val] += 1
                prev = s[i]
                a = True
                for v in list(vowels):
                    a = (a and ((db.get(v, 0) % 2) == 0))
                if (a == True):
                    largest.append(''.join(s[i:(i + windowSize)]))
                if (a == True):
                    return largest[(-1)]
                print a
            if (a == True):
                return largest[(-1)]
            return a
        windowSize = len(s)
        while (windowSize > 0):
            r = slidingWindow(windowSize)
            if (r != False):
                return len(r)
            windowSize = (windowSize - 1)
        return 0