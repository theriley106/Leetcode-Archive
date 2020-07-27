class Solution:

    def findTheDifference(self, s, t):
        tDiff = list((set(t) - set(s)))
        if (len(tDiff) == 0):
            s = list(s)
            t = list(t)
            for val in s:
                t.remove(val)
            return t[0]
        return tDiff[0]