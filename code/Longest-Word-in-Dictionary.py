class Solution(object):

    def longestWord(self, words):
        a = {}
        for val in words:
            a[val] = False
        for val in words:
            i = 1
            while (val[:(- i)] in a):
                i += 1
            a[val] = (val[:(- i)] == '')
        g = sorted([e for e in a.keys() if (a[e] == True)], key=len)
        maxLength = len(g[(-1)])
        prevVal = g[(-1)]
        print g
        y = []
        for val in g[::(-1)]:
            if (len(val) == maxLength):
                y.append(val)
            else:
                break
        return sorted(y)[0]