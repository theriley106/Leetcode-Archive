class Solution(object):

    def minWindow(self, s, t):
        self.count = 0

        def is_same(db1, db3):
            for (k, v) in db3.items():
                if (k not in db1):
                    return False
                if (v > db1[k]):
                    return False
            return True
        startPoint = 0
        endPoint = (len(s) - 1)
        db2 = {}
        for v in t:
            if (v not in db2):
                db2[v] = 0
            db2[v] += 1
        self.found = ''
        leftPoint = 0
        rightPoint = (len(t) - 1)
        correctVals = []
        testDB = {}
        if (len(t) <= len(s)):
            for i in range((len(t) - 1)):
                if (s[i] not in testDB):
                    testDB[s[i]] = 0
                testDB[s[i]] += 1
        else:
            return ''
        prevRight = None
        reachedEnd = False
        minLen = float('inf')
        minVal = ''
        while ((max(rightPoint, len(s)) - leftPoint) >= len(t)):
            if (s[rightPoint] not in testDB):
                testDB[s[rightPoint]] = 0
            if (prevRight != rightPoint):
                testDB[s[rightPoint]] += 1
            prevRight = rightPoint
            self.count += 1
            if (is_same(testDB, db2) == False):
                if ((rightPoint + 1) < len(s)):
                    rightPoint += 1
                else:
                    if reachedEnd:
                        return minVal
                    leftPoint += 1
                    if (leftPoint < len(s)):
                        testDB[s[leftPoint]] = (testDB[s[leftPoint]] - 1)
                        if (testDB[s[leftPoint]] == 0):
                            del testDB[s[leftPoint]]
                        break
            else:
                if (rightPoint == (len(s) - 1)):
                    reachedEnd = True
                if (len(s[leftPoint:(rightPoint + 1)]) < minLen):
                    minVal = s[leftPoint:(rightPoint + 1)]
                    minLen = len(s[leftPoint:(rightPoint + 1)])
                self.found = s[leftPoint:(rightPoint + 1)]
                testDB[s[leftPoint]] = (testDB[s[leftPoint]] - 1)
                if (testDB[s[leftPoint]] == 0):
                    del testDB[s[leftPoint]]
                leftPoint += 1
        return minVal