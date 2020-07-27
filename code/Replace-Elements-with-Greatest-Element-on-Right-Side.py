class Solution(object):

    def replaceElements(self, arr):
        index = 0
        db = {}
        maxVal = float('-inf')
        prevVal = float('-inf')
        for (i, val) in enumerate(reversed(arr)):
            if (i != 0):
                if (prevVal > maxVal):
                    maxVal = prevVal
                db[i] = maxVal
            else:
                db[0] = (-1)
            prevVal = val
        db2 = []
        for (i, val) in enumerate(reversed(arr)):
            db2.append(db[i])
        return reversed(db2)
        print db